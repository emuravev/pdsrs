import re

from sympy import simplify
from sympy.parsing.sympy_parser import parse_expr

from sympy.logic.boolalg import BooleanFalse, BooleanTrue

def split(prog):
	return list(map(lambda a: a.strip(), prog.split(';')))

def __weakest_precondition(prog, postcond):
	if prog.find(';') == -1 and not prog.startswith('if'):
		var, val = list(map(lambda a: a.strip(), prog.split(':='))) 
		# print([var, val])
		wp = postcond.replace(var, val)
		# print(wp, postcond)
		return wp
		ex = parse_expr(wp).simplify()
		if type(ex) not in (BooleanFalse, BooleanTrue):
			wp = str(ex)
		# print(wp, type(ex.simplify()))
		return wp
	elif prog.startswith('if'):
		rcnd = re.compile('if \((.*)\) then')
		rthen = re.compile(' then \((.*)\) else')
		relse = re.compile(' else \((.*)\)')

		cnd = rcnd.search(prog).group(1)
		then = rthen.search(prog).group(1)
		els = relse.search(prog).group(1)

		thvc = '({}) & ({})'.format(cnd, postcond)
		thwp = __weakest_precondition(then, thvc)

		elvc = '({}) & ~({})'.format(cnd, postcond)
		elwp = __weakest_precondition(els, elvc)
		

		res = '({}) | ({}) >> ({})'.format(thwp, elwp, postcond)

		# print(prog)
		# print([cnd, then, els])
		# print([thvc, elvc])
		# print([thwp, elwp])
		# print([res])
		return res

	else:
		_prog = split(prog)
		#print(_prog)
		new_wp = __weakest_precondition(_prog[-1], postcond)
		# print(new_wp)
		__prog = ' ; '.join(_prog[:-1])
		#print(__prog)
		return __weakest_precondition(__prog, new_wp)

def weakest_precondition(prog, postcond):
	res = __weakest_precondition(prog, postcond)
	ex = parse_expr(res).simplify()
	#print(type(ex))
	#print([ex, res])
	if type(ex) == BooleanTrue:
		return '0 = 0'
	elif type(ex) == BooleanFalse:
		return '1 = 0'
	else:
		res = str(ex)
		res = res.replace('>>', '?>')
		res = res.replace('|', '||')
		res = res.replace('&', '&&')

		return res


print(__weakest_precondition('x := 5 ; if ( x > 5 ) then ( z := 3 ) else ( z := 6 ) ', 'z > 5'))