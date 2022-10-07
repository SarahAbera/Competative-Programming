881. Boats to Save People

class Solution(object):
    def numRescueBoats(self, people, limit):
        people.sort()
        i = 0
        j = len(people) -1 
        boats = 0
        while i <= j :
            weight = people[i] + people[j]
            if weight <= limit:
                i += 1
                j -= 1
            else:
                j-= 1
            boats += 1
        return boats 
