def appendAndDelete(s, t, k):
    i = 0

    while i < len(s) and i < len(t):
        if s[i] == t[i]:
            i += 1
        else:
            break

    delete = len(s) - i
    append = len(t) - i

    operations = delete + append

    if operations <= k:
        if (k - operations) % 2 == 0:
            return "Yes"

    if k >= len(s) + len(t):
        return "Yes"

    return "No"    
