import numpy
import time
import random

class Neuron():
	def __init__(self, threshold, leak, spike_val):
		self.threshold = threshold
		self.leak = leak
		self.output = 0
		self.membrane_pot = 0
		self.spike_val = spike_val

	def spike(self, weights = [], connections = []):
		# V(t) = V(t-1) + (S_pos)(n_pos)(t) - (S_neg)(n_neg)(t) - leak
		tally = 0.0
		for x in range(0,len(weights)):
			if connections[x] != 0:
				tally = (connections[x] * weights[x]) + tally
		self.membrane_pot = self.membrane_pot + tally 
		if self.membrane_pot > self.threshold:
			#spike
			#print("Spike!")
			self.membrane_pot = 0
			self.output = self.spike_val
		else:
			if self.output > 0:
				self.output += (-1)*(random.randrange(1,leak+1,1))
			else:
				self.output = 0
		return self.output


class SynapseArray():
	def __init__(self, size, spike_val):
		self.connections = []
		self.weights = []
		self.weights_temp = []
		for x in range(0,size):
			self.weights.append(random.randrange(0,spike_val+1,1))
		self.weights_temp = self.weights
		self.connections = [[random.randrange(-1,2,1) for y in range(size)] for x in range(size)]

if __name__ == "__main__":
	size = 128
	threshold = 60
	leak = 5
	spike_val = 100
	num_tests = 10000
	synapses = SynapseArray(size, spike_val)
	brain = []
	for x in range(0,size):
		brain.append(Neuron(threshold, leak, spike_val))
		brain[x].output = synapses.weights[x]
	print("before")
	#print(synapses.connections)
	print(synapses.weights)
	for x in range(0,num_tests):
		for y in range(0,size):
			synapses.weights_temp[y] = brain[y].spike(synapses.weights, synapses.connections[y])
		synapses.weights = synapses.weights_temp
		#print(synapses.weights)
	print("after")
	print(synapses.weights)


