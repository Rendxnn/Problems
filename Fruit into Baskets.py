class Solution:
    def totalFruit(self, fruits) -> int:
        max_total = 0
        counter = 0
        i = 0
        changed = False
        f1, f2 = None, None
        while i < len(fruits):
            current = fruits[i]
            print(i, counter)
            if f1 is None:
                f1 = current
                counter += 1
            elif f2 is None and current != f1:
                f2 = current
                counter += 1
            else:
                if current == f1 or current == f2:
                    counter += 1
                else:
                    changed = True
                    f1, f2 = None, None
                    i -= 1
                    while i - 1 >= 0 and fruits[i] == fruits[i - 1]:
                        i -= 1
                    if max_total < counter:
                        max_total = counter
                    counter = 0
            if not changed:
                i += 1
            else:
                changed = False

        if counter > max_total:
            return counter
        return max_total


print(Solution.totalFruit(Solution, [0,1,6,6,4,4,6]))