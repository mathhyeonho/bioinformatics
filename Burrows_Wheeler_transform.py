# The pre-requisites

data = "codespeedy"
# change to code download? txt file data after

data += '$'

words = list(data)

list = []

# Rotation of the string

for i in range(len(words)):
    word = data[-1] + data[:-1]
    new = ''.join(word)
    data = new
    list.append(new)

print(list)

# Sorting elements alphabetically/lexicographically

sort = sorted(list)

print(sort)

# Extracting last characters

for i in range(len(words)):
    element = sort[i]
    last = element[-1]
    print(last)