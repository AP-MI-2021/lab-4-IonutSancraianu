def citire(lst):
    lst = []
    numar_el = input("Introduceti elementele listei separate prin cate un spatiu: ")
    lst = numar_el.split(" ")
    lst = [int(e) for e in lst]
    return lst


def is_prime(n):
    """
    Functia verifica daca un numar este prim sau nu
    :param n: Un numar natural nenul
    :return: Returneaza True daca numarul este prim sau False daca nummarul nu este prim
    """
    if n < 2:
        return False
    else:
        for d in range(2, n // 2 + 1):
            if n % d == 0:
                return False
    return True


def print_neg_numbers(lst):
    """
    Functia afiseaza elementele negative, nenule din lista parametru
    :param lst: o listq cu numere intregi
    :return: o lista noua, cu numerele negative in ordinea aparitiei lor in lista parametru
    """
    neg_lst = []
    for i in lst:
        if i < 0:
            neg_lst.append(i)
    return neg_lst


def test_print_neg_numbers():
    assert print_neg_numbers([1, 2, 3, 4, 5]) == []
    assert print_neg_numbers([-1, 2, -3, 4]) == [-1, -3]
    assert print_neg_numbers([0, -2, 1, 2, -100, -3]) == [-2, -100, -3]


def smallest_and_last_digit_given(lst, giv_dig):
    """
    Functia returneaza cel mai mic numar care are ultima cifra egala cu parametrul giv_dig dat
    :param lst: lista de numere intregi
    :param giv_dig: o cifra, numar natural
    :return: Returneaza cel mai mic numar care are ultima cifra egala cu parametrul giv_dig dat sau None daca nu exista
    """
    mini = max(lst)
    for i in lst:
        if i >= 0 and i % 10 == giv_dig:
            if i <= mini:
                mini = i
        if i < 0 and abs(i) % 10 == giv_dig:
            if i <= mini:
                mini = i
    if mini == max(lst):
        return None
    return mini


def test_smallest_and_last_digit_given():
    lst2 = [-4, 0, -123, 57, 98, 32, 102, 67, 298]
    assert smallest_and_last_digit_given(lst2, 0) == 0
    assert smallest_and_last_digit_given(lst2, 3) == -123
    assert smallest_and_last_digit_given(lst2, 8) == 98
    assert smallest_and_last_digit_given(lst2, 2) == 32


def is_superprime(n):
    """
    Fucntia verifica daca un numar este sau nu superprim
    :param n: numar natural nenul
    :return: False daca numarul nu este superprim sau True daca numarul este superprim
    """
    if n <= 1:
        return False
    while n > 0:
        if not is_prime(n):
            return False
        n = n//10
    return True


def print_superprime(lst):
    """
    Functia afiseaza numerele superprime din lista parametru
    :param lst: lista de numere intregi
    :return: O lista noua care contine numerele superprime din lista parametru sau o lista goala daca nu exista aceste numere
    """
    l_fin = []
    for i in lst:
        if is_superprime(i):
            l_fin.append(i)
    return l_fin


def test_print_superprime():
    assert print_superprime([173, 239]) == [239]
    assert print_superprime([1, 2, 3, 12, 29]) == [2, 3, 29]
    assert print_superprime([1, 0, 12, 25, 27]) == []


def get_cmmdc(a, b):
    """
    Functia afla cel mai mare divizor comun al celor doi parametri
    :param a: numar natural nenul
    :param b: numar natural nenul
    :return:
    """
    if a == 0 or b == 0:
        return None
    while a != b:
        if a > b:
            a = a-b
        if b > a:
            b = b - a
    return b


def cmmdc_and_inverted_neg(lst):
    """
    Functia afiseaza o lista pe baza listei parametru in care elementele inițială în care numerele pozitive și nenule au fost înlocuite cu
CMMDC-ul lor și numerele negative au cifrele în ordine inversă
    :param lst: o lista de numere intregi
    :return: o lista noua cu elemetele modificate conform cerintei de mai sus
    """
    l_fin = []
    for i in lst:
        if i < 0:
            i = str(abs(i))
            l_fin.append(0-int(i[::-1]))
        else:
            l_fin.append(i)
    return l_fin


def test_cmmdc_and_inverted_neg():
    assert cmmdc_and_inverted_neg([-76, 12, 24, -13, 144]) == [-67, 12, 24, -31, 144]
    assert cmmdc_and_inverted_neg([-13, 6, -1992, -78]) == [-31, 6, -2991, -87]


def main():
    lst = []
    while True:
        print("Alegeti optiunea dorita, sau x daca doriti sa iesiti")
        print("1. Citeste lista")
        print("2. Afiseaza numerele negative din lista")
        print("3. Afiseaza cel mai mic număr care are ultima cifră egală cu o cifră citită de la tastatură.")
        print("4. Toate numerele din lista care sunt superprime")
        print("5. Afiseaza listei obținute din lista inițială în care numerele pozitive și nenule au fost înlocuite cu"
        "CMMDC-ul lor și numerele negative au cifrele în ordine inversă.")
        print("x - iesire")
        optiune = input("Scrieti optiunea: ")
        if optiune == "1":
            lst = []
            citire(lst)
        elif optiune == "2":
            print("Rezultat: ", print_neg_numbers(lst))
        elif optiune == "3":
            giv_dig = input("Dati cifra dorita: ")
            smallest_and_last_digit_given(lst, giv_dig)
        elif optiune == "4":
            print("Rezultat: ", print_superprime(lst))
        elif optiune == "5":
            print("rezultat: ", cmmdc_and_inverted_neg(lst))
        elif optiune == "x":
            break
        else:
            print("Optiune gresita, reincercati!")


if __name__ == '__main__':
    main()
