import random


class Perceptron:
    def __init__(self, learning_rate=0.1):
        self.w1 = random.random()
        self.w2 = random.random()
        self.bias = random.random()
        self.learning_rate = learning_rate

    def fit(self, X, y):
        for epoch in range(20):
            for i in range(len(X)):
                print(X[i],y[i])
                prediction = self.predict(X[i])
                error = y[i] - prediction
                if error == 0:
                    continue
                self.w1 += self.learning_rate * error * X[i][0]
                self.w2 += self.learning_rate * error * X[i][1]
                self.bias += self.learning_rate * error

        print(self.w1,self.w2)

    def predict(self, x):
        z = x[0] * self.w1 + x[1] * self.w2 + self.bias
        if z > 0:
            return 1
        else:
            return 0