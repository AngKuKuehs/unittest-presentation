import unittest
from unittest.mock import patch

import requests

from Employee import Employee

class TestEmployee(unittest.TestCase):
    """
    A test for the employee class should ensure that:
    """
    # @classmethod
    # def setUpClass(cls):
    #     return super().setUpClass()
    
    # @classmethod
    # def tearDownClass(cls):
    #     return super().tearDownClass()

    def setUp(self):
        self.emp_1 = Employee("John", "Ang", "johnang@email.com", 5000)
        self.emp_2 = Employee("Sean", "Ong", "seanong@email.com", 6000)
        self.emp_3 = Employee("Ryan", "Tan", "ryantan@email.com", 7000)
    
    def tearDown(self):
        pass

    def test_name_change(self):
        "Test case for name change"
        self.emp_1 = Employee("John", "Ang", "johnang@email.com", 5000)
        self.emp_2 = Employee("Sean", "Ong", "seanong@email.com", 6000)
        self.emp_3 = Employee("Ryan", "Tan", "ryantan@email.com", 7000)

        self.emp_1.first_name = "Bjorn"
        self.emp_2.first_name = "XiaoMing"
        self.emp_3.first_name = "XiaoHua"

        self.assertEqual(self.emp_1.first_name, "Bjorn")
        self.assertEqual(self.emp_2.first_name, "XiaoMing")
        self.assertEqual(self.emp_3.first_name, "XiaoHua")


    def test_email_change(self):
        "Test case for email change"
        self.emp_1 = Employee("John", "Ang", "johnang@email.com", 5000)
        self.emp_2 = Employee("Sean", "Ong", "seanong@email.com", 6000)
        self.emp_3 = Employee("Ryan", "Tan", "ryantan@email.com", 7000)

        self.emp_1.email = "Bjorn@gmail.com"
        self.emp_2.email = "XiaoMing@gmail.com"
        self.emp_3.email = "XiaoHua@gmail.com"

        self.assertEqual(self.emp_1.email, "Bjorn@gmail.com")
        self.assertEqual(self.emp_2.email, "XiaoMing@gmail.com")
        self.assertEqual(self.emp_3.email, "XiaoHua@gmail.com")

    def test_raise(self):
        "Test case for giving employees a raise"
        self.emp_1 = Employee("John", "Ang", "johnang@email.com", 5000)
        self.emp_2 = Employee("Sean", "Ong", "seanong@email.com", 6000)
        self.emp_3 = Employee("Ryan", "Tan", "ryantan@email.com", 7000)

        self.emp_1.give_raise(0.1)
        self.emp_2.give_raise(0.1)
        self.emp_3.give_raise(0.1)

        self.assertEqual(self.emp_1.pay, 5000 * 1.1)
        self.assertEqual(self.emp_2.pay, 6000 * 1.1)
        self.assertEqual(self.emp_3.pay, 7000 * 1.1)

    def test_get_schedule_mock(self):
        "Test case for getting schedule with mocked http requests"
        with patch('Employee.requests.get') as mocked_get:
            # Valid response
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Mon: 1500-1800; Tue: 0900-1200, 1400-1800; Thu: 0800-1200"

            schedule = self.emp_1.get_schedule()

            mocked_get.assert_called_with("http://production-server.com/get-sched?name=Ang")
            self.assertEqual(schedule, "Mon: 1500-1800; Tue: 0900-1200, 1400-1800; Thu: 0800-1200")

            # Invalid response
            mocked_get.return_value.ok = False
            mocked_get.return_value.text = None

            schedule = self.emp_2.get_schedule()

            self.assertEqual(schedule, "Bad Response!")

    def test_get_schedule_api(self):
        "Test case for getting schedule with local API"
        response = requests.get(f"http://0.0.0.0:5005/get-sched?name={self.emp_1.last_name}")

        with patch('Employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = response.ok
            mocked_get.return_value.text = response.text

            schedule = self.emp_1.get_schedule()

            mocked_get.assert_called_with("http://production-server.com/get-sched?name=Ang")
            self.assertEqual(schedule, "Mon: 1500-1800; Tue: 0900-1200, 1400-1800; Thu: 0800-1200")
