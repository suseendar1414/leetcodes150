#solving every pattern problem
#pattern 1
# *
# **
# ***
# ****

# num = 4

def patternprob1(num):
    for row in range(num+1):
        for col in range(row):
            print('*',end=" ")
        print('\n')

#patter2
# *****
# *****
# *****
# *****
# *****

def patternprob2(num):
    for row in range(num+1):
        for col in range(num+1):
            print('*',end = " ")
        print('\n')

#pattern3
# *****
# ****
# ***
# **
# *

def patternprob3(num):
    for row in range(num+1,0,-1):
        for col in range(row):
            print('*',end = " ")
        print('\n')            



#pattern4 
# 1
# 12
# 123
# 12345

# num = 5

def patternprob4(num):
    for row in range(1,num+1):
        for col in range(1,row+1):
            print(col,end = " ")
        print('\n')  


#pattern 5
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *
# num = 10

def patternprob5(num):
    for row in range(1,(num+1)//2):
        for col in range(row):
            print("*",end = " ")
        print()
    for row in range((num//2),0,-1):
        for col in range(row):
            print("*",end = " ")
        print()
        # for col in range(row,0,-1):
        #     print("*",end = " " )


#      *
#     ***
#    *****
#   *******
#    *****
#     ***
#      *

# num = 5

def patternprob6(num):
    for row in range(num):
        for space in range(num-row):
            print(" ",end="")

        for col in range(2 * row -1):
            print("*",end = "")

        print()

    for row in range(num ,0,-1):
        for space in range(num - row):
            print(" ",end="")
        
        for col in range(2 * row - 1 ):
            print("*",end = "")

        print()


        #    333
        #    313
        #    323
        #    333

num = 4

def patternprob7(num):
    num = 2 * num
    for row in range(1,num -1):
        for col in range(1,num):
            hello = num - min(min(row,col),min(num - 1 - row,num - 1 - col))
            print(hello,end="")
        print()



patternprob7(num)