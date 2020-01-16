class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        answer = []
        lastValue = sum([i for i in A if (i & 1) == 0])
        for q in range(len(queries)):
            #print(q)
            val, index = queries[q][0], queries[q][1]
            if (A[index] & 1) == 0: # target even
                if (val & 1) == 0: # this even 
                    answer.append(lastValue + val)
                    lastValue += val
                else: # this odd
                    answer.append(lastValue - A[index])
                    lastValue -= A[index]
            else:# target odd
                if (val & 1) == 0: # this even 
                    answer.append(lastValue)
                else: # this odd
                    answer.append(lastValue + A[index] + val)
                    lastValue += (A[index] + val)
            A[index] += val
        return answer
