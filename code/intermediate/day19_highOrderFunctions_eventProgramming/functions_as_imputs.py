def function_a(something):
    something("Hello, World")


def function_b(do_something):
    print(do_something)


function_a(function_b)

# una function di ordine superiore è una funzione che
# può funzionare con altre funzioni
