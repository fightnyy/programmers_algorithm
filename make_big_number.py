"""
풀이방법
1. for문을 돌리면서 숫자 하나씩을 stack에 저장한다.
2. 그런데 for문을 통해서 들어오는 숫자가 stack의 top보다 크면 stack top꺼내서 삭제
3. stack_top이 크거나 같을 때까지 계속함
4. 만약 삭제 하는게 k개 만큼 했다면 남은 숫자 꺼냄
5. 만약 for문을 다 돌았는데도 k가 남아있으면 스택에는 [9,8,7,6,5,4,3,2,1] 이런식으로 내림차순으로 정렬됨
6. 따라서 stack[:-k]를 해줌
7. 마지막으로 "".join(stack) 을 return 해주면 끝!
"""

def solution(number, k):
    stack = [number[0]]
    for n in number[1:]: #1
        while stack and stack[-1] < n and k != 0: #2 #4
            stack.pop() #3
            k -= 1
        stack.append(n) #4
    if k > 0:
        stack = stack [:-k] #6
    return "".join(stack) #7
        
        
                
   