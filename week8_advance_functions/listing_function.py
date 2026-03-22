def fn1(num):
    return num + 1

x = 3
y = fn1(x)

print(x)
print(y)


def fn2(lyst):
    return lyst.append('a')

lyst_1 = [1,2,3]
print(lyst_1)

# This way is to actually add / append the 'a' into lyst_1 to = [1,2,3,a]
fn2(lyst_1)
print(lyst_1)




