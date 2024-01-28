#!/usr/bin/env python3

from collections import defaultdict
import heapq
import sys
import unittest

# nlargest & sorted
class MostTradedStock1:
    def __init__(self):
        self._ticker2shares = defaultdict(int)

    def execute_trade(self, ticker, shares):
        print('New Trade (ticker|shares): {}|{}'.format(ticker, shares))

        self._ticker2shares[ticker] += shares
        print('Total Volume (ticker|shares): {}|{}\n'.format(ticker, \
                                                             self._ticker2shares[ticker]))

    def top_stocks1(self, n):
        return heapq.nlargest(n, zip(self._ticker2shares.values(), \
                                     self._ticker2shares.keys()))

    def top_stocks2(self, n):
        return sorted(zip(self._ticker2shares.values(), \
                          self._ticker2shares.keys()), reverse=True)[:n]
# manual heapq
class MostTradedStock2:
    def __init__(self):
        self._ticker2shares = defaultdict(int)

    def execute_trade(self, ticker, shares):
        print('New Trade (ticker|shares): {}|{}'.format(ticker, shares))

        self._ticker2shares[ticker] += shares

        print('Total Volume (ticker|shares): {}|{}\n'.format(ticker, \
                                                             self._ticker2shares[ticker]))

    def top_stocks(self, n):
        h = []
        for ticker, shares in self._ticker2shares.items():
            # heapq creates min-heap, negate to simulate max-heap
            heapq.heappush(h, (-shares, ticker))

        # TODO: need to negate the shares, but how? lambda?
        #return [heapq.heappop(h) for i in range(len(h)) if i < n]

        result = []
        m = min(n, len(h))
        for i in range(m):
            item = heapq.heappop(h)
            result.append((-item[0], item[1]))

        return result

class TestMostTradedStock(unittest.TestCase):

    def test_mst1_top2(self):

        mts = MostTradedStock1()

        mts.execute_trade('MSFT', 400)
        mts.execute_trade('AMZN', 1000)
        mts.execute_trade('AAPL', 80)
        mts.execute_trade('AAPL', 800)
        mts.execute_trade('GOOG', 2000)
        mts.execute_trade('AMZN', 100)
        mts.execute_trade('MSFT', 2100)

        self.assertEqual(mts.top_stocks1(3), \
                         [(2500,'MSFT'), (2000,'GOOG'), (1100,'AMZN')])

        self.assertEqual(mts.top_stocks2(3), \
                         [(2500,'MSFT'), (2000,'GOOG'), (1100,'AMZN')])

    def test_mst2_top2(self):

        mts = MostTradedStock2()

        mts.execute_trade('MSFT', 400)
        mts.execute_trade('AMZN', 1000)
        mts.execute_trade('AAPL', 80)
        mts.execute_trade('AAPL', 800)
        mts.execute_trade('GOOG', 2000)
        mts.execute_trade('AMZN', 100)
        mts.execute_trade('MSFT', 2100)

        self.assertEqual(mts.top_stocks(3), \
                         [(2500,'MSFT'), (2000,'GOOG'), (1100,'AMZN')])

if __name__ == '__main__':
    sys.exit(unittest.main())
