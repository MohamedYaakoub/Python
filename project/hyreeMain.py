"""
User Interface
"""

import eel
from hyreeLogin import *
from hyreeUpdateProfile import *
from hyreeDashboard import *





def main():
    """ Function that initiates the app's UI by using the eel package
        """
    eel.init('front_end')
    eel.start('home.html', size=(800, 1050))


if __name__ == "__main__":
    main()
