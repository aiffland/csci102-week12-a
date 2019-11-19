# Aidan Iffland
# CSCI 102 Sec B
# Week 12 part A

def PrintOutput(string):
    return print("OUTPUT", string)

def LoadFile(string):
    tot_list=[]
    with open(string, 'r') as f:
        for line in f:
            tot_list.append(line)

    return tot_list

    
            
