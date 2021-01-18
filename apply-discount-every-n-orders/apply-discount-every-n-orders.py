class Cashier:
​
    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.cnt = 0
        self.discount = discount
        self.products = products
        self.prices = prices
        self.d = defaultdict()
        for i in range(len(products)):
            self.d[products[i]] = i
​
    def getBill(self, product: List[int], amount: List[int]) -> float:
        total = 0
        self.cnt += 1
        for i in range(len(product)):
            idx = self.d[product[i]]
            total += self.prices[idx] * amount[i]
        
        if self.cnt == self.n:
            total = total - ((self.discount * total)/100)
            self.cnt = 0
        return total
​
# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)
