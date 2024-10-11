#step_one
chr="##$$$@!yalpstcejorp EPUVT****9887"
y=(chr.split("!")[1].split("*")[0])
print(y)
#step_two
m,h=(y.split(" "))
z=(m[::-1])
print(z)
print(h[::-1]) 
#step_three
c=h.replace("E","A").replace("U","O")
print(c) 
print(f"{z} {c}") 
