from fastapi import FastAPI

from app.routes.expenses import router as expense_router

app = FastAPI(
    title="Expense Tracker API",
    version="1.0.0",
)
app.include_router(expense_router)