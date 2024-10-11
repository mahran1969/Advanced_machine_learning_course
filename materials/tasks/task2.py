#step_one
chr="###!!@mocleW EPGTQ!!!6789"
x=(chr.split("@")[1].split("!")[0])
print(x)
#step_two
m,h=(x.split(" "))
print(m[::-1])
om=h[::-1]
print(om)
#step_3
vowels="aeiouAEIOU"
for i in vowels:
  if i in om:
    o=om.replace(i,"")
    print(o) 
print(f"{m} {o}")
