D1 = {'A':1,'B':2,'C':3,'D':4}
D2 = {'A':10,'B':20,'X':3}

a_dict = {}

for key in D1:
    if key in D2:
        a_dict[key] = [D1[key], D2[key]]

print(a_dict)