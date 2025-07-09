from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Time Complexity : O(n)
        # total_tank: net gas balance for the entire trip
        # curr_tank: gas balance for the current segment
        # start_index: candidate starting station
        total_tank = 0
        curr_tank = 0
        start_index = 0

        for i in range(len(gas)):
            gain = gas[i] - cost[i]
            total_tank += gain
            curr_tank += gain

            # If at any point, curr_tank < 0, it means we cannot reach station i+1
            # from the current start_index. So we reset start_index to i+1
            # and reset curr_tank for the new trial segment.
            if curr_tank < 0:
                start_index = i + 1
                curr_tank = 0

        # After the full pass, if total_tank < 0, it means total gas < total cost
        # So completing the circuit is impossible
        return start_index if total_tank >= 0 else -1
                
            