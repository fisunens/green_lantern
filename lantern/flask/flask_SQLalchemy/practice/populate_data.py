import csv


def get_users():
    with open('users.csv', 'r') as file:
        reader = csv.DictReader(file)
        users = [i for i in reader]
    return users
