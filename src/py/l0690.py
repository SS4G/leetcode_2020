class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """
        epsDict = {}
        for ep in employees:
            epsDict[ep.id] = ep
        fifo = []
        fifo.append(id)
        rd = 0
        while rd < len(fifo):
            for subId in epsDict[fifo[rd]].subordinates:
                fifo.append(subId)
            rd += 1
        totalImportnce = 0
        for id in fifo:
            totalImportnce += epsDict[id].importance
        return totalImportnce

