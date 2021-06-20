# a programme with list of dictionaries that searches for the the number that ends with 8 and email that ends with .net
'''details=[{'name':'Todd', 'phone':'555-1414', 'email':'todd@mail.net'},
{'name':'Helga', 'phone':'555-1618', 'email':'helga@mail.net'},
{'name':'Princess', 'phone':'555-3141', 'email':''},
{'name':'LJ', 'phone':'555-2718', 'email':'lj@mail.net'}]

for i in range(len(details)):
    if (details[i]['phone'][-1])== '8':
        print(details[i]['name'])
    if '.net'not in details[i]['email']:
        print(details[i]['name'])'''


# a programme that searches for a number with a given condition
'''List = [1,14,5,9,12]
def NumList,condition):
    return ([i for i in List if eval(condition)])
print(Num(List,'i>11'))'''


# a programme that encodes a message and decodes it too
'''from random import*
num= input('enter sentence:')
alpha = 'abcdefghijklmnopqrstuvwxyz'
l= list('qwertyuiopasdfghjklzxcvbnm')
#shuffle(l)

encode = str.maketrans(dict(zip(alpha,l)))
decode = str.maketrans(dict(zip(l,alpha)))

encoded= num.translate(encode)
decoded= encoded.translate(decode)
print(encoded)
print(decoded)'''


# a programme that ask random questions from a list of questions and give sthe corresponding answer
'''from random import*
questions=['who is the best player in the world?:',
'who is the richest man in the world?:',
'who is the president of America?:', 
'who was the first man on the moon?:', 'ass or boobs:?']

anwsers=['lionel messi','jeff bezzos', 'donald trump', 
'codeine', 'boobs']
compiled = list(zip(questions,anwsers))
shuffle(compiled )
for i in range(len(questions)):
    guess = input(compiled [i][0])
    print('correct' if guess == compiled [i][1] else 'wrong')'''


# a programme that will tell you the current path a file is on you computer
'''from os import*
for (path, dirs, files) in walk ('C:/Users/INTEL/Documents/'):
    print('current path', path)
    print('directories', dirs)
    print('files', files)
    for filename in files:
        if filename[-3:]=='.py':
            print(filename)'''


# a programme that prints the number with odd occurences
'''def arr(n):
    a = max([i for i in n if (n.count(i)%2)!=0 or (n.count(i)==1)])
    return a
print(arr([5,4,3,2,1,5,4,3,2,10,10]))
print(arr([1,1,1,1,1,1,1,1,1,1,10,1]))
print(arr([20,1,1,2,2,3,3,5,5,4,20,4,5]))'''


# a python programme that will play an audio file from a known folder
'''from playsound import playsound
p = open('C:/Users/INTEL/Desktop/germaine python/N Brymo_Ara.MP3')
playsound ('C:\\Users\\INTEL\\Desktop\\germaine python\\N Brymo_Ara.MP3' )'''



# a python programme that converts a text to audio
'''from playsound import playsound
from gtts import*
def playaudio(audio):
        playsound(audio)
def convert_to_audio(text):
        audio = gTTS(text)
        audio.save('textaudio.mp3')
        playsound('textaudio.mp3')
convert_to_audio('johnson is a bad bad boy')'''


# playing with the datetime module
'''from datetime import*
d = datetime.now()
print(d.strftime('%x %X'))
print(d.strftime('%d %m %y %Y'))
print(d.strftime('%A %B %d'))
print(d.strftime('%a %b')) 
print(d.strftime('%H %I :%M'))'''


