import re

from sympy import simplify
from sympy.parsing.sympy_parser import parse_expr

from sympy.logic.boolalg import BooleanFalse, BooleanTrue

def split(prog):
	return list(map(lambda a: a.strip(), prog.split(';')))

def parse_if(prog):
	cnd = '' ; th = '' ; el = ''
	nb = 0
	is_cnd = True ; is_th = False ; is_el = False

	for i in range(2, len(prog)):
		if prog[i] == '(':
			nb += 1
		if prog[i] == ')':
			nb -= 1

		if not is_el:
			if prog[i+1:i+5] == 'then' and nb == 0:
				is_cnd = False
				is_th = True

			if prog[i+1:i+5] == 'else' and nb == 0:
				is_th = False
				is_el = True

		if is_cnd:
			cnd += prog[i]
		if is_th:
			th += prog[i]
		if is_el:
			el += prog[i]

	cnd = cnd.strip()
	th = th.strip()[4:].strip()
	el = el.strip()[4:].strip()
	if th[0] == '(' and th[-1] == ')':
		th = th[1:-2].strip()
	if el[0] == '(' and el[-1] == ')':
		el = el[1:-2].strip()
	if cnd[0] == '(' and cnd[-1] == ')':
		cnd = cnd[1:-2].strip()
	return cnd, th, el 

def __weakest_precondition(prog, postcond):
	#print([prog, postcond])
	if prog.find(';') == -1 and not prog.startswith('if'):
		var, val = list(map(lambda a: a.strip(), prog.split(':='))) 
		# print([var, val])
		wp = postcond.replace(var, val)
		# print(wp, postcond)
		return wp
		ex = parse_expr(wp)#.simplify()
		if type(ex) not in (BooleanFalse, BooleanTrue):
			wp = str(ex)
		# print(wp, type(ex.simplify()))
		return wp
	elif prog.startswith('if'):
		cnd, then, els = parse_if(prog)
		#print([cnd, then, els])

		thwp = __weakest_precondition(then.strip(), postcond)
		thvc = '({}) & ({})'.format(cnd, thwp)
		#thwp = __weakest_precondition(then, thvc)

		elwp = __weakest_precondition(els.strip(), postcond)
		elvc = '(~({})) & ({})'.format(cnd, elwp)
		#elwp = __weakest_precondition(els, elvc)
		
		res = '(({}) | ({}))'.format(thvc, elvc)
		#res = '(({}) >> ({})) | (({}) >> ({}))'.format(thvc, thwp, elvc, elwp)

		# print(prog)
		
		# print([thvc, elvc])
		# print([thwp, elwp])
		#print([res])

		return res

	else:
		_prog = split(prog)
		#print(_prog)
		new_wp = __weakest_precondition(_prog[-1], postcond)
		#print([new_wp])
		__prog = ' ; '.join(_prog[:-1])
		#print([__prog])
		return __weakest_precondition(__prog, new_wp)

def weakest_precondition(prog, postcond):
	res = __weakest_precondition(prog, postcond)
	ex = res
	#ex = parse_expr(res).simplify()
	#print(type(ex))
	#print([ex, res])
	if type(ex) == BooleanTrue:
		return '0 = 0'
	elif type(ex) == BooleanFalse:
		return '1 = 0'
	else:
		#res = str(ex)
		#res = res.replace('>>', '?>')
		#res = res.replace('|', '||')
		#es = res.replace('&', '&&')

		return res


#print(__weakest_precondition('x := 5 ; if ( x > 5 ) then ( z := 3 ) else ( z := 6 ) ', 'z > 5'))