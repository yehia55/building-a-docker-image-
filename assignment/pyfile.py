import re
from string import digits
l1=open('/home/yahia/docker/assignment/book1','r')
book1=l1.read()
remove_digits = str.maketrans('', '', digits)
book1 = book1.translate(remove_digits)
book1= re.sub(r'[^\w\s]','',book1)
book1=re.sub(' +', ' ', book1)
book1=book1.split()
l2=open('/home/yahia/docker/assignment/book2','r')
book2=l2.read()
remove_digits = str.maketrans('', '', digits)
book2 = book2.translate(remove_digits)
book2= re.sub(r'[^\w\s]','',book2)
book2=re.sub(' +', ' ', book2)
book2=book2.split()
common=set(set(book1)&set(book2))
print(common)