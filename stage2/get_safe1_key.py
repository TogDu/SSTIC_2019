#!/usr/bin/python
# -*- coding: utf-8 -*

import hashlib
import sys
import binascii
import bitarray
# from Crypto.Cipher import AES
def info(msg):
	print("[\033[34;1mi\033[0m] %s" % (msg))

def ok(msg):
	print("[\033[32;1m+\033[0m] %s" % (msg))

def warn(msg):
	print("[\033[33;1mw\033[0m] %s" % (msg))

def error(msg):
	print("[\033[31;1m!\033[0m] %s" % (msg))


def sec_dev_f1(in_1, in_2, in_3):
	# return (( not in_1 and in_2)or(in_1 and in_3))
	if in_1:
		return in_3
	else:
		return in_2

def sec_dev_fop(bp, op):
	# return (bp and not op) or (not bp and op)
	return bp^op

def sec_dev_fcalc(op, a, b, feedback):
	i1 =  a ^ b
	i2 = a and b
	i3 = a or b
	
	i4 = i1 ^ feedback
	
	feedback = i2 or (i1 and feedback)
	
	j1 = sec_dev_f1(op[0], i1, i4) 
	j2 = sec_dev_f1(op[0], i2, i3)
	
	return (sec_dev_f1(op[1], j2, j1), feedback)
	
def sec_dev_input_filter(input, bp):
	#identity or shift right by 1
	ba = bitarray.bitarray(bin(input)[2:])
	ba.reverse()
	for i in range(len(ba), 8):
		ba.append(0)
		
	o = bitarray.bitarray(8)
	for i in range(8):
		o[i] = sec_dev_f1(bp, ba[i], ba[(i-1)%8])
	return o

def sec_dev_op_filter(op, bp):
	fop = op ^ bp

	fop = bitarray.bitarray(bin(fop)[2:])
	fop.reverse()
	for i in range(len(fop), 2):
		fop.append(0)
		
	return fop
	
	
def boolTable3(f):
	for a in range(2) :
		for b in range(2):
			for c in range(2):
				print('%d %d %d : %d'%(a,b,c, f(a,b,c)))
				
def boolTable2(f):
	for a in range(2):
		for b in range(2):
			print('%d %d : %d'%(a,b, f(a,b)))
			
def test_op(op):	
	a  = 0xf2
	b  = 0x7f
	
	bp = [0, 0, 0]
	fa = sec_dev_input_filter(a, bp[1])
	fb = sec_dev_input_filter(b, bp[2])
	fop = sec_dev_op_filter(op, bp[0])
	
	print(fa)
	print(fb)
	o = bitarray.bitarray(8)
	feedback = 0
	for i in range(8):
		o[i], feedback = sec_dev_fcalc(fop, fa[i], fb[i], feedback)
	print(o)
	o.reverse()
	print('%02x %02x %02x : %02x'%(a, b, op, ord(o.tobytes())))
	# boolTable2(sec_dev_fop)
	# boolTable3(sec_dev_f1)
	# sec_dev_input_filter(0x46, 1)
	# sec_dev_input_filter(0x92, 0)

def test():
	for i in range(4):
		test_op(i)
	#op0 : and 
	#op1 : xor 
	#op2 : or 
	#op3 : ?? 

	
BP = [0, 0, 0]

#This function was empty.
def secure_device(a,b,op):
	global BP
	out = 0
	"""
	TODO : 
		- Implémentation de la communication avec le secure element
			* Entrées A et B (A0 = bit de poids faible)
			* Entrée OP
			* Sortie Out (Out0 = bit de poids faible)
			* Les boutons permettent à l'utilisateur de rentrer sa combinaison secrète pour le déchiffrement
		- Supprimer les docs de conception 
	"""
	fa = sec_dev_input_filter(a, BP[1])
	fb = sec_dev_input_filter(b, BP[2])
	fop = sec_dev_op_filter(op, BP[0])
	
	o = bitarray.bitarray(8)
	feedback = 0
	for i in range(8):
		o[i], feedback = sec_dev_fcalc(fop, fa[i], fb[i], feedback)
	o.reverse()
	# print('%02x %02x %02x : %02x'%(a, b, op, ord(o.tobytes())))
	return ord(o.tobytes())

