class Expression(object):
	def __init__(self):
		self.content = []
		pass

	def __iter__(self):
		return iter(self.content)

	def __getitem__(self, i):
		return self.content[i]

	def __str__(self):
		pass

	def __eq__(self, other):
		raise NotImplementedError

	def __resolve_one(self):
		return '(__true__ | !__true__)'

	def __resolve_zero(self):
		return '(__false__ & !__false__)'

	def resolve_variable(self, var):
		if isinstance(var, int):
			if var == 0:
				return self.__resolve_zero()
			elif var == 1:
				return self.__resolve_one()
		elif isinstance(var, str):
			return var


class Value(Expression):
	def __init__(self):
		self.content = []
		pass

	def __translate(self):
		pass

	def __str__(self):
		return '$'.join(map(str, self.content))

	def __eq__(self, other):
		if type(other) != Addition:
			return Compare(self, other)
		else:
			return other == self

	def __add__(self, other):
		return Addition(self, other)

	def __neg__(self):
		raise NotImplementedError

	def __lt__(self, other):
		return LessThen(self, other)

	def __gt__(self, other):
		return GreaterThen(self, other)

	def __repr__(self):
		return 'NoI'

class IntValue(Value):
	def __init__(self, value, base: int=4):
		if type(value) == int:
			self.content = self.__translate(value=value, base=base)
		elif type(value) == list:
			self.content = value
		else:
			raise TypeError('{}'.format(type(value)))

	def __translate(self, value: int, base: int=4) -> list:
		if value > 0:
			res = '{0:04b}'.format(value)
		else:
			value += 1
			res = '{0:04b}'.format(value)
			res = ''.join([('0' if i == '1' else '1') for i in res])
		res = [int(i) for i in res]

		return res

	def __neg__(self):
		x = [(1 if i == 0 else 0) for i in self.content]
		x = list(map(lambda a: a[0], IntValue(x) + IntValue(1)))
		return IntValue(x)

class VarValue(Value):
	def __init__(self, name, base: int=4):
		if type(name) == str:
			self.content = self.__translate(name=name, base=base)
		elif type(name) == IntValue:
			self.content = self.__from_IntValue(name=name.content)
		elif type(name) == VarValue:
			self.content = name.content
		elif type(name) == list:
			self.content = name
		else:
			raise TypeError('{}'.format(type(name)))

	def __translate(self, name: str, base: int=4) -> list:
		return [x + '_' + i for x, i in zip([name for _ in name*base], map(str, range(base)))]

	def __from_IntValue(self, name):
		#!
		return list(map(lambda a: (1 if a == 1 else 0), name))

	def __neg__(self):
		x = list(map(lambda a: '!' + a, self.content))
		x = list(map(lambda a: a[0], VarValue(x) + IntValue(1)))
		return VarValue(x)

class Compare(Expression):
	def __init__(self, x, y):
		#if type(x) != VarValue and type(x) != IntValue:
	#		raise TypeError('{}'.format(type(x)))
	#	if type(y) != VarValue and type(y) != IntValue:
#			raise TypeError('{}'.format(type(y)))

		if (type(x) == VarValue or type(x) == IntValue) and\
		   (type(y) == VarValue or type(y) == IntValue):
			self.content = self.__create(x=x.content, y=y.content)
		#elif type(x) == Addition:
		#	self.content = self.__create(x=[i[0] for i in x], y=y.content)
		#elif type(y) == Addition:
		#	self.content = self.__create(x=x.content, y=[i[0] for i in y])
		else:
			raise TypeError

	def __create(self, x:list, y:list) -> list:
		return list(zip(x, y))

	def __str__(self):
		return ' & '.join(['(' + self.resolve_variable(x) + ' <-> '\
					 + self.resolve_variable(y) + ')' for x, y in self.content])

	def resolve_variable(self, var):
		return super().resolve_variable(var)

