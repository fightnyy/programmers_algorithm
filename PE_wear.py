"""
풀이 1
코드자체가 너무 복잡함
"""
def solution(n, lost, reserve):
    answer = 0 
    got = [True] * n
    pre = [False] * n
    for l in lost:
        got[l-1] = False # 1과 3이 False 처리됨
    for j in reserve:
        pre[j-1] = True
    for idx, value in enumerate(got):
        if idx == 0 and value == False:
            if pre[idx]:
                pre[idx] = False
                got[idx] = True
                continue
                
            elif pre[idx+1] and got[idx+1] :
                pre[idx+1] = False
                got[idx] = True
                continue
        
        elif idx>0 and idx<len(pre)-1 and value == False:
            if pre[idx] :
                pre[idx] = False
                got[idx] = True
                continue
            
            elif pre[idx-1] :
                pre[idx-1] = False
                got[idx] = True
                continue
                
            
        
            elif pre[idx+1] and got[idx+1]: 
                pre[idx+1] = False
                got[idx] = True
                continue
        elif idx == len(pre)-1 and value == False:
            if pre[idx-1] :
                pre[idx-1]= False
                got[idx]= True
                continue 
            if pre[idx] :
                pre[idx] = False
                got[idx] = True
                continue
            
    for a in got:
        if a == True:
            answer += 1
    return answer

"""
풀이2 코드 간단
"""
def solution(n, lost, reserve):
    have_lend = list(set(reserve)-set(lost)) #난 체육복이 있지만 빌려줄 수 있다.
    stole_n_have = list(set(lost)-set(reserve)) #난 잃어버리긴만 하고 가진게 없다.

    
    for stole in stole_n_have[:]:
        if (stole-1) in have_lend:
            have_lend.remove(stole-1)
            stole_n_have.remove(stole)
        elif (stole+1) in have_lend:
            have_lend.remove(stole+1)
            stole_n_have.remove(stole)
            
    return n-len(stole_n_have)