import credential_handler
from googleapiclient.discovery import build



def create_expenses(_values):
    SPREADSHEET_ID = "1rnYyBf3xr2Y8NCDSPtEJFGWfHBRcup00bumLbctTfkA"
    creds = credential_handler.get_creds()
    service = build("sheets", "v4", credentials=creds)
    cell_range = "Sheet1!A4"

    values = _values
        

    
    body = {"values": values}
    request = service.spreadsheets().values().update(
        spreadsheetId = SPREADSHEET_ID, 
        range = cell_range, 
        valueInputOption="USER_ENTERED", 
        body=body
        ).execute()

    
