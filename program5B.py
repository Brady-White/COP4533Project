from typing import List, Tuple

def program5B(n: int, W: int, heights: List[int], widths: List[int]) -> Tuple[int, int, List[int]]:
    """
    Solution to Program 5B
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
    # Initialized dp array for storing min_cost, num_platforms, platform_distribution for each painting
    dp = [(0, 0, [])] * (n + 1)

    # Iteration over each painting to determine the optimal arrangements up to that painting
    for i in range(1, n + 1):
        total_width = 0 # total width of current platform
        max_height = 0  # max height for current platform
        min_cost, num_platforms, best_distribution = float('inf'), 0, []

        # Checking all the possible configuations of paintings ending at ith painting
        for j in range(i, 0, -1):
            total_width += widths[j - 1]  # add the width
            if total_width > W:
                break  # break loop if width goes too far
            max_height = max(max_height, heights[j - 1])  # Updated the max height for platform
            current_cost = dp[j - 1][0] + max_height  #  cost of configuration from j to i

            # Updated if the current config has a lower cost
            if current_cost < min_cost:
                min_cost = current_cost
                num_platforms = dp[j - 1][1] + 1  # increment the platform counter
                best_distribution = dp[j - 1][2] + [i - j + 1]  #update platform distribution

        # update dp[i] with the best configuration found for the first i paintings
        dp[i] = (min_cost, num_platforms, best_distribution)

    # Return the # of platforms used, optimal total height, and the platform distribution
    return dp[n][1], dp[n][0], dp[n][2]



if __name__ == '__main__':
    n, W = map(int, input().split())
    heights = list(map(int, input().split()))
    widths = list(map(int, input().split()))
    m, total_height, num_paintings = program5B(n, W, heights, widths)
    print(m)
    print(total_height)
    for i in num_paintings:
        print(i)