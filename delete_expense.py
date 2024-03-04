import credential_handler
from googleapiclient.discovery import build



def delete_expeneses(cell_range: str):
    SPREADSHEET_ID = "1rnYyBf3xr2Y8NCDSPtEJFGWfHBRcup00bumLbctTfkA"
    creds = credential_handler.get_creds()
    service = build("sheets", "v4", credentials=creds)
    cell_range = "Sheet1!A2:D50"


    service.spreadsheets().values().clear(
        spreadsheetId = SPREADSHEET_ID, 
        range = cell_range, 
        ).execute()


