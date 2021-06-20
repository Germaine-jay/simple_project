from datetime import*

# class To_do_list:
#     def __init__(task,date,time,duration):
#         self.task = task
#         self.date = date
#         self.time = time
#         self.duration = duration

#     def time(self):
#         time = datetime.()


# class task_scheduler :
# def to_do(task)
# task=[]
# print('enter task, date, time, duration :')
# schedule = input(':'), input(':'), input(':')
# schedule = list(schedule)
# task.append(schedule)
# i=1
# while i>1 :
#         print('enter task, date, time, duration :')
#         schedule = input(':'), input(':'), input(':')
#         schedule = list(schedule)
#         task.append(schedule)
#         i+=1 
# print(task)

#     def __init__(task,date,time):
#         for i in range(len(task_scheduler.task)):
#             self.task = task_scheduler.task[i][0]
#             self.date = task_scheduler.task[i][1]
#             self.time = task_scheduler.task[i][2]
#             # self.duration = duration
        
#     def meet(self):
#         return self.task
#     def date(self):
#         return self.date
#     def time(self):
#         return self.time

# n= task_scheduler.task
# print(n.meet(), n.date, n.time)


# print(task_scheduler)
# for i in range(len(p)):
#     print(p[i])

from datetime import*


# task=[]
# p=int(input('enter task range:'))
# i=0
# while i != p :
        # print('enter task_name, date, time, duration (minutes), description:')
        # schedule = input(':'), input(':'), input(':')
        # schedule = list(schedule)
        # task.append(schedule)
#         i+=1
# print(task)

# for i in range (len(task)):
# for order in task:
#         date_string = date(order[1])
#         p = date_string + timedelta(days=i)
#     print(datetime.strftime(p, '%A %B %d'))
#     print(' '.join(order))

# print('this is your task for ',day)
# print(task)




# a reminder that will terminate when you hit done
import re

# task_list= []
# for i in range(2):
#         # task = input('enter task name : ')
#         # task_time = input('enter task time : ')
#         task = 'kill someone'
#         task_time = '7-30'
#         task_time = re.sub(r'\D' , ':' ,task_time)
#         schedule = task,task_time
#         schedule = list(schedule)
#         task_list.append(schedule)
# for i in task_list:
#         print(i[1])

# from winsound import PlaySound
# PlaySound('SystemQuestion', )

from playsound import playsound
p = open('C:/Users/INTEL/Desktop/germaine python/N Brymo_Ara.MP3')
playsound ('C:\\Users\\INTEL\\Desktop\\germaine python\\N Brymo_Ara.MP3' )

# from playsound import playsound
# from gtts import*
# def playaudio(audio):
#         playsound(audio)
# def convert_to_audio(text):
#         audio = gTTS(text)
#         audio.save('textaudio.mp3')
#         playsound('textaudio.mp3')
# convert_to_audio('johnson is a bad bad boy')


# playsound ('N Brymo_Ara.MP3' )

# from winsound import*
# MessageBeep(type=MB_ICONHAND)

# from winsound import Beep
# Beep(500,1000)


task = []
print('enter task, date, time, duration :')
dates = eval(input('task date : '))
date = date(dates)
task_date = datetime.strftime(date, '%A %B %d')
schedule = input('task name:'), input('task time:'), input('task description:')
dictionary = dict([('task name',schedule[0]) , ('task time', schedule[1]), ('task description',schedule[2]), ('task date', task_date)])
task.append(dictionary)

while date != 'done':
        
        print('enter task, date, time, duration :')
        dates = eval(input('task date : '))
        date = date(dates)
        task_date = datetime.strftime(date, '%A %B %d')
        schedule = input('task name:'), input('task time:'), input('task description:')
        dictionary = dict([('task name',schedule[0]) , ('task time', schedule[1]), ('task description',schedule[2]), ('task date', task_date)])
        task.append(dictionary)

# printformat = '''
# task date = 
# task time = 
# task name =
# task description =  '''

                
print(task)