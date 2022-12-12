import os
from typing import Optional, Union


def get_next_element(class_mark: str) -> Union[str, None]: # Optional[str]:
    '''path to the next instance of the class'''
    path = os.path.join("dataset", class_mark)
    names_list = os.listdir(path)
    names_list.append(None)
    for name in names_list:
        yield name