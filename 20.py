def is_valid(s):
    """
    :type s: str
    :rtype: bool
    """
    brackets_dict = {'(': ')', '[': ']', '{': '}'}
    i = 1
    s = list(s)
    if len(s) == 0:
        return True
    elif len(s) % 2 is not 0:
        return False
    while len(s) > 0:
        if s[i - 1] in brackets_dict.keys() and s[i] == brackets_dict.get(s[i - 1]):
            del s[i - 1:i + 1]
            i -= 1
        elif s[i] in brackets_dict.keys() and s[i - 1] in brackets_dict.keys():
            i += 1
        else:
            return False
        if len(s) == 0:
            return True
        if i == 0:
            i += 1
        if i == len(s):
            return False


print(is_valid(""))
