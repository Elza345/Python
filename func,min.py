def minimal(l):
    min_number = l[0]
    for el in l:
        if el < min_number:
            min_number = el

    return min_number

nums1 = [5,2,8,6,15,22]
min1 = minimal(nums1)

nums2 = [2.1,5.1,3.2,0.5]
min2 = minimal(nums2)

if min1 < min2:
    print(min1)
else:
    print(min2)