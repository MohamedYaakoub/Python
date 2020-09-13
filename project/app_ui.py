"""
User Interface
"""

import eel
import pandas as pd


class JobRequests:
    """" This class handles the data from the job_requests database.

        Args:
        file (str): Path of the csv file with the job requests

        Attributes:
        df (str): This is where the data from the csv file is stored """

    def __init__(self, file):
        self.job_offers = pd.read_csv(file)
        self.available = self.job_offers[self.job_offers['status'] == "available"]


@eel.expose
def write_jobs():
    """ This function writes the available jobs for a user in the HTML file

    When the body of the main.html file is loaded (<body onload="eel.write_jobs()">), this function
    is called to write the available jobs to a user by using the JavaScript function eel.post_job()
     """
    jobs = JobRequests("simulation/job_requests.csv")
    for _, row in jobs.available.iterrows():
        eel.post_job(row['company'], row['title'], row['description'], row['id'])


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
        eel.login_accepted()
    # eel.login_accepted()


def main():
    """ Function that initiates the app's UI by using the eel package
        """
    eel.init('front_end')
    eel.start('login.html', size=(800, 1200))


if __name__ == "__main__":
    main()
