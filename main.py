from fastapi import FastAPI
import credential_handler
import get_expenses
import create_expense
import gmail_reader

app = FastAPI()

credential_handler.get_creds()

@app.get("/get-expenses")
def get_expense():
    return get_expenses.get_values()
#return to user the data rather than returning null

@app.get("/get-expense-by-type")
def get_expense_by_type(type: str):
    return get_expenses.get_values()

@app.post("/create-expense")
def create_new_expense(expense_type: str):
    expense = gmail_reader.fetch_email_data().append(expense_type)
    return create_expense.create_expenses(expense)

