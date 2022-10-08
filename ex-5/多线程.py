from threading import Thread
def fun(name):
    for i in range(1000):
        print(name,i)
def main():
    # 装载线程
    for i in range(1000):
        print("main",i)
# main()
T1 = Thread(target=fun,args=('liu',))
T2=Thread(target=fun,args=('1e',))
T1.start()
T2.start()
# class Mythread(Thread):
#     def run(self):
#         for i in range(1000):
#             print('fun',i)


