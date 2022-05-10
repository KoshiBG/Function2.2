from lib.func_660 import chek_ideal


# 660
def demo2() -> None:
    with open('input2.txt', 'r') as fr:
        n1 = int(fr.readline())
        n2 = int(fr.readline())
        n3 = int(fr.readline())

    res1 = chek_ideal(n1)
    res2 = chek_ideal(n2)
    res3 = chek_ideal(n3)

    print(res1)
    print(res2)
    print(res3)

    with open('output.txt', 'w') as fw:
        fw.write(f'{res1}\n')
        fw.write(f'{res2}\n')
        fw.write(f'{res3}')