from solary import calculate_salary
from people import get_employees
from datetime import datetime
import subprocess

if __name__ == '__main__':
    print("Let's start")
    print()
    print('now_date: ', datetime.now())
    calculate_salary()
    get_employees()
# image2ascii 0.6.2 pip install image2ascii
# https://pypi.org/project/image2ascii/#description
    subprocess.run(['image2ascii', 'python_logo.png', '--color', '--fill'])
    print()
    print('Done')