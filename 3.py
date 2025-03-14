# 443. String Compression

class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if not chars:
            return 0

        group = None
        count = 0
        index = 0
        for e in chars:
            if group is None:
                group = e
                count = 1
            elif group == e:
                count += 1
            else:
                chars[index] = group
                index += 1
                if count > 1:
                    for s in str(count):
                        chars[index] = s
                        index += 1

                group = e
                count = 1
        if group is not None:
            chars[index] = group
            index += 1
            if count > 1:
                for s in str(count):
                    chars[index] = s
                    index += 1
        return index


s = Solution()
print(s.compress(["a"]))