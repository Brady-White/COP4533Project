from typing import List, Tuple

    
def program2(n: int, W: int, heights: List[int], widths: List[int]) -> Tuple[int, int, List[int]]:
    """
    Solution to Program 2
    
    Parameters:
    n (int): number of paintings
    W (int): width of the platform
    heights (List[int]): heights of the paintings
    widths (List[int]): widths of the paintings

    Returns:
    int: number of platforms used
    int: optimal total height
    List[int]: number of paintings on each platform
    """
    ############################
    # Given the heights h1, . . . , hn, where ∃k such that ∀i < j ≤ k, hi ≥ hj and ∀k ≤ i <
    # j, hi ≤ hj , and the base widths w1, . . . , wn of n paintings, along with the width W of the
    # display platform, find an arrangement of the paintings on platforms that minimizes the
    # total height.
    # (Note: The heights of the paintings follow a unimodal function with a single local minimum,
    # as in Example 3.)
    ############################
    #Consider the test case below.
    #n = 7, W = 10
    #h = [21, 19, 17, 16, 11, 5, 1]
    #w = [7, 1, 2, 3, 5, 8, 1]
    #For a test case like this, the input will be EXACTLY as follows. The first line will contain the values of "n" and "W" separated by a whitespace. The second line will contain the array of "h", with each element separated by a whitespace. Finally, the third line will contain the array of "w", with each element, once again, separated by a white space. This will be the case for all test cases. The sample input is given below.
    #7 10
    #21 19 17 16 11 5 1
    #7 1 2 3 5 8 1
    # Sort paintings by height in descending order
    platforms = []  # Each entry is (remaining_width, max_height, num_paintings)
    current_platform = [W, 0, 0]  # Initialize the current platform

    for i in range(n):
        width, height = widths[i], heights[i]

        # If the current painting fits within the current platform width limit
        if current_platform[0] >= width:
            current_platform[0] -= width
            current_platform[1] = max(current_platform[1], height)  # Update max height for this platform
            current_platform[2] += 1  # Increase painting count
        else:
            # Save the completed platform and start a new one
            platforms.append(current_platform)
            current_platform = [W - width, height, 1]

    # Append the last platform
    platforms.append(current_platform)

    # Calculate total height and the number of paintings on each platform
    total_height = sum(platform[1] for platform in platforms)
    num_paintings = [platform[2] for platform in platforms]
    num_platforms = len(platforms)

    return num_platforms, total_height, num_paintings
    
if __name__ == '__main__':
    n, W = map(int, input().split())
    heights = list(map(int, input().split()))
    widths = list(map(int, input().split()))

    m, total_height, num_paintings = program2(n, W, heights, widths)

    print(m)
    print(total_height)
    for i in num_paintings:
        print(i)
    