from numpy import *
import scipy
import pywt
from statsmodels.robust import mad
import matplotlib.pyplot as plt

def waveletSmooth( x, wavelet="db4", level=1, title=None ):
    # calculate the wavelet coefficients
    # returns tuple [cA,cDn,...,cD1] one approx. and details coefficients
    # use mode "periodization", or 'per', wavelet decompose(as for wavedec) the vector. len(cA)=len(cD) = len(x)/(2**n)
    coeff = pywt.wavedec( x, wavelet, mode="per" )
    # calculate a threshold
    # mean absolute deviation of cD_level
    sigma = mad( coeff[-level] )
    #threshold = \sigma*\sqrt(2*log(n)/n)
    uthresh = sigma * np.sqrt( 2*np.log(len( x )))
    #apply soft threshold to cD_n
    coeff[1:] = ( pywt.threshold( i, value=uthresh, mode="soft" ) for i in coeff[1:] )
    # reconstruct the signal using the thresholded coefficients
    y = pywt.waverec( coeff, wavelet, mode="per" )
#     f, ax = plt.subplots()
#     plt.plot( x, color="b", alpha=0.1 )
#     plt.plot( y, color="b" )
#     if title:
#         ax.set_title(title)
#     ax.set_xlim((0,len(y)))
    return y[:-1]

waveletSmooth(rawdata)

# wavelet = pywt.Wavelet('haar')
# levels  = (np.floor(np.log(rawdata))).astype(int)
# WaveletCoeffs = pywt.wavedec2( rawdata, wavelet, level=levels)

# denoise = pywt.threshold(rawdata,1,'soft')
# plt.plot(denoise)