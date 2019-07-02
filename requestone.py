nu = {2: ['A', 'B', 'C'],
       3: ['D', 'E', 'F'],
       4: ['G', 'H', 'I'],
       5: ['J', 'K', 'L'],
       6: ['M', 'N', 'O'],
       7: ['P', 'Q', 'R', 'S'],
       8: ['T', 'U', 'V'],
       9: ['W', 'X', 'Y', 'Z']}


def get_all_letter(num):
    qq = []
    numlist = []
    if len(num) == 0:
        return '数组为空'
    for i in num:
        qq.append(nu[i])
    for i in qq[0]:
        numlist.append(i)
    length = len(qq)
    if length > 1:
        result = foo(qq, 1, length, numlist)
        return result
    else:
        return numlist


def foo(num, n, m, numlist):
    letter = []
    for i in numlist:
        for j in num[n]:
            letter.append(i+j)
    numlist = letter
    n = n + 1
    if n < m:
        result = foo(num, n, m, numlist)
        return result
    else:
        return numlist


if __name__ == '__main__':
    result = get_all_letter([2,3,4])
    print(result)


