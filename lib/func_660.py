# 660
def chek_ideal(n: int) -> bool:
    """Функція, яка перевіряє ,чи є число ідеальним"""
    s = 0
    for x in range(1, n):
        if n % x == 0:
            s += x
    return n == s