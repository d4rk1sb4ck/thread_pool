from thread_pool import ThreadPool , CustomThread

#Initiate ThreadPool
th = ThreadPool(max_workers=300)

#Simple Function
def test():
  print("Hello World!")
 
# Simply Append Thread To Start Proccess
th.appendThread(CustomThread(target=test,args=()))
