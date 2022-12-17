import random


with open('drone_simple.py', 'w') as f:
    for i in range(1,75):
        f.write(f'''
drone_{i}=Drone({i})''')