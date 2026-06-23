name = "Harry"#double qouted string

nameshort = name[0:3]

print(nameshort)
character1 = name[1]
print(character1)

print(name[-4:-1])
print(name[1:4])#negative slicing..use this trick
print(name[1:])#is same as print(name[1:5])
print(name[:4])#is same as print(name[0:4])
print(name[1:5])

# slicing  with skip
x = "0123456789"
print(x[1:8:3])