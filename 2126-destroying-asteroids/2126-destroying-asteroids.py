class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        for x in asteroids:
            if x <= mass:
                mass += x
            else:
                return False
            
        return True