def step1():
	r = secure_device(0x35,0x27,3)
	r = secure_device(0x7e,r,3)
	r = secure_device(0x66,r,2)
	r = secure_device(0x8,r,1)
	r = secure_device(0x13,r,0)
	r = secure_device(0x1f,r,1)
	r = secure_device(0xa,r,2)
	r = secure_device(0xd3,r,0)
	r = secure_device(0xc6,r,3)

	return r

def step2():
	r= secure_device(0xde,0xab,0)
	r= secure_device(0x67,r,3)
	r= secure_device(0x2a,r,2)
	r= secure_device(0x6d,r,1)
	r= secure_device(0x4a,r,3)
	r= secure_device(0xe7,r,0)
	r= secure_device(0x1c,r,1)
	r= secure_device(0x35,r,0)
	r= secure_device(0xde,r,3)
	r= secure_device(0xf7,r,0)
	r= secure_device(0xda,r,2)
	return r

def step3():
	r = secure_device(0x14,0x23,3)
	r = secure_device(0x72,r,0)
	r = secure_device(0x48,r,3)
	r = secure_device(0x53,r,1)
	r = secure_device(0xa7,r,0)
	r = secure_device(0x5f,r,1)
	r = secure_device(0x3,r,3)
	r = secure_device(0xb7,r,3)
	r = secure_device(0x73,r,1)
	r = secure_device(0x37,r,3)
	r = secure_device(0xc5,r,2)
	r = secure_device(0xa4,r,1)
	r = secure_device(0x30,r,0)
	r = secure_device(0xdd,r,2)
	return r

def step4():
	r = secure_device(0xb0,0x42,2)
	r = secure_device(0xbc,r,2)
	r = secure_device(0xfc,r,2)
	r = secure_device(0x54,r,3)
	r = secure_device(0x30,r,2)
	r = secure_device(0x97,r,1)
	r = secure_device(0xe8,r,2)
	r = secure_device(0xd6,r,0)
	r = secure_device(0x26,r,0)
	r = secure_device(0xeb,r,0)
	r = secure_device(0x68,r,1)
	r = secure_device(0x26,r,0)
	r = secure_device(0x9,r,3)
	r = secure_device(0x2a,r,2)
	r = secure_device(0xa9,r,3)
	return r

def step5():
	r = secure_device(0xff,0x12,0)
	r = secure_device(0xfd,r,1)
	r = secure_device(0xe5,r,1)
	r = secure_device(0x26,r,3)
	r = secure_device(0x85,r,3)
	r = secure_device(0x63,r,1)
	r = secure_device(0x93,r,3)
	r = secure_device(0xba,r,2)
	r = secure_device(0x97,r,0)
	r = secure_device(0xab,r,1)
	r = secure_device(0x6e,r,3)
	r = secure_device(0xfd,r,0)
	r = secure_device(0x4c,r,3)
	r = secure_device(0x50,r,0)
	r = secure_device(0xa,r,2)
	r = secure_device(0xfc,r,3)
	r = secure_device(0xe3,r,2)
	r = secure_device(0xa6,r,3)
	r = secure_device(0x64,r,2)
	r = secure_device(0x8e,r,3)
	r = secure_device(0xc1,r,1)
	return r

def step6():
	r = secure_device(0x90,0x77,1)
	r = secure_device(0x8e,r,0)
	r = secure_device(0xbd,r,2)
	r = secure_device(0x39,r,2)
	r = secure_device(0x4c,r,2)
	r = secure_device(0xc5,r,2)
	r = secure_device(0xb6,r,3)
	r = secure_device(0x93,r,1)
	r = secure_device(0x9f,r,3)
	r = secure_device(0xd6,r,3)
	r = secure_device(0x6e,r,2)
	r = secure_device(0x39,r,3)
	r = secure_device(0x40,r,1)
	r = secure_device(0x14,r,2)
	r = secure_device(0xe6,r,3)
	return r

