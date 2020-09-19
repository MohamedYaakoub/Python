from project.backend import Database,Request,User, get_userinfo
import time

def login():

    where = input(str("login or new user? "))   #implement in the UI

    if where == "login":
        username = input(str("username: "))
        pw = input(str("password: "))

        userinfo = get_userinfo()               #gurantees similar pull

        ids = userinfo[0].tolist()
        usernames = userinfo[1].tolist()         #Should login with Email!!
        passwords = userinfo[2].tolist()         #find better method?

        if username in usernames:
            index = usernames.index(username)
            if pw in passwords[index]:
                print("you are in!!")
                print("your user id is " + ids[index])

                #TODO: familirize the system with other information of the user
                #current_user =  #class
                online_log(userinfo[-1],1)

            else:
                print("Incorrect Password")     #user should try again
        else:
            print("Non existing username")      #user should try again

    elif where == "new user":
        emails = get_userinfo()[4].tolist()             #check with earlier better method
        email = input(str("Email: "))

        while email in emails:
            print("email already in use")
            email = input(str("Email: "))

        user = User(input(str("name: ")),
                    input(str("Data of birth ""dd/mm/yyyy"": ")),           #give error if wrong format provided
                    input(str("Location (where you currently live): ")),
                    input(str("Job Prefrences: ")),                         #should be a drop down menu
                    input(str(email)),
                    input(str("Password: ")))
        user.user_id = "Hy - " + str(user.user_id)
        user.add_user()
        print("User successfully added.")


def online_log(userinfo,index):
    userinfo.add_cell(index+1, 8, "Online")
    while True:       #True essentially means that the user is online
        userinfo.add_cell(index+1, 9, Request.get_time())
        time.sleep(15)


#online_log()
login()

