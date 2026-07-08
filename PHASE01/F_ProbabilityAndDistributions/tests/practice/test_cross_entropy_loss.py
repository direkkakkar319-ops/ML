import sys
import pytest
import torch as th 
import torch.nn as nn

sys.path.append(r"E:\ML\PHASE01\F_ProbabilityAndDistributions\practice")
from cross_entropy_loss import cover_cross_entropy_loss


def test_cover_cross_entropy_loss():
    logits = [2.0, 0.5, -1.0, 3.0, 0.1]
    target_index = 3
    custom_loss = cover_cross_entropy_loss(logits=logits, target_index=target_index)

    criterion = nn.CrossEntropyLoss()
    logits_tensor = th.tensor(data=[logits], dtype=th.float32)
    target_tensor = th.tensor(data=[target_index])
    torch_loss = criterion(logits_tensor, target_tensor).item()

    assert custom_loss == pytest.approx(torch_loss, rel=1e-6)
