import os

from utils.syntax_tree import SyntaxTree
from utils.eval import evaluate
from utils.precondition import weakest_precondition
from utils.parser import parse_wp

class Ui(object):
	def __init__(self, argv):
		self.depth = argv.depth
		self.path = argv.file
		self.postcond = argv.postcond
		self.pgm = ''
		self.wp = None

		if self.path != None:
			self.pgm = self.__read_pgm()

		if not (self.pgm == None or self.postcond == None):
			self.wp = weakest_precondition(self.pgm, self.postcond)

		if not argv.inline or argv.inline not in ('t', 'true'):
			self.__main_loop()
		else:
			if self.wp != None:
				res = parse_wp(self.wp)

				with open('/home/larry/Desktop/tmp/project/translator/limboole1.1/eqv.in', 'w') as f:
					f.write(res)
				cmd = '../translator/limboole1.1/limboole /home/larry/Desktop/tmp/project/translator/limboole1.1/eqv.in'
				os.system(cmd)

	def __get_help(self):
		return 	'\'wp\'\t- generate weakest precondition\n'\
				'\'check\'\t- check wp using SAT solver\n'\
				'\'eval\'\t- evaluate wp using polish notation calculator\n'\
				'\'postcond\'\t- enter new postcondition\n'\
				'\'pgm\'\t- enter new program\n'\
				'\'check_depth\'\t- check depth of program\n'\
				'\'vals\'\t- print state of system\n'\
				'\'depth\'\t- enter new depth\n'\
				'\'file\'\t- read program from file\n'\
				'\'help\'\t- this message'

	def __read_pgm(self):
		with open(self.path,'r') as f:
			pgm = f.read().replace('\n', '')
		return pgm

	def __check_depth(self):
		tr = SyntaxTree(self.pgm)
		return tr.depth()

	def __main_loop(self):
		buff = ''

		while buff not in ('quit', 'exit', 'q'):
			if self.depth == None:
				print('depth not specified')
			if self.path == None:
				print('path not specified')
			if self.postcond == None:
				print('postcondition not specified')
			if self.pgm == '':
				print('program not specified')
			if self.wp == None:
				print('weakest precondition not generated')
			buff = input('cmd: ')

			if buff == 'vals':
				print('depth:\t{}'.format(self.depth))
				print('path:\t{}'.format(self.path))
				print('postc:\t{}'.format(self.postcond))
				print('pgm:\t{}'.format(self.pgm != ''))
				print('wp:\t{}'.format(self.wp))

			if buff == 'help':
				print(self.__get_help())
			if buff == 'file':
				self.path = input('enter new path: ')
				self.pgm = self.__read_pgm()
			if buff == 'depth':
				self.depth = int(input('enter new depth: '))
			if buff == 'print':
				if self.postcond == None or self.pgm == None:
					print('postcondition or program not specified')
				else:
					print('postcond: {}\nprogram:\n{}'.format(self.postcond, self.pgm))
			if buff == 'check_depth':
				if self.depth == None:
					print('depth not specified')
				else:
					print('pgm depth:{}\nset depth:{}'.format(self.__check_depth(), self.depth))
			if buff == 'pgm':
				self.pgm = input('enter new program: \n')
			if buff == 'postcond':
				self.postcond = input('enter new postcondition: ')
			if buff == 'eval':
				if self.wp != None:
					print(evaluate(self.wp))
				else:
					print('run \'check\'')
			if buff == 'wp':
				if not (self.pgm == None or self.postcond == None):
					self.wp = weakest_precondition(self.pgm, self.postcond)
				else:
					print('specify program or postcondition')
			if buff == 'check':
				if self.wp != None:
					res = parse_wp(self.wp)

					with open('/home/larry/Desktop/tmp/project/translator/limboole1.1/eqv.in', 'w') as f:
						f.write(res)

					cmd = '../translator/limboole1.1/limboole /home/larry/Desktop/tmp/project/translator/limboole1.1/eqv.in'
					os.system(cmd)
				else:
					print('run \'check\'')
		
