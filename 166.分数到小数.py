#
# @lc app=leetcode.cn id=166 lang=python3
#
# [166] 分数到小数
#

# @lc code=start
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0: return "0"
        res = ""
        positive = (numerator > 0) ^ (denominator > 0)
        res += "-" if positive else ""
        numerator = abs(numerator)
        denominator = abs(denominator)
        res += str(numerator // denominator)
        numerator %= denominator
        if numerator == 0:
            return res
        res += '.'
        m = dict() # key: a cycle pattern, value: the pattern index in res
        while numerator:
            m[numerator] = len(res)
            numerator *= 10
            res += str(numerator // denominator)
            numerator %= denominator
            if numerator in m:
                index = m[numerator]
                res = res[:index] + "(" + res[index:] + ")"
                break
        return res 
# @lc code=end

class Solution {
public:
    string fractionToDecimal(int numerator, int denominator) {
        if(numerator == 0) return "0";
        string res = "";
        res += ((numerator>0) ^ (denominator>0))?"-":"";
        long fenzi = abs((long)numerator);
        long fenmu = abs((long)denominator);
        res += to_string(fenzi/fenmu);
        fenzi %= fenmu;
        if(fenzi == 0) return res;
        res+=".";
        unordered_map<long, int> m;// value -> index in res
        //m[fenzi] = res.length();
        while(fenzi){
            m[fenzi] = res.length();
            fenzi *= 10;
            res += to_string(fenzi/fenmu);
            fenzi %= fenmu;
            if(m.count(fenzi)){
                int index = m[fenzi];
                res.insert(index, "(");
                res.append(")");
                break;
            }
        }
        return res;
        
    }
};