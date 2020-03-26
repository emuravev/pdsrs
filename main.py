import os
from parser import Lexer, parse_cmds
from precondition import weakest_precondition

prog = 'x := 5 ; y := 4 ; z := x + y'
vc = 'z > 5'

# prog = 'x := 5 ; if ( x > 5 ) then ( z := 3 ) else ( z := 6 ) '
# vc = 'z < 5'

wp = weakest_precondition(prog, vc)
res = parse_cmds(wp)

with open('/home/larry/Desktop/tmp/project/translator/limboole1.1/eqv.in', 'w') as f:
	f.write(res)

cmd = '../translator/limboole1.1/limboole /home/larry/Desktop/tmp/project/translator/limboole1.1/eqv.in'
os.system(cmd)