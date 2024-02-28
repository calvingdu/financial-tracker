import credential_handler
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


def get_values():

    SPREADSHEET_ID = "1rnYyBf3xr2Y8NCDSPtEJFGWfHBRcup00bumLbctTfkA"

    try: 
        creds = credential_handler.get_creds()
        service = build("sheets", "v4", credentials=creds)
        sheets = service.spreadsheets()
        
        result = sheets.values().get(spreadsheetId=SPREADSHEET_ID, range="Sheet1!A2:D20").execute()
        
        values = result.get("values", [])
        expenses = []

        for row in values:
            expenses.append(row)
        print(expenses)
        return expenses

    except HttpError as error:
        print(error)
        return None
    