def step7():
	r = secure_device(0xf,0xab,3)
	r = secure_device(0xa2,r,1)
	r = secure_device(0x7c,r,0)
	r = secure_device(0x34,r,1)
	r = secure_device(0x14,r,1)
	r = secure_device(0xe7,r,0)
	r = secure_device(0xb9,r,0)
	r = secure_device(0xf1,r,2)
	r = secure_device(0xd5,r,1)
	r = secure_device(0x4e,r,2)
	r = secure_device(0xe,r,2)
	r = secure_device(0x6,r,0)
	r = secure_device(0x7d,r,2)
	r = secure_device(0x87,r,3)
	r = secure_device(0xbc,r,0)
	r = secure_device(0xd4,r,3)
	r = secure_device(0x8a,r,1)
	r = secure_device(0xe7,r,3)
	r = secure_device(0x9e,r,1)
	r = secure_device(0x58,r,0)
	r = secure_device(0x24,r,2)
	r = secure_device(0x44,r,3)
	r = secure_device(0xc9,r,1)
	r = secure_device(0xd4,r,1)
	r = secure_device(0x1d,r,3)
	r = secure_device(0xcd,r,0)
	r = secure_device(0xde,r,1)
	r = secure_device(0x54,r,0)
	r = secure_device(0x5e,r,2)
	r = secure_device(0x46,r,1)
	r = secure_device(0x21,r,0)
	r = secure_device(0xff,r,1)
	r = secure_device(0x51,r,0)
	r = secure_device(0x78,r,1)
	r = secure_device(0x2f,r,3)
	r = secure_device(0xed,r,2)
	r = secure_device(0x4b,r,3)
	r = secure_device(0x4d,r,2)
	return r

def step8():
	r = secure_device(0x88,0x74,0)
	r = secure_device(0x48,r,2)
	r = secure_device(0x11,r,2)
	r = secure_device(0x76,r,0)
	r = secure_device(0x2b,r,3)
	r = secure_device(0xf8,r,2)
	return r


def init():
	r = secure_device(0x46,0x92,0)
	r = secure_device(0xdf,r,2)
	r = secure_device(0x3e,r,0)
	r = secure_device(0x3a,r,3)
	r = secure_device(0x36,r,2)
	r = secure_device(0x8e,r,2)
	r = secure_device(0xc9,r,3)
	r = secure_device(0xe7,r,1)
	r = secure_device(0x29,r,2)
	r = secure_device(0xc2,r,2)
	r = secure_device(0x79,r,0)
	r = secure_device(0x2a,r,2)
	r = secure_device(0x4c,r,3)
	r = secure_device(0xde,r,0)
	r = secure_device(0x88,r,0)
	r = secure_device(0x8b,r,2)
	r = secure_device(0x97,r,3)
	r = secure_device(0x6a,r,2)
	r = secure_device(0x60,r,1)
	r = secure_device(0x0f,r,0)
	r = secure_device(0x5b,r,3)
	r = secure_device(0xd0,r,2)
	r = secure_device(0xa9,r,1)
	r = secure_device(0xe3,r,3)
	r = secure_device(0xd0,r,1)
	r = secure_device(0x27,r,0)
	r = secure_device(0x90,r,0)
	r = secure_device(0x3b,r,1)
	r = secure_device(0x66,r,2)
	r = secure_device(0xe2,r,0)
	r = secure_device(0x24,r,3)
	r = secure_device(0xee,r,1)
	r = secure_device(0xf2,r,3)
	return r

