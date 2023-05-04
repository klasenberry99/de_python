
def modify_x():
    assert x<=5, 'x should not exceed 5. The value of x was {}'.format(x)
"""
try:
    x=10
    modify_x()
    
except:
    
    print('modify_x() function was not executed successly.')
    

    
try:
    x=10
    modify_x()  
    
except AssertionError as error:
    print(error)
    print('modify_x() function was not executed successly')
    print(error)
 """ 
 
def modify_x():
    assert x<=5, 'x should not exceed 5. The value of x was {}'.format(x)  
    
try:
    x=10 
    f=open('myfile.txt')
    modify_x() 
except FileNotFoundError as fnf_error:
    print(fnf_error)
    print('myfile.txt does not exist') 
except AssertionError as error:
    print(error)
    print('modify_x() function was not executed successly')