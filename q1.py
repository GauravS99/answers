# Time complexity: O(n)
# Space complexity: O(1) 

# This code assumes that only letters from a-z are used. The space complexity above relies on this assumption. 

def print_most_repeating(s):
    """
    Question 1:
    
    Given a string, print out the character that is repeated the most times consecutively followed by the number of times it appears in the entire string.
    
    Example:
    "ssimemoaimmms" should print out the result "m5" (the longest sequence of m's is 3 and there are a total of 5 m's)
    """
    
    if len(s) == 0:
        return ""
    
    # look up table to maintain counts
    counts = {}
    for i in range(26): 
        counts[chr(ord('a') + i)] = 0
    
    maxi = [s[0], 1]
    current = [s[0], 0]
    for char in s:
        if char == current[0]:
            current[1] += 1
        else:
            if current[1] > maxi[1]:
                maxi[0] = current[0]
                maxi[1] = current[1]
            current[0] = char
            current[1] = 1

        counts[char] += 1

    # one more check because the longest sequence may be at the very end
    if current[1] > maxi[1]:
        maxi[0] = current[0]

    return maxi[0] + str(counts[maxi[0]]) # for two strings, this okay. With more, probably should use join. 