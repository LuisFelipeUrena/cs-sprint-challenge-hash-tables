def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # create a dictionary of weights and indices
    from itertools import permutations
    if len(weights) == 1:
        return None
    # weights = weights.sort()
    w_and_indices = {val:idx for idx,val in enumerate(weights)}
    if len(weights) > 2:
        possible_combinations = permutations(weights, 2)
        possible_combinations = list(possible_combinations)
        for i in possible_combinations:
            if sum(i) == limit:
                result = (w_and_indices[i[0]], w_and_indices[i[1]])
                result = sorted(result,reverse=True)
                return (result[0],result[1])
    elif sum(weights) == limit:
        result = [i for i, e in enumerate(weights)]
        result = sorted(result,reverse=True)
        return (result[0], result[1])
        
        # result = (w_and_indices[weights[1]], w_and_indices[weights[0]])
        # # result = sorted(result,reverse=True)
        # return (result[0],result[1])
        # return (w_and_indices[weights[0]], w_and_indices[weights[1]])
    else:
        return None 

    # return None        



    # return None
