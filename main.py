from Task1 import run1
from Task2 import run2
from Task3 import run3
from Task4 import get_next_element

if __name__ == '__main__':
    run1('cat', 'annotationfor5cat.csv')
    run1('dog', 'annotationfor5dog.csv')

    run2('datasetlab5', 'annotation.csv')
    run3('annotation.csv', 'datasetcopy2')

    for item in get_next_element('сфе'):
        print(item)



#find . -name "*.DS_Store" -type f -delete