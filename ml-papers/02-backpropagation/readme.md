🧪 Learning Representations by Back-Propagating Errors
Paper: Learning representations by back-propagating errors
Authors: David E. Rumelhart, Geoffrey E. Hinton, Ronald J. Williams
Published: 1986
Link: https://www.nature.com/articles/323533a0

🎯 Goal of the Paper
What problem is the paper solving?
What’s the key idea or contribution?

Introduces backpropagation as a general method for training multi-layer feedforward neural networks.

Demonstrates that multi-layer networks can learn non-linearly separable functions like XOR.

Provides a practical way to compute gradients efficiently using the chain rule.

🧠 Model Architecture
What is the structure of the proposed model?

Input size: 2 (binary input for XOR)

Number of layers: 2 (1 hidden layer + 1 output layer)

Hidden units: 3 neurons in hidden layer

Activation function(s): Sigmoid for both hidden and output layers

Output type: Single neuron for binary classification (output ∈ [0, 1])

🧮 Mathematical Formulas
What are the key equations?

Forward Pass:

Linear combination: z = w · x + b

Activation: a = 1 / (1 + exp(-z)) (Sigmoid)

Loss Function:

MSE:
L = (1/2) * Σ(y_true - y_pred)^2

Backpropagation:

Output layer error:
δ = (y_pred - y_true) * sigmoid_derivative(output)

Hidden layer error:
δ = Σ(output_δ * w) * sigmoid_derivative(hidden)

Weight update:
w -= learning_rate * δ * input

Bias update:
b -= learning_rate * δ

📚 Learning Algorithm
How is the model trained?

Type: Supervised Learning

Optimization: Manual gradient descent

Update Rules: Weight and bias updated using derivatives from backpropagation

Epochs: 1000 iterations through the full XOR dataset (4 examples)

✅ Tests & Results
How do you know your model works?

 Accuracy/loss curve: ✅ MSE curve plotted

 Comparison to paper results: ❌ Not compared

 Does it solve XOR? ✅ Accuracy 100%

 Manual print/debug: ✅ Printed MSE, weights, predictions

🧠 Observations & Reflections
What did you learn?

What worked well:
Forward and backward pass logic is now clear and traceable.

Correctly implemented sigmoid and its derivative.

What went wrong:
❌ Used two output neurons for XOR instead of one — caused instability.

❌ Used argmax() on [0, 1] target vectors instead of scalar labels.

❌ learning_rate was initially too high, causing loss to increase.

❌ Bias update was initially wrong (missing delta).

❌ Misunderstood output activation behavior — needed to threshold at 0.5 for binary classification.

What surprised me:
Even small bugs (e.g. in sigmoid_derivative or weight indexing) can completely stop learning.

Initial weights and learning rate affect convergence dramatically.

❗ Known Limitations
Where does this implementation fall short?

❌ No support for batching or vectorized operations (inefficient).

❌ Manual implementation without autograd (e.g., PyTorch or TensorFlow).

❌ Only works for fixed-size inputs and outputs (no dynamic architectures).

❌ Only MSE loss used — for classification, cross-entropy would be better.

❌ No input normalization or early stopping.