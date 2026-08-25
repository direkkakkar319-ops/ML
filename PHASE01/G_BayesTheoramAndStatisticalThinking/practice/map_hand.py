"""
Question:
    MAP by hand.
    Given observed data (7 heads in 10 coin flips), compute the MAP
    estimate of the bias using a Beta(2,2) prior.
    Compare it to the MLE estimate (7/10).

    here alpha prior and beta prior are same = 2
"""
def MLE_estimate(number_of_outcome, total_number):
    return number_of_outcome/total_number

def MAP_estimate(heads_outcomes, tails_outcomes, alpha_prior, beta_prior):
    _alpha_post = alpha_prior + heads_outcomes
    _beta_post = beta_prior + tails_outcomes
    mode = (_alpha_post - 1) / (_alpha_post + _beta_post - 2)
    return mode

heads, tails = 7, 3
alpha_prior, beta_prior = 2, 2

mle_estimate = MLE_estimate(number_of_outcome=heads, total_number=heads+tails)
map_estimate = MAP_estimate(
    heads_outcomes=heads,
    tails_outcomes=tails,
    alpha_prior=alpha_prior,
    beta_prior=beta_prior
    )

print(f"MLE estimate: {mle_estimate:.4f}")
print(f"MAP estimate: {map_estimate:.4f}")