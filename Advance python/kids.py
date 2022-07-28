class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        a = []
        most_candy = max(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= most_candy:
                a.append(True)
            else:
                a.append(False)
        return a
        