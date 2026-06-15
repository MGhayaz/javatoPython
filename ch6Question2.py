marksList = []
print("Subject 1 = physics, Subject 2 = Chemistry, Subject 3 = Maths, Subject 4 = Second Language, Subject 5 = First Language, Subject 6 = Social")
for i in range(6):
    marks = int(input(f"Please enter marks for Subject {i+1} : "))
    if marks < 0 or marks > 100 : 
        print("Invalid Marks entered")
        exit()
    else : marksList.append(marks) 

singleSubjectStatus = True
for marks in marksList : 
    if marks < 33 :
        singleSubjectStatus = False
  
total = sum(marksList)
percentage = total / len(marksList)

if percentage >= 40 :
    totalMarksStatus = True
else : totalMarksStatus = False

if singleSubjectStatus and totalMarksStatus :
    print("candidate is Qualified")
else : print("Promoted")    