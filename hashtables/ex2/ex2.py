#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    cache = {}
    # append each source as a key and the destination as the value in the cache
    for ticket in tickets:
        cache[ticket.source] = ticket.destination
    #create an array to hold the route 
    route = []
    # append the starting ticket
    route.append(cache['NONE'])
    # loop thru the array
    for ticket in tickets:
        # make the next ticket the last ticken in the route
        next_ = route[-1]
        # append the destination attached to that source to the route
        route.append(cache[next_])
        # if the last element in the route is none, we made it to the end.
        if route[-1] == "NONE":
            return route
        


    return route
