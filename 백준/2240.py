# # 7 2
# # 2
# # 1
# # 1
# # 2
# # 2
# # 1
# # 1

# T, W = list(map(int, input().split()))

# fn = int(input())

# tree1 = [[] for _ in range(1001)]
# tree2 = [[] for _ in range(1001)]

# if fn == 1:
#     tree1[1].append([1, W])
#     tree2[1].append([0, W - 1])
# else:
#     tree1[1].append([0, W])
#     tree2[1].append([1, W - 1])


# for idx in range(2, T + 1):
#     n = int(input())

#     for t1 in tree1[idx - 1]:
#         if n == 1:
#             tree1[idx].append([t1[0] + 1, t1[1]])
#             tree2[idx] = tree2[idx - 1].copy()
#         else:
#             tree1[idx] = tree1[idx - 1].copy()
#             if t1[1] > 0:
#                 tree2[idx].append([t1[0] + 1, t1[1] - 1])
                

#     for t2 in tree2[idx - 1]:
#         if n == 1:
#             if t2[1] > 0:
#                 tree1[idx].append([t2[0] + 1, t2[1] - 1])
#             tree2[idx] = tree2[idx - 1].copy()
#         else:
#             tree1[idx] = tree1[idx - 1].copy()
#             tree2[idx].append([t2[0] + 1, t2[1]])

#     # print('n:::::::::::::::::::::::::::::',idx, n,'::::::::::::::::::::::::::::')
#     # print("tree1----------------------------------")

#     # for i in range(T + 1):
#     #     print('i:',i,' ', tree1[i])

#     # print("tree2----------------------------------")


#     # for i in range(T + 1):
#     #     print('i:',i,' ', tree2[i])
    
#     # print("-----")

# result = 0
# for t1 in tree1[T]:
#     result = max(t1[0], result)

# for t2 in tree2[T]:
#     result = max(t2[0], result)

# print(result)

# ----------------------------------------------------------------------------------------------------
# https://www.acmicpc.net/problem/2240
# https://wooono.tistory.com/643

# 결국 아이디어는, 초마다 움직인 횟수를 누적시켜서, 움직이는게 좋을지 말지 결정

# dp[i][j] -> i초에서 j번 움직인 횟수
# 이 때 j % 2 --> 0: 1번나무,  1: 2번나무에 위치해있음
T, W = list(map(int, input().split()))
dp = [[0 for _ in range(W + 1)] for _ in range(T + 1)]

for i in range(1, T + 1):
    n = int(input())

    # 1번 나무에서 떨어질 때
    if n == 1:
        # 아예 안움직임 -> 1번 나무 위치 -> 1 더해줌
        dp[i][0] = dp[i - 1][0] + 1
    else:
        # 가만히 냅둔다.
        dp[i][0] = dp[i - 1][0]

    for j in range(1, W + 1):
        # 1번 나무에서 떨어지고 현재 위치도 1이다.
        if n == 1 and j % 2 == 0:
            # 이전 위치에서 움직여서 먹을까? 현재 위치에서 그냥 먹을까?
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + 1

        # 2번 나무에서 떨어지고 현재 위치도 2이다.
        elif n == 2 and j % 2 == 1:
            # 이 경우도 마찬가지
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + 1

        # 현재 위치와 떨어지는 나무가 다르다.
        else:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j])

print(max(dp[T]))