n=int(input())
if n%2!=0:
        print("Weird")
elif n%2==0:
        if n in range(2,6):
                print("Not Weird")
        elif n in range(6,20):
                print("Weird")
        elif n in range(20,101):
                print("Not Weird")
else:
        print("Invalid input")
                
                
