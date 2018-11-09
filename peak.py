import numpy as np
from numpy import diff
import denoising
def findcenter(rawdata,offset,top_n):
    """return the locations of possible peaks
    ----
    parameters:
    rawdata = input rawdata
    offset = offset to ignore the endpoints of an array to avoid pseudo-peaks
    top_n = the largest top_n peaks
    
    return:
    returns an ndarray of top_n locations
    """
    #set the offset from two ends of the array
    offset = 100
    #find the first and second derivative
    first_der = np.append(diff(denoising.waveletSmooth(rawdata)),0)
    second_der = np.append(diff(first_der),0)
    #find the inverse radius of curvature
    radius_inverse = abs(second_der)/((1+(first_der)**2)**1.5)
    #return the location of peaks which is located at the largest inversed radius
    return np.argsort(radius_inverse[offset:-offset])[::-1][:top_n]+offset