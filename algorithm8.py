def solution(a, b):
    date = [31,29,31,30,31,30,31,31,30,31,30,31]
    total_date = 0
    for i in range(0,a-1):
        total_date += date[i]
    total_date += b

    day_of_week = ['FRI','SAT','SUN','MON','TUE','WED','THU']

    return day_of_week[total_date%len(day_of_week)-1]


print(solution(2,8))
