from scipy.ndimage.filters import maximum_filter
import numpy as np
import matplotlib.pyplot as plt
import bitarray
import binascii 

#open numpy plot
x = np.load('power.npz')
data = x['arr_0']
plt.plot(data)
plt.show()

#filter on RSA exponentiation
data2 = data[700000:1500000]

#filter noise/transform input to a sinusoide like form
flt = maximum_filter(data2, 200)
plt.plot(flt)
plt.show()

#squarify input
threshold = flt> 0.19
plt.plot(threshold)
plt.show()

#Target's RSA modular exponentiation is implemented using two differents calculus depending on key (square or square and multiply)
#See https://en.wikipedia.org/wiki/Modular_exponentiation

#calculate waveform "lenght" (is this a square or a square-and-multiply?)
count = 0
arr =  []
for v in threshold:
    if v == False:
        if count != 0:
            arr.append(count)
            count= 0
    else:
        count += 1

#Transfor to boolean list
arr = np.array(arr[:-4])
tf = arr > 350

#to bitarray
ba = bitarray.bitarray(list(tf))
#endianness...
ba.reverse()
#RSA key :)
print(binascii.hexlify(ba.tobytes()))
