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
        self.accepted = self.job_offers[self.job_offers['status'] == "accepted"]
        self.rejected = self.job_offers[self.job_offers['status'] == "rejected"]


def write_new_jobs(jobs):
    if jobs.shape[0] > 0:
        for _, row in jobs.iterrows():
            eel.post_job(row['company'], row['title'], row['description'], row['id'])
    else:
        eel.printNoJobs()


def write_old_jobs(jobs):
    if jobs.shape[0] > 0:
        for _, row in jobs.iterrows():
            eel.post_old_jobs(row['company'], row['title'], row['description'], row['id'])
    else:
        eel.printNoJobs()


@eel.expose
def write_jobs(status):
    """ This function receives the jobs from the db an call a function to print the jobs in the dashboards

    When the body of the hyreeDashboard.html file is loaded (<body onload="eel.write_jobs()">), this function
    is called to check what type of job needs to be printed ( Availble, accepted or rejected). Then,
    This function calls either write_new_jobs() or write_new_jobs() to add the content in the dashboard
     """

    file = "simulation/job_requests.csv"
    jobs_data = JobRequests(file)

    if status == 'available':
        jobs = jobs_data.available
        write_new_jobs(jobs)
    elif status == 'accepted':
        jobs = jobs_data.accepted
        write_old_jobs(jobs)
    elif status == 'rejected':
        jobs = jobs_data.rejected
        write_old_jobs(jobs)
    else:
        eel.printNoJobs()


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
    else:
        eel.sleep(0.5)  # This sleep is needed to first load the page and then display the alert of Login rejected
        eel.login_rejected()
    # eel.login_accepted()


@eel.expose
def get_user_information():
    eel.sleep(3.0)  # Test if waiting for info works
    eel.writeUserInformation('ui@hyre.com', '123', 'Somewhere')

@eel.expose
def update_user_information(email, password, location):
    # get user information again to see if something has changed
    eel.sleep(1.0) # Test if waiting for updating info works
    #eel.updateAccepted()
    eel.updateRejected()




@eel.expose
def change_profile(email, password, location):
    # Check if something changed and save it in database
    print(email, password, location)


def main():
    """ Function that initiates the app's UI by using the eel package
        """
    eel.init('front_end')
    eel.start('home.html', size=(800, 1050))


if __name__ == "__main__":
    main()
