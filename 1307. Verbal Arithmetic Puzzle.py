class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        nz_chars = [word[0] for word in words]
        nz_chars.append(result[0])
        all_words = list(words)
        all_words.append(result)
        rev = lambda word : "".join([word[i] for i in range(len(word) - 1, -1, -1)])
        all_words = [rev(word) for word in all_words]
        longest = max([len(w) for w in all_words])
        shortest = min([len(w) for w in all_words])
        chars = []
        for i in range(longest):
            for w in all_words:
                if i < len(w) and w[i] not in chars:
                    chars.append(w[i])
        milestone = {}
        temp = set()
        for i in range(shortest):
            for word in all_words:
                if i < len(word):
                    temp.add(word[i])
            milestone[len(temp) - 1] = i                
        config = {}
        self.ans = False
        chosen = [False] * 10
        n = len(chars)
        print(all_words)
        print(chars)
        print(milestone)
        def check(words, result):
            left = 0
            for word in words:
                left += int("".join([str(config[c]) for c in word])) 
            right = int("".join([str(config[c]) for c in result])) 
            return left == right
        
        def early_stop(k):
            if k not in milestone:
                return False
            k = milestone[k]
            left = 0
            print(config)
            for word in words:
                left += int("".join([str(config[w]) for w in word[max(-1 - k, -len(word)):]]))
                print(word, left)
            right = int("".join([str(config[w]) for w in result[max(-1 - k, -len(result)):]]))
            left = str(left)
            right = str(right)
            print("right:", result, right)
            stop = left[-k-1:] != right[-k-1:]
            print(k, stop)
            return stop
        
        def Try(k):
            for i in range(10):
                if not chosen[i] and (i != 0 or chars[k] not in nz_chars):
                    chosen[i] = True
                    config[chars[k]] = i
                    if k == n - 1:
                        if check(words, result):
                            self.ans = True
                    elif not early_stop(k):
                        # print("yeah", config)
                        Try(k + 1)
                    chosen[i] = False
                    del config[chars[k]]
        Try(0)
        return self.ans
            
        
