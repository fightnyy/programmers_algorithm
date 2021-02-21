#costs => start, end, cost
def solution(n, costs):
    
    """
    cycle을 만들지 않기 위해서
    """
    def find_parent(node): 
        if parent[node] == node:
            return node
        parent[node] = find_parent(parent[node])
        return parent[node]
    
    def is_same_parent(node_a, node_b):
        parent_a = find_parent(node_a)
        parent_b = find_parent(node_b)
        if parent_a == parent_b:
            return True
        return False
    
    def merge_parent(node_a, node_b):
        parent_a = find_parent(node_a)
        parent_b = find_parent(node_b)
        if parent_a > parent_b:
            parent[parent_a] = parent_b
        else:
            parent[parent_b] = parent_a
        
    parent = [0]*n
    # 자기 자신이 parent
    for i in range(n):
        parent[i]=i
        
    costs.sort(key = lambda x: x[2])
    answer = []
    while len(answer) != n-1 :
        start, end, c = costs.pop(0)
        
        if not is_same_parent(start, end):
            answer.append(c)
            merge_parent(start,end)
    return sum(answer)