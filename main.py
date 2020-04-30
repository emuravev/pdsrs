import os

import examples as ex
from parser import parse_wp
from precondition import weakest_precondition
from utils import evaluate

wp = weakest_precondition(*ex.coins12)
print(wp)

print(evaluate(wp))

res = parse_wp(wp)

#print(res)

with open('/home/larry/Desktop/tmp/project/translator/limboole1.1/eqv.in', 'w') as f:
	f.write(res)

cmd = '../translator/limboole1.1/limboole /home/larry/Desktop/tmp/project/translator/limboole1.1/eqv.in'
os.system(cmd)
