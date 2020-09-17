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
def register(email, password, password_repeat, user_type):
    print(email, password, password_repeat, user_type)

@eel.expose
def hyree_register(first_name, last_name, email, password1, password2):
    print(first_name, last_name, email, password1, password2)

    # ADD MORE CHECKS
    if password1 == password2:
        eel.hyreeRegisterAccepted()
    else:
        eel.hyreeRegisterRejected()

def main():
    pass


if __name__ == "__main__":
    main()
