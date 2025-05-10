A = "Make a lot of money"
B = "buy now"
C = "subscribe this"
D = "click this"

message = input("Enter your Comment...... ")

if((A in message) or (B in message) or (C in message) or (D in message)):
    print("This comment is considered as spamm")
else:
    print("This comment is not considered as spamm")