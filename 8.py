#22 Generate Parentheses

def recurs(now, opened_now, need_opened, need_closed, res):
    if need_opened == 0 and need_closed == 0:
        res.append(now)
        return
    if need_opened:
        recurs(now + "(", opened_now+1, need_opened-1, need_closed, res)
    if opened_now:
        recurs(now + ")", opened_now - 1, need_opened, need_closed - 1, res)




def generateParenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """
    res = []
    recurs("", 0, n, n, res)
    return res


a = generateParenthesis(4)
b = ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]

a.sort()
b.sort()

print(a)
print(b)