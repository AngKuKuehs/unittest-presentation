import requests

class Employee():
    def __init__(self, first_name, last_name, email, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.pay = pay

    def give_raise(self, raise_pct):
        self.pay *= (1 + raise_pct)
    
    def get_schedule(self):
        response = requests.get(f"http://production-server.com/get-sched?name={self.last_name}")
        if response.ok:
            return response.text
        else:
            return 'Bad Response!'
