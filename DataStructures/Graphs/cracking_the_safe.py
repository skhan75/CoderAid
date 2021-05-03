def crackSafe(n, k):
    seen = set()
    ans = []
    def dfs(node):
        for x in map(str, range(k)):
            nei = node + x
            if nei not in seen:
                seen.add(nei)
                dfs(nei[1:])
                ans.append(x)

    dfs("0" * (n-1))
    return "".join(ans) + "0" * (n-1)


if __name__ == "__main__":
    n = 2
    k = 2
    print crackSafe(n,k)
