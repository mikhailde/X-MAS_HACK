import threading
import drone
from time import sleep


class drone_generate(threading.Thread):
    def run(self):
        drone.launch()
        pass

if __name__ == '__main__': # Автогенерация дронов
    for i in range(5):
        thread = drone_generate()
        thread.start()
        del thread
        sleep(0.25)
