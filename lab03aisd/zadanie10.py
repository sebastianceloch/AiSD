def balanced_parentheses(n):
    def parentheses(left, right, s):
        if right == n:
            print(s)
            return
        if left < n:
            parentheses(left + 1, right, s + "(")
        if right < left:
            parentheses(left, right + 1, s + ")")

    parentheses(0, 0, "")
print(balanced_parentheses(4))