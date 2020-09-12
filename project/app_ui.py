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
    jobs = JobRequests("simulation/job_requests.csv")
    for _, row in jobs.available.iterrows():
        eel.post_job(row['company'], row['title'], row['description'], row['id'])


@eel.expose
def log_out():
    pass

@eel.expose
def log_in(email,password):
    if (email.lower()=="ui@hyre.com") and (password == '123'):
        eel.login_accepted()
    # pass

def main():
    eel.init('front_end')
    eel.start('login.html', size=(800, 1200))


if __name__ == "__main__":
    main()
