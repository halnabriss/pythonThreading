#!/usr/bin/python3
import time
import random
import threading


# The following function takes a delay per second parameter and a task number

def printNumber(delay, task):
  print("Starting task Number: " + str(task) + " The task expected to last for "+ str(mydelay) + " Seconds") 
  time.sleep(delay)
  print("Completed Task Number: "+ str(task) )


## The following for loop calls the previous function without threading
## This means that after completing one task, the next task starts

print("Now we are going to run the tasks without threading!!")

for x in range(1,5):
  mydelay = random.randint(1,10)
  printNumber(mydelay, x)



### In the following loop we are going to use threading to run all the tasks at once, then wait for
### each task to complete its delay timer
print("#####################################################################")
print("#####################################################################")
print("#####################################################################")
print("Run with threading, tasks with short timers will complete earlier")

for x in range(1,5):
  mydelay = random.randint(1,10)
  t = threading.Thread(target=printNumber, args=(mydelay,x))
  t.start()
