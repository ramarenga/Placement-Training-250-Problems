class Solution(object):
    def kItemsWithMaximumSum(self, num, zero, neg, k):
        bag = []

        for i in range(num):
            bag.append(1)

        for i in range(zero):
            bag.append(0)

        for i in range(neg):
            bag.append(-1)

        total = sum(bag[:k])
        return total