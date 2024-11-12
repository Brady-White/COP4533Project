from typing import List, Tuple


def program3(n: int, W: int, heights: List[int], widths: List[int]) -> Tuple[int, int, List[int]]:
    """
    Solution to Program 3
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
    min_cost = float('inf')
    best_platform_count = 0
    best_distribution = []
    # Here we are iterating over all the possible subsets/masks of paintings into their perspective platforms
    for i in range(0, 1 << (n - 1)):  # Generating all partitions
        platform_count = 0
        platform_heights = []
        current_width = 0
        max_height = 0
        distribution = []
        last_index = 0
        # Traverse paintings and partition them based on the current partition or whats called the "mask"
        for j in range(n):
            # Checking ot see if there is a partition after the jth painting
            if i & (1 << j):
                # If a partition is made after jth painting complete the current platform
                # if (j - last_index) > 0:
                platform_heights.append(max_height)
                distribution.append(j - last_index)
                platform_count += 1
                current_width = widths[j]
                max_height = heights[j]
                last_index = j
            else:
                # add painting to the current platform
                if current_width + widths[j] <= W:
                    current_width += widths[j]
                    max_height = max(max_height, heights[j])
                else:
                    # If adding the painting exceeds the platform width create a new one
                    # if (j - last_index) > 0:
                    platform_heights.append(max_height)
                    distribution.append(j - last_index)
                    platform_count += 1
                    current_width = widths[j]
                    max_height = heights[j]
                    last_index = j
        # Last platform
        # if (n - last_index) > 0:
        platform_heights.append(max_height)
        distribution.append(n - last_index)
        platform_count += 1
        # Calculate the total height for this specific partition configration
        total_height = sum(platform_heights)
        # update the best config if this one has a smaller total height
        if total_height < min_cost:
            min_cost = total_height
            best_platform_count = platform_count
            best_distribution = distribution
    return best_platform_count, min_cost, best_distribution


if __name__ == '__main__':
    n, W = map(int, input().split())
    heights = list(map(int, input().split()))
    widths = list(map(int, input().split()))
    m, total_height, num_paintings = program3(n, W, heights, widths)
    print(m)
    print(total_height)
    for i in num_paintings:
        print(i)