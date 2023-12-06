from application.solary import calculate_salary
from application.db.people import get_employees
from datetime import datetime
import subprocess
import image2ascii
import subprocess

if __name__ == '__main__':
    print("Let's start")
    print()
    print('now_date: ', datetime.now())
    calculate_salary()
    get_employees()
    print('image2ascii: ',image2ascii.VERSION)
    subprocess.run(['image2ascii', 'python_logo.png', '--color', '--fill'])
    print()
    print('Done')
