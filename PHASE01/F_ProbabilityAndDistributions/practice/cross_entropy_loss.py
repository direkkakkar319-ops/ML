"""
Question:
    Compute the cross-entropy loss for a 5-class classifier
    that outputs logits [2.0, 0.5, -1.0, 3.0, 0.1] when the 
    correct class is index 3. 
    Then verify your answer with PyTorch's nn.CrossEntropyLoss.
"""
import sys

sys.path.append(r"E:\ML\PHASE01\F_ProbabilityAndDistributions\core")
from softmax_and_log_probabilities import cross_entropy_loss

def cover_cross_entropy_loss(logits:list, target_index:int)->float:
    return cross_entropy_loss(logits=logits, target_index=target_index)

logits = [2.0, 0.5, -1.0, 3.0, 0.1]
print(cover_cross_entropy_loss(logits, 3))
