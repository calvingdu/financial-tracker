import credential_handler
import get_expenses
from googleapiclient.discovery import build



def create_expenses(_values):
    SPREADSHEET_ID = "1rnYyBf3xr2Y8NCDSPtEJFGWfHBRcup00bumLbctTfkA"
    creds = credential_handler.get_creds()
    service = build("sheets", "v4", credentials=creds)
    cell_range = "Sheet1!A6"
    values = _values
    current_values = get_expenses.get_values()

    body = {"values": values}

    next_row = len(current_values) + 2

    service.spreadsheets().values().update(
        spreadsheetId = SPREADSHEET_ID, 
        range = f'Sheet1!A{next_row}', 
        valueInputOption="USER_ENTERED", 
        body=body
        ).execute()
