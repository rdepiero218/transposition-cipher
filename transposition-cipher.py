

import random

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

keyword = 'HELP'

msg = 'FORTIFY THE EMBASSY PLR'

msg = msg.replace(' ', '')

msg_rows = []

for i in range(0, len(msg), len(keyword)):
    row = list(msg[i:i+4])
    print(row)
    msg_rows.append(row)

print(msg_rows)

if len(msg_rows[-1]) < len(keyword):
    num_letters_needed = len(keyword) - len(msg_rows[-1])
    for i in range(num_letters_needed):
        msg_rows[-1].append(random.choice(letters))


print(msg_rows)

# get column order
# need info from keyword - column order
keyword_vals = []


for char in keyword:
    char_index = letters.find(char)
    keyword_vals.append(char_index)
    print('char: ', char, 'index', char_index)

print('letter values = ', keyword_vals)

print('get column order')

col_order = []

tmp_key_vals = keyword_vals.copy()

for i in range(len(keyword_vals)):
    # get min value in list
    curr_min_val = min(tmp_key_vals)
    # get index of min value in orginal list
    curr_min_index = keyword_vals.index(curr_min_val)

    print('val = ', curr_min_val, 'index', curr_min_index)
    # add index to col order
    col_order.append(curr_min_index)
    # remove min value to find next min value
    tmp_key_vals.remove(curr_min_val)

    print('tmp_key_vals post remove', tmp_key_vals)

print('column order = ', col_order)

print('PRINT TRANSLATED MSG')
print('------------------------')
translated_msg = ''
for col in col_order:
    print('col', col)
    for row in msg_rows:
        print('row ', row)
        translated_msg += row[col]
        print(translated_msg)

print(translated_msg)

print_msg = ''
for i in range(0, len(translated_msg),3):
    print_msg += translated_msg[i:i+3] + ' '


print(print_msg)


## Decrypting

print('DECRYPTING - split up msg')

row_len = int(len(translated_msg)/len(keyword))

print(row_len)

transposed_msg = [ [] for i in range(row_len)]

for i in range(0, len(translated_msg)):

    


new_msg_rows = []

for i in range(0, len(translated_msg), row_len):
    
    row = list(translated_msg[i: i+row_len])
    new_msg_rows.append(row)

print(new_msg_rows)

translated_msg_rows = [ [] for i in range(row_len)]

print(translated_msg_rows)

for i in range(len(new_msg_rows)):

    for char in row:
        translated_msg_rows.append(new_msg_rows[char])

print(translated_msg_rows)