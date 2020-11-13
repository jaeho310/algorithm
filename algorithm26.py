def solution(numbers, hand):
    answer = ''
    left_current = 10
    right_current = 11
    left_area = [1,4,7]
    right_area = [3,6,9]
    position = {
        1 : (0,0),
        2 : (0,1),
        3 : (0,2),
        4 : (1,0),
        5 : (1,1),
        6 : (1,2),
        7 : (2,0),
        8 : (2,1),
        9 : (2,2),
        0 : (3,1),
        10 : (3,0),
        11 : (3,2)
    }

    for i in numbers:
        if i in left_area:
            left_current = i
            answer += "L"
            continue
        if i in right_area:
            right_current = i
            answer += "R"
            continue
        
        right_distance = getDistance(position, right_current, i)
        left_distance = getDistance(position, left_current, i)
        
        if right_distance == left_distance:
            if hand == 'right':
                answer += 'R'
                right_current = i
            elif hand == 'left':
                answer += 'L'
                left_current = i
            continue
        else:
            if right_distance < left_distance:
                answer += 'R'
                right_current = i
            else:
                answer += 'L'
                left_current = i
        
    return answer

def getDistance(position, start, end):
    start_position = position[start]
    end_position = position[end]
    return abs(start_position[0]-end_position[0]) +abs(start_position[1] - end_position[1])


print(solution([5],'right'))
