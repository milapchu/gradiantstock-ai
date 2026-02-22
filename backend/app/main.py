from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
import os
import traceback
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
from .models import Shop
from .database import shops_coll

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Temporarily allow all for development
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

DATABASE_URL = os.getenv("DATABASE_URL")

@app.get("/")
async def health_check():
    app_status = "GradiantStock Backend Live"  # ✅ renamed to app_status
    db_status = "Disconnected"

    if DATABASE_URL:
        try:
            client = AsyncIOMotorClient(DATABASE_URL)
            await client.admin.command('ismaster')
            db_status = "Connected & Responding"
        except Exception as e:
            db_status = f"Connection Error: {str(e)}"
    else:
        db_status = "Missing DATABASE_URL in .env"

    return {
        "status": app_status,
        "database": db_status
    }

@app.post("/register")
async def register_shop(shop: Shop):
    try:
        # Check if the shop already exists
        existing = await shops_coll.find_one({"shop_id": shop.shop_id})
        if existing:
            raise HTTPException(status_code=400, detail="Shop ID already exists")

        await shops_coll.insert_one(shop.model_dump())
        return {"message": "Success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

@app.post("/login", status_code=status.HTTP_201_CREATED)
async def login_shop(shop_id: str, password: str):
    db_shop = await shops_coll.find_one({"shop_id": shop_id})
    if not db_shop:
        raise HTTPException(status_code=401, detail="Invalid Shop ID")

    if not (password==db_shop["password"]):
        raise HTTPException(status_code=401, detail="Incorrect Password")

    return {"message": "Login successful", "shop_name": db_shop["name"]}