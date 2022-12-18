import threading
import drone
from time import sleep
import os

class drone_generate(threading.Thread):
    def run(self):
        drone.launch()
        pass

if __name__ == '__main__': # Автогенерация дронов
    with open('status.txt', 'w+') as f: f.write('start')
    for i in range(10):
        thread = drone_generate()
        thread.start()
        del thread
        sleep(0.25)
    while True:
        if input() == 'break':
            with open('status.txt', 'w') as f: f.write('stop')
            break

