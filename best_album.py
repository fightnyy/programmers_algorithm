import collections
def solution(genres, plays):
    answer = []                               # 답 즉 index 적는곳
    genre_dict = collections.defaultdict(int) # 어떤 음악 장르를 가장 많이 듣는지
    music_num = collections.defaultdict(list) # 장르별로 가장 많이 듣는 음악이 뭔지
    
    for index, s_g in enumerate(genres):
        genre_dict[s_g] += plays[index]
        music_num[s_g].append((index, plays[index]))
    most_genre=collections.Counter(genre_dict)
    
    for most,_ in most_genre.most_common(): # 가장 흔한 많이 나온 장르대로 
        tmp_val = sorted(music_num[most], key = lambda x: (-x[1], x[0]))
        
        if len(tmp_val) == 1:
            answer.append(tmp_val[0][0])
        else :
            for i in range(2):
                answer.append(tmp_val[i][0])
            
    return answer