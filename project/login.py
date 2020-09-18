import eel

@eel.expose
def log_out():
    pass


@eel.expose
def log_in(email, password):
    """ This function approves or declines the log in of a user

        When the user try to log in, the JavaScript function login() sends to python the user email and password. If
        approved, python indicates to the JS function login_accepted() that the login was accepted.

        Args:
        email(str):  User email
        password(str): User password

        Returns:
        None

        """
    if (email.lower() == "ui@hyre.com") and (password == '123'):
        eel.accept_hyree()
    elif (email.lower() == "ui2@hyre.com") and (password == '123'):
        eel.accept_hyrer()
    else:
        eel.login_rejected()
    # eel.login_accepted()

@eel.expose
def hyree_register(first_name, last_name, email, password1, password2):
    print(first_name, last_name, email, password1, password2)

    # ADD MORE CHECKS
    if password1 == password2:
        eel.hyreeRegisterAccepted()
    else:
        eel.hyreeRegisterRejected()

@eel.expose
def hyrer_register(name, email, password1, password2):
    print(name, email, password1, password2)
    # name is array with [firstName, lastName, companyName]
    if password1 == password2:
        eel.hyrerRegisterAccepted()
    else:
        eel.hyrerRegisterRejected()

@eel.expose
def choose_preferences(preferences):
    print(preferences)
    # go to database
    eel.preferences_accepted()
    #eel.preferences_rejected()

@eel.expose
def save_position(longitude, latitude):
    print(longitude, latitude)
    eel.location_accepted()
    #eel.location_rejected()

def main():
    pass


if __name__ == "__main__":
    main()
