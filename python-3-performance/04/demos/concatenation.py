import random


@profile
def main():
    orders = [str(random.randint(0, 100)) for _ in range(50_000)]

    report = ''
    for o in orders:
        report += o
    
    ''.join(orders)


main()