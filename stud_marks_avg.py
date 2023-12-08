1. Given a 2-D String array of student-marks find the student with the highest average and output his average score. 
If the average is in decimals, floor it down to the nearest integer.
  
Example 1:
Input:  [{"Bob","87"}, {"Mike", "35"},{"Bob", "52"}, {"Jason","35"}, {"Mike", "55"}, {"Jessica", "99"}]
Output: 99
Explanation: Since Jessica's average is greater than Bob's, Mike's and Jason's average.

Solution: 
from collections import defaultdict

def highest_average_score(marks):
    total_marks = defaultdict(int)
    subject_count = defaultdict(int)

    for student, score in marks:
        total_marks[student] += int(score)
        subject_count[student] += 1

    max_average = float('-inf')

    for student in total_marks:
        total = total_marks[student]
        count = subject_count[student]
        average = total // count

        max_average = max(max_average, average)

    return max_average

# Example usage:
input_marks = [("Bob", "87"), ("Mike", "35"), ("Bob", "52"), ("Jason", "35"), ("Mike", "55"), ("Jessica", "99")]
result = highest_average_score(input_marks)
print("Output:", result)



