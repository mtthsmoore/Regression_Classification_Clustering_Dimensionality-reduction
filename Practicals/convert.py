import sys

states = {}
with open(sys.argv[1]) as f:
	for row in f:
		l=row.rstrip().split(',')
		for s in l[1:]:
			states[s] = True
			
state_list = list(states.keys())

print "plant,%s" % ','.join(state_list)
with open(sys.argv[1]) as f:
	for row in f:
		l=row.rstrip().split(',')
		buf = ""
		for state in state_list:
			if state in l[1:]:
				buf += ',1'
			else:
				buf += ',0'
		print "%s%s" % (l[0],buf)


