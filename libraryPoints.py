import os
import random
#Library points tracker
#   IDs

#Bartavious#6327
#JakesKhakis247#8768
#PigeonAnon#1999
#Randoman#2408
#Quinnsky#0369
#crowbarsdeny#1361
#airlesswing#0022

#how to specific which player gets them?

userID = 'zac'


def get_name(userID):       #repalce userID with whatever discord needs
    players = ['BARTAVIOUS',
               'JAKESKHAKIS247',
               'PIGEONANON',
               'RANDOMAN',
               'QUINNSKY',
               'CROWBARSDENY',
               'AIRLESSWING']
    if userID in players:
        return players.index(userID)         #returns the palcement in the array. 
'''                                              #this gives us the line to edit for each players score
def award_points():
    #https://stackoverflow.com/questions/4719438/editing-specific-line-in-text-file-in-python
    with open('library_points.txt', 'rt+') as file:
        all_lib_points = file.readlines()     #reads all the lines

    current_value = all_lib_points[get_name(member.name)]
    reward = random.randint(1,11)
    final_value = int(current_value) + reward
    
    all_lib_points[get_name(userID)] = '%s\n' % str(final_value)   #gives us the line number, and types in a random librayr point value

    print('%d points to the member' %reward)
    
    with open('library_points.txt', 'rt+') as file:
        file.writelines(all_lib_points)


def revoke_points():
    with open('library_points.txt', 'rt+') as file:
        all_lib_points = file.readlines()     #reads all the lines

    current_value = all_lib_points[get_name(member.name)]
    reward = random.randint(1,11)
    final_value = int(current_value) - reward
    
    all_lib_points[get_name(userID)] = '%s\n' % str(final_value)   #gives us the line number, and types in a random librayr point value

    print('%d points from the member' %reward)
    
    with open('library_points.txt', 'rt+') as file:
        file.writelines(all_lib_points)
    



        
award_points()
revoke_points()
 
'''



#let's descope this a bit.
#   New task: Write a program that can keep track of a users' value (points)
with open("library_points.txt", "rt") as lp: #opens
    contents = lp.readlines()         #reads the file
#lp.close()
#print(contents)

#get users' LP value
get_name('AIRLESSWING')                     #REPLACE this with actual call from discord!!! member.name
contents[get_name('AIRLESSWING')] = '0'     #rewrites line to fit user

with open('library_points.txt', 'w') as file:
    file.writelines(contents)               #writes ot the file


#So, to just print value:  First we need a message, then figur eout name
#Just read out all library points
#   "Library Point score"
with open("library_points.txt", "rt") as lp: #opens
    contents = lp.readlines()         #reads the file

print("Zeezee has %s Library Points\nCora has %s Library Points\nAu Loria has %s Library Points\nArchibald has limitless Library Points\nRaiann has %s Library Points")



