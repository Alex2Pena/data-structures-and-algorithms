def is_anagram(s1, s2):
    s1lower = s1.lower()
    s2lower = s2.lower()
    if not s1 and s2:
        return TypeError
    if(sorted(s1lower) == sorted(s2lower)):
        return True
    else:
        return False
