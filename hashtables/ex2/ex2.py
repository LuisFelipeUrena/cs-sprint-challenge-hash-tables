#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # first find which tickets are the starting tickets and which one is the end ticket
    for ticket in tickets:
        if ticket.source == None:
            

    return route
