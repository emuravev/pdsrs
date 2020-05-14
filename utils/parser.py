import re
from functools import reduce

from utils.value import IntValue, VarValue

class Lexer(object):
	def __init__(self, lang):
		self.lang = lang

	def lex(self, pgm):
		res = []
		buff = ''
		for i in range(len(pgm)):
			buff += pgm[i]
			__buff = buff#.strip()
			for k, v in self.lang.items():
				if re.match(k, __buff) != None:
					res += [(__buff, v)]
					buff = ''
					break
			else:
				raise NameError('no such key \'{}\' in language'.format(__buff))
		return res

class Parser(object):
	def __init__(self):
		#! add language
		pass

	def parse(self, tokens):
		# comparison C -> IC | VC
		# int 
		# addition A -> IA | VA | VIA
		# vars addition: VA -> VAR AEQV VAR
		# var int addition: VIA -> VAR AEQV (INT | IA)
		# ints addition: IA -> (IA AEQV IA) | (INT AEQV INT)
		# var: VAR -> LETTER | (DIGIT | LETTER)
		# int: INT -> DIGIT | DIGIT
		pass

def parse_cmd(cmd):
	if cmd.find('=') != -1:
		c1, c2 = list(map(lambda a: a.strip(), cmd.split('=')))

		if c1.find('+') == -1:
			if not c1.isdigit():
				_c1 = VarValue(c1)
			else:
				_c1 = IntValue(int(c1))

		else:
			if c1.count('+') > 1:
				vals = list(map(lambda a: a.strip(), c1.split('+')))
				is_digit_vals = reduce(lambda a, b: a and b, list(map(lambda a: a.isdigit(), vals)))
				if is_digit_vals:
					_c1 = IntValue(sum(map(int, vals)))
				else:
					raise NameError('Not implemented')
			else:
				c1_1, c1_2 = list(map(lambda a: a.strip(), c1.split('+')))

				if not c1_1.isdigit():
					_c1_1 = VarValue(c1_1)
				else:
					_c1_1 = IntValue(int(c1_1))

				if not c1_2.isdigit():
					_c1_2 = VarValue(c1_2)
				else:
					_c1_2 = IntValue(int(c1_2))

				if type(_c1_1) == IntValue and type(_c1_2) == IntValue:
					_c1 = IntValue(_c1_1._val + _c1_2._val)
				else:
					_c1 = _c1_1 + _c1_2


		if c2.find('+') == -1:
			if not c2.isdigit():
				_c2 = VarValue(c2)
			else:
				_c2 = IntValue(int(c2))
		else:
			if c2.count('+') > 1:
				vals = list(map(lambda a: a.strip(), c2.split('+')))
				is_digit_vals = reduce(lambda a, b: a and b, list(map(lambda a: a.isdigit(), vals)))
				if is_digit_vals:
					_c2 = IntValue(sum(map(int, vals)))
				else:
					raise NameError('Not implemented')
			else:
				c2_1, c2_2 = list(map(lambda a: a.strip(), c2.split('+')))

				if not c2_1.isdigit():
					_c2_1 = VarValue(c2_1)
				else:
					_c2_1 = IntValue(int(c2_1))

				if not c2_2.isdigit():
					_c2_2 = VarValue(c2_2)
				else:
					_c2_2 = IntValue(int(c2_2))

				if type(_c2_1) == IntValue and type(_c2_2) == IntValue:
					_c2 = IntValue(_c2_1._val + _c2_2._val)
				else:
					_c2 = _c2_1 + _c2_2

		return _c1 == _c2


	elif cmd.find('>') != -1:
		c1, c2 = list(map(lambda a: a.strip(), cmd.split('>')))

		if c1.find('+') == -1:
			if not c1.isdigit():
				_c1 = VarValue(c1)
			else:
				_c1 = IntValue(int(c1))

		else:
			if c1.count('+') > 1:
				vals = list(map(lambda a: a.strip(), c1.split('+')))
				is_digit_vals = reduce(lambda a, b: a and b, list(map(lambda a: a.isdigit(), vals)))
				if is_digit_vals:
					_c1 = IntValue(sum(map(int, vals)))
				else:
					raise NameError('Not implemented')
			else:
				c1_1, c1_2 = list(map(lambda a: a.strip(), c1.split('+')))

				if not c1_1.isdigit():
					_c1_1 = VarValue(c1_1)
				else:
					_c1_1 = IntValue(int(c1_1))

				if not c1_2.isdigit():
					_c1_2 = VarValue(c1_2)
				else:
					_c1_2 = IntValue(int(c1_2))

				if type(_c1_1) == IntValue and type(_c1_2) == IntValue:
					_c1 = IntValue(_c1_1._val + _c1_2._val)
				else:
					_c1 = _c1_1 + _c1_2


		if c2.find('+') == -1:
			if not c2.isdigit():
				_c2 = VarValue(c2)
			else:
				_c2 = IntValue(int(c2))
		else:
			if c2.count('+') > 1:
				vals = list(map(lambda a: a.strip(), c2.split('+')))
				is_digit_vals = reduce(lambda a, b: a and b, list(map(lambda a: a.isdigit(), vals)))
				if is_digit_vals:
					_c2 = IntValue(sum(map(int, vals)))
				else:
					raise NameError('Not implemented')
			else:
				c2_1, c2_2 = list(map(lambda a: a.strip(), c2.split('+')))

				if not c2_1.isdigit():
					_c2_1 = VarValue(c2_1)
				else:
					_c2_1 = IntValue(int(c2_1))

				if not c2_2.isdigit():
					_c2_2 = VarValue(c2_2)
				else:
					_c2_2 = IntValue(int(c2_2))

				if type(_c2_1) == IntValue and type(_c2_2) == IntValue:
					_c2 = IntValue(_c2_1._val + _c2_2._val)
				else:
					_c2 = _c2_1 + _c2_2

		return _c1 > _c2

	elif cmd.find('<') != -1:
		c1, c2 = list(map(lambda a: a.strip(), cmd.split('<')))
		if c1.find('+') == -1:
			if not c1.isdigit():
				_c1 = VarValue(c1)
			else:
				_c1 = IntValue(int(c1))

		else:
			if c1.count('+') > 1:
				vals = list(map(lambda a: a.strip(), c1.split('+')))
				is_digit_vals = reduce(lambda a, b: a and b, list(map(lambda a: a.isdigit(), vals)))
				if is_digit_vals:
					_c1 = IntValue(sum(map(int, vals)))
				else:
					raise NameError('Not implemented')
			else:
				c1_1, c1_2 = list(map(lambda a: a.strip(), c1.split('+')))

				if not c1_1.isdigit():
					_c1_1 = VarValue(c1_1)
				else:
					_c1_1 = IntValue(int(c1_1))

				if not c1_2.isdigit():
					_c1_2 = VarValue(c1_2)
				else:
					_c1_2 = IntValue(int(c1_2))

				if type(_c1_1) == IntValue and type(_c1_2) == IntValue:
					_c1 = IntValue(_c1_1._val + _c1_2._val)
				else:
					_c1 = _c1_1 + _c1_2


		if c2.find('+') == -1:
			if not c2.isdigit():
				_c2 = VarValue(c2)
			else:
				_c2 = IntValue(int(c2))
		else:
			if c2.count('+') > 1:
				vals = list(map(lambda a: a.strip(), c2.split('+')))
				is_digit_vals = reduce(lambda a, b: a and b, list(map(lambda a: a.isdigit(), vals)))
				if is_digit_vals:
					_c2 = IntValue(sum(map(int, vals)))
				else:
					raise NameError('Not implemented')
			else:
				c2_1, c2_2 = list(map(lambda a: a.strip(), c2.split('+')))

				if not c2_1.isdigit():
					_c2_1 = VarValue(c2_1)
				else:
					_c2_1 = IntValue(int(c2_1))

				if not c2_2.isdigit():
					_c2_2 = VarValue(c2_2)
				else:
					_c2_2 = IntValue(int(c2_2))

				if type(_c2_1) == IntValue and type(_c2_2) == IntValue:
					_c2 = IntValue(_c2_1._val + _c2_2._val)
				else:
					_c2 = _c2_1 + _c2_2
		return _c1 < _c2

