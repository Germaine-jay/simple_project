import re

text_to_search = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

metacharacters (Neededto be escaped):
. ^ $ * + ? {} [] \ | ()

germanine.com

jsonosii@gmail.com
Germaine.100@yahoo.gov
Badb-07-007@Hotmail.net
tryboy09@me.org

321-555-4321
123.555.1234

Mr. Schafer
Mr Smith
Mrs Davis
Mrs. Robinson
Mr. T
'''

sentence = 'Start a sentence and thrn bring it to an end'


#pattern = re.compile(r'(?i)m(r|rs)\.?\s\w+')
#pattern = re.compile(r'(?i)\w+.*\-?\d?.?\d?.@\w+.\w+')#email
#pattern = re.compile(r'[a-zA-Z0-9.-]+\d?@[a-zA-Z.]+')#email
matches = pattern.findall(text_to_search)

for m in matches:
        print(m)
