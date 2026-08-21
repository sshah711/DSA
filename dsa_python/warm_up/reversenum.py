def reverse_num(n):
    copyn = n
    rev = 0
    # last digit (reminder) n%10
    # remove last digit n/10
    if n == 0:  # corner case
        return 0
    n = abs(n)  # corner case

    while n > 0:
        rem = n % 10
        rev = 10 * rev + rem
        n = n // 10

    final= -rev if copyn < 0 else rev
    # Define exact 32-bit signed limits

    l = 2**31
    if final < -l or final > l-1 :
        return 0
    return final

    # if(copyn<0):
    #     return -rev
    # else:
    #     return rev


n = 211

print(reverse_num(n))


def rev(n):
    # Slice the absolute value string to reverse digits, convert to int to drop '0's
    reversed_int = int(str(abs(n))[::-1])
    
    # Re-apply minus sign if original was negative
    final_val = -reversed_int if n < 0 else reversed_int
    
    # 32-bit overflow check for this approach too
    if final_val < -2**31 or final_val > (2**31 - 1):
        return 0
        
    return final_val

print(rev(-980)) 