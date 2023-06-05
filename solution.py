class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:

        length = len(coordinates)
        point1 = []
        point2 = []
        found = False

        for i in range(length):
            for j in range(i+1,length):
                if coordinates[i][0] - coordinates[j][0] != 0:
                    point1, point2 = coordinates[i], coordinates[j]
                    found = True
                    break
            if found:
                break        

        if not found:
            return True

        slope = (point1[1]-point2[1])/(point1[0]-point2[0])

        for point in coordinates:
            if point[1] - point2[1] != slope * (point[0] - point2[0]):
                return False

        return True