def parse_wp(wp):
	lang = {'^\($':'LBR', '^\)$':'RBR', '^>$':'GREATER', '^<$':'LESS', '^&$':'LAND', '^\|$':'LOR', '^~$':'LNOT', \
  		'^[a-z]$':'LETTER', '^[0-9]$':'DIGIT', '^\=$':'AEQV', '^\+$':'APLUS', '^\ $':'SPACE'}

	l = Lexer(lang)
	r = l.lex(wp)

	_res = ''; _buff = ''
	is_eqv = False

	for i, (c, t) in enumerate(r):
		if is_eqv:
			if t == 'RBR':
				is_eqv = False
				_res += str(parse_cmd(_buff.strip()))
				_buff = ''
				_res += c
				continue
			_buff += c
		else:
			if t == 'DIGIT':
				is_eqv = True
				_buff += c
				continue
			_res += c
	if _buff != '':
		_res += str(parse_cmd(_buff.strip()))

	return _res

def _old_parse_wp(wp):
	res = '' ; buf = ''
	is_eq = False
	for c in wp:
		if not is_eq:
			if c.isdigit():
				buf += c
				is_eq = True
				continue

			res += c
		else:
			if c.isdigit():
				buf += c
				res += str(parse_cmd(buf))
				buf = ''
				is_eq = False
				continue
			buf += c
	return res


def _parse_cmds(cmds):
	cmd = ''
	is_added = False
	pcmds = []
	#print(cmds)
	for i in range(1, len(cmds)):
		#print([i, cmd, pcmds])
		if cmds[i-1:i+1] == '&&':
			#pcmds += [' ( ']
			pcmds += [cmd.strip()]
			#pcmds += [' ) ']
			pcmds += [' & ']
			cmd = ''
			is_added = True
		elif cmds[i-1:i+1] == '||':
			#pcmds += [' ( ']
			pcmds += [cmd.strip()]
			#pcmds += [' ) ']
			pcmds +=[' | ']
			cmd = ''
			is_added = True
		elif cmds[i-1:i+1] == '?>':
			#pcmds += [' ( ']
			pcmds += [cmd.strip()]
			#pcmds += [' ) ']
			pcmds += [' -> ']
			cmd = ''
			is_added = True
		else:
			if is_added:
				is_added = False
				continue
			cmd += cmds[i-1]
	cmd += cmds[-1]
	#pcmds += [' ( ']
	pcmds += [cmd.strip()]
	#pcmds += [' ) ']
	#print(pcmds)

	for i in range(len(pcmds)):
		if pcmds[i].strip() in  ('&', '(', ')', '|', '->', '', '!'):
			continue
		else:
			pcmds[i] = str(parse_cmd(pcmds[i]))

	return ''.join(pcmds)