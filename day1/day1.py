file =  open('input.txt')
list_of_items = file.read().splitlines()
nr_of_items = range(len(list_of_items))
current_record = 0
weight_of_current_elf = 0
for i in nr_of_items:
    if list_of_items[i] == '':
        current_record = max(current_record,weight_of_current_elf)
        weight_of_current_elf = 0
        continue
    weight_of_current_elf += int(list_of_items[i])
    if i == nr_of_items:
        current_record = max(current_record, weight_of_current_elf)
print(current_record)