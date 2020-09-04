def intersection(arrays):
    """
    YOUR CODE HERE
    """
    cache = {}
    # loop thru the outer arrays
    for a in arrays:
        # loop thru each item in the inner array
        for i in a:
            # if the item is in the cache, add 1
            if i in cache:
                cache[i] += 1
            # otherwise just add 1 as the value
            else:
                cache[i] = 1
    #the results are the count of numbers that match the lenght of the array 
    results = [i for i in cache if cache[i]==len(arrays)]
    return results


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
