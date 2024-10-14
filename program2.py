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

    painting_count = []  # List to store the number of paintings on each platform
    current_platform = [W, 0, 0]  # Initialize the current platform [remaining_width, max_height, painting_count]
    num_platforms = 0  # Counter for the number of platforms used
    total_height = 0  # Variable to accumulate the total height of platforms
    is_increasing = False  # Boolean flag to indicate if we're in the "increasing" phase of the unimodal sequence
    switched = False  # Boolean flag to track when we switch to the increasing phase

    for i in range(n):
        width, height = widths[i], heights[i]  # Get the current painting's width and height

        # Check if we are moving to the "increasing" phase of the unimodal sequence
        if not is_increasing and i > 0 and height > heights[i - 1] and height > current_platform[1]:
            is_increasing = True  # We've hit the minimum, now heights will increase

        # Check if the current painting fits on the current platform or if we've just switched to increasing
        if current_platform[0] < width or (is_increasing and not switched):
            # If we just switched to increasing, update the `switched` flag
            if is_increasing and not switched:
                switched = True

            # Finalize the current platform by adding its height and painting count
            painting_count.append(current_platform[2])
            total_height += current_platform[1]
            num_platforms += 1

            # Start a new platform with the current painting
            current_platform = [W - width, height, 1]
        else:
            # If the painting fits, update the platform's remaining width, max height, and painting count
            current_platform[0] -= width
            current_platform[1] = max(current_platform[1], height)
            current_platform[2] += 1

    # Finalize the last platform
    num_platforms += 1
    total_height += current_platform[1]
    painting_count.append(current_platform[2])

    return num_platforms, total_height, painting_count
    
if __name__ == '__main__':
    n, W = map(int, input().split())
    heights = list(map(int, input().split()))
    widths = list(map(int, input().split()))

    m, total_height, num_paintings = program2(n, W, heights, widths)

    print(m)
    print(total_height)
    for i in num_paintings:
        print(i)
    
