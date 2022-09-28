for x in range(0,151):
    print(x)

for x in range(0,1001,5):
    print(x)

for x in range(0,101):
    if x % 10 == 0:
        print("Coding Dojo")
    elif x % 5 == 0:
        print("Coding")
    else:
        print(x)

sum = 0
x = 1
while x <= 5000000:
    sum += x
    x += 2
print(sum)

for a in range(2018,0,-4):
    print(a)

low_num = 15
high_num = 43
mult = 7
for x in range(low_num,high_num+1):
    if x % mult == 0:
        print(x)