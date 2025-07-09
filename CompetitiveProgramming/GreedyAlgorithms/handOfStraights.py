from collections import Counter
import heapq
from typing import List


class Solution:
    def isNStraightHand(self,hand: List[int], groupSize: int) -> bool:
        # Time Complexity : O(nlogn)
        # If total cards aren't divisible by groupSize, we can't form groups
        if len(hand) % groupSize != 0:
            return False

        # Count the frequency of each card value
        count = Counter(hand)
        
        # Use a min-heap to process cards in increasing order
        min_heap = list(count.keys())
        heapq.heapify(min_heap)

        while min_heap:
            first = min_heap[0]  # Get the smallest available card to start a group

            # Try to build a group of size 'groupSize' starting from 'first'
            for i in range(groupSize):
                curr = first + i
                if count[curr] == 0:
                    # Cannot form a group if any required card is missing
                    return False
                count[curr] -= 1
                if count[curr] == 0:
                    # If card count reaches zero, remove it from the heap
                    if curr != min_heap[0]:
                        # If the card count reaches zero and it is not the minimum card
                        # Then the set cannot be formed 
                        # As there would be an element before it and hence a consecutive sequence cannot be formed
                        return False
                    heapq.heappop(min_heap)

        return True