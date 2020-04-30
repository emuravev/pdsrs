DEBUG = False

def applyOp(op, a, b, c = None):
	if op == '+': return a + b
	if op == '-': return a - b
	if op == '*': return a * b
	if op == '/': return a / b
	if op == '^': return a ** b
	if op == '<': return a < b
	if op == '>': return a > b
	if op == '=': return a == b
	if op == '&': return a and b
	if op == '|': return a or b
	if op == '~': return not a
	if op == '?': return b if a else c

	return None

def calc(q):
	stack = []
	var = 0
	while len(q):
		token = q.pop(0)
		if applyOp(token, 1, 1) == None:
			stack.append(token)
			var += 1
		else:
			if token == '~':
				a = stack.pop()
				stack.append(applyOp(token, a, 42))
				if DEBUG: print(token, a, " => ", stack[-1])

			elif token == '?':
				c, b, a = stack.pop(), stack.pop(), stack.pop()
				stack.append(applyOp(token, a, b, c))
				if DEBUG: print(token, a, b, c, " => ", stack[-1])
			else:
				b, a = stack.pop(), stack.pop()
				stack.append(applyOp(token, a, b))
				if DEBUG: print(a, token, b, " => ", stack[-1])

	return stack.pop()

def precedence(op):
	if op in '<>=':
		return -1
	if op in '~?*/^':
		return 1
	return 0

def revpolishnotation(expr):
	i = 0
	output = []
	operators = []
	while i < len(expr):
		if expr[i].isdigit() or (i+1 < len(expr) and expr[i] == '-' and expr[i+1].isdigit()):
			negative = False
			if (expr[i] == '-'):
				i += 1
				negative = True
			n = int(expr[i])
			while i+1 < len(expr) and expr[i+1].isdigit():
				n = int(expr[i+1]) + n * 10
				i += 1
			output.append(-n if negative else n)
		elif expr[i] in "abcdefghijklmnopqrstuvwxyz":
			output.append(expr[i])
		elif expr[i] == ' ' or expr[i] == ',':
			i += 1
			continue
		elif expr[i] == '(':
			operators.append(expr[i])
		elif expr[i] == ')':
			while operators[-1] != '(':
				output.append(operators.pop())
			operators.pop()
		else:
			while len(operators) and precedence(operators[-1]) >= precedence(expr[i]) and operators[-1] != '(':
				output.append(operators.pop())
			operators.append(expr[i])
		i += 1

	while len(operators):
		output.append(operators.pop())

	return output

def evaluate(expr):
	return calc(revpolishnotation(expr))

#print(evaluate(input().strip()))