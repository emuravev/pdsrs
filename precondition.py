import re

def __split(prog):
	return list(map(lambda a: a.strip(), prog.split(';')))

def __parse_if(prog):
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
	if prog.find(';') == -1 and not prog.startswith('if'):
		var, val = list(map(lambda a: a.strip(), prog.split(':='))) 

		wp = postcond.replace(var, val)

		return wp

	elif prog.startswith('if'):
		cnd, then, els = __parse_if(prog)

		thwp = __weakest_precondition(then.strip(), postcond)
		thvc = '({}) & ({})'.format(cnd, thwp)

		elwp = __weakest_precondition(els.strip(), postcond)
		elvc = '(~({})) & ({})'.format(cnd, elwp)

		res = '(({}) | ({}))'.format(thvc, elvc)

		return res

	else:
		_prog = __split(prog)
		new_wp = __weakest_precondition(_prog[-1], postcond)
		__prog = ' ; '.join(_prog[:-1])

		return __weakest_precondition(__prog, new_wp)

def weakest_precondition(prog, postcond):
	return __weakest_precondition(prog, postcond)
