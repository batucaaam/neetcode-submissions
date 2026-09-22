class Solution:
    def calPoints(self, operations: List[str]) -> int:
        rec = []
        for i in range(len(operations)):
            if operations[i] == "+":
                rec.append(int(rec[-1]) + int(rec[-2]))
            elif operations[i] == "D":
                rec.append(2 * int(rec[-1]))
            elif operations[i] == "C":
                rec.pop()
            else:
                rec.append(int(operations[i]))
        return sum(rec)