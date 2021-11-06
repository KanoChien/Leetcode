
class Solution(object):
    def longestPalindrome(self, s):

        if(len(s)==1):
            return s
        elif(len(s)==2):
            if(s[0]==s[1]):
                return s
            else:
                return s[0]
        max_length = 0
        for i in range(len(s)):


            length=1
            #odd len
            l,r=i,i
            while(s[l]==s[r]):
                length=r-l+1
                if(max_length<length):
                    max_length=length
                    answer= s[l:r+1]
                l=l-1
                r=r+1
                if(l<0):
                    break
                if(r>=len(s)):
                    break

            l,r=i,i+1
            if(r>=len(s)):
                break
            #even len
            length=1
            while(s[l]==s[r]):
                length=r-l+1
                if(max_length<length):
                    max_length=length
                    answer= s[l:r+1]
                l=l-1
                r+=1

                if(l<0):
                    break
                if(r>=len(s)):
                    break
        return answer
s=Solution()
a=s.longestPalindrome("cbbd")
print(a)