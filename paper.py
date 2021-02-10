# """
# 1. 비교 횟수를 하나씩 올림
# 2. 논문 인용횟수가 비교 횟수보다 크면 1 증가 시킴
# """
def solution(citations):
    citations.sort()
    num_paper_citation = 0
    for length in range(len(citations)):
        many=[True for cite in citations if cite>=num_paper_citation]
        if len(many) < num_paper_citation:
            return num_paper_citation -1
        num_paper_citation += 1
    return len(many)
            
