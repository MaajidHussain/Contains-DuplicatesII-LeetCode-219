class Solution:
    def containsNearbyDuplicate(self, nums, k):
        index_map = {}  # Dictionary to store the most recent index of each number
        
        for i, num in enumerate(nums):
            if num in index_map:
                # Check if the difference between current index and last seen index is <= k
                if i - index_map[num] <= k:
                    return True
            # Update the most recent index of the current number
            index_map[num] = i
        
        return False

# Example usage
solution = Solution()
nums = [1, 2, 3, 1, 2, 3, 4]
k = 4
result = solution.containsNearbyDuplicate(nums, k)
print(result)  # Output should be True, as there are duplicates within distance <= k
