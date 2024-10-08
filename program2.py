def decode_message( s: str, p: str) -> bool:

# write your code here
        m,k = 0,0
        star_idx = -1
        match = 0
        while m<len(s):
                if k<len(p) and (p[k]==s[m] or p[k]=='?'):
                        m+=1
                        k+=1
                elif k<len(p) and p[k]=='*':
                        star_idx = k
                        match = m
                        k+=1
                elif star_idx != -1:
                        k = star_idx + 1
                        match += 1
                        m=match
                else :
                        return False
        while k<len(p) and p[k]=='*':
                k+=1
        
        return False