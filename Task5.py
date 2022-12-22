import csv
import os
from typing import Optional, Union


class IteratorTask1:
    '''iterator class for task 1'''
    def __init__(self, path: str) -> None:
        '''class constructor'''
        self.file_names = os.listdir(os.path.join('dataset', path))
        self.counter = 0
        self.limit = len(self.file_names)
        self.path = path

    def __next__(self) -> Union[str, None]:
        '''move on to the next element on the task after the iteration'''
        if self.counter < self.limit:
            self.counter += 1
            return os.path.join(self.path, self.file_names[self.counter-1])
        else:
            raise StopIteration

    def __iter__(self):
        return self


class IteratorTask2:
    '''iterator class for task 1'''
    def __init__(self, class_name: str,  path: str) -> None:
        '''class constructor'''
        self.file_names = os.listdir(os.path.join(path))
        for name in self.file_names:
            if not class_name in name:
                self.file_names.remove(name)

        self.limit = len(self.file_names)
        self.counter = 0
        self.path = path

    def __next__(self) -> Union[str, None]:
        '''move on to the next element on the task after the iteration'''
        if self.counter < self.limit:
            self.counter += 1
            return os.path.join(self.path, self.file_names[self.counter-1])
        else:
            raise StopIteration

    def __iter__(self):
        return self

class IteratorTask3:
    '''iterator class for task 1'''
    def __init__(self, class_name: str,  path: str, annotation_name: str) -> None:
        '''class constructor'''
        self.file_names = list()
        with open(os.path.join(path, annotation_name)) as file:
            reader = csv.reader(file, delimiter=',')
            for file_info in reader:
                if file_info[1] == class_name:
                    self.file_names.append()
        for name in self.file_names:
            if not class_name in name:
                self.file_names.remove(name)

        self.limit = len(self.file_names)
        self.counter = 0
        self.path = path

    def __next__(self) -> Union[str, None]:
        '''move on to the next element on the task after the iteration'''
        if self.counter < self.limit:
            self.counter += 1
            return os.path.join(self.path, self.file_names[self.counter-1])
        else:
            raise StopIteration

    def __iter__(self):
        '''iterator defining'''
        return self