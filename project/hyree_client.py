from project.backend import Database,Request,User,find
import time
import threading

def login():

    where = input(str("login or new user? "))   #implement in the UI
    database = Database("client_secret_1.json", "User Database")
    user_database = database.get_all()
    #usernames = user_database["Name"].tolist()
    passwords = user_database["Password"].tolist()
    emails = user_database["Email"].tolist()

    if where == "login":
        email = input(str("email: "))
        pw = input(str("password: "))

        if email in emails:
            index = emails.index(email)

            if pw in passwords[index]:
                print("you are in!!")
                current_user = find(user_database,Email=email)[1].iloc[0]       #Here you can import all attributes such as Hyree ID, email, password
                print("your user id is " + current_user["Hyree ID"])


                onlinelog = threading.Thread(target=online_log, args=(database,index), daemon=True)
                onlinelog.start()

                print("weeeeeeeeeeeeeeeeee")
                time.sleep(100)

            else:
                print("Incorrect Password")     #user should try again

        else:
            print("Non existing username")      #user should try again

    elif where == "new user":
        #emails = get_userinfo()[4].tolist()             #check with earlier better method
        email = input(str("Email: "))

        while email in emails:
            print("email already in use")
            email = input(str("Email: "))

        user = User(input(str("name: ")),
                    input(str("Data of birth ""dd/mm/yyyy"": ")),           #give error if wrong format provided
                    input(str("Location (where you currently live): ")),
                    input(str("Job Prefrences: ")),                         #should be a drop down menu
                    input(email),
                    input(str("Password: ")))
        user.user_id = "Hy - " + str(user.user_id)
        user.add_user()
        print("User successfully added.")
        login()             #to login again


def online_log(userinfo,index):
    userinfo.add_cell(index+2, 8, "Online")
    while True:       #True essentially means that the user is online
        userinfo.add_cell(index+2, 9, Request.get_time1())
        time.sleep(2)


#online_log()
#login()

#TODO: add function that allwos for editing







#print(list(currentuser[1]))