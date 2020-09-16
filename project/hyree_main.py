"""
User Interface
"""

import eel
from hyree_login import *
from hyree_update_profile import *
from hyree_dashboard import *

def main():
    """ Function that initiates the app's UI by using the eel package
        """
    eel.init('front_end')
    eel.start('home.html', size=(800, 1050))

if __name__ == "__main__":
    main()
