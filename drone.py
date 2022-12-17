import os
import time
from time import sleep
from multiprocessing import Process
import hashlib


class Drone():
    def __init__(self,destiny) -> None:
        self.paylist = []
        self.filename = ''
        self.id = 0 # Четырехзначный вид надо сделать
        self.energy = 50
        self.location = [0,0,0]
        self.destiny = destiny
        self.tasks = []
        self.time = time.time()


    def PayList(self):
        for file in os.listdir():
            if 'paylist' in file: # Возможно несколько paylist
                self.filename = file
                break
        if self.filename:
            with open(self.filename,'r') as file: self.paylist = [line for line in file.readlines()]


    def generate_id(self):
        if not os.path.isfile('ids.txt'):
            with open('ids.txt','w+') as f: f.write('1')
        with open('ids.txt','r') as f:
            while True:
                try:
                    self.id = int(f.readline())
                    break
                except: pass
        with open('ids.txt','w') as f: f.write(str(self.id+1))


    def stat(self):
            
            with open(f'stats/{self.id}', 'w+') as f:
                f.write(f'''
ID = {self.id}
Energy = {self.energy}
Location = {self.location}
Destiny = {self.destiny}
Time = {time.time()-self.time}
                ''')


    def read_paylist(self):
        result = []
        for line in self.paylist:
            flag = False
            stack = []
            for i in line:
                if i == '{': flag = True
                elif i == '}':
                    flag = False
                    stack.append(' ')
                elif flag: stack.append(i)
            result.append(''.join(stack))
        # print(result)
        self.tasks = [x.split()[1] for x in result if int(x.split()[0].split('-')[1]) == self.id]

    def lidar(self):
        print('Дрон', self.id, 'занят lidar')
        sleep(5)
        self.energy -= 12
        # print(self.energy)
        if self.energy < 0: self.energy = 0
        print('Дрон', self.id, 'закончил lidar')

    def delivery(self):
        print('Дрон', self.id, 'занят delivery')
        sleep(5)
        self.energy -= 12
        # print(self.energy)
        if self.energy < 0: self.energy = 0
        print('Дрон', self.id, 'закончил delivery')
        
    def detection(self):
        print('Дрон', self.id, 'занят detection')
        sleep(5)
        self.energy -= 12
        # print(self.energy)
        if self.energy < 0: self.energy = 0
        print('Дрон', self.id, 'закончил detection')

    def impact(self):
        print('Дрон', self.id, 'занят impact')
        sleep(5)
        self.energy -= 12
        # print(self.energy)
        if self.energy < 0: self.energy = 0
        print('Дрон', self.id, 'закончил impact')

    def start(self):
        
        self.PayList() # paylist
        self.generate_id()
        p = Process(target=self.stat, args = ())
        
        self.read_paylist()

        task_dict = {
            'lidar':self.lidar,
            'delivery':self.delivery,
            'detection':self.detection,
            'impact':self.impact
        }
        first_hash = hashlib.md5(open(self.filename,'rb').read()).hexdigest()
        p.start()
        while True:
            
            for task in self.tasks:
                
                if self.energy >= 12:
                    p.join()
                    task_dict[task]()
                    p.start()
                    
                else:
                    print(f'Дрон {self.id} разряжен')
                    # p.join()
                    break
            p.join()
            self.tasks = []
            second_hash = hashlib.md5(open(self.filename,'rb').read()).hexdigest()
            if second_hash != first_hash:
                first_hash = second_hash
                self.PayList()
                self.read_paylist()




        
        


def launch(destiny = 'sky'):
    proc = Drone(destiny)
    proc.start()

if __name__ == '__main__':
    launch()
