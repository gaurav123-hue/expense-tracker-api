from fastapi import APIRouter, status
from app.models import Expense
from app.services.expense_service import (
    create_expense,
    delete_expense_by_id,
    get_all_expenses,
    get_expense_by_id,
    update_expense_by_id
)

"""
Expense Routes

This module defines all HTTP endpoints related to expense management.

Responsibilities:
- Receive HTTP requests
- Validate incoming request data
- Delegate business logic to the service layer
- Return HTTP responses

Routes should remain lightweight and should not contain
business logic or database operations.
"""

# All endpoints in this router will automatically be prefixed with '/expenses'
# and grouped under the "Expenses" section in Swagger UI.
router = APIRouter(
    prefix="/expenses",
    tags=["Expenses"]
)

@router.post("/", status_code=status.HTTP_201_CREATED)
def add_expense(expense: Expense):
    """
    Create a new expense.

    Receives expense data from the client and delegates
    the creation process to the service layer.

    Returns:
        A success message along with the newly created expense.
    """

    created_expense = create_expense(expense)

    return {
        "message": "Expense added successfully!",
        "expense": created_expense
    }

@router.get("/")
def get_expenses():
    """
    Retrieve all stored expenses.

    Returns:
        A list containing all recorded expenses.
    """

    return {
        "expenses": get_all_expenses()
    }

@router.get("/{expense_id}")
def get_expense(expense_id: int):
    """
    Retrieve a single expense using its unique ID.

    Args:
        expense_id: The unique identifier of the expense.

    Returns:
        The matching expense if found.

    Raises:
        HTTPException (404) if the expense does not exist.
    """

    return {
        "expense": get_expense_by_id(expense_id)
    }

@router.put("/{expense_id}")
def update_expense(expense_id: int, updated_expense: Expense):
    """
    Update an existing expense by its unique ID.

    Args:
        expense_id: The unique identifier of the expense to be updated.
        updated_expense: The new data for the expense.

    Returns:
        The updated expense if found.

    Raises:
        HTTPException (404) if the expense does not exist.
    """

    return {
        "expense": update_expense_by_id(expense_id, updated_expense)
    }

@router.delete("/{expense_id}")
def delete_expense(expense_id: int):
    """
    Delete an existing expense by its unique ID.

    Args:
        expense_id: The unique identifier of the expense to be deleted.

    Returns:
        A success message if the expense was deleted.

    Raises:
        HTTPException (404) if the expense does not exist.
    """

    delete_expense_by_id(expense_id)

    return {
        "message": "Expense deleted successfully!"
    }