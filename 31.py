# 71. Simplify Path


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        elements = path.split('/')
        now = []
        for elem in elements:
            if not elem:
                continue
            elif elem == '.':
                continue
            elif elem == '..':
                if now:
                    del now[-1]
            else:
                now.append(elem)
        return '/' + '/'.join(now)


s = Solution()
print(s.simplifyPath("/.../a/../b/c/../d/./"))

