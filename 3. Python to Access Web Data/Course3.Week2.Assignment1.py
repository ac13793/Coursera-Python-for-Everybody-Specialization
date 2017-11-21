import re
fileName = input("Enter file name")
print("File name:", fileName)
if(1 > len(fileName)):
    fileName = "regex_sum_50134.txt" #Name of actual data file name
try:
    fhand = open(fileName)
except:
    print("File does not exist!!")
count = 0
sum = 0
for line in fhand:
    line = line.strip()
    numbers = re.findall("([0-9]+)", line)
    if(0 < len(numbers)):
        for num in numbers:
            count = count + 1
            sum = sum + int(num)
print("Count:", count)
print("Sum:", sum)