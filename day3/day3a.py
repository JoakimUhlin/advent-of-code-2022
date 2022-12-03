file =  open('input')
list = file.read().splitlines()

def value(char):
    if char.islower():
        return ord(char)-96
    else:
        return ord(char)-38

accum_value = 0
for element in list:
    le = len(element)
    mid = int(le/2)
    p1 = element[:mid]
    p2 = element[mid:]
    common = set(p1).intersection(set(p2)).pop()
    val = value(common)
    accum_value += val

print(accum_value)
