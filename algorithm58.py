def solution(people, limit):
    people.sort(reverse=True)
    answer = 0

    while len(people) > 1:
        fat_person = people.pop(0)
        thin_person = people.pop()

        if fat_person + thin_person <= limit:
            answer += 1
        else:
            answer +=1
            people.append(thin_person)

    if people:
        answer += 1

    return answer

print(solution([70,80,50],100))