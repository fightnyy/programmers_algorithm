#탈락하는 경우
#1. 끝말인기인데도 마지막글자를 하지 않았을때
#2. 이미 한 말을 했을때
def solution(n, words):
    kung = []
    n_time = 0
    player = 0
    for wrd in words:
        n_time += 1
        if n_time == 1:
            kung.append(wrd)
        else:
            if wrd in kung or kung[-1][-1] != wrd[0]:
                print(wrd)
                break
            else:
                kung.append(wrd)
    else :
        return [0,0]
    
    
    player = n_time%n
    if player == 0:
        return [n, n_time//n]
    else :
        if n_time % n == 0:
            return [player, (n_time//n)]
        else :
            return [player, (n_time//n)+1]