#step_one
x="Amit_ml@gmail.edu"
user_name=(x.split("@")[0])
print(user_name) 
#step_two
domain=(x.split("@")[1].split(".")[0])
print(domain)
endswith=x.split(".")[1]
#step_3
if endswith=="com":
  print("Commercial Domain")
elif endswith=="edu":
  print("Educational Domain")
else:
  print("other domain")


