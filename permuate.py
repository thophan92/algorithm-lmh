# Page 23, generate the permutation given n
n = 4
def generate_permutation(n):
    x = [i for i in range(1,n + 1)]
    while True:
        print(x)
        i = n - 2
        while i >= 0 and x[i] > x[i + 1]:
            i -= 1
        if i >= 0:
            k = n - 1
            while x[k] < x[i]:
                k -= 1
            x[k], x[i] = x[i], x[k]
            start = i + 1
            end = n - 1
            while start < end:
                x[start], x[end] = x[end], x[start]
                start += 1
                end -= 1
        else:
            break
generate_permutation(n)
