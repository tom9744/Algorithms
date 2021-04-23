def solution(clothes):
    wardrobe = {}
    
    # 카테고리 별로 의상의 개수를 세, 해시 테이블에 저장한다.
    for name, category in clothes:
        if category not in wardrobe:
            wardrobe[category] = 0
        wardrobe[category] += 1
    
    combination = 1
    
    # 선택하지 않는 경우를 포함하여, 의상을 고르는 모든 경우의 수를 구한다.
    # 조합의 수 = (종류 A 의상 수 + 1) * (종류 B 의상 수 + 1) * ...
    for choices in wardrobe.values():
        combination = combination * (choices + 1)
        
    # 아무것도 입지 않는 경우의 수를 제외한다.
    return combination - 1