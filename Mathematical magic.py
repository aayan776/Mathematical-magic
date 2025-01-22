#Armstrong number
number = int(input("Number: "))
digit = len(str(number))
result = 0
temp = number
while temp > 0:
    digit = temp % 10
    result += digit ** 3
    temp //= 10
if result == number:
    print(f"{number} is an Armstrong number")
else:
    print(f"{number} is not an armstrong number")
#Finding factors
def find_factors(num):
    print(f"The factors of {num} are:")
    for i in range(1, num + 1):
        if num % i == 0:
            print(i)
num = int(input("Enter number: "))
find_factors(num)
#Convert roman to integer
def roman_to_int(roman_inp):
    dict1 = {"M" : 1000, "D" : 500, "C" : 100, "L" : 50, "X" : 10, "V" : 5, "I" : 1}
    result_int = 0
    for i in range(0, len(roman_inp) - 1):
        if dict1[roman_inp[i]] < dict1[roman_inp[i + 1]]:
            result_int -= dict1[roman_inp[i]]
        else:
            result_int += dict1[roman_inp[i]]
    return result_int + dict1[roman_inp[-1]]
roman_inp = input("Input Roman numerals: ")
print(f"Integer value of roman numerals: {roman_to_int(roman_inp)}")