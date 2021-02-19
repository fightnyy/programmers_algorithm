
def solution(people, limit):
    people.sort()
    boat_num = 0
    first, last = 0,len(people)-1
    while first <= last:
        boat_num += 1
        if people[first]+people[last]<=limit:
            first+=1
        last -= 1
        
    return boat_num