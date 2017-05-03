
#find the all combination of array
def find_container(n, containers):
    if n < 0:
        return [[]]
    if n == 0:
         return [[]]
    all_changes = []
    
    for last_used_container in containers:
        combos= find_container(n - last_used_container, containers)
        for combo in combos:
            combo.append((last_used_container))
            all_changes.append(combo) 
    return all_changes

k=5
container=[4,2]
all_result=find_container(k, container)
#print all_result
optimize=[]
closet=[]
#find exact match or cloaset one
for combo in all_result:
    if((len(optimize)==0 or len(combo)<=len(optimize)or (sum(combo)<sum(optimize))) and sum(combo)==k):
        optimize=combo
    elif((len(closet)==0 or len(combo)<=len(closet) or (sum(combo)<sum(closet)))  and sum(combo)>k):
        closet=combo

if(len(optimize)==0):
    print closet
else :
    print optimize
   