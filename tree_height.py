import sys
import threading
import re
from array import *
import numpy as np

def compute_height(n, parents):
    nodes = np.zeros(n,dtype=int)
    tree_height = 0
    
    for i in range(n):
        length = 0
        par_of_i = i
        while par_of_i != -1:
            if nodes[par_of_i] != 0:
                length += nodes[par_of_i]
                break 
            else:
                length += 1
                par_of_i = parents[par_of_i]
                
        nodes[i] = length
        
        if length > tree_height:
            tree_height = length

    return tree_height

def main():
    command=input()
    parents=array('i')
    if 'I' in command:
        n=int(input())
        par=input()
        a=re.split(' ',par)
        for x in a: 
             parents.append(int(x))

    
    if 'F' in command:
        file=input()
        name="test/"+file
        if 'a' in file:
            print("wrong file name")
        else:
            with open(name,"r") as file:
                n=int(file.readline())
                lines=file.readlines()
                nodes=lines[1:]
                for nodes in lines:
                    a=re.split(' ',nodes)
                    for x in a:
                     parents.append(int(x))
                   
    
    length=compute_height(n,parents)
    print(length)
    
sys.setrecursionlimit(10**7)  
threading.stack_size(2**27)   
threading.Thread(target=main).start()
