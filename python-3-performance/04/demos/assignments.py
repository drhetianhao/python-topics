import random

def multiple_assignments(order):
    order_subtotal, order_tax, order_shipping = order

def individual_assignments(order):
    order_subtotal = order[0]
    order_tax = order[1]
    order_shipping = order[2]

@profile
def main():
    orders = [(random.randint(0, 100),
               random.randint(0, 100),
               random.randint(0, 100)) for _ in range(100_000)]
    
    for o in orders:
        multiple_assignments(o)
        individual_assignments(o)

    
main()