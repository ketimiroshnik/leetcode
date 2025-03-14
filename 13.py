# 849. Maximize Distance to Closest Person

def maxDistToClosest(seats):
    """
    :type seats: List[int]
    :rtype: int
    """
    ans = 0
    was_one = 0
    now = 0
    for i in range(len(seats)):
        x = seats[i]
        if x == 0:
            now += 1
            continue

        if x == 1 and not was_one:
            was_one = 1
            ans = max(ans, now)
            now = 0
        else:
            ans = max(ans, now // 2 + now % 2)
            now = 0
    ans = max(ans, now)
    return ans


print(maxDistToClosest([0,1,0,0,0,0]))