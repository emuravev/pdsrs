from value import IntValue, VarValue


x = IntValue(-8)
y = VarValue('y')
f = VarValue('f')
z = IntValue(-8)
print(x + z)
#y = IntValue(1)
#print(x.content)
#print(x)
#print(y == f)
#print(y + f)
#print(y < f)

#print(x == y)
#print(x + y)
#print(x + y)
#print(y.content)
#print(y)
#a = x + z
#print(a.content)
#print(a)
#x_sub = z+y
#print(x)
#print(z + y)
#f=IntValue([i[0] for i in (y + z).content])
#print(f)
#print(f<x)

cmds = 'x = 4 ; y = 1 ; z = x + y ; z > y'
cmds = list(map(lambda a: a.strip(), cmds.split(';')))
#print(cmds)

res = []
for cmd in cmds:
	if cmd.find('=') != -1:
		c1, c2 = list(map(lambda a: a.strip(), cmd.split('=')))
		#print([c1, c2], c2.isdigit())
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

		res.append(_c1 == _c2)
	elif cmd.find('>') != -1:
		c1, c2 = list(map(lambda a: a.strip(), cmd.split('>')))
		print([c1, c2], c2.isdigit())
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

		res.append(_c1 > _c2)

	elif cmd.find('<') != -1:
		c1, c2 = list(map(lambda a: a.strip(), cmd.split('<')))
		print([c1, c2], c2.isdigit())
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

		res.append(_c1 < _c2)


print(list(map(str, res)))