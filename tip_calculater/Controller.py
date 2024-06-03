"""
Controller.py by Afton Jones
Some functions to controll the tip calculater.
"""

# Imports

# Functions
def get_tip(money, percent):
    tip = money * (percent / 100)
    return tip

def get_total(money, tip):
    total = money + tip
    return total

# Global scope
if __name__ == "__main__":
    pass