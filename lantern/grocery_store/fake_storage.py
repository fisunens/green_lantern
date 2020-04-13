from itertools import count

from store_app import NoSuchUserError, NoSuchStoreError


class Repository:
    def __init__(self):
        self._objects = {}
        self._id_counter = count(1)


class FakeStorage:
    def __init__(self):
        self._users = FakeUsers()
        self._goods = FakeGoods()
        self._stores = FakeStores()

    @property
    def users(self):
        return self._users

    @property
    def goods(self):
        return self._goods

    @property
    def stores(self):
        return self._stores


class FakeUsers(Repository):

    def add(self, user):
        user_id = next(self._id_counter)
        self._objects[user_id] = user
        return user_id

    def get_user_by_id(self, user_id):
        try:
            return self._objects[user_id]
        except KeyError:
            raise NoSuchUserError(user_id)

    def update_user_by_id(self, user_id, user):
        if user_id in self._objects:
            self._objects[user_id] = user
        else:
            raise NoSuchUserError(user_id)


class FakeGoods(Repository, FakeStorage):

    def add(self, goods):
        for item in goods:
            self._objects[next(self._id_counter)] = item
        return len(goods)

    def get_goods(self):
        response = []
        for goods in self._objects.items():
            temp = goods[1]
            _id = {'id': goods[0]}
            temp.update(_id)
            response.append(temp)
        return response

    def update_goods(self, goods_upd):
        updated = 0
        not_exist = []
        for good in goods_upd:
            id_upd = good['id']
            data_upd = self._objects.get(id_upd, '')
            # found id for update
            if data_upd:
                self._objects.update({id_upd: good})
                updated += 1
            else:
                not_exist.append(id_upd)

        return {'successfully_updated': updated, 'errors': {'no such id in goods': not_exist}}


class FakeStores(Repository):

    def add(self, store):
        store_id = next(self._id_counter)
        self._objects[store_id] = store
        return store_id

    def get_store_by_id(self, store_id):
        try:
            return self._objects[store_id]
        except KeyError:
            raise NoSuchStoreError(store_id)

    def update_store_by_id(self, store_id, store):
        if store_id in self._objects:
            self._objects[store_id] = store
        else:
            raise NoSuchStoreError(store_id)
