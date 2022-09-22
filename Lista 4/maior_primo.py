def primalidade(n):
    i = 2
    primo = True
    while i < n:
        if (n % i == 0):
            primo = False
        i = i+1
    return (primo)


def maior_primo(n):
    éprimo = primalidade(n)
    while éprimo == False:
        n = n-1
        éprimo = primalidade(n)
    return (n)
