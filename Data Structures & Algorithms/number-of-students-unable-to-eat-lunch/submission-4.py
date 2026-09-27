class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = Counter(students)
        result = len(students)

        for j in sandwiches:
            if count[j] > 0:
                count[j] -= 1
                result -= 1
            else:
                break
        return result