import threading, multiprocessing
from Student import Student

local_school = threading.local()

def loop():
    x = 0
    while True:
        x = x ^ 1

def process_student():
    std = local_school.student
    print('Hello, %s (in %s)' %(std.name, threading.current_thread().name))

def process_thread(name):
    local_school.student = name
    process_student()

if __name__ == '__main__':
    alice = Student('Alice')
    bob = Student('Bob')
    t1 = threading.Thread(target = process_thread, args = (alice,), name = 'Thread-A')
    t2 = threading.Thread(target = process_thread, args = (bob,), name = 'Thread-B')
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    