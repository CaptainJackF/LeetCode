# -- coding:utf-8 --
'''
	20. Valid Parentheses
	给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
	括号必须以正确的顺序关闭，"()" 和 "()[]{}" 是有效的但是 "(]" 和 "([)]" 不是。
'''

Test_signal = { "(":")", "[":"]", "{":"}"}

test = "(){}"
test1 = "([)]"

stack = []
for i in test1:
	if i in Test_signal:
		target = Test_signal[ i]
	elif i != target:
		print( False)
	else:
		print( True)
