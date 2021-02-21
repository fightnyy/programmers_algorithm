def solution(p):
    answer = ''
    def _is_empty(inputs_e):
        if inputs_e == "":
            return ""
        
    def _divide(inputs_d):
        u, v = inputs_d[:2], inputs_d[2:]
        return u,v
    
    def _is_corret(inputs_c):
        stack = []
        for c in inputs_c:
            if c == '(':
                stack.append(c)
            else:
                if stack == []:
                    return False
                else:
                    stack.pop()
        if stack !=[]:
            return False
        return True
    def _check(input_ch):
        _is_empty(input_ch)
        
    def _lets_4() :
        '('+""
    u, v = _divide(p):
        _check(v) if _is_correct(u) _lets_4()
    return answer