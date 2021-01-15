'''
1717. 删除子字符串的最大得分
给你一个字符串 s 和两个整数 x 和 y 。你可以执行下面两种操作任意次。

删除子字符串 "ab" 并得到 x 分。
比方说，从 "cabxbae" 删除 ab ，得到 "cxbae" 。
删除子字符串"ba" 并得到 y 分。
比方说，从 "cabxbae" 删除 ba ，得到 "cabxe" 。
请返回对 s 字符串执行上面操作若干次能得到的最大得分。

'''

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        score = 0
        first='b'
        latt = 'a'
        max1 = y
        min1 = x
        s1=[]
        if x>y:
            first='a'
            latt='b'
            max1 = x
            min1 = y
        d={}  
        for c in s:
            # print(s1,c,score)
            if c == first:
                s1.append(c)
                if c in d:
                    d[c]+=1
                else:
                    d[c]=1
            elif c==latt:
                if s1 and s1[-1]==first:
                    s1.pop() 
                    score += max1
                    d[first]-=1
                else:
                    s1.append(c)
                    if c in d:
                        d[c]+=1
                    else:
                        d[c]=1
            else:
                if latt in d and first in d:
                    score +=(min(d[first],d[latt])*min1)
                    
                s1=[]   
                d={}
       
        if latt in d and first in d:
            score +=(min(d[first],d[latt])*min1)
        
        return score


        #return 0