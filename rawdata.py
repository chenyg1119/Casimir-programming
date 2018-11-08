import numpy as np

def raw(N, center, width, strength, sigma):
    """generate raw data and return raw[N]
    
    ------
    parameter:
    N = total # of data
    center = center of signal
    width = width of the signal
    strength = signal strength
    sigma = noise strength
    
    ------
    return:
    raw data
    """
    rawspace = np.linspace(0.4*np.pi,0.7*np.pi,N)
    signal_interval = np.linspace(0,np.pi,width)
    signal = strength*np.sin(signal_interval)
    pure = np.sin(rawspace)
    noise = sigma*np.random.normal(0,1,N)
    pure[int(center-np.floor(width/2)):int(center-np.floor(width/2)+width)] += signal
    return pure, pure + noise