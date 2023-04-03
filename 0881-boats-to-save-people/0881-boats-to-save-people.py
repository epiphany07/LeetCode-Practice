class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        # print(people[-1]>=limit)
        c=0
        # if people[-1]+people[0]>limit:
        #     return len(people)
        # while people[-1]>=limit:
        #     print(people[-1])
        #     c+=1
        #     people.pop()
        print(c)
        x=0
        y=len(people)-1
        while x<=y:
            c+=1
            # print(x,y)
            if people[x]+people[y]<=limit:
                x+=1
            y-=1
    
        return c
            

        