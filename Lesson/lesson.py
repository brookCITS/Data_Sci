import matplotlib.pyplot as plt
import numpy as np


#Basic Plotting
xpoints = np.array([0, 5])
ypoints = np.array([0, 5])

#plt.plot(xpoints, ypoints)
#plt.show()

'''
#Markers
plt.plot(xpoints, ypoints, marker='o')
plt.show()

plt.plot(xpoints, ypoints, marker='*')
plt.show()

plt.plot(xpoints, ypoints, marker='+')
plt.show()

plt.plot(xpoints, ypoints, marker='D')
plt.show()

'''


'''
#Markers with formated strings
plt.plot(xpoints, ypoints, '*:m')
plt.show()
plt.plot(xpoints, ypoints, 'o-g')
plt.show()
plt.plot(xpoints, ypoints, 'D:r', ms=20)
plt.show()
plt.plot(xpoints, ypoints, 'P--b', ms=50)
plt.show()

'''
'''

#Plot labels and title
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
temperatures = [72, 75, 68, 80, 82, 77, 79]

plt.plot(days, temperatures, 'o-g')
plt.xlabel('Days of the Week')
plt.ylabel('Temperature (°F)')
plt.title('Weekly Temperature Changes')
plt.grid()
plt.show()

'''

#SubPlots
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
week1_temp = [72, 75, 68, 80, 82, 77, 79]
week2_temp = [73, 80, 64, 93, 92, 53, 65]

#plot 1:
plt.subplot(2, 1, 1)
plt.plot(days,week1_temp, 'o-g')
plt.ylabel('Temperature (°F)')
plt.title('Week 1 Temperature Changes')

#plot 2:

plt.subplot(2, 1, 2)
plt.plot(days,week2_temp, '*:r')
plt.xlabel('Days of the Week')
plt.ylabel('Temperature (°F)')
plt.title('Week 2 Temperature Changes')

plt.show()
