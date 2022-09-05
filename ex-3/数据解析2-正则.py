import re
s='''

'''
item1=re.compile(r'<div class=.*?>(?P<book_menu>.*?)</div>')
result=item1.finditer(s)
for item in result:
    print(item.group('book_menu'))

