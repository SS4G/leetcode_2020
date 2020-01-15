from collections import Counter
class Solution(object):
    def binsearch(self, array, n):
        """
        array is sorted 
        find index where array[index] < n <= array[index + 1]
        """
        left = 0
        right = len(array) - 1
        mid = 0
        while left <= right:
            mid = (left + right) >> 1
            if array[mid] > n:
                right = mid - 1
            elif array[mid] < n:
                left = mid + 1
            else:
                left = mid + 1
        return right

    def numSmallerByFrequency(self, queries, words):
        """
        :type queries: List[str]
        :type words: List[str]
        :rtype: List[int]
        """
        words_fs = [self.f(w) for w in words]
        words_fs.sort()
        results = []
        for q in queries:
            res = self.binsearch(words_fs, self.f(q))
            #print(words_fs, self.f(q), res)
            results.append(len(words_fs) - 1 - res)
        return results

    def f(self, str0):
        cnt = Counter(str0)
        return cnt[min(cnt.keys())]

if __name__ == "__main__":
    s = Solution()
    queries = ["bbb","cc"]
    words = ["a","aa","aaa","aaaa"]
    print(s.numSmallerByFrequency(queries, words))