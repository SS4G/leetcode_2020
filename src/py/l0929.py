class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        uniqueEmailSet = set()
        for email in emails:
            pass
            sps = email.split("@")
            #print(sps)
            localName = sps[0]
            domain = sps[1]
            #print(localName)
            localName = localName.replace(".", "")
            brkIdx = 0
            idx = localName.find("+")
            if idx != -1:
                localName = localName[:idx]
            uniqueEmailSet.add("{}@{}".format(localName, domain))
        return len(uniqueEmailSet)

if __name__ == "__main__":
    s = Solution()
    l = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
    print(s.numUniqueEmails(l))
