import math

# Neuron
class Neuron:
    def __init__(self, weights, bias, learning_rate):
        self.weights = weights
        self.bias = bias
        self.learning_rate = learning_rate

    def forward(self, x):
        self.last_input = x
        z = sum(x_i * w_i for x_i, w_i in zip(x, self.weights)) + self.bias
        self.last_output = 1 / (1 + math.exp(-z))  # Sigmoid
        return self.last_output

    def backward(self, delta):  # delta is already error * sigmoid_derivative
        for i in range(len(self.weights)):
            self.weights[i] -= self.learning_rate * delta * self.last_input[i]
        self.bias -= self.learning_rate * delta

    def sigmoid_derivative(self):
        return self.last_output * (1 - self.last_output)


# Layer
class Layer:
    def __init__(self, neurons):
        self.neurons = neurons

    def forward(self, x):
        return [neuron.forward(x) for neuron in self.neurons]

    def backward(self, deltas):
        for neuron, delta in zip(self.neurons, deltas):
            neuron.backward(delta)


# Network
class Network:
    def __init__(self, hidden_layer, output_layer):
        self.hidden_layer = hidden_layer
        self.output_layer = output_layer

    def forward(self, x):
        self.hidden_output = self.hidden_layer.forward(x)
        return self.output_layer.forward(self.hidden_output)

    def backward(self, output_errors):
        # Oblicz deltę warstwy wyjściowej
        output_deltas = [error * neuron.sigmoid_derivative()
                         for neuron, error in zip(self.output_layer.neurons, output_errors)]

        self.output_layer.backward(output_deltas)

        # Oblicz błędy dla warstwy ukrytej
        hidden_errors = []
        for j, hidden_neuron in enumerate(self.hidden_layer.neurons):
            error = sum(
                output_deltas[i] * self.output_layer.neurons[i].weights[j]
                for i in range(len(self.output_layer.neurons))
            )
            hidden_errors.append(error)

        self.hidden_layer.backward(hidden_errors)
