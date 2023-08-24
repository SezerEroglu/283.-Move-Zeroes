# 283.-Move-Zeroes

# Stats

    Runtime: Beats 75.15% of Python3 submissions
    Memory: Beeats 85.70% of Python3 submissions

# Explanation

    We iterate through the array. When we encounter a nonZero element, we switch positions with the last known nonZero position and increment the nonZero index by one.
    If we encounter a zero we leave it as is. This will transfer every nonZero item to the last nonZero index, which is incremented by one after every carriage.