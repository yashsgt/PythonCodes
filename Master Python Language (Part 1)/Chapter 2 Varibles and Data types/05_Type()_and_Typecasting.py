a = 5
t = type(a)
print(t)

b = 56.4
t = type(b)
print(t)

c = "Yash Rajput"
t = type(c)
print(t)

d = "45.88"
t = type(d)
print(t)

# Output for all those will come like <class 'x'> where, x may be int, float, str, etc.

a = "31.2"
b = float(a)  # 'a' but the type should be float. Here 'a' is used as a float function to store in 'b' 
t = type(b)  # We can covert any function into any another function with different variables by using this process......

print(t)
