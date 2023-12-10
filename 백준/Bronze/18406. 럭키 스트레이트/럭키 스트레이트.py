number = str(input())
number_2 = int(len(list(number))/2)

num_1 = 0
num_2 = 0
for i in number[number_2:]:
    num_1 += int(i)

for i in number[:number_2]:
    num_2 += int(i)

if num_1 == num_2:
    print("LUCKY")
else:
    print("READY")