import codecs
import time
from threading import Thread
from time import sleep


def write_words(word_count, file_name):
    with codecs.open(file_name, 'w', 'utf-8') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {i}')
            sleep(0.1)


w5 = Thread(target = write_words,args=(10, 'example5.txt'))
w6 = Thread(target = write_words,args=(30, 'example6.txt'))
w7 = Thread(target = write_words,args=(200, 'example7.txt'))
w8 = Thread(target = write_words,args=(100, 'example8.txt'))

start = time.time()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

elapsed_mono = time.time() - start

start = time.time()


w5.start()
w6.start()
w7.start()
w8.start()

w5.join()
w6.join()
w7.join()
w8.join()

elapsed_multi = time.time() - start

print(f'mono: {elapsed_mono} \nthreaded: {elapsed_multi}')