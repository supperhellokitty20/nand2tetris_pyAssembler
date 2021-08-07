import sys 


if __name__ == "__main__" :   
    '''
    print("This script is use for testing the file for different line\n ") 
    print("Please input files with this syntax : ./diff.py <file1> <file2> ") 
    print("After running the script will output different line of the file") 
    '''
    file_1= sys.argv[1]
    file_2= sys.argv[2]

    f1 =open(file_1,"r").readlines() 
    f2 =open(file_2,"r").readlines()  
    comp = zip(f1,f2)
    l=0 
    same = True  
    for x,y in comp :  
        l+=1 
        if x!=y : 
            same =False 
            print("At line ",l ) 
            print("file1",x) 
            print("file2",y) 
    if same :  
        print("WOAHHH it's the sameee LMAOOO") 


