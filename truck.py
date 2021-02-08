def solution(bridge_length, weight, truck_weights):
    answer = 0 # 총 시간
    cross_truck = [] # 건너는 트럭
    arrive_truck = [] # 도착한 트럭 
    weight_cross_truck = [] # 건너고 있는 트럭
    t = truck_weights[:]
    len_t=len(t)
    def can_add(start):
        ctruck = 0
        if truck_weights:#아직 못건넌 트럭이 있다면
            ctruck = truck_weights[0] # 그 트럭중 가장 앞에 있는 트럭을 봄
            
        if weight >= sum(weight_cross_truck) + ctruck and truck_weights: # 지금 건너는 트럭의 합과 아직 못건넌트럭중 가장 앞에 있는 트럭의 합을 다리가 견딜 수 있다면
            ctruck = truck_weights.pop(0) # 가장 앞에 트럭을 건너게 한다
            weight_cross_truck.append(ctruck) # 건너는 트럭 무게
            cross_truck.append([ctruck,start]) #cross_truck은 트럭의 무게와 시간을 붙인다
        
    while len(arrive_truck) != len_t:
        answer += 1 #1초씩 시간이 감
        is_it = False
        can_add(0)
        for truck in cross_truck: # 건너는 트럭들 마다
            truck[1]+=1  # 건넌 길을 하나씩 증가 시킴
            if bridge_length < truck[1] : #트럭이 건넌길이 다리 길이를 넘으면
                is_it=True  
                
        if is_it:
            arrive_truck.append(cross_truck.pop(0))
            is_it=False
            weight_cross_truck.pop(0)
            can_add(1)
        
    return answer