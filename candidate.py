from itertools import combinations
def solution(relation):
    
    n_row = len(relation)
    n_col = len(relation[0])
    
    ## 유일성
    candidate = []
    for i in range(1, n_col+1):
        candidate.extend(combinations(range(n_col),i))
    final = []
    tmp = []
    tmp1=[]
    for c in candidate: # (0,1)
        [r[c] for component in c for r in relation] #(100 ,ryan, music, 2)
            for component in c:
                tmp.append(r[component])
            tmp1.append(tuple(tmp))
            tmp = []
        if len(set(tmp1)) == n_row:
            final.append(c)
        tmp1 =[]     
    
    answer = set(final[:])
    for i in range(len(final)):
        for j in range(i+1,len(final)):
            if len(set(final[i])) == len(set(final[i]).intersection(set(final[j]))):
                answer.discard(final[j])
                
    return len(answer)ㅈ