import webbrowser
import time

total_breaks = 3
break_counter = 0

print ('Programs started on: ' + time.ctime())
while (break_counter < total_breaks):
    time.sleep(10)
    webbrowser.open('https://www.youtube.com/watch?v=NbESCYhKhxY&list=PLOYiOEBRifzdLalap_7sOj0x9u2UC1E0Y&index=6')
    break_counter = break_counter + 1