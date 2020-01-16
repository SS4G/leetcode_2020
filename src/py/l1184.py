class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        totalDistance = sum(distance)
        if start < destination:
            minIdx, maxIdx = start, destination
        else:
            minIdx, maxIdx = destination, start
        halfSum = sum(distance[start: destination])
        return min(halfSum, totalDistance-halfSum)
