spamLine1 = "Make a lot of money"
spamLine2 = "buy now"
spamLine3 = "subscribe this" 
spamLine4 = "click this"

message = input("Please enter the Message : ")

if((spamLine1.lower() in message.lower()) or (spamLine2.lower() in message.lower()) 
   or (spamLine3.lower() in message.lower()) or (spamLine4.lower() in message.lower())):
    print("Spam Detected")
else :
    print("Good to go")    
