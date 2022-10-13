#!/usr/bin/env python3
#intersection, difference, union and symetrical difference 
SetA={3,14,15,9,26,5,35,9}
SetB={60,22,14,0,9}

#intersection (elements in both sets)
print(SetA&SetB)

#difference
print(SetA-SetB)

#union combines both sets but removes duplicates
print(SetA|SetB)

#symemetrical difference (only in first set plus only in second set with duplicates removed)
print(SetA^SetB)
