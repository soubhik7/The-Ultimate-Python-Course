name = "Harry"

nameshort = name[0:3] # start from index 0 all the way till 3 (excluding 3)
text = "Python is awesome"
result = text.split('o')[1]  # Split by whitespace by default
print(result)
result2 = text.rsplit('o', 1)[1]
print(result2)

print(nameshort)
character1 = name[1]
print(character1)