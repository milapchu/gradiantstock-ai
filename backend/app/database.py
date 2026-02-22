import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv()

# The connection
client = AsyncIOMotorClient(os.getenv("DATABASE_URL"), authSource="admin", tls=True,retryWrites=True, serverSelectionTimeoutMS=5000)
db = client.gradiantstock_db

# Collection handles for easy import elsewhere
shops_coll = db.get_collection("shops")
products_coll = db.get_collection("products")
inventory_coll = db.get_collection("inventory")