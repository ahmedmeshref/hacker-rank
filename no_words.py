#
# from collections import OrderedDict
#
# d= OrderedDict()
# n= int(input())
# for i in range(n):
#     s=input()
#     if s in d.keys():
#         d[s]+=1
#     else:
#         d[s]=1
# print(len(d.keys()))
# print(' '.join([str(d[k]) for k in d.keys()]))
# print(d)



def sort_l(l):
    count = 0
    for no_1 in l:
        for no_2 in l[count:]:
            if no_1 > no_2:
                l[count] = no_2
                l[count + 1] = no_1
                count += 1
    print(l)


l = [2, 0, 1, 3, 4, 2, 3]
sort_l(l)