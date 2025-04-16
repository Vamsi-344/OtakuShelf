from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import psycopg2
from utils.scrape import scrapeChapter
import re

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

conn = psycopg2.connect(database = "postgres", 
                    user = "postgres", 
                    host= 'localhost',
                    password = "postgres",
                    port = 5432)

@app.on_event("startup")
async def startup_event():
    # Open a cursor to perform database operations
    cur = conn.cursor()
    # Execute a command: create novels table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS novels (
            id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            author VARCHAR(50),
            title VARCHAR(250) NOT NULL,
            slug VARCHAR(100) NOT NULL,
            status VARCHAR(20),
            description TEXT
        );
    """)

    cur.execute("""
        CREATE OR REPLACE FUNCTION update_updated_at_column()
        RETURNS TRIGGER AS $$
        BEGIN
            NEW.updated_at = NOW();
            RETURN NEW;
        END;
        $$ LANGUAGE plpgsql;
                
        DROP TRIGGER IF EXISTS trg_updated_at ON novels;

        CREATE TRIGGER trg_updated_at
        BEFORE UPDATE ON novels
        FOR EACH ROW
        WHEN (OLD.* IS DISTINCT FROM NEW.*)
        EXECUTE FUNCTION update_updated_at_column();
    """)

    
    cur.execute("""CREATE TABLE IF NOT EXISTS chapters (
        id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
        novel_id UUID,
        FOREIGN KEY (novel_id) REFERENCES novels(id),
        chapter_number INT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        title VARCHAR(250) NOT NULL,
        slug VARCHAR(100) NOT NULL,
        body TEXT[]
        );
        """)
    
    cur.execute("""
        CREATE OR REPLACE FUNCTION update_updated_at_column()
        RETURNS TRIGGER AS $$
        BEGIN
            NEW.updated_at = NOW();
            RETURN NEW;
        END;
        $$ LANGUAGE plpgsql;

        DROP TRIGGER IF EXISTS trg_updated_at ON chapters;
                
        CREATE TRIGGER trg_updated_at
        BEFORE UPDATE ON chapters
        FOR EACH ROW
        WHEN (OLD.* IS DISTINCT FROM NEW.*)
        EXECUTE FUNCTION update_updated_at_column();
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS categories (
            id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
            category VARCHAR(50) NOT NULL,
            slug VARCHAR(100) NOT NULL
        );
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS chapter_categories (
            category_id UUID,
            chapter_id UUID,
            CONSTRAINT pk_id PRIMARY KEY (chapter_id,category_id)
        );
    """)


    # Make the changes to the database persistent
    conn.commit()
    # Close cursor and communication with the database
    cur.close()
    # conn.close()

def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)         # Remove punctuation
    text = re.sub(r'[\s_-]+', '-', text)         # Replace space/underscore with hyphen
    text = re.sub(r'^-+|-+$', '', text)          # Strip hyphens
    return text

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/fetch_novel")
async def fetchNovel(author: str, novel_name: str, status: str, description: str, no_of_chapters: int, base_url: str, image_url: str):
    cur = conn.cursor()
    novel_slug = slugify(novel_name)
    cur.execute(
    "INSERT INTO novels(author, title, status, slug, description, image_url) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id",
    (author, novel_name, status, novel_slug, description, image_url)
    )
    novel_id = cur.fetchone()[0]
    print("Inserted novel successfully with: ", novel_id)
    for i in range(887, 888):
        print("Scraping for", base_url+'/chapter-'+str(i))
        heading, paras = scrapeChapter(base_url+'/chapter-'+str(i))
        print(heading)
        cur.execute(
        "INSERT INTO chapters(novel_id, chapter_number, title, slug, body) VALUES (%s, %s, %s, %s, %s) RETURNING id",
        (novel_id, i, heading, 'chapter-'+str(i), paras)
        )
        chapter_id = cur.fetchone()[0]
        print("Inserted chapter successfully with: ", chapter_id)
        conn.commit()
    # conn.commit()
    # conn.close()
    cur.close()
    return {"message": "Novel Chapters Scraped Successfully"}

@app.get("/novels")
async def getNovels():
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM novels;"
    )
    rows = cur.fetchall()
    conn.commit()
    novels = []
    for row in rows:
        novel = {}
        novel["author"], novel["title"], novel["slug"], novel["status"], novel["description"], novel["image_url"] = row[3:9]
        novels.append(novel)
    cur.close()
    return {"response": novels}

@app.get("/novel/{novel_slug}")
async def fetchNovelInfo(novel_slug: str):
    cur = conn.cursor()
    cur.execute("""
        SELECT novels.title, novels.author, novels.status, novels.description, novels.image_url, chapters.chapter_number, chapters.title, chapters.slug, chapters.updated_at
        FROM novels
        INNER JOIN chapters
        ON novels.id = chapters.novel_id
        WHERE novels.slug=%s
    """, (novel_slug,))
    rows = cur.fetchall()
    novel_details = {}
    chapter_details = []
    for row in rows:
        chapter = {}
        novel_details["title"], novel_details["author"], novel_details["status"], novel_details["description"], novel_details["image_url"] = row[:5]
        chapter["chapter_number"], chapter["title"], chapter["slug"], chapter["updated_at"] = row[5:]
        chapter_details.append(chapter)
    cur.close()
    return {"novel": novel_details, "chapters": chapter_details}

@app.get("/novel/{novel_slug}/{chapter_slug}")
async def fetchChapterInfo(novel_slug: str, chapter_slug: str):
    cur = conn.cursor()
    cur.execute("""
        SELECT novels.title, chapters.title, chapters.body
        FROM novels
        INNER JOIN chapters
        ON novels.id = chapters.novel_id
        WHERE novels.slug=%s AND chapters.slug=%s
    """, (novel_slug, chapter_slug))
    novel_title, chapter_title, chapter_body = cur.fetchone()[:]
    cur.close()
    return {"novel_title": novel_title, "title": chapter_title, "body": chapter_body}