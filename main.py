from fastapi import FastAPI
import credential_handler
import get_expenses
import create_expense
import gmail_reader
import delete_expense

app = FastAPI()

credential_handler.get_creds()

@app.get("/get-expenses")
def get_expense():
    return get_expenses.get_values()
#return to user the data rather than returning null

@app.get("/get-expense-by-type")
def get_expense_by_type(type: str):
    valid_expense = []
    all_expenses = get_expenses.get_values()
    # all_expenses = [['01-Feb', 'Insurance', '-$100.00', 'Vehicle'], 
    #                 ['01-Feb', 'McDonalds', '-$100.00', 'Meal'], 
    #                 ['Feb20', 'MCDONALDS', '$7.34', 'meal']]
    
    for external in all_expenses:
        if (external[3].lower()) == type.lower():
            valid_expense.append(external)
            
    return valid_expense

@app.delete("/delete-expense")
def delete_expense(cell_range: str, date: str, amount: int):
    for expense in get_expenses.get_values():
        print(null)
    return delete_expense.delete_expenses(cell_range)


@app.post("/create-expense")
def create_new_expense(expense_type: str):
    expense = gmail_reader.fetch_email_data().append(expense_type.lower())
    return create_expense.create_expenses(expense)

