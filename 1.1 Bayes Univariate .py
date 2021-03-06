import numpy as np
import statistics

#declaring the feature vector for the three classes
class1 = np.array([1.58,0.67,1.04,-1.49,-0.41,1.39,1.20,-0.92,0.45,-0.76])

class2 = np.array([0.21,0.37,0.18,-0.24,-1.18,0.74,-0.38,0.02,0.44,0.46])

class3 = np.array([-1.54,5.41,1.55,1.86,1.68,3.51,1.40,0.44,0.25,-0.66])

#print("class 1:", class1, '\n')
#print("class 2:", class2, '\n')
#print("class 3:", class3, '\n')

#the unknown pattern we need to classify
x = 1.8

#var = variance
#calculating mean and variance for class1
mean1 = np.mean(class1)
var1 = (statistics.pvariance(class1))

#calculating mean and variance for class2
mean2 = np.mean(class2)
var2 = (statistics.pvariance(class2))

#calculating mean and variance for class3
mean3 = np.mean(class3)
var3 = (statistics.pvariance(class3))

#print ("mean for class 1:", mean1, '\n')
#print ("mean for class 2:", mean2, '\n')
#print ("mean for class 3:", mean3, '\n')

#print ("variance for class1:", var1, '\n')
#print ("variance for class2:", var2, '\n')
#print ("variance for class3:", var3, '\n')

#substituting mean and variance in the discriminant function for each class
g1 = -0.5*np.log(var1) - (x-mean1)*(x-mean1)/(2*var1) + np.log(1/3)

g2 = -0.5*np.log(var2) - (x-mean2)*(x-mean2)/(2*var2) + np.log(1/3)

g3 = -0.5*np.log(var3) - (x-mean3)*(x-mean3)/(2*var3) + np.log(1/3)

#print(g1)
#print(g2)
#print(g3)

#comparing the discriminant functions with each other
if (g1 > g2) & (g1 > g3):
    print('The classification result for the unknown pattern x is that it belongs to class 1')

elif (g2 > g1) & (g2 > g3):
    print('The classification result for the unknown pattern x is that it belongs to class 2')

else:
    print('The classification result for the unknown pattern x is that it belongs to class 3')
