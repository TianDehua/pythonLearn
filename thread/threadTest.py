import time, threading

#银行卡余额
balance = 0

lock = threading.Lock()

def change_it(n):
    #先存后取
    global balance
    balance += n
    balance -= n

def run_thread(n):
    for i in range(10000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()
        

# 创建一个线程 target 为函数，args为可变参数
t1 = threading.Thread(target=run_thread, args=(5, ))
t2 = threading.Thread(target=run_thread, args=(8, ))
t1.start()
t2.start()
t1.join()
t2.join()
print("balance=", balance)

