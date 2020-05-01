import csv


def get_users():
    with open('users.csv', 'r') as file:
        reader = csv.DictReader(file)
        users = [i for i in reader]
    return users


def get_goods():
    with open('goods.csv', 'r') as file:
        reader = csv.DictReader(file)
        goods = [i for i in reader]
    return goods


def get_stores():
    with open('stores.csv', 'r') as file:
        reader = csv.DictReader(file)
        stores = [i for i in reader]
    return stores
