from project.backend import Database,Request,User,find
import time
import eel

@eel.expose
def log_out():
    pass

def login_acc(email, password, df):
    current_user = df[df['Email'] == email.lower()]
    if (current_user["Password"] == password).any():
        return True
    return False

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
    user_type = "Hyree" # This should be turned into an argument
    if user_type == 'Hyree':
        user_database = Database("client_secret_1.json", "User Database").get_all()
        if login_acc(email, password, user_database):
            eel.accept_hyree()
            return True
    return False


@eel.expose
def hyree_register(first_name, last_name, email, password1, password2):
    print(first_name, last_name, email, password1, password2)

    # ADD MORE CHECKS
    if email.lower() in ['exist@hyre.com']:
        eel.error_pop_up('This email is already registered!')
    elif password1 == password2:
        eel.hyreeRegisterAccepted()
    else:
        eel.error_pop_up('The password does not match')

@eel.expose
def hyrer_register(name, email, password1, password2):
    print(name, email, password1, password2)
    # name can be array (firstname, lastname) if personal, or string (companyname) for companies
    if password1 == password2:
        eel.hyrerRegisterAccepted()
    else:
        eel.error_pop_up('The password does not match')

@eel.expose
def choose_preferences(preferences):
    print(preferences)
    # go to database
    eel.preferences_accepted()
    # If preferences are rejected use: eel.error_pop_up("Your preferences were not saved!")

@eel.expose
def save_position(longitude, latitude):
    print(longitude, latitude)
    eel.location_accepted()
    #eel.location_rejected()

def main():
    pass


if __name__ == "__main__":
    main()
