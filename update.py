import credential_handler
from googleapiclient.discovery import build

SPREADSHEET_ID = "1rnYyBf3xr2Y8NCDSPtEJFGWfHBRcup00bumLbctTfkA"

def update_values(SPREADSHEET_ID):
    creds = credential_handler.get_creds()
    service = build("sheets", "v4", credentials=creds)
    sheets = service.spreadsheets()

    # result = sheets.values().get(spreadsheetId=SPREADSHEET_ID, range="Sheet1!B2:C20").execute()

    # values = result.get('values', [])


    testData = [["01-Feb", "Insurance", -100, "Vehicle"], ["05-Feb", "McDonalds", -12.46, "Meal"]] 

    request = sheets.values().update(spreadsheetId = SPREADSHEET_ID, range="Sheet1!A2", valueInputOption="USER_ENTERED", body={"values": testData}).execute()
