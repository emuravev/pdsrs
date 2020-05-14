from utils.precondition import parse_if, parse_caseof

class Node(object):
	def __init__(self, cmd, nodes):
		self.cmd = cmd
		self.nodes = nodes

	def __str__(self):
		return self.cmd

class SyntaxTree(object):
	def __init__(self, prog):
		self.tree = self.__create_tree(prog)

	def __create_tree(self, prog):
		cmds = list(map(lambda a: a.strip(), prog.split(';')))
		#print(cmds)
		for c in cmds:
			if c.find(':=') != -1 and not c.startswith('if') and not c.startswith('case'):
				continue
			else:
				if c.startswith('if'):
					__cnd, __th, __el = parse_if(c)
					return Node(__cnd, [self.__create_tree(__th), self.__create_tree(__el)])
				elif c.startswith('case'):
					__r = parse_caseof(c)
					return Node('({}) ? ({})'.format(*__r['cnd']), [self.__create_tree(__r['eq_part']),\
						self.__create_tree(__r['le_part']), self.__create_tree(__r['gr_part'])])
				else:
					raise NotImplementedError

		return Node('leaf', [])

	def __depth(self, d=0, head=None):
		if head == None:
			head = self.tree

		if len(head.nodes) == 0:
			return d
		else:
			return max(list(map(lambda a: self.__depth(d+1, a), head.nodes)))

	def depth(self):
		return self.__depth()
		
		
