def is_valid(self, s):

    dict_p = {'(': ')', '[': ']', '{': '}'}
    i = 0
    stack = []

    while True:
        if len(stack) == 0 and i == len(s):
            return True
        if (i >= len(s) and len(stack) > 0) or len(s) <= 1:
            return False
        if len(stack) == 0 and s[i] in dict_p.keys() or s[i] in dict_p.keys() and stack[-1] in dict_p.keys():
            stack.append(s[i])
        elif len(stack) > 0:
            if stack[-1] in dict_p.keys() and dict_p.get(stack[-1]) == s[i]:
                stack.pop()
            elif stack[-1] in dict_p.keys() and dict_p.get(stack[-1]) != s[i]:
                return False
        else:
            return False
        i += 1

print(is_valid(""))
print(is_valid("[[[]]]"))
print(is_valid("[}(){}"))
