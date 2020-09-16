import eel

@eel.expose
def get_user_information():
    eel.sleep(3.0)  # Test if waiting for info works
    eel.writeUserInformation('ui@hyre.com', '123', 'Somewhere')

@eel.expose
def update_user_information(email, password, location):
    print(email, password, location)
    # get user information again to see if something has changed
    eel.sleep(1.0) # Test if waiting for updating info works
    #eel.updateAccepted()
    eel.updateRejected()