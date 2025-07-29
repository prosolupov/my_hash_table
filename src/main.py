from soupsieve.css_types import pickle_register

from src.hash_table import HashTable

if __name__ == '__main__':
    h = HashTable()
    print(len(h.get_all()))

    h.put(3, 'Один')
    h.put(11, 'Два')
    h.put(19, 'Три')

    print(hash(3))

    print(h.get(11).value)
    print(len(h.get_all()))

    print(h.remove(11))
    #
    # h.remove(4)

