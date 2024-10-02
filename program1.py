from typing import List, Tuple

def program1(n: int, W: int, heights: List[int], widths: List[int]) -> Tuple[int, int, List[int]]:
    """
    Solution to Program 1
    
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
    total_cost = 0
    num_platforms = 0
    current_width = 0
    current_max_height = 0
    paintings_on_platform = []
    current_paintings_count = 0
    
    for i in range(n):
        if current_width + widths[i] > W:
            # Finalize current platform
            total_cost += current_max_height
            num_platforms += 1
            paintings_on_platform.append(current_paintings_count)
            # Start a new platform
            current_width = widths[i]
            current_max_height = heights[i]
            current_paintings_count = 1
        else:
            # Add to the current platform
            current_width += widths[i]
            current_max_height = max(current_max_height, heights[i])
            current_paintings_count += 1
    
    # Add the cost of the last platform
    total_cost += current_max_height
    num_platforms += 1
    paintings_on_platform.append(current_paintings_count)
    
    return num_platforms, total_cost, paintings_on_platform



if __name__ == '__main__':
    n, W = map(int, input().split())
    heights = list(map(int, input().split()))
    widths = list(map(int, input().split()))

    m, total_height, num_paintings = program1(n, W, heights, widths)

    print(m)
    print(total_height)
    for i in num_paintings:
        print(i)
    