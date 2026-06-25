from neuron import Neuron


class Layer:
    """
    Represents a fully connected neural network layer.

    A layer is a collection of neurons that all receive the same
    input vector. Each neuron independently computes its output,
    producing one element of the layer's output.
    """

    def __init__(self, n_inputs, n_outputs):
        """
        Initialize the layer.

        Creates the specified number of neurons, where each neuron
        is connected to every input feature.

        Args:
            n_inputs: Number of input features received by each
                neuron.
            n_outputs: Number of neurons in the layer.
        """
        self.neurons = [Neuron(n_inputs) for _ in range(n_outputs)]

    def __call__(self, x):
        """
        Perform a forward pass through the layer.

        Each neuron receives the same input vector and computes its
        own output.

        Args:
            x: Iterable containing the input values.

        Returns:
            A list of Value objects, one for each neuron in the
            layer.
        """
        return [neuron(x) for neuron in self.neurons]

    def parameters(self):
        """
        Return all trainable parameters in the layer.

        Collects the parameters from every neuron and flattens them
        into a single list.

        Returns:
            A list containing every weight and bias in the layer.
        """
        return [
            parameter
            for neuron in self.neurons
            for parameter in neuron.parameters()
        ]
