names = [
    "Amit",
    "Rahul",
    "Priya",
    "Sneha",
    "Arjun",
    "Neha",
    "Rohit",
    "Pooja",
    "Kiran",
    "Anjali",
    "Vikram",
    "Meena",
    "Suresh",
    "Deepak",
    "Kavya",
    "Naveen",
    "Lakshmi",
    "Manoj",
    "Ayesha",
    "Ravi"
]

input =input("Name pls : ")
if(input in names) :
    print("Name Exists already")
else :
    print("New name detected")
    names.append(input)    