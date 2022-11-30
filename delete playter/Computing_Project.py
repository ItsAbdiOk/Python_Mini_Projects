# libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from numpy import mean as ma
#%%
"This code is to clean the txt file"
d_mpc = open('Distance_Mpc.txt', 'r') # read in the data
TempList = []# the list which will hold d_mpc
distance_array = np.array([]) # the array that will hold the list

for line in d_mpc:  # read the file
    row = line.split()   # split the line into rows
    if row[-1] == '1':   # check if the last item in the row is 0
        TempList.append(row) # if it is then append the row to the list
for i in range(len(TempList)): # delete the last item in the row
    del TempList[i][-1]

distance_array = np.array(TempList) # store the list in an array


def gaussian_linear(x,a,mu,sig,m,c): # the function that I want to fit to my curves with
    gaus = a*np.exp(-(x-mu)**2/(2*sig**2)) # gaussian distribution
    line = m*x+c # linear equation
    return gaus + line
#%%
"This code is to set up fitted graphs"
#[Reference] I took some code from core worksheet 2
Halpha_spectral = np.loadtxt("Halpha_spectral_data.csv", skiprows=3, delimiter=",")
TempArray= []
for i in range(0,60,2):
    if str(int(Halpha_spectral[0][i])) not in distance_array[:,0]: # ignore invalid data
        continue
    x = Halpha_spectral[:,i][1:] # iterate through for dependent variable (spectral intensity)
  
    TempArray.append([x]) # store the data in a list
    y = Halpha_spectral[:,i+1][1:] # iterate through for independent variable (frequency)
    No = Halpha_spectral[:,i][0]
    
    #calculations made using the average first and last data points
    m = (ma(y[0:40]) - ma(y[959:999]))/(ma(x[0:40]) - ma(x[959:999]))
    c = ma(y[0:40]) - m*ma(x[0:40]) # mean imported as ma
    #residuals to flatten the curve
    residuals = y - (m*x + c)    
    
    a = max(residuals)
    amp = max(residuals) - min(residuals)
    #[Reference: https://numpy.org/doc/stable/reference/generated/numpy.where.html]
    ind = np.where(np.isclose(a,residuals)) # mean
    sig = np.std(x, ddof=1) #std
    
    initial_guess = [amp,x[ind][0],sig,m,c]

    po,po_cov = curve_fit(gaussian_linear,x,y,initial_guess,maxfev = 10000000) #maxfev increases the number of permutations from scipy
    #further formatting
    nl = np.linspace(min(x),max(x),1000)
     
bruh = []
for number in TempArray[:1000]:
    bruh = number + bruh

sum = 0
for item in bruh:
    sum = sum + item

print (sum)