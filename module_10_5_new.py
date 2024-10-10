import time
import multiprocessing as mp


def read_info(name):
    all_data = []
    with open(name,'r') as file:
        while True:
            s = file.readline()
            if s == '':
                break
            all_data.append(s)

if __name__ == '__main__':
    first_time = time.time()
    read_info('file 1.txt')
    read_info('file 2.txt')
    read_info('file 3.txt')
    read_info('file 4.txt')
    print(time.time() - first_time)
    with mp.Pool(processes=4) as pool:
        second_time = time.time()
        l = ['file 1.txt','file 2.txt','file 3.txt','file 4.txt']
        pool.map(read_info, l)
        print(time.time() - second_time)


