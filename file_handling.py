f=open(r"C:\\Users\\Hp\\Documents\\employee.txt")
data=f.read().split("\n")
f.close()
s=0
dic={}
for l in data[1:]:
    d=l.split()
    dic[d[0]]=int(d[1])
    s+=int(d[1])

print(dic,"\nthe sum of salaries:",s)
