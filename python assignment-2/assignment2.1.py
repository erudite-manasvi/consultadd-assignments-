# Write a Python program to find the common elements between two lists.

#-------------------------------------Solution 1--------------------------------
def present(v1,v2):
        res = []
        
        for item in v1:
            if item in v2:
                res.append(item)
        
        res.sort()        
        return res
    
def common_element(v1,v2):
        if len(v2)>len(v1):
            return present(v1,v2)
            
        return present(v2,v1)


# -------------------------------------- Sloution 2--------------------------------

def common_element2(v1,v2):
    res = [x for x in v1 if x in v2]
        
    res.sort()
        
    return res

# ---------------------------------- Sloution 3-------------------------------
def common_element3(v1,v2):
        v1.sort()
        v2.sort()
        
        res=[]
        
        i=0
        j=0
        
        while(i<len(v1) and j<len(v2)):
            if v1[i]==v2[j]:
                res.append(v1[i])
                i+=1
                j+=1
                
            elif v1[i]<v2[j]:
                i+=1
            else: j+=1
        
        return res


#------------------------------------ Solution 4 ------------------------------
from collections import Counter

def common_element4(v1,v2):
        res = []
        
        track = Counter(v1)
        
        for item in v2:
            if track[item]>0:
                res.append(item)
                track[item]-=1
                
        res.sort()
        
        return res

l1 = [1, 2, 3, 4, 5]
l2 = [4, 5, 6, 7, 8]
print(common_element(l1,l2))