def work():
	global BP
	
	info("Dechiffrement du conteneur\n")

	info("Initialisation du secure element")

	info("Merci d'appuyer les 4 boutons du secure element puis appuyer sur entrée")
	BP = [3, 1, 1]
	if init()!=0xa1:
		error("Mauvaise initialisation, vérifiez l'état du sécure élement")
		sys.exit(0)
	else:
		ok("Initialisation, check 1 OK")
	
	info("Merci de relâcher les 4 boutons du secure element puis appuyer sur entrée")
	BP = [0, 0, 0]
	if init()!=0xe0:
		error("Mauvaise initialisation, vérifiez l'état du sécure élement")
		sys.exit(0)
	else:
		ok("Initialisation, check 2 OK")


	warn("Calcul de la clef de déchiffrement du conteneur, préparez vous à appuyer sur les boutons")
	

	info("Step 1, appuyez sur entrée quand la combinaison de boutons est enfoncée")
	input()
	s1 = step1()
	info("Step 2, appuyez sur entrée quand la combinaison de boutons est enfoncée")
	input()
	s2 = step2()
	info("Step 3, appuyez sur entrée quand la combinaison de boutons est enfoncée")
	input()
	s3 = step3()
	info("Step 4, appuyez sur entrée quand la combinaison de boutons est enfoncée")
	input()
	s4 = step4()
	info("Step 5, appuyez sur entrée quand la combinaison de boutons est enfoncée")
	input()
	s5 = step5()
	info("Step 6, appuyez sur entrée quand la combinaison de boutons est enfoncée")
	input()
	s6 = step6()
	info("Step 7, appuyez sur entrée quand la combinaison de boutons est enfoncée")
	input()
	s7 = step7()
	info("Step 8, appuyez sur entrée quand la combinaison de boutons est enfoncée")
	input()
	s8 = step8()


	key = bytearray([s1,s2,s3,s4,s5,s6,s7,s8])
	h = hashlib.sha256(key).hexdigest()

	

	if "00c8bb35d44dcbb2712a11799d8e1316045d64404f337f4ff653c27607f436ea" == h:
		ok("Hash ok")
		info("Dérivation de la clef AES safe_01")
		aes_key = hashlib.scrypt(key,salt =b"sup3r_s3cur3_k3y_d3r1v4t10n_s4lt",n=1<<0xd,r=1<<3,p=1<<1,dklen=32)
		info("aes key : %s" % aes_key.hex())
		info("Vous pouvez sauvegarder cette clef en utilisant /root/tools/add_key.py key")
	else:
		error("Mauvais hash, déchiffrement impossible")

def bf():
	global BP
	BP = [3, 1, 1]
	if init() == 0xa1:
		print('init all on  : OK')
	else:
		print('emulation failure for all on %x!=a1'%init())
		return
		
	BP = [0, 0, 0]
	if init()==0xe0:
		print('init all off  : OK')
	else:
		print('emulation failure for all off %x!=e0'%init())
		return
	
	s1 = []
	s2 = []
	s3 = []
	s4 = []
	s5 = []
	s6 = []
	s7 = []
	s8 = []
	
	i = 0
	for op in range(4):
		for shA in range(2):
			for shB in range(2):
				BP = [op, shA, shB]
				print('%d %s'%(i, str(BP)))
				i += 1
				s1.append(step1())
				s2.append(step2())
				s3.append(step3())
				s4.append(step4())
				s5.append(step5())
				s6.append(step6())
				s7.append(step7())
				s8.append(step8())
	print("s1 : "+str(s1))			
	print("s2 : "+str(s2))			
	print("s3 : "+str(s3))			
	print("s4 : "+str(s4))			
	print("s5 : "+str(s5))			
	print("s6 : "+str(s6))			
	print("s7 : "+str(s7))			
	print("s8 : "+str(s8))			
			
	
	# for i1 in range(len(s1)):
	 # for i2 in range(len(s2)):
	  # for i3 in range(len(s3)):
	   # for i4 in range(len(s4)):
	    # for i5 in range(len(s5)):
	     # for i6 in range(len(s6)):
	      # for i7 in range(len(s7)):
	       # for i8 in range(len(s8)):
	
	key = bytearray([s1[11],s2[6],s3[12],s4[8],s5[13],s6[10],s7[2],s8[10]])
	h = hashlib.sha256(key).hexdigest()
	if "00c8bb35d44dcbb2712a11799d8e1316045d64404f337f4ff653c27607f436ea" == h:
		ok("Hash ok")
		info("Dérivation de la clef AES safe_01")
		aes_key = hashlib.scrypt(key,salt =b"sup3r_s3cur3_k3y_d3r1v4t10n_s4lt",n=1<<0xd,r=1<<3,p=1<<1,dklen=32)
		info("aes key : %s" % aes_key.hex())
	
def main():
	bf()
	# work()
	

if __name__ == '__main__':
	main()
