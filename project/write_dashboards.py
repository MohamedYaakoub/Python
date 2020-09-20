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
        self.active = self.job_offers[self.job_offers['status'] == "active"]


def write_available_jobs(jobs):
    """ Send to JS the available jobs to a hyree to be posted in their dashboard

        Args:
        jobs(df):  Data Frame with jobs available

         """
    if jobs.shape[0] > 0:
        for _, row in jobs.iterrows():
            eel.post_job(row['company'], row['title'], row['description'], row['id'])
    else:
        eel.printNoJobs()


def write_hyree_history(jobs):
    """ Send to JS the accepted or rejected jobs to the hyree profile page

            Args:
            jobs(df):  Data Frame with jobs available

             """
    if jobs.shape[0] > 0:
        for _, row in jobs.iterrows():
            eel.post_old_jobs(row['company'], row['title'], row['description'], row['id'])
    else:
        eel.printNoJobs()


def write_active_jobs(jobs):
    """ Send to JS the active jobs created by hyrer to be posted on his profile pages.

            Args:
            jobs(df):  Data Frame with jobs available

             """
    if jobs.shape[0] > 0:
        for _, row in jobs.iterrows():
            eel.post_active_job(row['company'], row['title'], row['description'], row['id'])
    else:
        eel.printNoJobs()


def write_accepted_jobs(jobs):
    """ Send to JS the jobs accepted to be posted on the hyrer dashboard

            Args:
            jobs(df):  Data Frame with jobs available

             """
    if jobs.shape[0] > 0:
        for _, row in jobs.iterrows():
            eel.post_accepted_job(row['company'], row['title'], row['description'], row['id'])
    else:
        eel.printNoJobs()


@eel.expose
def write_jobs(status, hyrer=False):
    """ This function receives the jobs from the db an call a function to print the jobs in the dashboards

    When the body of the hyreeDashboard.html file is loaded (<body onload="eel.write_jobs()">), this function
    is called to check what type of job needs to be printed ( Available, accepted or rejected). Then,
    This function calls either write_new_jobs() or write_new_jobs() to add the content in the dashboard

    Args:
            status(str):  str with type of job it is requested to write
            hyrer(bol):  True if the user is a hyrer
     """

    file = "simulation/job_requests.csv"
    jobs_data = JobRequests(file)

    if status == 'available':
        jobs = jobs_data.available
        write_available_jobs(jobs)
    elif status == 'accepted':
        jobs = jobs_data.accepted
        if hyrer:
            write_accepted_jobs(jobs)
        else:
            write_hyree_history(jobs)
    elif status == 'rejected':
        jobs = jobs_data.rejected
        if hyrer:
            write_hyree_history(jobs)
        else:
            write_hyree_history(jobs)
    elif status == 'active':
        jobs = jobs_data.active
        write_active_jobs(jobs)
    else:
        eel.printNoJobs()


@eel.expose
def get_new_job_data(job_type, job_other_type, job_description, job_offer, start_date, end_date):
    """ This function gets from js the data entered by a hyrer when requesting a new job

    Args:
    job_type(str):  Title of the job when selected from the options given to the user
    job_other_type(str): Title of the job when typed by the user
    job_description(str): Description of the job
    job_offer(int): Job value in euros estimated by the hyrer
    start_date(str): Start date (yyyy-mm-dd)
    end_date(str): End date (yyyy-mm-dd)
     """

    pass
