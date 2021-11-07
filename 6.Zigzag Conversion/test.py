class Solution(object):
    def convert(self, s, numRows):
        table = []
        length = len(s)
        answer = ""
        row_step = []
        if numRows == 1:
            return s
        elif numRows == 2:
            for i in range(0, len(s), 2):
                answer += s[i]
            for i in range(1, len(s), 2):
                answer += s[i]
            return answer
        row_step=start_row_step = numRows * 2 - 2

        mid=float(numRows)/2-0.1
        for i in range(0, numRows):
            count = i
            current_step=start_row_step
            while (count < len(s)):
                table.append(count)
                count += current_step
                current_step = row_step - current_step
                if(current_step<=0):
                    current_step=row_step
            start_row_step = start_row_step - 2
            if(start_row_step==0):
                start_row_step=row_step
        for i in table:
            answer+=s[i]
        return answer

s=Solution()

a=s.convert(s="PAYPALISHIRING",numRows=4)
print(a)