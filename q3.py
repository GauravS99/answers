# m,n are the number of elements in a,b respectively 
# Time complexity: O(m + n)
# Space complexity: O(m + n)


def get_counts(counts, arr):
    """
    Given dict, a dictionary of counts of elements,
    update dict with elements in arr
    """
    for el in arr:
        if(el not in counts):
            counts[el] = 0
        counts[el] += 1 

def find_least_represented(a, b):
    """
    Question 3:
    
    Given two arrays of integers, find and return the least represented element(s) between both arrays.  Order does not matter for the resulting array.
    
    Example:
    [1, 1, 4, 4, 2, 3] and [1, 3, 2, 2] should return [4, 3]    (there are only two 4's and two 3's, but three 1's and 2's)
    """
    counts = {}
    get_counts(counts, a)
    get_counts(counts, b)

    leastRepresented = set()
    leastCount = None

    for key in counts:
        if(leastCount is None or counts[key] < leastCount):
            leastRepresented.clear()
            leastCount = counts[key]
            leastRepresented.add(key)
        elif(counts[key] == leastCount):
            leastRepresented.add(key) 

    return list(leastRepresented)

if __name__ == "__main__":
    print(find_least_represented([1, 1, 4, 4, 2, 3], [1, 3, 2, 2] ))


    
