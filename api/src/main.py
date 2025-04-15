from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import psycopg2
from utils.scrape import scrapeChapter

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
            title VARCHAR(50) NOT NULL,
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
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        title VARCHAR(50) NOT NULL,
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

    # Make the changes to the database persistent
    conn.commit()
    # Close cursor and communication with the database
    cur.close()
    # conn.close()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/fetch_novel")
async def fetchNovel(author: str, novel_name: str, status: str, description: str, no_of_chapters: int, base_url: str):
    cur = conn.cursor()
    cur.execute(
    "INSERT INTO novels(author, title, status, description) VALUES (%s, %s, %s, %s) RETURNING id",
    (author, novel_name, status, description)
    )
    novel_id = cur.fetchone()[0]
    print("Inserted novel successfully with: ", novel_id)
    for i in range(2, 5):
        print("Scraping for", base_url+'/chapter-'+str(i))
        heading, paras = scrapeChapter(base_url+'/chapter-'+str(i))
        cur.execute(
        "INSERT INTO chapters(novel_id, title, body) VALUES (%s, %s, %s) RETURNING id",
        (novel_id, heading, paras)
        )
        chapter_id = cur.fetchone()[0]
        print("Inserted chapter successfully with: ", chapter_id)
    conn.commit()
    conn.close()
    cur.close()
    return {"message": "Novel Chapters Scraped Successfully"}

