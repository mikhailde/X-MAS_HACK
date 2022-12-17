import random

class Drone:
    def __init__(self,i) -> None:
        self.id = i
        self.task = ''
        self.energy = 50
        self.location = [0,0,0]
        self.destiny = {random.choice(['sky','land'])}

    def read_paylist(self,paylist):
        stack = []
        for i in paylist:
            if i == '{': flag = True
            elif i == '}':
                flag = False
                stack.append(' ')
            elif flag: stack.append(i)
        if int(''.join(stack).split()[0].split('-')[1]) == self.id: self.task = ''.join(stack).split()[1] 
        print(self.task)
        self.start()

    def start(self):
        task_dict = {
            'lidar':self.lidar,
            'delivery':self.delivery,
            'detection':self.detection,
            'impact':self.impact
        }
        task_dict[self.task]()


drone_1=Drone(1)
drone_2=Drone(2)
drone_3=Drone(3)
drone_4=Drone(4)
drone_5=Drone(5)
drone_6=Drone(6)
drone_7=Drone(7)
drone_8=Drone(8)
drone_9=Drone(9)
drone_10=Drone(10)
drone_11=Drone(11)
drone_12=Drone(12)
drone_13=Drone(13)
drone_14=Drone(14)
drone_15=Drone(15)
drone_16=Drone(16)
drone_17=Drone(17)
drone_18=Drone(18)
drone_19=Drone(19)
drone_20=Drone(20)
drone_21=Drone(21)
drone_22=Drone(22)
drone_23=Drone(23)
drone_24=Drone(24)
drone_25=Drone(25)
drone_26=Drone(26)
drone_27=Drone(27)
drone_28=Drone(28)
drone_29=Drone(29)
drone_30=Drone(30)
drone_31=Drone(31)
drone_32=Drone(32)
drone_33=Drone(33)
drone_34=Drone(34)
drone_35=Drone(35)
drone_36=Drone(36)
drone_37=Drone(37)
drone_38=Drone(38)
drone_39=Drone(39)
drone_40=Drone(40)
drone_41=Drone(41)
drone_42=Drone(42)
drone_43=Drone(43)
drone_44=Drone(44)
drone_45=Drone(45)
drone_46=Drone(46)
drone_47=Drone(47)
drone_48=Drone(48)
drone_49=Drone(49)
drone_50=Drone(50)
drone_51=Drone(51)
drone_52=Drone(52)
drone_53=Drone(53)
drone_54=Drone(54)
drone_55=Drone(55)
drone_56=Drone(56)
drone_57=Drone(57)
drone_58=Drone(58)
drone_59=Drone(59)
drone_60=Drone(60)
drone_61=Drone(61)
drone_62=Drone(62)
drone_63=Drone(63)
drone_64=Drone(64)
drone_65=Drone(65)
drone_66=Drone(66)
drone_67=Drone(67)
drone_68=Drone(68)
drone_69=Drone(69)
drone_70=Drone(70)
drone_71=Drone(71)
drone_72=Drone(72)
drone_73=Drone(73)
drone_74=Drone(74)

while True:
    paylist = input()
    drone_1.read_paylist(paylist)