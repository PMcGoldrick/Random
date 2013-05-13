#!/usr/bin/env python
# -*- coding:utf-8 -*-
import timeit


l1 = [["a", "b", "c"], ["c", "d", "e"], ["e", "f", "g"]]

l2 = [["a", "b", "c"], ["c", "d", "e"], ["e", "f", "g"],
      ["g", "h", "i"], ["i", "j", "k"], ["k", "l", "m"]]

l3 = [["a", "b", "c", "m", "n", "o"], ["c", "d", "e", "o", "p", "q"],
      ["e", "f", "g", "q", "r", "s"], ["g", "h", "i", "s", "t", "u"],
      ["i", "j", "k", "u", "v", "w"], ["k", "l", "m", "w", "x", "y"]]


def something(L):
    """ Original implementation during interview
    Chose this over itertools implementation for explicitness and to
    illustrate my thought process.
    """
    d = {}
    for lst in L:
        for ele in lst:
            d[ele] = None
    return d.keys()


def useSets(L):
    """ Illustrating to a friend how much overhead the function calls produce
    when using set.add() """
    a = set()
    for lst in L:
        for ele in lst:
            a.add(ele)
    return list(a)


if __name__ == "__main__":
    t1 = timeit.timeit(stmt="""something(l1)""", setup="""from __main__ import something, l1, l2, l3""", number=100000)
    t2 = timeit.timeit(stmt="""something(l2)""", setup="""from __main__ import something, l1, l2, l3""", number=100000)
    t3 = timeit.timeit(stmt="""something(l3)""", setup="""from __main__ import something, l1, l2, l3""", number=100000)

    # Most optimal, less explicit, and what I would have actually done if not in an interview
    t4 = timeit.timeit(stmt="""list(set(itertools.chain(*l1)))""", setup="""import itertools;from __main__ import l1""", number=100000)
    t5 = timeit.timeit(stmt="""list(set(itertools.chain(*l2)))""", setup="""import itertools;from __main__ import l2""", number=100000)
    t6 = timeit.timeit(stmt="""list(set(itertools.chain(*l3)))""", setup="""import itertools;from __main__ import l3""", number=100000)

    t7 = timeit.timeit(stmt="""useSets(l1)""", setup="""from __main__ import useSets, l1, l2, l3""", number=100000)
    t8 = timeit.timeit(stmt="""useSets(l2)""", setup="""from __main__ import useSets, l1, l2, l3""", number=100000)
    t9 = timeit.timeit(stmt="""useSets(l3)""", setup="""from __main__ import useSets, l1, l2, l3""", number=100000)
    print t1, t2, t3
    print t4, t5, t6
    print t7, t8, t9

# 0.156848907471 0.241784095764 0.395983934402
# 0.128484010696 0.162086009979 0.242503881454
# 0.221457958221 0.350140094757 0.596086978912
