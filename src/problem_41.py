# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Facebook.
#
# Given an unordered list of flights taken by someone, each represented as 
# (origin, destination) pairs, and a starting airport, compute the person's
# itinerary. If no such itinerary exists, return null. If there are multiple
# possible itineraries, return the lexicographically smallest one. All flights
# must be used in the itinerary.
#
# For example, given the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'),
# ('YUL', 'YYZ'), ('HKO', 'ORD')] and starting airport 'YUL', you should return
# the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].
#
# Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] and starting
# airport 'COM', you should return null.
#
# Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')]
# and starting airport 'A', you should return the list ['A', 'B', 'C', 'A', 'C']
# even though ['A', 'C', 'A', 'B', 'C'] is also a valid itinerary. However, the
# first one is lexicographically smaller.

def solution(L, airport):
    if L is None or len(L) == 0:
        return None

    # If there's only one element left and the first element is the airport,
    # then return the last element in the tuple. That is the final destination
    if len(L) == 1 and L[0][0] == airport:
        return list(L[0])

    # Search for the flight
    for i in range(0, len(L)):
      flight = L[i]

      if flight[0] == airport:
        # Remove this index from the list of flights
        L.pop(i)
        
        # Concatonate the origin flight with the rest of the list
        return [flight[0]] + solution(L, flight[1]) 

    # Airport not found
    return []
