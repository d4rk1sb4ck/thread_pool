from threading import Thread , Event
from socket import *
THREAD_STATE_NOT_USED = 1
THREAD_STATE_USED = 2
class CustomThread(Thread):
    def __init__(self,target,args):
        super().__init__(target=target,args=args)
        self.state = THREAD_STATE_NOT_USED
    def setState(self):
        self.state = THREAD_STATE_USED
class ThreadPool:
    def __init__(self,max_workers=300):
        self.main_list = []
        self.temp_list = []
        self.max_workers = max_workers
        Thread(target=self.run).start()
    def run(self):
        while True:
            self.charge()
            for thread in self.temp_list:
                if thread.state == THREAD_STATE_NOT_USED:
                    thread.start()
                    thread.setState()
                elif thread.state == THREAD_STATE_USED:
                    try:
                        if thread.is_alive():
                            pass
                        else:
                            self.temp_list.remove(thread)
                    except Exception as e:
                        pass

    def charge(self):
        while len(self.main_list) > 0 and len(self.temp_list) < self.max_workers:
            data = self.main_list[0]
            self.temp_list.append(data)
            self.main_list.pop(0)
    def appendThread(self,thread):
        self.main_list.append(thread)
