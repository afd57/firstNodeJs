'''
Thread tutorial
'''
import time
from threading import Thread
import subprocess


def run_function(second):
    '''
    Sleeping function
    for thread tutorial
    '''
    subprocess.run("exit 1", shell=True, check=True)
    print(f"sleeping {second} sec from thread {second}")
    time.sleep(second)
    print(f"finished sleeping from thread {second}")


if __name__ == "__main__":
    list_of_thread = set()
    for i in range(5, 30):
        t = Thread(target=myfunc, args=(i,))
        list_of_thread.add(t)
        t.start()
    print('Threads has been started')
    [t.join() for t in list_of_thread]
    print('Threads is finish, Continue another line')
