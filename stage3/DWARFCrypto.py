import struct 

g_Lookup3 = [ 	0x489DDDDE, 0x067990F1, 0x95BF74A9, 0x77941EE7, 0x0E6D80E3,
				0x2DEDAF8B, 0xFB92CD42, 0xD0E867C0, 0xF2B3A3FB, 0x6C39CE47,
				0xE74F99E0, 0x5A24F221, 0xD6378FEA, 0xE23CA8C4, 0x84E3B1BC,
				0xCE5E10BF, 0xA2B364DA, 0x41F250F0, 0x0FE97040, 0x1CC05266,
				0x16F87E4B, 0x515E26B7, 0xEEA48DCB, 0x62B357E4, 0x39BD2041,
				0x72CD387A, 0xF37AAC8B ]
				
g_Lookup = [ 0x5963B39B, 0x30F75ADD, 0x103FECBC, 0x00392E7A, 0x35DF7ADF,
			0xE19ABD13, 0xDAF8B35C, 0xF8798214, 0xB30C2305, 0x067980E9,
			0x6900D940, 0x035E876F, 0xA3857014, 0x56C8E162, 0xE9748F56,
			0x91D4E409, 0xDCC75A09, 0xAC65F52F, 0x8571DD07, 0x019EDCF6,
			0x51CEF9EB, 0x1EB1B17D, 0x0ABE446F, 0x3B277CFE, 0x843869BC,
			0xB23EA298, 0x7C296F51, 0xCD799972, 0x62180A64, 0x0AC052D5,
			0xF0076205, 0x13183193, 0xB908CB94, 0x4BF4CD3C, 0xDEE5D48A,
			0xF64F9A74, 0xD64A15D0, 0xB2CAD434, 0x64E9013B, 0xF46CC1D2,
			0x9D78E9DB, 0x11789216, 0x335689E6, 0x074C7EDB, 0xE6EB6185,
			0xD020170B, 0xF304AA15, 0xBCF2B69E, 0x4EB3D2EA, 0xD78D4D5C,
			0x7ED2BFC4, 0x58EBF0F3, 0x8B591C3F, 0xD3041F6B, 0x005CAE88,
			0xBA696F5C, 0xC16C8EDE, 0x9ABCBB27, 0x56D78D77, 0x765B3E20,
			0xCF37212D, 0x192E2DCF, 0x8CAF2806, 0xBC9A575B, 0x776421CE,
			0x527FB9EB, 0x69F84340, 0xADBC7BD7, 0x73F2C329, 0x737F8A7F,
			0xE301D3E4, 0x057EBEB2, 0x5859B858, 0x2CC41979, 0xEC69A639,
			0x53B0D523, 0x39A2F532, 0x8B29E35D, 0x44E2CE81, 0xCC10A16D,
			0x44D9FF58, 0x77102C14, 0xFB57817D, 0x3CF7C8C8, 0x1222868A,
			0x4173D5D1, 0x3529EE32, 0x7A9DF58E, 0x513525AC, 0x81954BAC,
			0xCE53CCF5, 0x79168728, 0xA2D660F8, 0xF30CC9CE, 0xF0B89C76,
			0x089FB3A9, 0xC919DBA8, 0x1F9E4DC3, 0xA2594E0C, 0x34FFE178,
			0xB04414FB, 0xD31FB33A, 0x184D0278, 0x2C816A9A, 0xB993F2F2,
			0xE4D8601C, 0x49E2EEDE, 0x9CD50CE1, 0xC03E1E77, 0xA901869E,
			0x7579DE50, 0x726AC4AB, 0x38D04840, 0xEABE1270, 0x8C40812D,
			0xE84976B7, 0x172B04AD, 0x756606C4, 0x66258491, 0xB5A0BEF8,
			0x6BCC5CF3, 0xA535AE94, 0xC97A87AA, 0x9103A8F6, 0xCC3B9E5F,
			0xBB20BE1F, 0xFFCFEF97, 0x90954F16, 0x501AE1A6, 0x6ED589CD,
			0x6826B02B, 0x565FF263, 0x8E8C369B, 0x6990BE7A, 0x3525B840,
			0x1847D7BB, 0x355A40C7, 0xA3579F10, 0xE9EDECAE, 0xD0337AB1,
			0x6355E5BA, 0x88975355, 0x5EC0F3CF, 0xA0D6213D, 0x75389387,
			0xE40216F0, 0xD980CCE0, 0x6C88C67C, 0x829D419C, 0x3BF6451B,
			0x11F07BFA, 0xC4C1154E, 0xBD0735EB, 0x9CF8DF9D, 0xE457BE75,
			0x63A6BD18, 0xEFE77FD3, 0x83421B63, 0x7F83072D, 0x44940F61,
			0xF8BDCDF7, 0x61C802CA, 0x0A30F9A8, 0x7FF03B37, 0xA26CC5A9,
			0xE10E570D, 0x95EA0C16, 0xA05E6B02, 0xC81D5384, 0x7785DB05,
			0x92C84C5F, 0x05584617, 0x82BCFE8D, 0x559EA1DA, 0x4FD5CDB0,
			0x9D871FED, 0xDD6F5539, 0x4ED1EF26, 0xFE6813C4, 0x1CFA71D5,
			0xD5613AEA, 0x0F1C9B8C, 0x2BCAC45D, 0x65D00F41, 0x689BE0D8,
			0x68B01100, 0x635BD280, 0x954D5D4B, 0x72887F79, 0xCE027A75,
			0xFCF01C66, 0x006A1BD3, 0x199A1C8E, 0x87D6EE25, 0x938E9F08,
			0xD8A11D4D, 0x2B9A4D81, 0xB6F5D2E5, 0xD15C325A, 0x64EAAFC1,
			0xFD33B61C, 0x43C1BD57, 0x37B8F048, 0x5CBA7CF2, 0x72810CD0,
			0xABFEF454, 0xA76384BA, 0xD8861440, 0x36DE5837, 0x0F6A03F1,
			0x10D48FA1, 0x5883EC2F, 0xA8C00C9B, 0x618FFEA4, 0xA05DA206,
			0xFFB9E97A, 0x8A376781, 0x3156B479, 0xE4AF5ECD, 0x87D9E06F,
			0xB4D4D459, 0xEB9A7D25, 0x59DFFEAA, 0xDC8BF553, 0x6DCE3C3A,
			0x2162970E, 0xE8C9929D, 0x6C3A9BF4, 0x45DA5392, 0x9CEEE7B0,
			0x3F68D4EB, 0xCD29434F, 0x0E4DF712, 0xB1A8C69A, 0x1C190F46,
			0x2B45873C, 0x46AFDFC9, 0x61E8883F, 0x979118C7, 0x70F991B1,
			0x1F82604D, 0xC18BF48F, 0xB327F4FF, 0x519A7508, 0xFA619B0D,
			0x268D1490, 0x567E37C2, 0x25A07691, 0x424359C0, 0x13320C53,
			0xEFF742FD, 0x48B945BA, 0xCFA8E711, 0x8F5FB519, 0x2B7332A5,
			0x10AA767C]

