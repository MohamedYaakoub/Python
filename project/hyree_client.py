from project.backend import Database,Request,User,find
import time
import threading

def login_acc(email, password, df):
    try:
        user = find(df, Email=email)[1].iloc[0]
        if user["Password"] == password:
            print("you are in!!")
            current_user = find(df, Email=email)[1].iloc[0]  # Here you can import all attributes such as Hyree ID, email, password
            print("your user id is " + current_user["Hyree ID"])
            return current_user
    except:
        print("Non existing email")
        pass
    return False, print("Incorrect Password")
#login_acc("yoyo","amen",Database("client_secret_1.json", "User Database").get_all())

def online_log(userinfo,index):
    userinfo.add_cell(index+2, 8, "Online")
    while True:       #True essentially means that the user is online
        userinfo.add_cell(index+2, 9, Request.get_time1())
        time.sleep(2)

# onlinelog = threading.Thread(target=online_log, args=(database,index), daemon=True)
# onlinelog.start()                                                                         #These should be implemented


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

def edit_user(user, name, email, D_O_B, Location, Prefrence, Password):
    user["Name"] = name
    user["Email"] = email
    user["Password"] = D_O_B
    user["Name"] = Location
    user["Email"] = Prefrence
    user["Password"] = Password
    #update name email password

def login():

    # where = input(str("login or new user? "))   #implement in the UI
    # database = Database("client_secret_1.json", "User Database")
    # user_database = database.get_all()


#online_log()
#login()

#TODO: add function that allwos for editing







#print(list(currentuser[1]))