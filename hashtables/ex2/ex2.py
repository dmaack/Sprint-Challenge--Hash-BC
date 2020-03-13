#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """

    key = 'NONE'

    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    index = 0
    while index < length:
        cur_destination = hash_table_retrieve(hashtable, key)
        
        route[index] = cur_destination
        key = cur_destination
        index += 1
    route = route[:-1]
    return route
        

    print('route', route)
    # pass
