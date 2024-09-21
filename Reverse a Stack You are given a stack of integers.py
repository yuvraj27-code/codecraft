def reverse_stack(stack):
    if not stack:  # Check if the stack is empty
        return stack  # Return immediately if empty

    # Use slicing to reverse the stack
    return stack[::-1]

# Example usage
stack = [1, 2, 3, 4, 5]
print("Original Stack:", stack)
reversed_stack = reverse_stack(stack)
print("Reversed Stack:", reversed_stack)
