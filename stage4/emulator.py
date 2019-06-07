import struct

#I had previously done a dump (from GDB) of unciphered opcodes. 
#This script aims to unassemble those opcodes 
#traces/opc_decomp.txt : raw output with additional gdb dumps (ciphered registers read/write and mem access)
#traces/vm.txt : cleaned output
f = open('traces/gdb_raw.txt', 'r')

opc = f.readline()
pc = 0
while opc:
	pc, opc = opc[:-1].split(':')
	opc_hex, = struct.unpack('>I', opc.decode('hex'))

	opc_1 = (opc_hex >> 0x14)&0xFF
	opc_2 = (opc_hex >> 0x12) & 3
	regID1 = (opc_hex >> 0xE)&0xF
	regID2 = (opc_hex >> 0xA)&0xF
	param = (opc_hex & 0x3FF)
	
	bExPrint = True
	if opc_1 == 0xC:	
		name = "MOV [0X10000+r%d], cst"%(regID1)
	elif opc_1 == 0xA:
		name = "RET r0"
	elif opc_1 == 0xD:
		name = "InitTimer"
	elif opc_1 == 0xE:
		name = "TimerJmp"
	elif opc_2 == 0:
		if opc_1 == 0:
			name = "MOV r%d, r%d"%(regID1, regID2)
			bExPrint = False
		elif opc_1 == 1:
			name = "DEC r%d"%regID1
			bExPrint = False
		elif opc_1 == 2:
			name = "ADD_270 r%d, r%d"%(regID1, regID2)
			bExPrint = False
		elif opc_1 == 3:
			name = "SUB r%d r%d"%(regID1, regID2)
			bExPrint = False
		elif opc_1 == 6:
			name = "XOR r%d, r%d"%(regID1, regID2)
			bExPrint = False
		elif opc_1 == 0xB:
			name = "SWAP r%d"%regID1
			bExPrint = False
		else:
			name = "ERROR"
	elif opc_2 == 3:
		if opc_1 == 0:
			name = "MOV r%d, %04x"%(regID1, param)
			bExPrint = False
		elif opc_1 == 2:
			name = "ADD r%d, %04x"%(regID1, param)
			bExPrint = False
		elif opc_1 == 3:
			name = "SUB r%d, %04x"%(regID1, param)
			bExPrint = False
		elif opc_1 == 4:
			name = "LSH r%d, %04x"%(regID1, param)
			bExPrint = False
		elif opc_1 == 5:
			name = "RSH r%d, %04x"%(regID1, param)
			bExPrint = False
		elif opc_1 == 6:
			name = "OP_83010026[%d]"%regID1
		elif opc_1 == 7:
			name = "AND r%d, %04x"%(regID1, param)
			bExPrint = False
		elif opc_1 == 8:
			name = "CACHE r%d"%regID1
			bExPrint = False
		elif opc_1 == 9:
			name = "JA r%d %04x"%(regID1, param)
			bExPrint = False
		else:
			name = "ERROR"
	elif opc_2 != 1:
		name = "mov [r%d], r%d"%(regID1, regID2)
	else:
		name = "MOV r%d, [r%d]"%(regID1, regID2)
		bExPrint = False
	if bExPrint:
		print('%s %s (%02x %02x %02x %02x %04x)'%(opc, name, opc_1, opc_2, regID1, regID2, param))
	else:
		print('%s %s %s'%(pc, opc, name))
		
	opc = f.readline()