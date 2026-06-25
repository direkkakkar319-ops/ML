from layer import Layer


class MLP:
    """
    Represents a Multi-Layer Perceptron (MLP).

    An MLP is a feedforward neural network composed of one or more
    fully connected layers. The output of each layer becomes the
    input to the next layer.

    The network architecture is defined by a list of layer sizes.
    For example:
        sizes = [3, 4, 4, 1]

    creates:
        - 3 input features
        - first hidden layer with 4 neurons
        - second hidden layer with 4 neurons
        - output layer with 1 neuron
    """

    def __init__(self, sizes):
        """
        Initialize the neural network.

        Consecutive values in `sizes` define the input and output
        dimensions of each layer.

        Args:
            sizes: List of integers describing the network
                architecture.
        """
        self.layers = [
            Layer(
                n_inputs=sizes[i],
                n_outputs=sizes[i + 1]
            )
            for i in range(len(sizes) - 1)
        ]

    def __call__(self, x):
        """
        Perform a forward pass through the network.

        The input is passed sequentially through every layer.

        Args:
            x: Iterable containing the input features.

        Returns:
            The network output.

            If the output layer contains one neuron, a single
            Value object is returned. Otherwise, a list of Value
            objects is returned.
        """
        for layer in self.layers:
            x = layer(x)

        return x[0] if len(x) == 1 else x

    def parameters(self):
        """
        Return all trainable parameters in the network.

        Collects the parameters from every layer and flattens them
        into a single list.

        Returns:
            A list containing every weight and bias in the MLP.
        """
        return [
            parameter
            for layer in self.layers
            for parameter in layer.parameters()
        ]