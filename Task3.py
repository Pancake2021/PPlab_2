import os
import random
import shutil
import csv
from typing import Optional

from Task2 import create_dir


def get_element(class_name: str) -> Optional[str]:
    '''getting the path to the item'''
    for file_name in os.listdir(os.path.join("dataset", class_name)):
        yield file_name


def create_randomname_file(annotation_name: str, dir_copy: str) -> None:
    '''creating a file where the names will be in random order'''
    file_number = list(range(10001))
    random.shuffle(file_number)
    counter = 1
    create_dir(dir_copy)
    for dataset_class in os.listdir("dataset"):
        for file_name in get_element(dataset_class):
            shutil.copy(os.path.join(os.path.join("dataset", dataset_class), file_name),
                        os.path.join(dir_copy, f"{file_number[counter]}.jpg"))

            with open(os.path.join(dir_copy, annotation_name), mode="a", newline='') as file:
                file_writer = csv.writer(file, delimiter=",")
                file_writer.writerow([f"{file_number[counter]}.jpg", dataset_class])
            counter += 1


def run3(annotation_name: str, dir_copy: str) -> None:
    create_randomname_file(annotation_name, dir_copy)
