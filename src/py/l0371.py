class Solution(object):
    def most(self, a, b, c):
        if (a == 0 and b == 0 and c == 0) or\
           (a == 0 and b != 0 and c == 0) or\
           (a != 0 and b == 0 and c == 0) or\
           (a == 0 and b == 0 and c != 0):
           #print("lees")
           return False
        return True

    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        result = 0
        carryMask = 0
        for i in range(32):
            mask = (1 << i)
            thisBit = ((a ^ b) & mask) ^ carryMask
            carryMask = ((1 << i) << 1) if self.most(a & mask, b & mask, carryMask) else 0
            #print("this=", bin(thisBit), "carry=", bin(carryMask))
            result |= thisBit
        return result 

if __name__ == "__main__":
    s = Solution()
    print(s.getSum(3, 1))