def ROR(x, n, bits = 32):
    mask = (2**n) - 1
    mask_bits = x & mask
    return (x >> n) | (mask_bits << (bits - n))

def ROL(x, n, bits = 32):
    return ROR(x, bits - n, bits)
	
def QSplit(qw):
	low = qw & 0xffffffff
	high = (qw & 0xffffffff00000000)>>0x20
	return low, high
	
def Loop4EC(x, y , i):
	global g_Lookup3
	v = g_Lookup3[i*2]
	i1 = (y+v) & 0xFFFFFFFF
	i2 = x^i1
	
	v2 = g_Lookup3[i*2 + 1]
	i3 = v2 | i2
	i4 = i3 ^ y
	return i2, i4

def Func482(a,  x, y):
	# print('FUNC 482 %x %x %x'%(a, x,y))
	a_low , a_high = QSplit(a)
	
	i1 = a_high ^ y 
	i2 = a_low ^ x
	
	i3 = ROL(i2, 4) ^ y
	i4 = ROR(i1, 0x12) ^ x
	
	return i3, i4

def UnFunc482(i,  x, y):
	# print('UNFUNC 482 %x %x %x'%(i, x,y))
	i3 , i4 = QSplit(i)
	
	i1 = ROL(i4^x , 0x12) 
	i2 = ROR(i3 ^y, 4)
	
	a_low = i2 ^ x 
	a_high = i1 ^ y 

	
	return (a_high<<0x20 | a_low)
	
def Func438(b, x, y):
	b_low , b_high = QSplit(b)
	
	i1 = b_low ^y
	i2 = ROL(i1, 0x1A)
	
	i3 = b_high ^ y ^ x
	i4 = ROR(i3, 0xe)
	
	return (i4<<0x20 | i2)

def UnFunc438(b, x, y):
	# print("UNFUNC 438 %x %x %x"%(b,x,y))
	i2, i4  = QSplit(b)
	
	i3 = ROL(i4, 0xe)
	i1 = ROR(i2, 0x1A)
	
	b_low = i1 ^y
	
	b_high = i3 ^ y ^ x
	
	return (b_high<<0x20 | b_low)
	
