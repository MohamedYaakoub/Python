"""
User Interface
"""

import eel
from login import log_in, log_out, register, hyree_register # pylint: disable=unused-import, disable=import-error
from hyree_update_profile import get_user_information, update_user_information # pylint: disable=unused-import, disable=import-error
from write_dashboards import JobRequests, write_available_jobs, write_hyree_history,write_active_jobs, write_accepted_jobs, write_jobs # pylint: disable=unused-import, disable=import-error

def main():
    """ Function that initiates the app's UI by using the eel package
        """
    eel.init('front_end')
    eel.start('home.html', size=(800, 1050))

if __name__ == "__main__":
    main()
