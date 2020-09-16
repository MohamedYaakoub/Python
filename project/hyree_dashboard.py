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
