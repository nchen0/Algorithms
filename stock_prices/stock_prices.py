#!/usr/bin/python

import argparse


def find_max_profit(prices):
    # num = float("inf")
    new_list = []
    for index, price in enumerate(prices):
        for i in range(index, len(prices)):
            new_list.append(prices[i] - price)
    new_list = [x for x in new_list if x != 0]
    return max(new_list)


if __name__ == '__main__':
    # You can test your implementation by running
    # `python stock_prices.py [prices]` where prices is comprised of
    # space-separated integer values
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
