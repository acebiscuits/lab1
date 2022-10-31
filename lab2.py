
import shutil
import random
import glob
import csv
import time
import cv2
import os 
                            
path = 'C:\\Users\\TUFman\\Desktop\\python\\python\\'
project_name = 'dataset'
folders = ['tiger', 'leopard']

def create_folder(path):
    if not os.path.exists(path):
        os.mkdir(path)

full_path = os.path.join(path, project_name)
create_folder(full_path)

for f in folders:
    folder = os.path.join(full_path, f)
    create_folder(folder)

class Iterator:
    def __init__(self, c_name):
        self.c_name = c_name
        self.counter = 0
        print(c_name)

    def __next__(self):
        self_path = 'C:\\Users\\TUFman\\Desktop\\python\\python\\dataset\\' + self.c_name + '\\' + str(self.counter).zfill(4) + '.jpg'
        if(os.path.exists(self_path)):
            #print(self_path)
            self.counter += 1
            return self_path
        else:
            raise StopIteration


def write_iteration_1(iter1, annotation_name):
    while(True):
        try:
            self_path = next(iter1)
            print(self_path)
            rel_path = 'python' + self_path.split('python')[2]
            print(rel_path)
            c_name = rel_path.split('\\')[2]
            print(c_name)
            with open(annotation_name, mode="a", encoding='utf-8') as write_file:
                file_writer = csv.writer(write_file, delimiter = ",", lineterminator="\r")
                file_writer.writerow([self_path, rel_path, c_name])
        except:
            break


annotation_name_1 = 'annotation_1.csv'
with open(annotation_name_1, mode="w", encoding='utf-8') as write_file:
    file_writer = csv.writer(write_file, delimiter = ",", lineterminator="\r")
    file_writer.writerow(['Абсолютный путь', 'Относительный путь', 'Класс'])


iter_1 = Iterator('tiger')
write_iteration_1(iter_1, annotation_name_1)

iter_2 = Iterator('leopard')
write_iteration_1(iter_2, annotation_name_1)

path_new = 'C:\\Users\\TUFman\\Desktop\\python\\data_new'
project_name_new = 'dataset'


create_folder(path_new)
    

full_path_new = os.path.join(path_new, project_name_new)
create_folder(full_path_new)

def copy_dataset(Iiter, annotation_name, new_path):
    while(True):
        try:
            print(new_path)
            self_path = next(Iiter)
            #print(self_path)
            add_path = self_path.split('\\dataset\\')[1]
            photo_path = os.path.join(new_path, add_path.split('\\')[0]) + '_' + add_path.split('\\')[1]
            #print(photo_path)
            shutil.copyfile(self_path, photo_path)
            relative_path = photo_path.split('\\python\\')[1]
            name_class = add_path.split('\\')[0]
            with open(annotation_name, mode="a", encoding='utf-8') as write_file:
                file_writer = csv.writer(write_file, delimiter = ",", lineterminator="\r")
                file_writer.writerow([photo_path, relative_path, name_class])
        except:
            break

annotation_name_2 = 'annotation_2.csv'
with open(annotation_name_2, mode="w", encoding='utf-8') as w_file:
    file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")
    file_writer.writerow(['Абсолютный путь', 'Относительный путь', 'Класс'])

Iiter1 = Iterator('tiger')
copy_dataset(Iiter1, annotation_name_2, full_path_new)

Iiter2 = Iterator('leopard')
copy_dataset(Iiter2, annotation_name_2, full_path_new)

random_number = list(range(0, 10001))
random.shuffle(random_number)

path_new_2 = 'C:\\Users\\TUFman\\Desktop\\python\\data_new_2'
project_name_new_2 = 'dataset'
    
create_folder(path_new_2)

full_path_new_2 = os.path.join(path_new_2, project_name_new_2)
create_folder(full_path_new_2)

def copy_dataset_2(Iiter, annotation_name, new_path, random_number):
    while(True):
        try:
            print(new_path)
            self_path = next(Iiter)
            #print(self_path)
            add_path = self_path.split('\\dataset\\')[1]
            #print(add_path)
            #print(random_number)
            photo_path = os.path.join(new_path, str(random_number.pop(0)).zfill(5)) + '.jpg'
            #print(photo_path)
            shutil.copyfile(self_path, photo_path)
            relative_path = photo_path.split('\\python\\')[1]
            name_class = add_path.split('\\')[0]
            with open(annotation_name, mode="a", encoding='utf-8') as write_file:
                file_writer = csv.writer(write_file, delimiter = ",", lineterminator="\r")
                file_writer.writerow([photo_path, relative_path, name_class])
        except:
            break

annotation_name3 = 'annotation_3.csv'
with open(annotation_name3, mode="w", encoding='utf-8') as w_file:
    file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")
    file_writer.writerow(['Абсолютный путь', 'Относительный путь', 'Класс'])

IIter1 = Iterator('tiger')
copy_dataset_2(IIter1, annotation_name3, full_path_new_2, random_number)

IIter2 = Iterator('leopard')
copy_dataset_2(IIter2, annotation_name3, full_path_new_2, random_number)
