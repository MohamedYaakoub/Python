from project.backend import Database,Request,User,find
import time
import threading



# database = Database("client_secret_1.json", "User Database")
# df = database.get_all()

def login_acc(email, password, df):
    try:
        current_user = find(df, Email=email)[1].iloc[0]         #fix find
        # print(current_user)
        if current_user["Password"] == password:
            print("you are in!!")
                                                    # Here you can import all attributes such as Hyree ID, email, password
            index = find(df,Email = email)[0][0]
            print("your user id is " + str(current_user["Hyree ID"]))
            return current_user, index
    except IndexError:
        return False, print("Non existing email")
    return False, print("Incorrect Password")


# print(login_acc("meow","amen",Database("client_secret_1.json", "User Database").get_all()))


def online_log(database,index):
    database.add_cell(index, 8, "Online")
    while True:                                             #True essentially means that the user is online
        database.add_cell(index, 9, Request.get_time1())
        time.sleep(2)


# onlinelog = threading.Thread(target=online_log, args=(database,index), daemon=True)
# onlinelog.start()


def email_in_use(email, df):        ##New user##    #True if the email is not in use
    try:
        err = find(df, Email = email)[1].iloc[0]
        return False, print("Email already in use")
    except:
        return True , email


# if True move on to newuser
# if email_in_use("hehe",Database("client_secret_1.json", "User Database").get_all()) is True:


def newuser(name, email, D_O_B, Location, Prefrence, Password, df):
    user = User(name,
                D_O_B,  # give error if wrong format provided
                Location,
                Prefrence,  # should be a drop down menu
                email,
                Password)
    user.user_id = "Hy - " + str(user.user_id)
    user.add_user()
    print("User successfully added.")


def edit_user(user, database, name, D_O_B, Location, Prefrence, Password):
    email = user["Email"]
    user["Name"] = name
    user["Date of birth"] = D_O_B
    user["Location"] = Location
    user["Preferences"] = Prefrence
    user["Password"] = Password

    df = database.get_all()                     #refresh to make sure you are on the lastest version
    id = find(df,Email = email)[0][0]           #get id to communicate correctly with the data sheet

    database.sheet.update("A" + str(id) +":G" + str(id), [user[0:7].tolist()])
    return "user successfully added!"


# x = login_acc("meow","amen",Database("client_secret_1.json", "User Database").get_all())[0]
# edit_user(x, database, "ahmad", "20/12/6000", "singapore", "gardener", "amen")
