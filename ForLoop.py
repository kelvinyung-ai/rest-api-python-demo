zen = '''
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
'''
for char in zen:
   if char not in 'aeiou':
      print (char, end='')

phrase = 'better than'
print('\n')

for line in zen.splitlines():
   if phrase in line:
      #print (line)
      print(line.replace(phrase, f"[{phrase}]"))