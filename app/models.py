from pydantic import BaseModel, Field
from datetime import datetime

#Expenses Model 
class Expense(BaseModel):
    amount: float
    category: str
    description: str

class ExpenseResponse(BaseModel):
    id: int
    amount: float
    category: str
    description: str
    created_at: datetime