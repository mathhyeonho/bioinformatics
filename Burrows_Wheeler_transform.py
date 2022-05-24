# The pre-requisites

data = "SIX.MIXED.PIXIES.SIFT.SIXTY.PIXIE.DUST.BOXES"
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


# Sorting elements alphabetically/lexicographically

sort = sorted(list)


# Extracting last characters

result = []

for i in range(len(words)):
    element = sort[i]
    last = element[-1]
    result.append(last)
print('transformed = ', ''.join(result))

# inverBWT

invert = ['' for _ in range(len(result))]
print(invert)

num = len(result)

for i in range(num):
    for j in range(num):
        invert[j] = result[j] + invert[j]
    invert.sort()
    print(invert)

print('inverted = ', invert[0])


    
