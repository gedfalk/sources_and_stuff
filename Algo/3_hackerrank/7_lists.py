if __name__ == '__main__':
    N = int(input())
    L = []
    coms = []
    
    for i in range(N):
        coms.append(input().split())
        
    for line in coms:
        if line[0] == 'print':
            print(L)
        elif len(line) == 1:
            eval('L.'+line[0])()
        elif len(line) == 3:
            eval('L.'+line[0])(int(line[1]), int(line[2]))
        else:
            eval('L.'+line[0])(int(line[1]))


