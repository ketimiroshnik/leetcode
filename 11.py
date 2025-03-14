# 933. Number of Recent Calls

class RecentCounter(object):

    def __init__(self):
        self.times = []
        self.last_start_index = None
        self.n = 0

    def ping(self, t):
        if t is None:
            return None
        """
        :type t: int
        :rtype: int
        """
        self.times.append(t)
        self.n += 1

        if self.n == 1:
            self.last_start_index = 0
            return 1

        new = self.last_start_index
        for i in range(self.last_start_index, self.n):
            if t - self.times[i] > 3000:
                new += 1
            else:
                break

        self.last_start_index = new
        return self.n - self.last_start_index


obj = RecentCounter()
print(obj.ping(1))
print(obj.ping(100))
print(obj.ping(3001))
print(obj.ping(3002))