from time import ctime
from random import randint
from oauth2client.service_account import ServiceAccountCredentials
import gspread
import ntplib
import numpy as np


class Database:
    def __init__(self, json, sheet_name):
        self.scope = ['https://spreadsheets.google.com/feeds',
                      'https://www.googleapis.com/auth/drive']
        self.creds = ServiceAccountCredentials.from_json_keyfile_name(json, self.scope)
        self.client = gspread.authorize(self.creds)
        self.sheet = self.client.open(sheet_name).sheet1
        #self.size = self.count()

    def get_all(self):
        return self.sheet.get_all_values()

    def add(self, request):
        # for entry in
        self.sheet.insert_row(request, 2)

    def add_cell(self, row, col, msg):
        self.sheet.update_cell(row, col, msg)

    def delete(self, index):
        self.sheet.delete_rows(index)

    def count(self):
        count = 0
        for entry in self.get_all():
            count += 1 if ''.join(entry) != '' else 0
        return count
    # e3mel: 1- remove() to remove entry given ID (either first matching entry or all)
    # e3mel: 2- clean() to remove empty lines automatically
    # e3mel: 3- amend(id, new_entry) to update given line (add just one cell)


class Request:
    def __init__(self, request_details):
        self.identifier = int(request_details[0])
        self.date = request_details[1]
        # e3mel: 4- get time automatically (from internet) and add request time. User
        self.time = request_details[2]
        self.location = str(request_details[3])
        self.hyrer = str(request_details[4])
        self.category = str(request_details[5])
        self.description = str(request_details[6])
        self.hyree_assigned = str(request_details[7])
        self.status = 'Active'

    @staticmethod
    def get_time():
        """Gets global time time

              :param :
              :return: time
            """
        ntp_client = ntplib.NTPClient()
        response = ntp_client.request('pool.ntp.org')  # Time zone
        return ctime(response.tx_time)

    def accept(self):
        self.status = 'Accepted'

    def reject(self):
        self.status = 'Active'

    def done(self):
        self.status = 'Done'


class User:
    user_database = Database("client_secret_1.json", "User Database")

    def __init__(self, name, birthdate, location, preferences, password, email):
        self.user_id = randint(10000, 99999)
        while str(self.user_id) in self.user_database.sheet.col_values(1):
            self.user_id = randint(10000, 99999)     # we need a better ID system for example Hyre-89273 or Hyree-34234
        self.name = name
        self.birthdate = birthdate
        self.location = location
        self.preferences = preferences
        self.password = password
        self.email = email

    def add_user(self):
        self.user_database.add([str(self.user_id), self.name,
                                self.birthdate, self.location,
                                self.preferences, self.email, self.password])

    # @classmethod
    # def number_users(cls):
    #     cls.users = 5

def get_userinfo():
    user_database = Database("client_secret_1.json", "User Database")
    alldata = np.array(user_database.sheet.get_all_values())                        #was not able to slice ROW from list so I used numpy
    #return user_database.sheet.col_values(2), user_database.sheet.col_values(7)
    return alldata[1:,0], alldata[1:,1], alldata[1:,6] , alldata[1:,5], alldata[1:,8], user_database        #leave "user_database" in its position
                                                                                                            #I use -1 index to import it,
                                                                                                            #if you want to add to the list add before "user database"


# Testing
# if __name__ == '__main__':
