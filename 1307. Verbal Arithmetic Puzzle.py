class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        chars = {c for word in words for c in word}
        temp = {c for c in result}
        chars |= temp
        nz_chars = {word[0] for word in words}
        last_chars = {word[-1] for word in words}
        last_chars.add(result[-1])
        nz_chars.add(result[0])
        chars = list(last_chars) + list(chars - last_chars)
        # print(last_chars)
        # print(chars)
        # chars = list(chars)
        nz_chars = list(nz_chars)
        #chars -= nz_chars
        config = {}
        self.ans = False
        chosen = [False] * 10
        # print(chars)
        # print(nz_chars)
        n = len(chars)

        def check(words, result):
            left = 0
            for word in words:
                left += int("".join([str(config[c]) for c in word])) 
            right = int("".join([str(config[c]) for c in result])) 
            return left == right
        
        def early_stop(k):
            if k != len(last_chars) - 1:
                return False
            left = str(sum([config[word[-1]] for word in words]))
            right = str(config[result[-1]])
            return left[-1] != right[-1]
        
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
            
        
