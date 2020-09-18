from project.backend import Database,Request,User, get_userinfo

def login():

    where = input(str("login or new user? "))   #implement in the UI

    if where == "login":
        username = input(str("username: "))
        pw = input(str("password: "))

        ids = get_userinfo()[0].tolist()
        usernames = get_userinfo()[1].tolist()
        passwords = get_userinfo()[2].tolist()         #find better method?

        if username in usernames:
            index = usernames.index(username)
            if pw in passwords[index]:
                print("you are in!!")
                print("your user id is " + ids[index])
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
login()


