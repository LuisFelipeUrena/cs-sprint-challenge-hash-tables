def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    
    from itertools import permutations
    if length == 1:
        return None
    # creating a dictionary of weights and indices
    w_and_indices = {val:idx for idx,val in enumerate(weights)}
    # if the lenght is greater than 2
    if length > 2:
        # get all the possible combinations of the given list in tuples of 2
        possible_combinations = permutations(weights, 2)
        possible_combinations = list(possible_combinations) # put them in this list
        # loop thru the possible combinations
        for i in possible_combinations:
            # if the sum of any of the tuples is equal to the limit
            if sum(i) == limit:
                # wrap it all together and return that accordingly
                result = (w_and_indices[i[0]], w_and_indices[i[1]])
                result = sorted(result,reverse=True)
                return (result[0],result[1])
    elif sum(weights) == limit:
        # in this case the given list is only 2 items long so we simplify everything
        result = [i for i, e in enumerate(weights)]
        result = sorted(result,reverse=True)
        return (result[0], result[1])
        
    # otherwise just return none
    else:
        return None 
