import numpy as np
import csv
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# This creates a convenient way to refer to each column in the
# csv file. it's in 'fieldnames' of Dictreader.
i=[]
for j in range(102):
	i.append(j)

# These hold the frequencies and their averaged intensities.
data = np.zeros((10,100))
frequency = np.zeros(100)
files = range(1,11)

# This iterates over each time(row) of a frequency(column) and
# gets an average at that frequency.
for file in files:
	for freq in range(2,102):
		with open('%s0ft_nobiastee.csv' % file, 'rb') as csvfile:
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
			data[file-1,freq-2]= summ/float(counter)


# There are some weird peaks at the edge of the bandwidth, so I 
# just sample the inner frequencies (e.g. [5:-5])
for file in files:
	# plt.plot(file*10, data[file-1][49],'bo', markersize=10)
	plt.plot(file*10, max(data[file-1][5:-5]),'ro')
plt.show()
# plt.savefig('peaksVdist.pdf', format='pdf')

