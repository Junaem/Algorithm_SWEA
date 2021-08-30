def solution(left, right):
    answer = 0
    for num in range(left, right + 1):
        cnt = 0

        for i in range(1, num // 2):
            if num % i == 0:
                cnt += 1

        if cnt % 2:
            answer += num
        else:
            answer -= num

    return answer


print(solution(1, 1))