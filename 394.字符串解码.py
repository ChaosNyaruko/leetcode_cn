#
# @lc app=leetcode.cn id=394 lang=python3
#
# [394] 字符串解码
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        def getDigit(start, s):
            ret = 0
            while start < len(s) and s[start].isdigit():
                ret = 10 * ret + int(s[start])
                start += 1
            return start, ret
        
        def getWord(start, s):
            pass

        # two stacks: one stores numbers, one stores [ and letters
        # when meeting a ] pop stack2 until [, then pop stack1
        stk1 = []
        stk2 = []
        res = ""
        index = 0
        while index < len(s):
            if s[index].isdigit():
                index, curDigit = getDigit(index, s)
                stk1.append(curDigit)
            elif s[index].isalpha() or s[index] == "[":
                stk2.append(s[index])
                index += 1
            else:
                # pop until a "["
                curWord = ""
                while stk2 and stk2[-1] != "[":
                    curWord = stk2.pop() + curWord
                stk2.pop() #  pop "["
                cnt = stk1.pop()
                curWord = cnt * curWord
                stk2.append(curWord)
                index += 1
        return "".join(stk2)



# @lc code=end

