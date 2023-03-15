def findMedianSortedArrays(nums1, nums2) -> float:
    A = nums1
    B = nums2
    total = len(A)+len(B)
    half = total//2

    if len(A) > len(B):
        A, B = B, A

    low = 0
    high = len(A)-1

    while True:
        mid = low+high >> 1
        other = half-mid-2

        Aleft = A[mid] if mid >= 0 else float("-inf")
        Aright = A[mid+1] if mid+1 < len(A) else float("inf")
        Bleft = B[other] if other >= 0 else float("-inf")
        Bright = B[other+1] if other+1 < len(B) else float("inf")

        if Aleft <= Bright and Aright >= Bleft:
            # odd
            if total % 2:
                return min(Aright, Bright)
            else:
                return (max(Aleft, Bleft)+min(Aright, Bright))/2

        elif Aleft > Bright:
            high = mid-1
        else:
            low = mid+1


nums1 = [1, 3]
nums2 = [2]

nums1 = [2]
nums2 = []

print(findMedianSortedArrays(nums1, nums2))
