#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    hashtable = HashTable(length)
   

    # adding weights to the hashtable
    for w in range(len(weights)):
        hash_table_insert(hashtable, weights[w], w)
        
        

    # finding the goal weight between the goal indeces
    for w in range(len(weights)):
        goal_item_weight = limit - weights[w]
        goal_index = hash_table_retrieve(hashtable, goal_item_weight)
        
        # print('weight', w)
        # print('goal_index', goal_index)

        if goal_index is not None:
            if goal_index > w: # making sure the higher value is the first output in the tuple
                return (goal_index, w)
            return (w, goal_index)
        
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")


# print(get_indices_of_item_weights([4,6,10,15,16], 5, 21))
