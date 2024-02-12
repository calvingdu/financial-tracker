import credential_handler
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SPREADSHEET_ID = "1rnYyBf3xr2Y8NCDSPtEJFGWfHBRcup00bumLbctTfkA"

def get_values(SPREADSHEET_ID):

    try: 
        creds = credential_handler.get_creds()
        service = build("sheets", "v4", credentials=creds)
        sheets = service.spreadsheets()
        
        result = sheets.values().get(spreadsheetId=SPREADSHEET_ID, range="Sheet1!B2:C20").execute()
        
        values = result.get("values", [])

        for row in values:
            print(row)
    except HttpError as error:
        print(error)