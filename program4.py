from typing import List, Tuple


def program4(n: int, W: int, heights: List[int], widths: List[int]) -> Tuple[int, int, List[int]]:
    """
    Solution to Program 4
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
    # Initialized dp array to store min_cost, num_platforms, platform_distribution for each painting
    dp = [(float('inf'), 0, [])] * (n + 1)
    dp[0] = (0, 0, [])  # basecase essentially

    # Iterating over each painting to determine the optimal arrangements up until that painting
    for i in range(1, n + 1):
        # Nested loop to go through all possible configurations ending at the painting i
        for j in range(1, i + 1):
            total_width = 0
            max_height = 0
            # 3rd loop Calculating the total width and max height for the configutation of paintings from j to i
            for k in range(j, i + 1):
                total_width += widths[k - 1]
                if total_width > W:
                    break  # break if goes beyond platform width
                max_height = max(max_height, heights[k - 1])

            # If the config of paintings from j to i can fit on a single  platform
            if total_width <= W:
                current_cost = dp[j - 1][0] + max_height  # Calculate the new cost if we are adding this platform
                # Update dp[i] if  configuration is lower in cost
                if current_cost < dp[i][0]:
                    dp[i] = (current_cost, dp[j - 1][1] + 1, dp[j - 1][2] + [i - j + 1])
    return dp[n][1], dp[n][0], dp[n][2]


if __name__ == '__main__':
    n, W = map(int, input().split())
    heights = list(map(int, input().split()))
    widths = list(map(int, input().split()))
    m, total_height, num_paintings = program4(n, W, heights, widths)
    print(m)
    print(total_height)
    for i in num_paintings:
        print(i)
