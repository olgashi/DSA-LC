num1 = '123'
num2 = '1000'

string_to_int = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '0': 0}
place_value = {0: 1, 1: 10, 2: 100, 3: 1000}

num1_arr = list(num1)
num2_arr = list(num2)
num1_arr = num1_arr[::-1]
num2_arr = num2_arr[::-1]
print(num1_arr)

sum1 = 0
sum2 = 0

for i in range(0, len(num1_arr)):
    mult = 0
    if string_to_int[num1_arr[i]] > 0:
        zeros = (10**i)
        if zeros == 0:
            mult = 1
        else:
            mult = zeros

        sum1 += mult * string_to_int[num1_arr[i]]

print(sum1)
for j in range(0, len(num2_arr)):
    mult = 0
    if string_to_int[num2_arr[j]] > 0:
        zeros = (10 ** j)
        if zeros == 0:
            mult = 1
        else:
            mult = zeros

        sum2 += mult * string_to_int[num2_arr[j]]

print(str(sum1 + sum2))