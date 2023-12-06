from application.solary import *
from application.db.people import *
from datetime import datetime

if __name__ == '__main__':
    print("Let's start")
    print()
    print('now_date: ', datetime.now())
    calculate_salary()
    get_employees()
    print()
    print('Done')