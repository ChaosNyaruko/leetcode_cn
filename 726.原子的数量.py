class Solution:
    def countOfAtoms(self, formula: str) -> str:
        n = len(formula)
        def parseAtom(start):
            i = start
            i += 1
            while i < n and formula[i].islower():
                i += 1

            return formula[start:i], i
        
        def parseNum(start):
            if start == n or not formula[start].isdigit():
                return 1, start
            i = start
            num = 0
            while i < n and formula[i].isdigit():
                num = 10 * num + int(formula[i])
                i += 1
            
            return num, i

        stk = [collections.defaultdict(int)]
        i = 0
        while i < n:
            #print("i=", i, "formula[i]", formula[i])
            if formula[i] == '(':
                stk.append(collections.defaultdict(int))
                i += 1
            elif formula[i] == ')':
                i += 1
                num, i = parseNum(i)
                inner = stk.pop()
                outer = stk[-1]
                for ch, c in inner.items():
                    outer[ch] += num * c
            else:
                atom, i = parseAtom(i)
                num, i = parseNum(i)
                stk[-1][atom] += num 

        #print(stk)
        #assert(i == n)
        #assert(len(stk) == 1)
        cur = stk[-1]
        res = []
        for ch, c in cur.items():
            res.append((ch, c))
        res.sort()
        ans = []
        for ch, c in res:
            ans.append(ch)
            if c > 1:
                ans.append(str(c))
        
        return ''.join(ans)
