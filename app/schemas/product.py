from pydantic import BaseModel, UUID4, Field
from typing import Optional
from datetime import datetime

class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float = Field(gt=0)
    category: str
    stock_quantity: int = Field(ge=0)

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    name: Optional[str] = None
    price: Optional[float] = Field(gt=0, default=None)
    category: Optional[str] = None
    stock_quantity: Optional[int] = Field(ge=0, default=None)

class Product(ProductBase):
    id: UUID4
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True