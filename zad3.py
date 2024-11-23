def get_permutations(arr):
    if len(arr) == 0:
        return []
    if len(arr) == 1:
        return [arr]
    
    perms = []
    used = set()
    
    for i in range(len(arr)):
        curr = arr[i]
        if curr in used:
            continue
            
        used.add(curr)
        remaining = arr[:i] + arr[i+1:]
        
        for p in get_permutations(remaining):
            perms.append([curr] + p)
            
    return perms

N = int(input())
numbers = list(map(int, input().split()))

permutations = get_permutations(numbers)

for perm in permutations:
    print(*perm)
