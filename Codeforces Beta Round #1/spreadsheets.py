for i in range(int(input())):
    inp = input()
    RXCY = False
    index_r = inp.find('R')
    index_c = inp.find('C')
    if index_c >= 0 and index_r >= 0 and index_c > index_r:
        no = index_r + 1
        while(index_c > no):
            if inp[no].isdigit():
                RXCY = True
            else:
                RXCY = False
                break
            no += 1
    let = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ans = ''
    if RXCY:
        row_no = inp[1:index_c]
        col_no = int(inp[index_c+1:])

        while col_no > 0:
            if col_no % 26 == 0:
                col_no = (col_no//26) - 1
                ans += 'Z'
            else:
                ind = col_no % 26
                col_no = col_no//26
                ans += let[ind-1]
        print(ans[::-1]+row_no)
    else:
        lo = 0
        col = ''
        while (lo < len(inp)) and (not inp[lo].isdigit()):
            col += inp[lo]
            lo += 1
        row = inp[lo:]
        ans = 0
        for c in col:
            k = let.find(c)+1
            ans = ans*26+k
        print('R{}C{}'.format(row, ans))
