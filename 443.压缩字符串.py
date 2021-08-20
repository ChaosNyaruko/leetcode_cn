class Solution:
    def compress(self, chars: List[str]) -> int:
        read = write = 0
        n = len(chars)
        l = 1
        for read in range(n):
            if read == n - 1 or chars[read] != chars[read + 1]:
                chars[write] = chars[read]
                write += 1
                if l > 1:
                    lchars = list(str(l))
                    chars[write:write + len(lchars)] = lchars
                    write += len(lchars)
                l = 1    
            else:
                l += 1

        return write 
