import numpy
import time
import random
import math

class Neuron():
	def __init__(self, window_size, threshold, inputs):
		self.threshold = threshold
		self.window_size = window_size
		self.output = 0
		self.num_inputs = inputs
		self.weights = [0 for i in range(0,self.num_inputs)]
		self.dendrites = [[0 for i in range(self.window_size)] for j in range(self.num_inputs)]
		
	def check_spike(self, input):

		#put new inputs at the front of the list

		for x in range(0, self.num_inputs):
			self.dendrites[x].insert(0, input[x])
			self.dendrites[x].pop(self.window_size)

		#calculate the membrane potential
		

		sum = [0 for i in range(0, self.num_inputs)]
		
		for x in range(0, self.num_inputs):
			for y in range(0, self.window_size):
				sum[x] += (self.dendrites[x][y] << ((self.window_size-1) - y))

		
		for x in range(0, self.num_inputs):
			sum[x] += (self.weights[x])

		
		for x in range(0, self.num_inputs):
			sum[x] *= self.dendrites[x][0]
		
		
		membrane_pot = 0
		for x in range(0, self.num_inputs):
			membrane_pot += sum[x]

	
		#spike and adjust weights

		if membrane_pot > self.threshold:
			self.output = 1
			#spike!
			for x in range(0, self.num_inputs):
				if self.dendrites[x][0] == 1:
					self.weights[x] += 5
				elif self.dendrites[x][1] == 1:
					self.weights[x] += 2
				elif self.dendrites[x][2] == 1:
					self.weights[x] += 1
				else:
					self.weights[x] += -10
		else:
			self.output = 0


		return self.output

		

		
		

if __name__ == "__main__":
	numNeruons = 128
	threshold = 254 * 1
	numTrials = 100
	brain = [Neuron(8, threshold, numNeruons) for i in range(0,numNeruons)] 

	inputNumber = [1 for u in range(0,numNeruons)]
	for x in range(0, numNeruons):
		if x % 2 == 0:
			inputNumber[x] = 1
	synapses = [[0 for i in range(0,numNeruons)] for j in range(0,numNeruons)]

	for x in range(0, numNeruons):
		synapses[x][x] = inputNumber[x]

	print("Test Number: ")
	print(inputNumber)
	print("Output before training: ")


	output = [0 for i in range(0, numNeruons)]

	print(output)


	print("Training...")
	for y in range(0, numTrials):
		for x in range(0,numNeruons):
			output[x] = brain[x].check_spike(synapses[x])
			#print(brain[x].weights)
		for j in range(0, numNeruons):
			synapses[j] = output
			synapses[j][j] = inputNumber[j]
	print("Done")
	print("Output after training on Test Number:")
	print(output)	

	for y in range(0, 1):
		for x in range(0,numNeruons):
			output[x] = brain[x].check_spike(synapses[x])
		for j in range(0, numNeruons):
			synapses[j] = output
			synapses[j][j] = inputNumber[j]
	print("Repeat Test Number after training")
	print(output)


	for g in range(0,numNeruons):
		if g % 3 == 1:
			synapses[g][g] = 1
		else:
			synapses[g][g] = 0
	inputNumber = [0 for u in range(0,numNeruons)]

	for u in range(0, numNeruons):
		if u % 3 == 1:
			inputNumber[u] = 1
		else:
			inputNumber[u] = 0

	print("New number to test:")
	print(inputNumber)

	for y in range(0, 1):
		for x in range(0,numNeruons):
			output[x] = brain[x].check_spike(synapses[x])
		for j in range(0, numNeruons):
			synapses[j] = output
			synapses[j][j] = inputNumber[j]
	print("New number output:")
	print(output)







				

	


