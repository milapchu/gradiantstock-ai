from fastapi import FastAPI
import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv()

app = FastAPI()

# Get the URL from your .env
DATABASE_URL = os.getenv("DATABASE_URL")

@app.get("/")
async def health_check():
    status = "GradiantStock Backend Live"
    db_status = "Disconnected"
    
    if DATABASE_URL:
        try:
            # Attempt to actually connect and ping the database
            client = AsyncIOMotorClient(DATABASE_URL)
            # The ismaster command is cheap and confirms the DB is responding
            await client.admin.command('ismaster')
            db_status = "Connected & Responding"
        except Exception as e:
            db_status = f"Connection Error: {str(e)}"
    else:
        db_status = "Missing DATABASE_URL in .env"

    return {
        "status": status,
        "database": db_status
    }