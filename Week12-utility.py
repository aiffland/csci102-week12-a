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


def ScoreFinder(team, points, player):
    index=-1
    for i in range(len(team)):
        them=team[i].lower()
        dude=player.lower()
        if them==dude:
            index=i

    if index!=-1:
        result="OUTPUT "+team[index]+" got a score of "+str(points[i])
    if index==-1:
        result="OUTPUT player not found"

    return result


def Union(uno, dos):
    added=uno+dos
    endresult=[]
    for i in added:
        if i not in endresult:
            endresult.append(i)
    return endresult


def Intersection(uno, dos):
    added=uno+dos
    endresult=[]
    for i in uno:
        if i in dos:
            endresult.append(i)
    return endresult


