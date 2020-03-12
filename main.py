from value import IntValue, VarValue

#cmds = 'x = 3 && y = 4 => z = x + y'
#cmds = 'x=4 && y=3 && z=7 => z=x+y'
#cmds = 'x=y => y=x'
cmds = 'a=3+a'
def parse_cmd(cmd):
	if cmd.find('=') != -1:
		c1, c2 = list(map(lambda a: a.strip(), cmd.split('=')))
		if c1.find('+') == -1:
			if not c1.isdigit():
				_c1 = VarValue(c1)
			else:
				_c1 = IntValue(int(c1))

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

			_c1 = _c1_1 + _c1_2


		if c2.find('+') == -1:
			if not c2.isdigit():
				_c2 = VarValue(c2)
			else:
				_c2 = IntValue(int(c2))
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
			c1_1, c1_2 = list(map(lambda a: a.strip(), c1.split('+')))

			if not c1_1.isdigit():
				_c1_1 = VarValue(c1_1)
			else:
				_c1_1 = IntValue(int(c1_1))

			if not c1_2.isdigit():
				_c1_2 = VarValue(c1_2)
			else:
				_c1_2 = IntValue(int(c1_2))

			_c1 = _c1_1 + _c1_2


		if c2.find('+') == -1:
			if not c2.isdigit():
				_c2 = VarValue(c2)
			else:
				_c2 = IntValue(int(c2))
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
			c1_1, c1_2 = list(map(lambda a: a.strip(), c1.split('+')))

			if not c1_1.isdigit():
				_c1_1 = VarValue(c1_1)
			else:
				_c1_1 = IntValue(int(c1_1))

			if not c1_2.isdigit():
				_c1_2 = VarValue(c1_2)
			else:
				_c1_2 = IntValue(int(c1_2))

			_c1 = _c1_1 + _c1_2


		if c2.find('+') == -1:
			if not c2.isdigit():
				_c2 = VarValue(c2)
			else:
				_c2 = IntValue(int(c2))
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

			_c2 = _c2_1 + _c2_2

		return _c1 < _c2


def parse_cmds(cmds):
	cmd = ''
	is_added = False
	pcmds = []
	for i in range(1, len(cmds)):
		if cmds[i-1:i+1] == '&&':
			pcmds += [' ( ']
			pcmds += [cmd.strip()]
			pcmds += [' ) ']
			pcmds += [' & ']
			cmd = ''
			is_added = True
		elif cmds[i-1:i+1] == '||':
			pcmds += [' ( ']
			pcmds += [cmd.strip()]
			pcmds += [' ) ']
			pcmds +=[' | ']
			cmd = ''
			is_added = True
		elif cmds[i-1:i+1] == '=>':
			pcmds += [' ( ']
			pcmds += [cmd.strip()]
			pcmds += [' ) ']
			pcmds += [' -> ']
			cmd = ''
			is_added = True
		else:
			if is_added:
				is_added = False
				continue
			cmd += cmds[i-1]
	cmd += cmds[-1]
	pcmds += [' ( ']
	pcmds += [cmd.strip()]
	pcmds += [' ) ']
	print(pcmds)

	for i in range(len(pcmds)):
		if pcmds[i].strip() in  ('&', '(', ')', '|', '->'):# or pcmds[i] == '|' or pcmds[i] == '->':
			continue
		else:
			pcmds[i] = str(parse_cmd(pcmds[i]))

	print(pcmds)
	return ''.join(pcmds)

print(parse_cmds(cmds))
