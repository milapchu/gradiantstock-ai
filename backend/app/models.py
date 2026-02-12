from pydantic import BaseModel, Field
from datetime import date, datetime

# --- Internal Shop Data ---

class Shop(BaseModel):
    name: str = Field(..., max_length=255)
    location: str = Field(..., max_length=50) # Name of the city

class Product(BaseModel):
    name: str = Field(..., max_length=255)
    category: str = Field(..., max_length=100)
    base_unit: str = Field(..., max_length=20) # e.g., 'kg', 'ml'

class Inventory(BaseModel):
    shop_id: str
    product_id: str
    quantity_on_hand: int
    arrival_date: date
    expiry_date: date
    batch_number: str = Field(..., max_length=50)
    on_promotion: bool = False
    temperature_sensitive: bool = False

class Sales(BaseModel):
    shop_id: str
    product_id: str
    quantity_sold: int

# --- External Information ---

class Event(BaseModel):
    name: str
    start_date: date
    end_date: date
    location: str
    event_type: str # e.g., 'festival', 'holiday'

class Weather(BaseModel):
    date: date
    location: str
    forecast_condition: str # e.g., 'Rainy'
    temp_high: int
    temp_low: int

# --- Recommendation Engine ---

class StockRecommendation(BaseModel):
    shop_id: str
    product_id: str
    recommended_stock_level: int
    reasoning: str # e.g., "High demand expected due to Music Festival"
    generated_at: datetime = Field(default_factory=datetime.now)