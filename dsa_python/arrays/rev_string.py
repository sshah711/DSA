
# without usnig new array reverse the string in place

def rev_string(s):
    n=len(s)
    for i in range(int(n/2)):
        # t=s[i]
        # s[i]=s[n-1-i]
        # s[n-1-i]=t
        s[i],s[n-1-i]=s[n-1-i],s[i]
    return s

s=["s","a","k","s","h","i"]
print(rev_string(s))



# reverse vovels
def reverseVowels(s):
        vowels = "aeiouAEIOU"
        s = list(s)

        left = 0
        right = len(s) - 1

        while left < right:

            while left < right and s[left] not in vowels:
                left += 1

            while left < right and s[right] not in vowels:
                right -= 1

            s[left], s[right] = s[right], s[left]

            left += 1
            right -= 1

        return "".join(s)



s="sakusohiii"
print(reverseVowels(s))