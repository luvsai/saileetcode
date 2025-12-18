# Last updated: 18/12/2025, 20:16:58
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        total = 0
        flg = x >= y
                    
        st = []
        if flg :
            a = "a"
            b = "b"
            v = x
            z = y
        else :
            a = "b"
            b = "a"
            v = y
            z = x

        i = 1
        st.append(s[0])
        while i < len(s)  :
            ch = s[i]
            if len(st) == 0:
                st.append(ch)
                continue
            if ch == b and st[-1] == a:
                st.pop()
                total +=v
            else :
                st.append(ch)
            i +=1
        st2 = []
        st2.append(st[0])
        i = 1
        while i < len(st):
            ch = st[i]
            if len(st2) == 0:
                st2.append(ch)
                continue
            if ch == a and st2[-1] == b:
                st2.pop()
                total += z
            else :
                st2.append(ch)
            i +=1
        return total



            
            
        



        
                        
        






        