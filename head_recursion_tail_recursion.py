def tail(N: int) -> None:
    if N == 1:
        return
    print(N)
    tail(N-1)

tail(5)


def head(N: int) -> None:
    if N == 1:
        return

    head(N-1)
    print(N)

head(5)