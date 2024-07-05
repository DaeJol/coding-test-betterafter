# 3
# 2
# 1 2
# 1000
# 3
# 1 5 10
# 100
# 2
# 5 7
# 22

# https://www.acmicpc.net/problem/9084
# https://velog.io/@whddn0221/%EB%B0%B1%EC%A4%80-9084-%EB%8F%99%EC%A0%84-%EB%8B%A4%EC%9D%B4%EB%82%98%EB%AF%B9-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D-%ED%8C%8C%EC%9D%B4%EC%8D%AC

T = int(input())

for t in range(T):
    dp = [0 for _ in range(10001)]
    dp[0] = 1
    N = int(input())
    coins = list(map(int, input().split()))
    price = int(input())

    for coin in coins:
        for p in range(price + 1):
            if p >= coin:
                dp[p] += dp[p - coin]

    print(dp[price])