def calculateMaxQualityScore(impact_factor, ratings):
    """
    Given an integer impact_factor and a list of ratings (which may be positive
    or negative), returns the maximum possible sum of a consecutive subarray
    after applying exactly one of:
      - Amplify a contiguous block: multiply each rating in the block by impact_factor
      - Adjust a contiguous block: divide each rating in the block by impact_factor
        (floor positives, ceil negatives)
    Runs in O(n) time and O(1) extra space.
    """
    n = len(ratings)

    # Precompute what each element would become if we amplify or adjust it:
    amplified = [x * impact_factor for x in ratings]
    adjusted = [
        (x // impact_factor) if x >= 0
        else -((-x) // impact_factor)
        for x in ratings
    ]

    def best_with_one_operation(modified):
        """
        Runs a 3-state Kadane sweep over the original ratings, where
        'modified' is either the amplified list or the adjusted list.
        States:
          - no_op:   best subarray ending here without having used the op yet
          - in_op:   best subarray ending here while inside the one modified segment
          - after_op: best subarray ending here after finishing that modified segment
        Returns the best sum that uses the operation exactly once.
        """
        # Initialize all three ending-here states.
        no_op    = 0              # haven't started special segment
        in_op    = float('-inf')  # currently inside special segment
        after_op = float('-inf')  # already used it, now back to original
        
        best_using_op = float('-inf')

        for i, original in enumerate(ratings):
            # Remember last step before overwriting
            prev_no_op, prev_in_op, prev_after_op = no_op, in_op, after_op

            # 1) Continue or start without ever using the operation
            no_op = max(prev_no_op + original, original)

            # 2) Either start the special segment here, or continue it
            in_op = max(
                prev_no_op + modified[i],  # start new segment at i
                prev_in_op + modified[i],  # continue segment
                modified[i]                # take i alone as a fresh segment
            )

            # 3) After finishing the special segment, back to original values
            after_op = max(
                prev_in_op + original,     # end segment at i-1, include original[i]
                prev_after_op + original,  # continue after-segment
                original                   # start fresh here (but we've used the op already)
            )

            # Track the best we've seen that has used the operation
            best_using_op = max(best_using_op, in_op, after_op)

        return best_using_op

    # Compute the best possible after one amplify, and the best after one adjust
    best_amplified = best_with_one_operation(amplified)
    best_adjusted  = best_with_one_operation(adjusted)

    # We have to apply exactly one strategy, so take the max of those two:
    return max(best_amplified, best_adjusted)


print(calculateMaxQualityScore(2,[5, -3, -3, 2, 4]))







