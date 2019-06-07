import struct 
def  printStack(s):
	for i in range(len(s)):
		print('%x'%s[i])

hashCounter = 0
def hook(pc, stack):
	global hashCounter
	if pc == 0x28E:
		print('[TRACE] DoCheck')
		printStack(stack)
	elif pc == 0x300:
		print('[TRACE] EndLoop')
		printStack(stack)
		# return 1, stack
	elif pc == 0x2EA:
		print('[TRACE] CRYPTO MID LOOP ')
		printStack(stack)
		# hashCounter += 1
		# if hashCounter == 4:
			# stack[-2] = 0x65850b36e76aaed5
			# stack[-1] = 0xd9c69b74a86ec613
			# stack[-5] = 0x65850b36e76aaed5
			# stack[-4] = 0xd9c69b74a86ec613
			
			# stack[-7] = 0x9fcdaa8c92085c68
			# stack[-8] = 0x77cb17b7f8a8a6f0
	elif pc == 0x3A0:
		print('[TRACE] End hash ? ')
		printStack(stack)
	elif pc == 0x3AC:
		print('[TRACE] Internal Crypto loop')
		printStack(stack)
	elif pc == 0x2C2:
		print('[TRACE] failed')
	elif pc == 0x2B7:
		print('[TRACE] whouhouuuuuuuuuuuuu!')
	# elif pc == 0x4EC:
		# print('[TRACE] Crypto : Loop4EC')
	# elif pc == 0xD83:
		# print('[TRACE] Crypto : LoopD83')
	return 0, stack
		
