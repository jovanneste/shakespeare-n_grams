import numpy as np

with open('Shakespeare.txt') as f:
	data = f.read().rstrip().split(' ')
data = [x.lower() for x in data if x!='' and '\n' not in x and "'" not in x.split() and "." not in x.split()]

counts = {}

def compute(n):
	for i in range(len(data)-n):
		if n==2:
			try:
				counts[(data[i], data[i+1])] += 1
			except:
				counts[(data[i], data[i+1])] = 0
		elif n==3:
			try:
				counts[(data[i], data[i+1], data[i+2])] += 1
			except:
				counts[(data[i], data[i+1], data[i+2])] = 0
		elif n==4:
			try:
				counts[(data[i], data[i+1], data[i+2], data[i+3])] += 1
			except:
				counts[(data[i], data[i+1], data[i+2], data[i+3])] = 0
		elif n==5:
			try:
				counts[(data[i], data[i+1], data[i+2], data[i+3], data[i+4])] += 1
			except:
				counts[(data[i], data[i+1], data[i+2], data[i+3], data[i+4])] = 0
		else:
			print("Sorry cannot do that.")



	sorted_counts = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))
	pop_words = list(sorted_counts.keys())[:10]
	print(pop_words)



compute(5)