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
    valid_expense = []
    # all_expenses = get_expenses.get_values()
    all_expenses = [['01-Feb', 'Insurance', '-$100.00', 'Vehicle'], 
                    ['01-Feb', 'McDonalds', '-$100.00', 'Meal'], 
                    ['Feb20', 'MCDONALDS', '$7.34', 'meal']]
    
    if len(all_expenses) > 1:
        for external in all_expenses:
            if (external[3].lower()) == type.lower():
                valid_expense.append(external)
    print(valid_expense)
    return valid_expense

@app.post("/create-expense")
def create_new_expense(expense_type: str):
    expense = gmail_reader.fetch_email_data().append(expense_type.lower())
    return create_expense.create_expenses(expense)

