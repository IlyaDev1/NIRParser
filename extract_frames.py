from datetime import timedelta
import cv2
import numpy as np
import os
import face_recognition
import time

def get_saving_frames_durations(cap, saving_fps):
    """Функция, которая возвращает список длительностей сохраняемых кадров"""
    s = []
    # получаем длительность клипа, разделив количество кадров на количество кадров в секунду
    clip_duration = cap.get(cv2.CAP_PROP_FRAME_COUNT) / cap.get(cv2.CAP_PROP_FPS)
    # используем np.arange() для выполнения шагов с плавающей запятой
    for i in np.arange(0, clip_duration, 1 / saving_fps):
        s.append(i)
    return s

def prog(video_file):
    filename, _ = os.path.splitext(video_file)
    filename = filename.split("/")[1]
    # создаем папку по названию видео файла
    if not os.path.isdir(filename):
        os.mkdir(filename)
    # читать видео файл    
    cap = cv2.VideoCapture(video_file)

    # получить FPS видео
    fps = cap.get(cv2.CAP_PROP_FPS)
    if fps == 0:
        os.system(f'rmdir /s /q {filename}')
        print('fps = 0')
        return False


    clip_duration = cap.get(cv2.CAP_PROP_FRAME_COUNT) / fps
    saving_frames_per_second = 1 / (clip_duration / 10)

    # получить список длительностей кадров для сохранения
    saving_frames_durations = get_saving_frames_durations(cap, saving_frames_per_second)
    # начало цикла
    count = 0
    save_count = 0
    face_count = 0
    while True:
        is_read, frame = cap.read()
        if not is_read:
            # выйти из цикла, если нет фреймов для чтения
            break
        # получаем длительность, разделив текущее количество кадров на FPS
        frame_duration = count / fps
        try:
            # получить самую первоначальную длительность для сохранения
            closest_duration = saving_frames_durations[0]
        except IndexError:
            # список пуст, все кадры сохранены
            break
        if frame_duration >= closest_duration:
            # если ближайшая длительность меньше или равна длительности текущего кадра,
            # сохраняем фрейм      
            saveframe_name = f'{filename}/frame{save_count}.png'
            cv2.imwrite(saveframe_name, frame)
            save_count += 1
            # удалить текущую длительность из списка, так как этот кадр уже сохранен
            try:
                saving_frames_durations.pop(0)
            except IndexError:
                pass

            image = face_recognition.load_image_file(saveframe_name)
            face_locations = face_recognition.face_locations(image)
            if(face_locations):
                face_count += 1

        # увеличить счечик кадров count
        count += 1

    # os.system(f'rmdir /s /q {filename}')
    face_perc = face_count / save_count
    listForDel = []
    if(face_perc < 0.8):
        return False
    return True


def geno():
    dir = 'Video/'
    videos = os.listdir(dir)
    for i in range(len(videos)):
        video_file = dir + videos[i]
        time.sleep(2)
        print(f'{dir}{videos[i]}:\t', end='')
        if not prog(video_file):
            print('video is not ok\n\n')
            os.remove(f'{dir}{videos[i]}')
        else:
            print('video is ok\n\n')


geno()
