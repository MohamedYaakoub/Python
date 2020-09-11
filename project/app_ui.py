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
        self.df = pd.read_csv(file)
        self.available = self.df[self.df['status'] == "available"]


def main():
    eel.init('front_end')

    jobs = JobRequests("simulation/job_requests.csv")
    for index, row in jobs.available.iterrows():
        eel.post_job(row['company'],row['title'],row['description'],row['id'])


    eel.start('main.html', size=(800, 1200) )



if __name__ == "__main__":
    main()

