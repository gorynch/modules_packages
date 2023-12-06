from application.solary import calculate_salary
from application.db.people import get_employees
from datetime import datetime
import subprocess

if __name__ == '__main__':
    print("Let's start")
    print()
    print('now_date: ', datetime.now())
    calculate_salary()
    get_employees()
    print()
    print('Done')