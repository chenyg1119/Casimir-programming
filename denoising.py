from numpy import *
import scipy
import pywt
# import seaborn
from statsmodels.robust import mad
import matplotlib.pyplot as plt

def waveletSmooth( x, wavelet="db4", level=1, title=None ):
    # calculate the wavelet coefficients
    coeff = pywt.wavedec( x, wavelet, mode="per" )
    # calculate a threshold
    sigma = mad( coeff[-level] )
    # changing this threshold also changes the behavior,
    # but I have not played with this very much
    uthresh = sigma * np.sqrt( 2*np.log( len( x ) ) )
    coeff[1:] = ( pywt.threshold( i, value=uthresh, mode="soft" ) for i in coeff[1:] )
    # reconstruct the signal using the thresholded coefficients
    y = pywt.waverec( coeff, wavelet, mode="per" )
    f, ax = plt.subplots()
    plt.plot( x, color="b", alpha=0.5 )
    plt.plot( y, color="b" )
    if title:
        ax.set_title(title)
    ax.set_xlim((0,len(y)))

waveletSmooth(rawdata)

# wavelet = pywt.Wavelet('haar')
# levels  = (np.floor(np.log(rawdata))).astype(int)
# WaveletCoeffs = pywt.wavedec2( rawdata, wavelet, level=levels)

# denoise = pywt.threshold(rawdata,1,'soft')
# plt.plot(denoise)