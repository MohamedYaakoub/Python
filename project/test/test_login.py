"""
Created on 27/09/2020

@author: Lucas V. dos Santos
"""


from project.backend import Database
from project.login import login_acc
import unittest

class testLogin(unittest.TestCase):

    def setUp(self):
        self.hyree = Database("../client_secret_1.json", "User Database").get_all()

    def test_hyree_log_in(self):
        self.assertEqual(login_acc('user@hyre.com','lucas',  self.hyree), True)
        self.assertEqual(login_acc('user@hyre.com', '123', self.hyree), False)

