'''
2880. Select Data
Solved
Easy
Companies
Hint
DataFrame students
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| student_id  | int    |
| name        | object |
| age         | int    |
+-------------+--------+

Write a solution to select the name and age of the student with student_id = 101.

The result format is in the following example.

 

Example 1:
Input:
+------------+---------+-----+
| student_id | name    | age |
+------------+---------+-----+
| 101        | Ulysses | 13  |
| 53         | William | 10  |
| 128        | Henry   | 6   |
| 3          | Henry   | 11  |
+------------+---------+-----+
Output:
+---------+-----+
| name    | age | 
+---------+-----+
| Ulysses | 13  |
+---------+-----+
Explanation:
Student Ulysses has student_id = 101, we select the name and age.
'''
import pandas as pd


def selectData(students: pd.DataFrame) -> pd.DataFrame:
    # new_df = students[students['student_id']==101]

    # mask = students['student_id']==101
    # new_df = pd.DataFrame(students[mask])

    # mask = students['student_id'].values==101
    # new_df = students[mask]

    # new_df = students.query('student_id==101')

    # new_reduced_df = new_df[['name','age']]
    # print(new_reduced_df)

    return students[students['student_id'] == 101][['name', 'age']]


def main():
    students = pd.DataFrame({
        'student_id': [101, 53, 128, 3],
        'name': ['Ulysses', 'William', 'Henry', 'Henry'],
        'age': [13, 10, 6, 11]
    })
    print(selectData(students))


if __name__ == '__main__':
    main()
