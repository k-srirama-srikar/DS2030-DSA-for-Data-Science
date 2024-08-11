number = int(input())
bookmark_set = set()
s1 = 0
# is_happy = False if number!=1 else True
sum1 = 0
def recurr_sum(n):
    if n<10:
        return n**2
    else:
        s = recurr_sum(n//10) + (n%10)**2
        return s
s_init = recurr_sum(number)
is_happy = True if s_init == 1 else False
bookmark_set.add(s_init)
sum1 = s_init
while sum1 !=1:
    sum1 = recurr_sum(sum1)
    if sum1 == 1:
        is_happy = True
        break
    elif sum1 not in bookmark_set:
        bookmark_set.add(sum1)
    elif sum1 in bookmark_set:
        break

print(is_happy)


