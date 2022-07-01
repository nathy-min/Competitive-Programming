class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        boxTypes.sort(key=lambda x:0-x[1])
        print boxTypes
        
        counter=0
        units=0
        while counter < len(boxTypes) and truckSize >= boxTypes[counter][0] :
            units += boxTypes[counter][1] * boxTypes[counter][0] 
            truckSize -= boxTypes[counter][0]
            counter += 1
        if truckSize and counter < len(boxTypes):
            units += boxTypes[counter][1] * truckSize
        return units    