from sortedcontainers import SortedList

class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        N = len(foods)
        lcuisines = list(set(cuisines))
        M = len(lcuisines)
        self.d = defaultdict(int) # maps food to cuisine
        self.food_rating = defaultdict(int)
        self.cuisine_to_i = defaultdict(int)
        for i in range(len(lcuisines)):
            self.cuisine_to_i[lcuisines[i]] = i
        self.A = [SortedList(key=lambda x: (-x[0], x[1])) for x in range(M)]
        for i in range(N):
            self.d[foods[i]] = cuisines[i]
            self.A[self.cuisine_to_i[cuisines[i]]].add([ratings[i], foods[i]])
            self.food_rating[foods[i]] = ratings[i]

    def changeRating(self, food: str, newRating: int) -> None:
        curr = self.food_rating[food]
        self.A[self.cuisine_to_i[self.d[food]]].remove([curr, food])
        self.A[self.cuisine_to_i[self.d[food]]].add([newRating, food])
        self.food_rating[food] = newRating

    def highestRated(self, cuisine: str) -> str:
        return self.A[self.cuisine_to_i[cuisine]][0][1]