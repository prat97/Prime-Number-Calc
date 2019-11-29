# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 14:11:21 2019

@author: Prat
"""

def iterative(num):
    
    while True:
        
        for i in range(2, num-1):
            
            if num % i == 0:
                
                return False
        
        return True

def calculate_iterative(num):
    
    while True:
        
        if iterative(num + 1):
            
            return num + 1
        
        num = num + 1
    

def recursive(num, d):
    
    if(d == 1):
        
        return True
    
    if(num % d == 0):
        
        return False
    
    return recursive(num, d-1)

def calculate_recursive(num):
    
    num = num
    
    while True:
        
        if recursive(num, num - 1):
            
            return num
        else:
            
            return calculate_recursive(num+1)
    
def main():
    
    x = 2
    x = calculate_recursive(x)
    print(x)
    ans = str(input("Do you want the next Prime number (Y or N): "))
    
    if ans != 'y' and ans != 'Y' and ans != 'n' and ans != 'N':
        
        ans = str(input("Please enter valid input! Do you want the next Prime number (Y or N): "))
    
    if ans == 'y' or ans == 'Y':
        
        while(True):
        
            x = calculate_recursive(x + 1)
            print(x)
            ans = str(input("Do you want the next Prime number (Y or N): "))
            
            if ans == 'n' or ans == 'N':
                
                break
            
            if ans == 'y' or ans == 'Y':
                
                continue
                
                ans = str(input("Please enter valid input! Do you want the next Prime number (Y or N): "))
    
    
if __name__ == '__main__':
    main()