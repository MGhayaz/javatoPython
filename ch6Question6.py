marks_input = int(input("Please enter marks: "))

if marks_input < 0 or marks_input > 100 : 
    print("Invalid Marks entered") 
    exit()

if(marks_input >= 90 and marks_input <= 100): print("Ex")

elif(marks_input >= 80 and marks_input <= 89): print("A")

elif(marks_input >= 70 and marks_input <= 79): print("B")

elif(marks_input >= 60 and marks_input <= 69): print("C")

elif(marks_input >= 50 and marks_input <= 59): print("D")

else: print("F")