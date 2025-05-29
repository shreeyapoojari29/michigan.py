ASCII_LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
ASCII_UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DECIMAL_DIGITS  = "0123456789"

def is_alpha(s):
    for c in s:
        if c not in ASCII_LOWERCASE and c not in ASCII_UPPERCASE:
            return False
    return True

def is_digit(s):
    for c in s:
        if c not in DECIMAL_DIGITS:
            return False
    return True

def to_lower(s):
    result = ''
    for c in s:
        if c in ASCII_UPPERCASE:
            result += ASCII_LOWERCASE[ASCII_UPPERCASE.index(c)]
        else:
            result += c
    return result

def to_upper(s):
    result = ''
    for c in s:
        if c in ASCII_LOWERCASE:
            result += ASCII_UPPERCASE[ASCII_LOWERCASE.index(c)]
        else:
            result += c
    return result

def find_chr(s, ch):
    if len(ch) != 1:
        return -1
    for i in range(len(s)):
        if s[i] == ch:
            return i
    return -1

def find_str(s, sub):
    for i in range(len(s) - len(sub) + 1):
        if s[i:i+len(sub)] == sub:
            return i
    return -1

def replace_chr(s, old, new):
    if len(old) != 1 or len(new) != 1:
        return ""
    result = ""
    for c in s:
        if c == old:
            result += new
        else:
            result += c
    return result

def replace_str(s, old, new):
    if old == "":
        result = new
        for c in s:
            result += c + new
        return result
    result = ""
    i = 0
    while i < len(s):
        if s[i:i+len(old)] == old:
            result += new
            i += len(old)
        else:
            result += s[i]
            i += 1
    return result
