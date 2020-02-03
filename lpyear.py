def is_leap(year):
    if year%4==0and(year%400==0 or year%100!=0) :
        return True
        
    else:
        return False
    
    # Write your logic here
    #return leap
year = int(input())
print(is_leap(year))
