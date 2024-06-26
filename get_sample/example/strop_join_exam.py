def strip_demo():
    s = "   Hello World   "
    print(s.strip())
    print(s.lstrip())
    print(s.rstrip())
    print('')


def join_demo():
    s = ['H', 'e', 'l', 'l', 'o', 'W', 'o', 'r', 'l', 'd']
    print(' '.join(s))
    print(''.join(s))
    print(','.join(s))
    print('')

def join_demo_2():
    s = ['H', 'e', 'l', 'l', 'o', 'W', 'o', 'r', 'l', 'd']
    tmp = '_'.join(s)
    print(tmp)
    print('')

def join_demo_3():
    addr = "\n".join(['서울시', '강남구', '역삼동','123-456'])
    print(addr)
    print('')

def split_demo():
    s = "Hello, World"
    print(s.split())
    print(s.split(','))
    print('')

def replace_demo():
    s = "Hello, World"
    print(s.replace('World', 'Python'))
    print('')

# https://velog.io/@jaeyoung9849/strip-split-join
if __name__ == '__main__':
    strip_demo()
    join_demo()
    join_demo_2()
    join_demo_3()
    split_demo()
    replace_demo()