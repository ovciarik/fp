# def _zip(*args):

#     to_iter = []
#     for arg in args:
#         to_iter.append(iter(arg))

#     result = []
#     try:
#         while True:
#             subresult = []
#             for i in to_iter:
#                 subresult.append(next(i))
#             result.append(subresult)
#     except:
#         pass

#     return result

# def zip2(a, b):

#     def _(a, b):

#         a_head = a[0]
#         a_tail = a[1:]
#         b_head = b[0]
#         b_tail = b[1:]

#         if a_tail == [] or b_tail == []:
#             return [(a_head, b_head)]
#         else:
#             return [(a_head, b_head), *_(a_tail, b_tail)]

#     return _(a, b)



def get_heads(*args):
    def _(a):
        head = a[0]
        head_head = head[0]
        tail = a[1:]
        if tail == [] or tail == tuple():
            return [head_head]
        else:
            return [head_head, *_(tail)]
    return _(args)

def get_tails(*args):
    def _(a):
        head = a[0]
        tail = a[1:]
        head_tail = head[1:]
        if tail == [] or tail == tuple():
            return [head_tail]
        else:
            return [head_tail, *_(tail)]
    return _(args)


def _zip(*args):
    def _(args):
        heads = get_heads(*args)
        tails = get_tails(*args)
        if not all(tails):
            return [heads]
        else:
            return [heads, *_(tails)]
    return _(args)


a = [1,2,3]
b = ['a', 'b', 'c']
c = ['a', 'b', 'c']

print(_zip(a, b, c))
print(_zip(a, b))
print(_zip(a))
# print(_zip([1]))

