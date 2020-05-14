import re

def __split(prog):
	return list(map(lambda a: a.strip(), prog.split(';')))

def parse_caseof(prog):
	cnd = ''
	eq_part = ''
	le_part = ''
	gr_part = ''

	_nbr = 0
	is_cnd = False ; is_eq = False ; is_le = False ; is_gr = False

	for i, c in enumerate(prog[4:]):
		if c == '(':
			_nbr += 1
		if c == ')':
			_nbr -= 1

		if _nbr == 1:
			if not is_cnd and not is_eq and not is_le and not is_gr:
				is_cnd = True
		if c == 'o' and prog[i+5] == 'f' and _nbr == 0:
			is_cnd = False
			is_eq = True
		if _nbr == 0 and c == '<':
			is_eq = False
			is_le = True
		if _nbr == 0 and c == '>':
			is_le = False
			is_gr = True

		if is_cnd:
			cnd += c
		if is_eq:
			if c in 'of:= ' and _nbr == 0:
				continue
			eq_part += c
		if is_le:
			if c in '< ' and _nbr == 0:
				continue
			le_part += c
		if is_gr:
			if c in '>; ' and _nbr == 0:
				continue
			gr_part += c

	cnd = list(map(lambda a: a.strip()[1:-1], cnd.strip()[1:-1].split('?')))
	eq_part = eq_part[1:-1]
	le_part = le_part[1:-1]
	gr_part = gr_part[1:-1]

	
	return {'cnd':cnd, 'eq_part':eq_part, 'le_part':le_part, 'gr_part':gr_part}

def __process_caseof(prog):
	d = parse_caseof(prog)

	res = 'if ({0} = {1}) then ({2}) else ( if ({0} < {1}) then ({3}) else ({4}))'\
			.format(*d['cnd'], d['eq_part'], d['le_part'], d['gr_part'])
	return res

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
		th = th[1:-1].strip()
	if el[0] == '(' and el[-1] == ')':
		el = el[1:-1].strip()
	if cnd[0] == '(' and cnd[-1] == ')':
		cnd = cnd[1:-1].strip()
	return cnd, th, el 

def __weakest_precondition(prog, postcond):
	if prog.find(';') == -1 and not prog.startswith('if') and not prog.startswith('case'):
		var, val = list(map(lambda a: a.strip(), prog.split(':='))) 

		wp = postcond.replace(var, val)

		return wp

	elif prog.startswith('case'):
		return __weakest_precondition(__process_caseof(prog), postcond)

	elif prog.startswith('if'):
		cnd, then, els = parse_if(prog)

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
