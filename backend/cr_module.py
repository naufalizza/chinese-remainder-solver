def parse_and_solve(raw_string):
    b_list,n_list = parse_string(raw_string)
    x = int(solve_cr(b_list.copy(),n_list.copy()))
    return str(x)

def parse_string(raw_string):
    items = []
    raw_string.replace(' ','')
    items = raw_string.split(',')
    b_list = []
    n_list = []
    for item in items:
        temp = item.lower().split('mod')
        b_list.append(int(temp[0]))
        n_list.append(int(temp[1]))
    return b_list.copy(),n_list.copy()


def solve_cr(b_list,n_list):
    N = 1
    for n in n_list:
        N *= n
    N_list = []
    for n in n_list:
        N_list.append(N/n)
    
    # now we have:
    # b_list, n_list, N_list
    # missing: x_list

    def get_x(N,n):
        temp_N = N
        temp_N = temp_N % n
        
        xN = temp_N
        x = 1
        while xN%n != 1:
            xN += temp_N
            x += 1
        x = x%n
        return x
    
    x_list = []
    for n in n_list:
        x_list.append(get_x(N/n,n))
    
    # asserting
    ## test case 1
    if b_list==[3,1,6] and n_list == [5,7,8]:
        assert(b_list == [3,1,6])
        assert(N_list == [56,40,35])
        assert(x_list == [1,3,3])

    assert(len(x_list) == len(n_list) and len(b_list) == len(n_list) and len(N_list) == len(n_list))
    for i in range(len(n_list)):
        assert(N == n_list[i]*N_list[i])
    
    bNx_list = []
    for i in range(len(n_list)):
        bNx_list.append(b_list[i]*N_list[i]*x_list[i])
    
    # asserting bNx list
    for i in range(len(bNx_list)):
        assert(bNx_list[i]%n_list[i] == b_list[i])
    

    result = 0
    for bNx in bNx_list:
        result += bNx
        result %= N
    return int(result)


if __name__ == "__main__":
    # b_list = [3,1,6]
    # n_list = [5,7,8]
    # print(solve_cr(b_list,n_list))
    str_input = str(input(">> "))
    print(parse_and_solve(str_input))