import random
import time
import matplotlib.pyplot as plt
from program1 import program1
from program2 import program2

# Generate monotonically non-increasing data for Program 1
def generate_monotonically_non_increasing_data(n):
    heights = sorted([random.randint(1, 100) for _ in range(n)], reverse=True)
    widths = [random.randint(1, 10) for _ in range(n)]
    return heights, widths

# Generate unimodal data for Program 2
def generate_unimodal_data(n):
    peak = random.randint(1, n-1)
    first_half = sorted([random.randint(1, 100) for _ in range(peak)], reverse=True)
    second_half = sorted([random.randint(1, 100) for _ in range(n - peak)])
    heights = first_half + second_half
    widths = [random.randint(1, 10) for _ in range(n)]
    return heights, widths

sizes = [1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000]
program1_times = []
program2_times = []

for size in sizes:
    # Generate data for Program 1 (monotonically non-increasing)
    heights_p1, widths_p1 = generate_monotonically_non_increasing_data(size)
    start_time = time.time()
    program1(size, random.randint(10, 30), heights_p1, widths_p1)
    program1_times.append(time.time() - start_time)

    # Generate data for Program 2 (unimodal function)
    heights_p2, widths_p2 = generate_unimodal_data(size)
    start_time = time.time()
    program2(size, random.randint(10, 30), heights_p2, widths_p2)
    program2_times.append(time.time() - start_time)

# Plotting for Program 1
plt.figure(figsize=(10, 5))  # Set figure size
plt.plot(sizes, program1_times, label='Program 1 Time', marker='o')
plt.xlabel('Input Size (n)')
plt.ylabel('Running Time (seconds)')
plt.title('Running Time of Program 1')
plt.legend()
plt.grid()
plt.show()

# Plotting for Program 2
plt.figure(figsize=(10, 5))  # Set figure size
plt.plot(sizes, program2_times, label='Program 2 Time', marker='o', color='orange')
plt.xlabel('Input Size (n)')
plt.ylabel('Running Time (seconds)')
plt.title('Running Time of Program 2')
plt.legend()
plt.grid()
plt.show()
