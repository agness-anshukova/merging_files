import os
new_file = 'new_file.txt'
line_numbers = {}
line_numbers[sum(1 for line in open('1.txt'))] = '1.txt'
line_numbers[sum(1 for line in open('2.txt'))] = '2.txt'
line_numbers[sum(1 for line in open('3.txt'))] = '3.txt'

size_by_asc = sorted(line_numbers.keys())
print( line_numbers )

with open(new_file,'w') as fw:
    for item in size_by_asc :
        with open(line_numbers[item]) as fr:
            fw.write(f'\n\n{line_numbers[item]}\n')
            fw.write(f'\n{item}\n\n')
            for idx, l in enumerate(fr): 
                fw.write(l)    
