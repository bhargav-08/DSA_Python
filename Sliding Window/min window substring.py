from collections import defaultdict


def minWindow(s: str, t: str) -> str:
    window = defaultdict(int)
    res = ""

    # Create map of unique character
    for char in t:
        window[char] += 1

    # Count of unique character
    count = len(window)

    # Create window and calculate substring till end
    i, j = 0, 0

    while j < len(s):
        if s[j] in window:
            window[s[j]] -= 1

            if window[s[j]] == 0:
                count -= 1

        # When not enough character is found in s just increment j
        if count > 0:
            j += 1

        # When all character are found
        elif count == 0:
            # calculate the minimum length and storing in result
            if not res:
                res = s[i:j+1]
            elif len(res) > j-i+1:
                res = s[i:j+1]

            # Further optimzation of length
            while count == 0:
                if s[i] in window:
                    window[s[i]] += 1
                    if window[s[i]] > 0:
                        count += 1

                i += 1
                if count == 0:
                    res = s[i:j+1] if len(res) > j-i+1 else res
            j += 1

    return res


s = "ADOBECODEBANC"
t = "ABC"
# s = "TOTMTAPTAT"
# t = "TTA"
print(minWindow(s, t))
