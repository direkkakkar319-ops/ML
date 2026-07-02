import math


def softmax(logits):
    max_logit = max(logits)
    shifted_logits = [z - max_logit for z in logits]
    exps = [math.exp(z) for z in shifted_logits]
    total = sum(exps)

    return [e/total for e in exps]

def log_softmax(logits):
    max_logit = max(logits)
    shifted_logits = [z - max_logit for z in logits]
    log_sum_exp = max_logit + math.log(sum(math.exp(z) for z in shifted_logits))

    return [z - log_sum_exp for z in logits]

def cross_entropy_loss(logits, target_index):
    log_probas = log_softmax(logits=logits)
    
    return -log_probas
