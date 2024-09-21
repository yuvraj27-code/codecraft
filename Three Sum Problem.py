def three_sum(nums):
    # Sort the array to facilitate the two-pointer technique and handle duplicates
    nums.sort()
    result = []
    n = len(nums)
    
    for i in range(n):
        # Skip duplicates for the first element of the triplet
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        left, right = i + 1, n - 1
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            if current_sum < 0:
                left += 1  # We need a larger sum, move the left pointer to the right
            elif current_sum > 0:
                right -= 1  # We need a smaller sum, move the right pointer to the left
            else:
                # We found a valid triplet
                result.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicates for the second element
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                
                # Skip duplicates for the third element
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                # Move both pointers after finding a valid triplet
                left += 1
                right -= 1
    
    return result

# Example usage
if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    triplets = three_sum(nums)
    print("Unique Triplets that sum to zero:", triplets)
