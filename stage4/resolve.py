#Stage 4 crypto alg reimplementation + decryption
def findInLookup(tid, needle, off):
	global lookup	
	out = None
	for i in range(0x110):
		idx = tid*0x10000 + i * 256 + off
		if ord(lookup[idx]) == needle:
			out=(i-0x10)&0xFF
	return out

def underivate(tid, r9):
	r4 = r9 >> 8 #73
	r6 = r9&0xFF #41
	r5 = findInLookup(tid, r4, r6) #r5=CD
	tid += 1
	if tid == 0xA:
		tid = 0
	
	r6 = findInLookup(tid, r6, r5) #r6=70
	tid += 1
	if tid == 0xA:
		tid = 0
		
	r1 = findInLookup(tid, r5, r6) #r1 =97
	tid += 1
	if tid == 0xA:
		tid = 0
		
	r1 = findInLookup(tid, r6, r1)+r1*256 #r1 =1397
	r1 &= 0xFFFF
	tid += 1
	if tid == 0xA:
		tid = 0
		
	return tid, r1

def derivate(tid, r1):
	global lookup
	r1_low = r1&0xFF
	r1_high = (r1>>8)&0xFF
	
	r6_o = ord(lookup[tid*0x10000+(r1_low+0x10)*256+r1_high])
	if tid == 0:
		tid = 0xA
	tid -= 1
	
	
	r5 = ord(lookup[tid*0x10000+(r1_high+0x10)*256+r6_o])
	if tid == 0:
		tid = 0xA
	tid -= 1
	
	
	r4 = ord(lookup[tid*0x10000+(r6_o+0x10)*256+r5])
	if tid == 0:
		tid = 0xA
	tid -= 1
	
	r6 = ord(lookup[tid*0x10000+(r5+0x10)*256+r4])
	if tid == 0:
		tid = 0xA
	tid -= 1
	
	return tid , r6*256+r4

def SWAP(x):
	return ((x&0xFF)<<8)|((x>>0x8)&0xFF)	
		
	
def decrypt(x, y, bBranch1=True, bLog=False, bBeStupid = False):
	r1 = (x >> 16)&0xFFFF
	r0 = x & 0xFFFF
	
	r3 = (y >> 16)&0xFFFF
	r2 = y & 0xFFFF
	
	r0 = SWAP(r0)
	r1 = SWAP(r1)
	r2 = SWAP(r2)
	r3 = SWAP(r3)
	if bLog: print('0:%02x %02x %02x %02X'%(r0,r1,r2,r3))
	tid = 0
	i = 0
	r8 = None
	while i < 0x20:
		if ((i)>>3)&1 == 0 :
			if bBranch1:
				r8 = r2
				r2 = r1
				r9 = r0
				r0xr1 = (r3 ^ (i+1))&0xFFFF
				r3 = r8
				tid, r1 = underivate(tid, r9)
				r0 = r1^r0xr1
			else:
				r3 = r0 ^ (i+2)
				tid, x = underivate(tid, 0)
				
			if bLog: print('1.%d:%02x %02x %02x %02X'%(i,r0,r1,r2,r3))
		else:
			r8 = r3
			r3 = r2
			r9 = r0
			r2 = (i+1) ^ r0 ^ r1
			
			r0 = r8
			tid, r1 = underivate(tid, r9)
			
			if bLog: print('2.%d:%02x %02x %02x %02X'%(i,r0,r1,r2,r3))
		
		i +=1
	if bBeStupid:	
		r0 = SWAP(r0)
		r1 = SWAP(r1)
		r2 = SWAP(r2)
		r3 = SWAP(r3)
	
	return r0*0x10000+r1, r2*0x10000+r3

def encrypt(x, y, bBranch1=True, bLog=False, bBeStupid = False):
	r0 = (x >> 16)&0xFFFF
	r1 = x & 0xFFFF
	
	r2 = (y >> 16)&0xFFFF
	r3 = y & 0xFFFF
	
	if bBeStupid:
		r1 = SWAP(r1)
		r0 = SWAP(r0)
		r2 = SWAP(r2)
		r3 = SWAP(r3)
	
	tid = 7
	r14 = 0x20
	while r14 > 0:
		r14 -= 1
		tid, r9 = derivate(tid, r1)
		if (r14>>3)&1 == 0:
			if bLog: print('1.%d:%02x %02x %02x %02X'%(r14,r0,r1,r2,r3))
			r8 = r3
			r3 = (r14+1) ^ r0 
			if bBranch1:
				r3 ^= r1 
				r0 = r9
				r1 = r2
				r2 = r8
		else:
			if bLog: print('2.%d:%02x %02x %02x %02X'%(r14,r0,r1,r2,r3))
			r8 = r0
			r0 = r9
			r1 = (r14+1) ^ r0  ^ r2 
			r2 = r3
			r3 = r8
	if bLog: print('0:%02x %02x %02x %02X'%(r0,r1,r2,r3))	
	r0 = SWAP(r0)
	r1 = SWAP(r1)
	r2 = SWAP(r2)
	r3 = SWAP(r3)
	
	return r1*0x10000+r0, r3*0x10000+r2
		
def decryptKey(a,b, bBranch=True, bLog=False, bBeStupid=False):
	x, y =decrypt(a,b,bBranch, bLog,bBeStupid)
	print ("%08x%08x"%(x,y)),
	a2,b2 = encrypt(x,y,bBranch, bLog,bBeStupid)
	if a2 != a or b2!=b:
		print ("%08x %08x"%(a2,b2))
		print('CHECK FAILED!!!')
		
		
f = open('lookup', 'rb')
lookup = f.read()
# resolve()
print('\nRESOLVE2')
decryptKey(0x612e7270,0x6766722e)
decryptKey(0x666E632E,0x2E76662E)
decryptKey(0x76706E73,0x66407279)
decryptKey(0x70766766,0x7465622E)



# resolve()
	
#expected : 
# 612e7270
# 6766722e
# 666e632e
# 2e76662e
# 76706e73
# 66407279
# 70766766
# 7465622e