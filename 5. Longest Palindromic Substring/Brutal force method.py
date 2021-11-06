# 5. Longest Palindromic Substring
# Brutal force method O(n^3)

def reverse_string(string):
    if len(string) == 0:
        return string
    else:
        return reverse_string(string[1:]) + string[0]


def is_Palingdrom_or_not(s):
    if (len(s) == 2 and s[0] == s[1]):
        return True
    elif (len(s) % 2 == 1):
        index = len(s) // 2
        a = s[0:index]
        b = s[index + 1:len(s)]
        if (a == reverse_string(b)):  ##example "abcba" index=[0,1,2,3,4]
            return True
    else:
        index = len(s) // 2
        a = s[0:index]
        b = s[index:len(s)]
        if (a == reverse_string(b)):
            return True
    return False


class Solution(object):

    def longestPalindrome(self, s):
        count = max_length = 0
        look_up_table = []
        answer = s[0]
        for i in range(len(s)):
            back_up = ""
            count = 0
            for j in range(i + 1, len(s)):

                if (count == 0):
                    back_up = back_up + s[i] + s[j]
                    count = 2
                else:
                    back_up = back_up + s[j]
                    count += 1

                if (back_up not in look_up_table):
                    if (is_Palingdrom_or_not(s=back_up) and count > max_length):
                        answer = back_up
                        look_up_table.append(answer)
                        max_length = count
        return answer
s=Solution()
print(s.longestPalindrome(s="civilwartestingwhetherthatnap"))