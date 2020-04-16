import os
from parser import parse_wp
from precondition import weakest_precondition
from utils import evaluate

# prog = 'x := 5 ; y := 4 ; z := x + y'
# vc = 'z > 5'

#prog = 'x := 7 ; if ( x > 5 ) then ( z := 3 ) else ( z := 6 ) '
#vc = 'z < 5'

#prog = 'e := 0 ; x := 2 ; y := 1 ; if ( x > y ) then ( e := 1 ) else ( e := 2 ) '#
#vc = '(e < 2) & (e = 1)'

# prog = 'd := 0 ; x := 1 ; y := 1 ; z := 1 ;'\
# 		' if ( x > y ) then ( if ( x > z ) then ( d := 1 ) else ( d := 3 ) ) else '\
# 		'( if ( y > z ) then ( d := 2 ) else ( d := 3 ) )'
# vc = 'd = 3'

prog = 'd := 0 ; x := 1 ; y := 1 ; z := 1 ; f := 1 ; '\
		'if ( x > y ) then ( if ( x > z ) then ( if ( x > f ) then ( d := 1 ) else ( d := 4 ) ) else '\
		' ( if ( z > f ) then ( d := 3 ) else ( d := 4 ) ) ) else ( if ( y > z ) then ( if ( y > f ) then ( d := 2 ) else ( d := 4 ) ) '\
		'else ( if ( z > f ) then ( d := 3 ) else ( d := 4 ) ) )'
vc = 'd = 4'

wp = weakest_precondition(prog, vc)
print(wp)
print(evaluate(wp))
res = parse_wp(wp)
print(res)

with open('/home/larry/Desktop/tmp/project/translator/limboole1.1/eqv.in', 'w') as f:
	f.write(res)

cmd = '../translator/limboole1.1/limboole /home/larry/Desktop/tmp/project/translator/limboole1.1/eqv.in'
os.system(cmd)