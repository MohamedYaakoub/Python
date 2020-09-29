from project.backend import Database, Request
import time
import eel

@eel.expose
def log_out():
    pass

def login_acc(email, password, df):
    """ Returns row of an user if log in is accepted


    :param email: User input email
    :param password: User input  password
    :param df: DataFrame of the Users Database

    :return: row of user accepted
    :rtype: int
    """
    current_user = df[df['Email'] == email.lower()]
    if (current_user["Password"] == password).any():
        return int(current_user.index[0] + 2), current_user['Hyree ID'].iloc[0]
    return False, False

def online_log(database,index):
    database.add_cell(index, 8, "Online")
    """ The while is still as a comment, because we still don't have a way of making it run in the bg"""
    # while True:
    #     database.add_cell(index, 9, Request.get_time1())
    #     time.sleep(2)

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
        user_database = Database("client_secret_1.json", "User Database")
        row, id = login_acc(email, password, user_database.get_all())
        if row:
            online_log(user_database,row)
            eel.accept_hyree(row,id)
            print(eel.user_row_id()())
            return True
        else:
            eel.error_pop_up("You have entered an invalid username or password!")
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
    user_database = Database("client_secret_1.json", "User Database").get_all()
    print(login_acc('user@hyre.com', 'lucas', user_database))


if __name__ == "__main__":
    main()
