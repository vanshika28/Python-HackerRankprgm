def count_substring(string, sub_string):
    lst = len(string)
    lsub = len(sub_string)
    count = 0
    for i in range(0 ,(lst - lsub +1)):
        if(string[i]== sub_string[0]):
            k=1
            for j in range (0,lsub):
                if(string[i+j]!=sub_string[j]):
                    k=0
                    break
            if k==1:
                count +=1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
