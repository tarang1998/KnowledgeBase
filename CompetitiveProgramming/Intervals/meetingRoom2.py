class Solution:
    # Time Complexity: O(n log n) — because we sort both start and end arrays
    # Space Complexity: O(1) — no extra space (ignoring sorting)

    def minMeetingRooms(self, start: List[int], end: List[int]) -> int:
        # Step 1: Sort start and end times
        start.sort()
        end.sort()
        
        n = len(start)
        rooms = 0        # Current rooms in use
        max_rooms = 0    # Max rooms ever used
        i = 0            # Pointer for start[]
        j = 0            # Pointer for end[]

        # Step 2: Traverse all start times
        while i < n:
            if start[i] < end[j]:
                # A meeting starts before the earliest one ends → need new room
                rooms += 1
                i += 1
            else:
                # A meeting has ended → free up a room
                rooms -= 1
                j += 1

            # Track max rooms used at any point
            max_rooms = max(max_rooms, rooms)

        return max_rooms
