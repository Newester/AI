#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import numpy as np
from scipy.fftpack import fft

x = np.array([1.0,2.0,-1.0,1.5])
y = fft(x) 
print(y)

from scipy.fftpack import ifft

x = np.array([1.0,2.0,-1.0,1.5])
y = fft(x)
yinv = ifft(y)
print(yinv)

from scipy import fftpack
time_step = 0.02
period = 5.
time_vec = np.arange(0,20,time_step)
sig = np.sin(2*np.pi/period*time_vec) + 0.5*np.random.randn(time_vec.size)
print(sig.size)

sample_freq = fftpack.fftfreq(sig.size,d = time_step)
sig_fft = fftpack.fft(sig)
print(sig_fft)

from scipy.fftpack import dct
from scipy.fftpack import idct

mydict =dct(np.array([4.,3.,5.,10.,5.,3.]))
print(mydict)
d = idct(np.array([4.,3.,5.,10.,5.,3.0]))
print(d)
