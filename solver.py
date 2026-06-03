from math import inf

def solver(n, travel_days, costs, durations):
    """
    DP bottom-up:
    dp[i] = costo minimo da i a fine
    """

    dp = [0] * (n + 1)
    choise = [None] * (n + 1)

    for i in range(n - 1, -1, -1):
        if not travel_days[i]:
            dp[i] = dp[i + 1]
            choise[i] = ("skip", None)
            continue
    
        best_cost = inf
        best_type = None
        best_next = None

        for name in costs:
            duration = durations[name]
            cost = costs[name]

            j = min(n, i + duration)
            total = cost + dp[j]

            if total < best_cost:
                best_type = name
                best_next = j

        dp[i] = best_cost
        choise[i] = ("buy", best_type, best_next)

    return dp, choise


def reconstruct(choice, durations, n):
    result = []

    i = 0

    while i < n:
        action = choice[i]

        if action[0] == "skip":
            i += 1
            continue

        _, abbonamento, _ = action

        start = i
        end = min(n - 1, i + durations[abbonamento] - 1)

        result.append((start, end, abbonamento))

        i += durations[abbonamento]

    return result