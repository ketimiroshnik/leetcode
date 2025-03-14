#560. Subarray Sum Equals K


def subarraySum(nums, k):
    ans = 0
    d = dict()
    d[0] = 1
    s = 0
    for i in range(len(nums)):
        s += nums[i]
        if (s - k) in d:
            ans += d[s-k]

        if s in d:
            d[s] += 1
        else:
            d[s] = 1
    return ans


print(subarraySum([1, 1, 1], 2))