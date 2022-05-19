import os

print(os.path.abspath('../'))

if not os.path.exists('./data'):
    os.mkdir('./data')

with open('./data/f.txt', 'w') as f_obj:
    f_obj.write("Hello World!")
    
print(os.path.basename('./data/f.txt'))