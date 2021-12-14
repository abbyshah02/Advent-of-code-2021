#Find number of times a sum of measurements is larger than previous sum of measurements.

from typing import List
from pathlib import Path

def find_increased_depths(depth_measurements: List[int]) -> int:
    """
    Returns the number of instances where the depth of the ocean increased from the previous measurement
    Parameters:
    depth_measurement - List of ocean depths
    """
    increased_count = 0

    s_index = 0
    prev_depth_measurement = 0
    sliding_window_length = 3
    e_index = s_index + sliding_window_length - 1

    while s_index != len(depth_measurements) and e_index < len(depth_measurements):
        depth_measurement_sum = 0
        for index in range(s_index, e_index):
            depth_measurement_sum += depth_measurements[index]
        depth_measurement_sum += depth_measurements[e_index]

        if prev_depth_measurement != 0 and depth_measurement_sum > prev_depth_measurement:
            increased_count += 1
        prev_depth_measurement = depth_measurement_sum
        s_index += 1
        e_index = s_index + sliding_window_length - 1

    
    return increased_count

if __name__ == "__main__":
    with open(Path(__file__).parent/'input1') as f:
        depth_measurements = list(map(int, f.readlines()))
        
    print(find_increased_depths(depth_measurements))
     