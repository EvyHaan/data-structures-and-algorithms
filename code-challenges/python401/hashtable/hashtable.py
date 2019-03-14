
class Hashtable:

    _array = [None] * 1024

    def hash(self, key):
        stringified_key = str(key)
        ascii_sum = 0
        for c in stringified_key:
            ascii_sum += ord(c)
        bucket_number = (ascii_sum * 599) % 1024
        return bucket_number

    def add(self, key, value):
        pass

    def get(self, key):
        pass

    def contains(self, key):
        pass

    def __repr__(self):
        pass
