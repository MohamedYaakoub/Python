"""
User Interface
"""

import eel
from login import log_in, log_out # pylint: disable=unused-import, disable=import-error
from hyree_update_profile import get_user_information, update_user_information # pylint: disable=unused-import, disable=import-error
from hyree_dashboard import JobRequests, write_new_jobs, write_old_jobs, write_jobs # pylint: disable=unused-import, disable=import-error

def main():
    """ Function that initiates the app's UI by using the eel package
        """
    eel.init('front_end')
    eel.start('home.html', size=(800, 1050))

if __name__ == "__main__":
    main()
