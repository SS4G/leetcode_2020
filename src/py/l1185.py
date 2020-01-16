import datetime as dt
class Solution(object):
    def dayOfTheWeek(self, day, month, year):
        """
        :type day: int
        :type month: int
        :type year: int
        :rtype: str
        """
        week_list = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

        dtime = dt.datetime(year=year, day=day, month=month)
        return week_list[dtime.weekday()]

if __name__ == "__main__":
    s = Solution()
    print(s.dayOfTheWeek(10, 2, 2019))

