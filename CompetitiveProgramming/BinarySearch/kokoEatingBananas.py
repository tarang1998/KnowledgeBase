
class Solution:

    # Time Complexity : O(log(max(piles)) * len(piles))
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # At the least Koko can eat 1 Banana per hour
        minBananasPerHour = 1

        # As Koko needs to eat all the bananas from the piles 
        # h should atleast be equal to the length of the piles
        # As koko cant touch two piles in an single hour
        # If h == len(piles)
        # Then max bananas Koko has to eat per hour is max element in the biles array
        maxBananasPerHour = max(piles)

        result = maxBananasPerHour

        # Use binary search to find the minimum no of bananas Koko needs to eat per hour

        while (minBananasPerHour <= maxBananasPerHour):

            midEatingSpeed = (minBananasPerHour + maxBananasPerHour)//2

            hours = 0 

            # Calculate total no of hours to complete the pile 
            for bananas in piles:
                hours += math.ceil(bananas/midEatingSpeed)

            # If no of hours is greater than h 
            # We need to increase the speed of eating bananas
            if(hours > h):
                minBananasPerHour = midEatingSpeed + 1

            # If no of hours is less than h 
            # midEatingSpeed could be the result, but need to explore more options
            # Using a lower Speed of eating 
            else:
                maxBananasPerHour = midEatingSpeed - 1
                result = min(result,midEatingSpeed)

        return result




