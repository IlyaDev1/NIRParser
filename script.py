from os import *


def ReName(user, num):
    dir = 'Video/'
    count = 0
    video = listdir(dir)
    for i in range(0, num):
        directory = dir + video[i]
        while directory[len(directory)-4::] != '.mp4':
            pass
        rename(f'{dir}{video[i]}', f'{dir}user{user}VideoNumber{count}.mp4')
        count += 1
