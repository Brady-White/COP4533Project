from typing import List, Tuple


def program5A(n: int, W: int, heights: List[int], widths: List[int]) -> Tuple[int, int, List[int]]:
    """
    Solution to Program 5A
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
    memo = {}  # Memoization dict for storing the results of the subproblems

    #Recursive function for solving the subproblems from  ith painting to the beginning
    def dp(i: int) -> Tuple[int, int, List[int]]:
        if i in memo:
            return memo[i]  # Return the memoization if already there

        min_cost = float('inf')  # Initialized min cost as inf
        platforms_used = 0
        platform_config = []

        width_sum = 0  # Sum of width of current platform
        max_height = 0  # Max height in current platform.

        # Iterate back to determine the valid platforms ending at the painting i
        for j in range(i, -1, -1):
            width_sum += widths[j]
            if width_sum > W:
                break  # break if goes beyond platform width

            max_height = max(max_height, heights[j])

            # Recursively call for subproblem
            prev_cost, prev_platforms, prev_config = dp(j - 1) if j > 0 else (0, 0, [])
            total_cost = prev_cost + max_height

            # Updated if the current configuration has a lower cost
            if total_cost < min_cost:
                min_cost = total_cost
                platforms_used = prev_platforms + 1
                platform_config = prev_config + [i - j + 1]

        # Storing the result in memo dict
        memo[i] = (min_cost, platforms_used, platform_config)
        return memo[i]

    # Calling function for the problem starting from the last painting
    total_cost, num_platforms, platform_list = dp(n - 1)
    return num_platforms, total_cost, platform_list


if __name__ == '__main__':
    n, W = map(int, input().split())
    heights = list(map(int, input().split()))
    widths = list(map(int, input().split()))
    m, total_height, num_paintings = program5A(n, W, heights, widths)
    print(m)
    print(total_height)
    for i in num_paintings:
        print(i)