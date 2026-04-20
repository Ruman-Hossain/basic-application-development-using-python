# While Loop In Python || Run Loop 3 Times
loop_control=1
while(loop_control<=3):
    age = int(input("Enter Your Age :"))
    if(age>=18):
        print(f"Test : {loop_control} : You are Eligible to be a Voter")
    else:
        print(f"Test : {loop_control} :You are not Eligible")
    loop_control = loop_control+1

# Foor Loop In Python || Run Loop 3 Times
for loop_control in range(1,4):
    age = int(input("Enter Your Age :"))
    if(age>=18):
        print(f"Test : {loop_control} : You are Eligible to be a Voter")
    else:
        print(f"Test : {loop_control} :You are not Eligible")
    loop_control = loop_control+1
