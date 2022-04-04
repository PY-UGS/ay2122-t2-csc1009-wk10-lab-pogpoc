#=========== Q3 Part 1 ==============
def course_code_converter(argument):
    switchCase = {
        "CSC1009": "Object-Oriented Programming",
        "CSC1010": "Computer Networking",
        "CSC1008": "Data Structures & Algorithm",
    }
    return switchCase.get(argument, "Invalid Course Code!") 

if __name__ == "__main__":
    argument = 0
    print(course_code_converter("CSC1009"))

#=========== Q3 Part 2 ==============    
numberList = []

for x in range (66, 103):
    if x % 2 > 0:  
        numberList.append(x)

numberList.sort(reverse=True)
print(numberList)