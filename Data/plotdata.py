import numpy as np
import csv
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


# This creates a convenient way to refer to each column in the
# csv file. it's in 'fieldnames' of Dictreader.
i=[]
for j in range(102):
	i.append(j)

# These hold the frequencies and their averaged intensities.
data = np.zeros(100)
frequency = np.zeros(100)

# This iterates over each time(row) of a frequency(column) and
# gets an average at that frequency. At the moment we'll just 
# change the file name to get to a different distance.
for freq in range(2,102):
	with open('10ft_nobiastee.csv', 'rb') as csvfile:
		reader = csv.DictReader(csvfile, fieldnames=i)
		t=0
		counter = 0
		summ = 0
		for row in reader:
			if t>0:
				summ += int(row[freq])
				counter += 1
			else:
				frequency[freq-2] = int(row[freq])
				t += 1
		data[freq-2]= summ/float(counter)

print 'Max Frequency:', frequency[np.argmax(data)]
print 'Max \'Intensity\':', max(data)

plt.plot(frequency, data)
plt.show()
