import numpy, random, os
lr = 1 #learning rate
bias = 1 #value of bias
weights = [random.random(),random.random(),random.random()] #weights generated in a list (3 weights in total, 2 for neurons, 1 for bias)

def Perceptron(input1, input2, output):
    outputP = input1*weights[0]+input2*weights[1]+bias*weights[2]
    #activation function
    if outputP>0:
        outputP = 1
    else:
        outputP = 0
    error = output - outputP
    #update weights
    weights[0] += error*input1*lr
    weights[1] += error*input2*lr
    weights[2] += error*bias*lr

#learning
for i in range(50) :
    Perceptron(1,1,1)
    Perceptron(1,0,1)
    Perceptron(0,1,1)
    Perceptron(0,0,0)

#testing
x = int(input())
y = int(input())
outputP = x*weights[0]+y*weights[1]+bias*weights[2]
if outputP>0:
    outputP=1
else:
    outputP=0
print(x,"or",y,"is:",outputP)

outputP = 1/(1+numpy.exp(-outputP)) #sigmoid function
