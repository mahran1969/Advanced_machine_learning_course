#step_one
text="&&&**$gnirtS PLIO!!@1234"
x=(text.split("$")[1].split("!")[0])
print(x)
#step_two
m,h=(x.split(" "))
z=(m[::-1])
print(z)
print(h[::-1])
#step_three
c=h.replace("I","E").replace("O","U")
print(c)
print(f"{z} {c}")
