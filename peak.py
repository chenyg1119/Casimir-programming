from numpy import diff
def findcenter(data,offset):
    offset = 100
    first_der = np.append(diff(denoised),0)
    second_der = np.append(diff(first_der),0)
    radius_inverse = abs(second_der)/((1+(first_der)**2)**1.5)
    return argmax(radius_inverse[offset:-offset])+offset