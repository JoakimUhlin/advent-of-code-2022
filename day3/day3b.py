file =  open('input')
list = file.read().splitlines()

def value(char):
    if char.islower():
        return ord(char)-96
    else:
        return ord(char)-38

accum_value = 0
for i in range(0,len(list),3):
    common = set(list[i]).intersection(set(list[i+1])).intersection(set(list[i+2])).pop()
    val = value(common)
    accum_value += val

print(accum_value)
