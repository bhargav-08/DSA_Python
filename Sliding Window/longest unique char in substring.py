from collections import Counter


def longestKSubstr(s, k):
    window = Counter()
    i, j = 0, 0
    ans = -1

    while j < len(s):
        # Caculation
        plus = {s[j]: 1}
        window += plus

        # Check the condition
        if len(window) < k:
            j += 1

        elif len(window) == k:
            ans = max(ans, j-i+1)
            j += 1

        elif len(window) > k:
            while window and len(window) > k:
                minus = {s[i]: 1}
                window -= minus
                i += 1

            j += 1

    return ans


S = "aabacbebebe"
K = 3
print(longestKSubstr(S, K))
