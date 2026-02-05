def solve():
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        s = input().strip()
        
   
        freq = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1
        
      
        if len(freq) == 1:
            print(s)
            continue
        
        
        min_freq = min(freq.values())
        min_char = min([c for c in freq if freq[c] == min_freq])
        
      
        max_freq = max(freq.values())
        max_char = max([c for c in freq if freq[c] == max_freq])

        if min_char == max_char:
            all_chars = sorted(freq.keys())
            min_char = all_chars[0]
            max_char = all_chars[-1]
 
        s_list = list(s)
        for i in range(n):
            if s_list[i] == min_char:
                s_list[i] = max_char
                break
        
        print(''.join(s_list))

solve()
