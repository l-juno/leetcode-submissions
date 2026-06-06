class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list()
        for n in range(len(position)):
            cars.append((position[n], speed[n]))
        cars.sort()
        
        fleetTime = []
        # initial fleet
        fleetTime.append((target - cars[-1][0]) / cars[-1][1])

        for i in range(len(cars)-2, -1, -1):
            currTime = (target - cars[i][0]) / cars[i][1]
            if currTime > fleetTime[-1]:
                fleetTime.append(currTime)
    
        return len(fleetTime)



        