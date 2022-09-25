# engprefix.py
# Cole Frauzel
# 2022-06-27

# Prints a float in engineering prefix notation
# i.e. Scientific notation but with powers of 3

n = 12345.678

print("n = " + str(n))

def float_to_sci(n: float) -> str:
    ret = " "
    n_str = str(n)
    dp = n_str.find('.')
    pow = 0
    
    if dp > 0:
        for c in n_str:
            print(c, end=' ')
        print('\n' + str(dp) + " digits before the dp")

        before_dp = n_str[0:dp]
        after_dp = n_str[dp+1:]

        print("digits before dp: " + before_dp)
        print("digits after dp:  " + after_dp)

        if before_dp == "0":
            pow -= 1

            while after_dp[0] == "0":
                after_dp = after_dp[1:]
                pow -= 1
            
            before_dp = after_dp[0]
            after_dp = after_dp[1:]

        else:
            pow = len(before_dp) - 1
            after_dp = before_dp[1:] + after_dp
            before_dp = before_dp[0]

        print(before_dp + "." + after_dp + "e" + str(pow))

    return ret

float_to_sci(n)