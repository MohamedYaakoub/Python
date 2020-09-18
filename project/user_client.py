import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time


# Find a workbook by name and open the first sheet
# Make sure you use the right name here.




class Database:
    def __init__(self):
        scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
                 "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret_3.json', scope)
        client = gspread.authorize(creds)
        self.sheet = client.open("Database 3").sheet1




