import os
import datetime
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

def seed_complete_schema():
    client = MongoClient(os.getenv("DATABASE_URL"))
    db = client.gradiantstock_db

    # 1. Shop Collection (Internal)
    shop_id = "yochi-hcmc-001"
    db.shops.update_one(
        {"shop_id": shop_id},
        {"$set": {
            "name": "Yochi Flagship",
            "location": "Ho Chi Minh City, District 1"
        }}, upsert=True
    )

    # 2. Product Collection (Internal)
    # This acts as your 'Master List'
    products = [
        {"product_id": "P001", "name": "Full Cream Milk", "category": "Dairy", "base_unit": "Liters"},
        {"product_id": "P002", "name": "Yochi Signature Cup", "category": "Packaging", "base_unit": "Units"},
        {"product_id": "P003", "name": "Matcha Powder", "category": "Powder", "base_unit": "KG"}
    ]
    for p in products:
        db.products.update_one({"product_id": p["product_id"]}, {"$set": p}, upsert=True)

    # 3. Inventory Collection (Internal - The Current State)
    inventory = [
    # P001: Dairy (High risk, fast turnover)
    {
        "shop_id": shop_id,
        "product_id": "P001",
        "batch_number": "MILK-BATCH-02",
        "quantity_on_hand": 45,
        "arrival_date": datetime.datetime(2026, 2, 10),
        "expiry_date": datetime.datetime(2026, 2, 17),
        "temperature_sensitive": True
    },
    # P002: Packaging (No real expiry, high volume)
    {
        "shop_id": shop_id,
        "product_id": "P002",
        "batch_number": "CUP-ORDER-JAN",
        "quantity_on_hand": 2000,
        "arrival_date": datetime.datetime(2026, 1, 15),
        "expiry_date": datetime.datetime(2029, 1, 1), # Far in the future
        "temperature_sensitive": False
    },
    # P003: Powder (Long shelf life, expensive)
    {
        "shop_id": shop_id,
        "product_id": "P003",
        "batch_number": "MATCHA-PREMIUM-01",
        "quantity_on_hand": 12,
        "arrival_date": datetime.datetime(2026, 2, 1),
        "expiry_date": datetime.datetime(2026, 8, 1), # 6 months shelf life
        "temperature_sensitive": False
    }
]
    db.inventory.delete_many({"shop_id": shop_id})
    db.inventory.insert_many(inventory)

    # 4. External Information (Events & Weather)
    # This is what the AI will 'read' to make recommendations
    db.events.insert_one({
        "name": "HCMC Midnight Marathon",
        "start_date": datetime.datetime(2026, 2, 15),
        "location": "District 1",
        "event_type": "Sports/High Traffic"
    })

    print("Full Schema Seeded")

if __name__ == "__main__":
    seed_complete_schema()