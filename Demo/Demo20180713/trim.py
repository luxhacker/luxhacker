def trim(s):
	n = len(s)
	while n>0:
		print('s:',s[n-1:n])
		m = s[n-1:n]
		n = n - 1
		if m==' ':
			print('sn:',n)
			break
		
	return s[n+1:len(s)]

print('ssss:',trim('  hello') )

