from fastapi import FastAPI, Path
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

@app.get("/get-expense-by-type")
def get_expense_by_type(type: str):
    valid_expense = []
    all_expenses = get_expenses.get_values()
    #[['01-Feb', 'Insurance', '-$100.00', 'Vehicle'], 
    # ['01-Feb', 'McDonalds', '-$100.00', 'Meal'], 
    # ['Feb10', 'gas', '-$60.00', 'Vehicle'], 
    # ['28-Feb', 'ESSOSMARTSHOP', '$60.00']]
    for external in all_expenses:
        if (external[3].lower()) == type.lower():
            valid_expense.append(external)
            
    return valid_expense

@app.delete("/delete-expense")
def delete_expense(date: str = Path(title="in format of DD-Mon"), amount: int = Path(title="in format of $00.00")):
    i = 2
    for expense in get_expenses.get_values():
        if (expense[0] == date) and (expense[3] == amount):
            cell_range = "Sheet1!A" + str(i) + ":D" + str(i)
            break
        else:
            i += 1
    return delete_expense.delete_expenses(cell_range)

@app.post("/refresh")
async def resync_new_emails():
    current_list = get_expense()
    new_emails =  gmail_reader.fetch_email_data()
    unreceived_emails = []
    for email in new_emails:
        if not (email in current_list):
            unreceived_emails.append(email)
    return create_expense.create_expenses(unreceived_emails)


@app.post("/create-expense")
def create_new_expense(expense_type: str):
    expense = gmail_reader.fetch_email_data()
    # expense[0].append("expense_type") ASK ASIM
    # print(expense)
    return create_expense.create_expenses(expense)
    

