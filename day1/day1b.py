file =  open('input.txt')
list_of_items = file.read().splitlines()
nr_of_items = range(len(list_of_items))
list_of_weights = []
weight_of_current_elf = 0
for i in nr_of_items:
    if list_of_items[i] == '':
        list_of_weights += [weight_of_current_elf]
        weight_of_current_elf = 0
        continue
    weight_of_current_elf += int(list_of_items[i])
    if i == nr_of_items:
        list_of_weights += [weight_of_current_elf]

list_of_weights = sorted(list_of_weights,reverse=True)
print(sum(list_of_weights[0:3]))