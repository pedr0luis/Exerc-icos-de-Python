v1=0
v2=1
print(v1+v2)
for C in range(19):
    v3=v1+v2
    print(C+1, v3)
    v1=v2
    v2=v3
