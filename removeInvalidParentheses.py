def remove_invalid_parentheses(s):
    # Once the count of ')' is more than '(' first appeared , the cycle will be exit instantly.
    # But if cycle over normally, the count of '(' is not less than ')'
    # To judge whether the 's' is valid
    def isvalid(s):
        ctr = 0
        for c in s:
            if c == '(':
                ctr += 1
            elif c == ')':
                ctr -= 1
                if ctr < 0:
                    return False
        # It contains a condition judgment that if ctr is 0 then returns True, or returns False.
        return ctr == 0

    # Transforming 's' into a Set
    level = {s}
    i = 0   # To store the cycle count
    while True:
        i = i + 1
        # Calling function 'filter' and return a list containing valid results
        valid = filter(isvalid, level)
        if valid:
            print i
            return valid   # This is the only one exit of this function and return a valid result(List)
        # 'level' is used to store all possible assembly after removing one invalid parentheses.
        level = {s[:i] + s[i+1:] for s in level for i in range(len(s))}
        print level


if __name__ == "__main__":
    ss = ")("
    # It's used to accept valid results
    valid = remove_invalid_parentheses(ss)
    print valid
