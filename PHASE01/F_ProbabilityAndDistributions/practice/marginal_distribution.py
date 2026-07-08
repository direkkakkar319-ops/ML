"""
Question:
    Build a joint distribution table for two loaded dice.
    Compute the marginal distributions and check whether the
    dice are independent.
"""
import random

def load_dice():
    random_numbers = [random.random() for _ in range(6)]
    total = sum(random_numbers)
    probability = [w/total for w in random_numbers]

    return probability

# assuming the dice are independent
def joint_distribution(dice_01, dice_02):
    """Forms joint distribution table for two dice"""
    joint = [[dice_01[i]*dice_02[j] for j in range(6)] for i in range(6)] 
    
    return joint 

def check_independence(dice_01, dice_02):
    """
    Checks if two dice are independent or not 

    Formula:
        P(X=i,Y=j)=P(X=i)xP(Y=j)
    """
    tolerance = 1e-10
    independent = True

    for i in range(6):
        for j in range(6):
            if abs(joint[i][j]-marginal_distribution_dice_01[i]*marginal_distribution_dice_02[j])>tolerance:
                independent=False
                break
        if not independent:
            break
    if independent:
        print("The two dice ARE independent")
    else:
        print("The two dice ARE NOT independent")


if __name__ == "__main__":
    dice_01 = load_dice()
    dice_02 = load_dice()

    joint = joint_distribution(
        dice_01=dice_01,
        dice_02=dice_02
        )

    # joint distribution table 
    for row in joint:
        print(row)

    # Marginal distributions
    # Dice 1
    marginal_distribution_dice_01 = [sum(row) for row in joint]
    print("Marginal distribution of Die 1:")
    for i, p in enumerate(marginal_distribution_dice_01, start=1):
        print(f"P(X={i}) = {p:.4f}")

    # Dice 2
    marginal_distribution_dice_02 = [
        sum(joint[i][j] for i in range(6))
        for j in range(6)
    ]
    print("Marginal distribution of Die 1:")
    for j, p in enumerate(marginal_distribution_dice_02, start=1):
        print(f"P(Y={j}) = {p:.4f}")

    print(check_independence(dice_01=dice_01, dice_02=dice_02))
