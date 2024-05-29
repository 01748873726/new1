#my_set={1,2,3,4,5}
#print(my_set)
#my_set=set([1,2,3,4,5])
#print(my_set)

#my_set={1,2,3,4,5}
#for item in my_set:
    #print(item)
set1={1,2,3}
set2={3,4,5}

union=set1|set2
union_set=set1.union(set2)
print(union_set)

intersection=set1 & set2
intersection_set=set1.intersection(set2)
print(intersection_set)


set1.intersection_update(set2)
print(set1)

