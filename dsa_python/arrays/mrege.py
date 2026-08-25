# Merge nums1 and nums2 into a single array sorted in non-decreasing order.


def merge( nums1, m, nums2, n):
    # num=nums1[:m]
    # p1=0
    # p2=0
    # for i in range(m+n):
    #     if p2>=n or (p1<m and num[p1]<=nums2[p2]):
    #         nums1[i]=num[p1]
    #         p1+=1
    #     else:
    #         nums1[i]=nums2[p2]
    #         p2+=1

    # return nums1

    p1 = m - 1
    p2 = n - 1
    p = m + n - 1

    while p2 >= 0:

        if (p1 >= 0) and (nums1[p1] > nums2[p2]):
            nums1[p] = nums1[p1]
            p1 -= 1

        else:
            nums1[p] = nums2[p2]
            p2 -= 1

        p -= 1

    return nums1

n1=[1,2,3,0,0,0]
m=3
n=3
n2=[2,4,6]
print(merge(n1,m,n2,n))