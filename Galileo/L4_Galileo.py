import Galileo 
import time
import threading


def loop_nav(ID):
    Galileo.go_nav()
    
def loop_ballSeeker(ID):
    Galileo.go_ballSeeker()
    
def main():
    
    print("starting the main Fuction")
    time.sleep(1)
    threads = []
    
    t = threading.Thread(target=loop_nav, args =(1,) )
    threads.append(t)
    t.start()
    print("started thread1, for navigation")
    
    t2 = threading.Thread( target = loop_ballSeeker, args =(2,) )
    threads.append(t2)
    t2.start()
    print("started thread2, for looking for the ball")
    
    t.join()
    t2.join()
    state = Galileo.state()




Galileo.ball_look()
    
    