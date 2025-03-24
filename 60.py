# 1650. Lowest Common Ancestor of a Binary Tree III

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def lowestCommonAncestor(self, node_p: 'Node', node_q: 'Node') -> 'Node':
        """Find the lowest common ancestor of two nodes in a binary tree with parent pointers.

        Args:
            node_p (Node): The first node.
            node_q (Node): The second node.

        Returns:
            Node: The lowest common ancestor of node_p and node_q.
        """
        a = node_p
        b = node_q
        while a != b:
            if a.parent:
                a = a.parent
            else:
                a = node_q
            if b.parent:
                b = b.parent
            else:
                b = node_p
        return a


"""
Как это работает?

Старт:
a начинает с p, b начинает с q.

Движение вверх:
Каждый шаг a и b поднимаются к своему родителю.
Если один из них достигает корня (parent == None), он "перепрыгивает" на начальную позицию другого.
a прыгает на q, если дошёл до корня.
b прыгает на p, если дошёл до корня.

Почему встреча в LCA неизбежна?

Пусть:
Lp = длина пути от p до LCA.
Lq = длина пути от q до LCA.
L = длина общего пути от LCA до корня.

Тогда:
a сначала пройдёт Lp шагов до LCA, потом L шагов до корня.
Потом он перепрыгнет на q и пройдёт ещё Lq шагов вверх до LCA.
Итого: a пройдёт Lp + L + Lq шагов.

Аналогично b:
Сначала Lq шагов до LCA, потом L до корня.
Потом перепрыгнет на p и пройдёт Lp шагов до LCA.
Итого: b пройдёт Lq + L + Lp шагов.

Вывод: Оба указателя пройдут одинаковое количество шагов (Lp + Lq + L) и встретятся ровно в LCA,
потому что после прохождения общего участка (L) они идут зеркально навстречу друг другу.


"""
