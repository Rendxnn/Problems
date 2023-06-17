class Solution:
    def generate(self, num_rows) -> list:
        ans = [[1], [1, 1]]
        for _ in range(num_rows):
            row = [1]
            last_row = ans[-1]
            index = 0
            while index + 1 < len(last_row):
                new_number = last_row[index] + last_row[index + 1]
                row.append(new_number)
                index += 1
            row.append(1)
            ans.append(row)
        return ans[:num_rows]


print(Solution().generate(5))
