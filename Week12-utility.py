# Aidan Iffland
# CSCI 102 Sec B
# Week 12 part A

def PrintOutput(string):
    begin="OUTPUT "
    string=begin+string
    return string


def LoadFile(string):
    tot_list=[]
    with open(string, 'r') as f:
        for line in f:
            tot_list.append(line)

    return tot_list


def UpdateString(string, letter, index):
    final=""
    change=list(string)
    change[int(index)]=letter
    for i in change:
        final+= i
    
    return final
    

def FindWordCount(list_boi, word):
    count=0
    for i in range(len(list_boi)):
        if list_boi[i]==word:
            count+=1

    return count