class Addition(Expression):
	def __init__(self, x, y):
		if type(x) != VarValue and type(x) != IntValue:
			raise TypeError('{}'.format(type(x)))
		if type(y) != VarValue and type(y) != IntValue:
			raise TypeError('{}'.format(type(y)))
		
		if type(x) == IntValue and type(y) == IntValue:
			self.content = self.__intint_create(x=x.content, y=y.content)
		elif type(x) == VarValue and type(y) == VarValue:
			self.content = self.__varvar_create(x=x.content, y=y.content)
		else:
			x, y = VarValue(x), VarValue(y)
			self.content = self.__varvar_create(x=x.content, y=y.content)

	def __intint_create(self, x:list, y:list) -> list:
		x, y = list(reversed(x)), list(reversed(y))
		z = [(x[0] ^ y[0], (x[0],y[0]))]#,None))]
		carry = x[0] & y[0]
		for i in range(1, len(x)):
			z += [(x[i] ^ y[i] ^ carry, (x[i], y[i], carry))]
			carry = (x[i] & y[i]) | (x[i] & carry) | (y[i] & carry)
		return list(reversed(z))

	def __varvar_create(self, x, y):
		x, y = list(map(str, reversed(x))), list(map(self.resolve_variable,reversed(y)))
		z = [(self.__resolve_xor([x[0], y[0]]), (x[0],y[0]))]
		carry = self.resolve_variable(x[0]) + ' & ' + self.resolve_variable(y[0])
		for i in range(1, len(x)):
			z += [(self.__resolve_xor([x[i], y[i], carry]), (x[i], y[i], carry))]
			carry = '({} & {}) | ({} & {}) | ({} & {})'.format(*list(map(self.resolve_variable, \
						[x[i], y[i], x[i], carry, y[i], carry])))
		return list(reversed(z))

	def __resolve_xor(self, vars):
		if len(vars) == 2:
			return '(!{0} & {1}) | ({0} & !{1})'.format(*list(map(self.resolve_variable, vars)))
		elif len(vars) == 3:
			return '(!{0} & !{1} & {2}) | (!{0} & {1} & !{2}) | ({0} & !{1} & !{2}) | ({0} & {1} & {2})'\
					.format(*list(map(self.resolve_variable, vars)))
		else:
			raise NotImplementedError

	def __eq__(self, other):
		if type(other) == Addition:
			return Compare(VarValue([i[0] for i in self.content]),\
				VarValue([i[0] for i in other.content]))
		else:
			return Compare(VarValue([i[0] for i in self.content]),other)

	def __str__(self):
		#!
		return ' & '.join(['(' + self.resolve_variable(val) + \
			' <-> (' + self.__resolve_xor(c) + '))' for val, c in self.content])

	def resolve_variable(self, var):
		return super().resolve_variable(var)

class  GreaterThen(Expression):
	def __init__(self, x, y):
		if type(x) != VarValue and type(x) != IntValue:
			raise TypeError('{}'.format(type(x)))
		if type(y) != VarValue and type(y) != IntValue:
			raise TypeError('{}'.format(type(y)))
		
		if type(x) == IntValue and type(y) == IntValue:
			self.content = self.__intint_create(x=x, y=y)
		elif type(x) == VarValue and type(y) == VarValue:
			self.content = self.__varvar_create(x=x, y=y)
		else:
			x, y = VarValue(x), VarValue(y)
			self.content = self.__varvar_create(x=x.content, y=y.content)

	def __intint_create(self, x, y):
		return (0, (x + (-y))[0][0])

	def __varvar_create(self, x, y):
		#!
		return (0, (x + (-y))[0][0])

	def resolve_variable(self, var):	
		return super().resolve_variable(var)

	def __str__(self):
		#!
		return ' <-> '.join(map(self.resolve_variable, self.content))

class  LessThen(Expression):
	def __init__(self, x, y):
		if type(x) != VarValue and type(x) != IntValue:
			raise TypeError('{}'.format(type(x)))
		if type(y) != VarValue and type(y) != IntValue:
			raise TypeError('{}'.format(type(y)))
		
		if type(x) == IntValue and type(y) == IntValue:
			self.content = self.__intint_create(x=x, y=y)
		elif type(x) == VarValue and type(y) == VarValue:
			self.content = self.__varvar_create(x=x, y=y)
		else:
			x, y = VarValue(x), VarValue(y)
			self.content = self.__varvar_create(x=x.content, y=y.content)

	def __intint_create(self, x, y):
		return (1, (x + (-y))[0][0])

	def __varvar_create(self, x, y):
		#!
		return (1, (x + (-y))[0][0])

	def resolve_variable(self, var):
		return super().resolve_variable(var)

	def __str__(self):
		#!
		return ' <-> '.join(map(self.resolve_variable, self.content))