def Emulate(code, entrypoint, maxCode):
	bPrintAll = False
	bPrintBranch = False
	bPrintLimited = True
	pc = entrypoint
	registers = [0, 0, 0, 0, 0, 0, 0, 0,
				 0, 0, 0, 0, 0, 0, 0, 0,
				 0, 0, 0, 0, 0, 0, 0, 0,
				 0, 0, 0, 0, 0, 0, 0, 0xDEAD0000]
	stack = []
	
	a = "00001111"
	b = "22223333"
	c = "44445555"
	d = "66667777"
	input = "SSTIC{Dw4rf_VM_1s_col_isn_t_It}\x00"
	# input = a + b + c +d +"\x00"
	while pc < maxCode:
		opc = ord(code[pc])
		name = ''
		size = 1
		bPush = True
		bMeaningfull = True
		bStop, stack = hook(pc, stack)
		if bStop == 1:
			break
		data = 0
		if opc == 1:
			data = struct.unpack('Q', code[pc+1:pc+9])[0]
			name = 'addr %16x'%data
			size += 8
		elif opc == 6:
			addr = stack.pop()
			if addr == 0xDEAD00A8:
				data = 0xDEAD1000
			elif addr == 0xDEAD1008:
				data = 0xAAAA0000
			elif addr&0xFFFF0000 == 0xAAAA0000:
				data = struct.unpack('Q', input[(addr&0xFF):(addr&0xFF)+8])[0]
			elif addr&0xFF0000 == 0x400000:
				addr = addr&0xFFFF
				data = struct.unpack('Q', code[addr:addr+8])[0] 
			else:
				print("[ERR] unknown deref %04x : %x"%(pc, addr))
				break
			name = 'deref *%x=%x'%(addr, data)
		elif opc == 8:
			data = ord(code[pc+1])
			name = 'const %02x'%data
			size += 1
			bMeaningfull = False
		elif opc == 0xc:
			data = struct.unpack('I', code[pc+1:pc+5])[0]
			name = 'const %x'%data
			size += 4
			bMeaningfull = False
		elif opc == 0xE:
			data = struct.unpack('Q', code[pc+1:pc+9])[0]
			name = 'const %x'%data
			size += 8
			bMeaningfull = False
		elif opc == 0x12:
			name = 'dup'
			data = stack[len(stack)-1]
			bMeaningfull = False
		elif opc == 0x13:
			name = 'drop'
			stack.pop()
			bPush = False
			bMeaningfull = False
		elif opc == 0x15:
			id = ord(code[pc+1])
			data = stack[-id-1]
			name = 'pick %d (%x)'%(id, data)
			size += 1
			bMeaningfull = False
		elif opc == 0x16:
			name = 'swap'
			a = stack.pop()
			data = stack.pop()
			stack.append(a)
			bMeaningfull = False
		elif opc == 0x17:
			name = 'rot'
			a = stack.pop()
			data = stack.pop()
			b = stack.pop()
			stack.append(a)
			stack.append(b)
			bMeaningfull = False
		elif opc == 0x1A:
			a = stack.pop()
			b = stack.pop()
			data = b & a 
			name = 'and (%x & %x = %x)'%(b, a, data)
		elif opc == 0x1C:
			a = stack.pop()
			b = stack.pop()
			data = b-a
			name = 'min (%x - %x = %x)'%(b,a, data)
		elif opc == 0x1E:
			a = stack.pop()
			b = stack.pop()
			data = b * a 
			name = 'mul (%x * %x = %x)'%(b, a, data)
		elif opc == 0x21:
			a = stack.pop()
			b = stack.pop()
			data = b | a
			name = 'or (%x | %x = %x)'%(b, a, data)
		elif opc == 0x22:
			a = stack.pop()
			b = stack.pop()
			data = b + a
			name = 'plus (%x + %x = %x)'%(b, a, data)
		elif opc == 0x24:
			a = stack.pop()
			b = stack.pop()
			data = b << a
			name = 'shl (%x << %x = %x)'%(b,a, data)
		elif opc == 0x25:
			a = stack.pop()
			b = stack.pop()
			data = b >> a
			name = 'shr (%x >> %x = %x)'%(b,a, data)
		elif opc == 0x27:
			a = stack.pop()
			b = stack.pop()
			data = b ^ a
			name = 'xor (%x ^ %x = %x)'%(b,a, data)
		elif opc == 0x28:
			off = struct.unpack('h', code[pc+1:pc+3])[0]
			name = 'bra %04x'%((pc+off+3)&0xFFFF)
			x = stack.pop()
			size += 2
			bPush = False
			if x > 0:
				size += off	
			else:
				bMeaningfull = False
			if bPrintBranch:
				print('%04x: '%pc),
				print(name)
		elif opc == 0x2F:
			off = struct.unpack('h', code[pc+1:pc+3])[0]
			name = 'skip %04x'%((pc+off+3)&0xFFFF)
			bPush = False
			size += 2 + off
			if bPrintBranch:
				print('%04x: '%pc),
				print(name)
		elif (opc >= 0x30 and opc < 0x50):
			data = opc - 0x30
			name = 'lit %d'%data
			bMeaningfull = False
		elif (opc >= 0x50 and opc < 0x70):
			name = 'reg%d'%(opc-0x50)
			data = registers[opc-0x50]
			bMeaningfull = False
		elif opc == 0x94:
			s = ord(code[pc+1])
			addr = stack.pop()
			if addr&0xFF0000 == 0x400000:
				addr = addr&0xFFFF
				if s == 4:
					data = struct.unpack('I', code[addr:addr+4])[0] 
				else:
					print("[ERR] unknown derefsz %04x : %x"%(pc, addr))
					break
			elif addr&0xFFFF0000 == 0xAAAA0000:
				data = 0
			else:
				print("[ERR] unknown derefsz range %04x : %x"%(pc, addr))
				break
			name = 'derefSz %d *%x=%x'%(s, addr, data)
			size += 1
		else:
			name = 'ERR : unknown opc %02x'%opc

			print('%04x: '%pc),
			print(name)
			break
			
		if  bPrintAll or (bPrintLimited and bMeaningfull): 
			print("%04x : %s"%(pc, name))
		if bPush:
			data &= 0xFFFFFFFFFFFFFFFF
			stack.append(data)
		pc += size
		pc &= 0xFFFF
	print("EXIT")
	print("pc : %04x"%pc)
	printStack(stack)
	
	
f = open('input.elf', 'rb')
data = f.read(0x2000)
Emulate(data, 0x258, 0x2000)
f.close()