def Crypto(a,b,c,d, it):
	global g_Lookup3
	
	b_low , b_high = QSplit(b)
	c_low , c_high = QSplit(c)
	d_low , d_high = QSplit(d)
	
	for i in range(it+1):
		v = g_Lookup3[12+i]
		i1 = v ^ c_low
		c_high = (0x45786532 + c_high) & 0xFFFFFFFF
		d_low = c_high ^d_low
		
		c_low = (i1 - c_high)&0xFFFFFFFF
		d_high = ROL(d_high, 4)
	
		if d_low & 0x80000000:
			i6 = 0x60bf080f
		else:
			i6 = 0x818f694a
			
		c_high = i6 ^ c_high ^ d_high
		
		
	x, y = b_low, b_high
	for i in range(6):
		x,y  = Loop4EC(x,y, i)
	i7, i8 = Func482(a, x, y)

	y2 = i8 ^ c_high 
	x2 = i7 ^ c_low
	
	new_a = (x2 |y2 << 0x20)
	
	for i in range(6):
		x2,y2 = Loop4EC(x2,y2, i)
	new_b = Func438(b,x2,y2) ^ (d_low | d_high<<0x20)
	
	return new_a,new_b

def UnCrypto(a,b,c,d, it):
	global g_Lookup3
	
	c_low , c_high = QSplit(c)
	d_low , d_high = QSplit(d)
	
	#KEY DERIVATION
	for i in range(it+1):
		v = g_Lookup3[12+i]
		i1 = v ^ c_low
		c_high = (0x45786532 + c_high) & 0xFFFFFFFF
		d_low = c_high ^d_low
		
		c_low = (i1 - c_high)&0xFFFFFFFF
		d_high = ROL(d_high, 4)
	
		if d_low & 0x80000000:
			i6 = 0x60bf080f
		else:
			i6 = 0x818f694a
			
		c_high = i6 ^ c_high ^ d_high
	
	x2 , y2 = QSplit(a)

	i7 = x2 ^c_low
	i8 = y2 ^c_high
	
	for i in range(6):
		x2,y2 = Loop4EC(x2,y2, i)
		
	clear_b = UnFunc438((b ^(d_low | d_high<<0x20)) ,x2,y2) 
	
	x, y = QSplit(clear_b)
	for i in range(6):
		x,y  = Loop4EC(x,y, i)
	clear_a = UnFunc482( (i7|( i8 << 0x20)), x, y)

	return clear_a,clear_b

def Hash(a, b):
	global g_Lookup
	for i in range(4):
		a_low , a_high = QSplit(a)
		b_low , b_high = QSplit(b)
		
		
		i1 = ((b_low + a_high) ^ a_low) & 0xFFFFFFFF
		i2 = a_high & b_low
		i3 = (b_low - i1) & 0xFFFFFFFF
		
		v = g_Lookup[b_high&0xFF]
		i4 = (i1 + v)& 0xFFFFFFFF
		
		i5 = (b_high>>8)^i4
		
		b = (i5<<0x20)|i3
		a = (i2<<0x20)|i4
	return a,b

def Encrypt(a, b, c, d):
	for i in range(4):
		ch, dh  = Hash(c, d)
		# print('hash1 : %x %x'%(ch, dh))
		enc_a, enc_b = a, b
		for l in range(15):
			enc_a, enc_b = Crypto(enc_a,enc_b,ch,dh, l )

		ah, bh   = Hash(enc_a, enc_b)
		# print('hash2 : %x %x'%(ch, dh))
		enc_c, enc_d = c,d
		for l in range(15):
			enc_c, enc_d = Crypto(enc_c,enc_d,ah,bh, l )
		a,b,c,d = enc_a, enc_b, enc_c, enc_d
		
	return a, b, c, d

def Decrypt(a,b,c,d):
	for i in range(4):
		ah, bh   = Hash(a, b)
		# print('hash2 : %x %x'%(ah, bh))
		dec_c, dec_d = c,d
		for l in range(15):
			dec_c, dec_d = UnCrypto(dec_c,dec_d,ah,bh, 14-l )
			
		ch, dh  = Hash(dec_c, dec_d)
		# print('hash1 : %x %x'%(ch, dh))
		dec_a, dec_b = a, b
		for l in range(15):
			dec_a, dec_b = UnCrypto(dec_a,dec_b,ch,dh, 14-l )

		a,b,c,d = dec_a, dec_b, dec_c, dec_d
	return a, b, c, d
		
def test():
	a_in = 0x77447b4349545353
	b_in = 0x315f4d565f667234
	c_in = 0x695f6c306f635f73
	d_in = 0x7d74495f745f6e73
	
	a, b, c ,d = Encrypt(a_in, b_in, c_in, d_in)
	print('encrypted %x %x %x %x'%(a,b,c,d))
	
	a,b,c,d = Decrypt(a,b,c,d)
	print('decrypted: %x %x %x %x'%(a,b,c,d))
	
	if a != a_in or b != b_in or c!= c_in or d!=d_in:
		print("[ERR] test failed")
	else:
		print('TEST OK')
	
test()
a = 0x65850b36e76aaed5
b = 0xd9c69b74a86ec613
c = 0xdc7564f1612e5347
d = 0x658302a68e8e1c24
a,b,c,d = Decrypt(a,b,c,d)
print('flag: %s'%(struct.pack('4Q', a, b,c,d)))

