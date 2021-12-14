#Find number of measurements larger than previous measurement.

from typing import List
from pathlib import Path

def find_increased_depths(depth_measurements: List[int]) -> int:
    """
    Returns the number of instances where the depth of the ocean increased from the previous measurement
    Parameters:
    depth_measurement - List of ocean depths
    """
    increased_count = 0

    index = 1
    prev_depth_measurement = depth_measurements[0]

    while index < len(depth_measurements):
        if depth_measurements[index] > prev_depth_measurement:
            increased_count += 1
        prev_depth_measurement = depth_measurements[index]
        index += 1
    
    return increased_count

if __name__ == "__main__":
    with open(Path(__file__).parent/'input1') as f:
        depth_measurements = list(map(int, f.readlines()))
        
    print(find_increased_depths(depth_measurements))
     