import math

from softmax import softmax

def cross_entropy_loss(true_classes, logits):
    probability = softmax(logits)
    return -math.log(probability[true_classes])

if __name__ == "__main__":
    logits = [2.0, 1.0, 0.1]
    true_class = 0

    probs = softmax(logits)
    loss = cross_entropy_loss(true_class, logits)

    print(f"Logits:      {logits}")
    print(f"Softmax:     {[f'{p:.4f}' for p in probs]}")
    print(f"True class:  {true_class}")
    print(f"Loss:        {loss:.4f} nats")
    print(f"Perplexity:  {math.exp(loss):.2f}")
