# n represents the number of words total

# Time complexity: O(nlogn) because the time for rest of the actions is asymptotically dominated by the sort
# Space complexity: O(n)

def combine_strings(a, b):
    """
    Question 2: 
    
    Given two strings containing words delimited by ';', return a single string that combines both strings together in alphabetical order.
    
    Example:
    "dog;cat;frog" and "mouse;truck;art" should return "art;cat;dog;frog;mouse;truck"
    """
    
    strArr = (";".join([a, b])).split(";") # join is better than concatenating with + 
    strArr.sort()

    result = ";"
    return result.join(strArr)
