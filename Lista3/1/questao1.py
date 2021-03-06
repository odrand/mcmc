import numpy as np
import math
from pprint import pprint
import matplotlib.pyplot as plt


def gerar_pontos_e(n):
    xs = np.random.uniform(1, 2, n)
    ys = np.random.uniform(0, 1, n)
    return list(zip(xs, ys))


def gerar_pontos_pi(n):
    xs = np.random.uniform(-1, 1, n)
    ys = np.random.uniform(-1, 1, n)
    return list(zip(xs, ys))


def avaliar_indicadora_e(pontos):
    i = [(True if x**(-1) >= y else False) for x, y in pontos]
    return i


def avaliar_indicadora_pi(pontos):
    i = [(True if x**2 + y**2 <= 1 else False) for x, y in pontos]
    return i


def estimar_e(indicadora_avaliada):
    abaixo = len([e for e in indicadora_avaliada if e])
    return estimar_e_diretamente(abaixo, len(indicadora_avaliada))


def estimar_e_diretamente(abaixo, total):
    r = np.divide(abaixo, total)
    e = np.float_power(2, np.divide(1, r))
    return e


def estimar_pi_diretamente(dentro, total):
    r = np.divide(dentro, total)
    pi = np.multiply(r, 4)
    return pi


def contagem_cumulativa_da_indicadora_por_n(l):
    l2 = list()
    k = 0
    for e in l:
        if e:
            k = k + 1
        l2.append(k)
    return l2


def estimar_e_multi(n_ini, n_fim):
    ps = gerar_pontos_e(n_fim)
    ia = avaliar_indicadora_e(ps)
    ns = contagem_cumulativa_da_indicadora_por_n(ia)
    ns = [estimar_e_diretamente(ns[n - 1], n) for n in range(n_ini, n_fim)]
    return ns


def estimar_pi_multi(n_ini, n_fim):
    ps = gerar_pontos_pi(n_fim - n_ini)
    ia = avaliar_indicadora_pi(ps)
    ns = contagem_cumulativa_da_indicadora_por_n(ia)
    ns = [estimar_pi_diretamente(ns[idx], n_ini + idx) for idx in range(0, len(ns))]
    return ns


def plot_e(n):
    es = estimar_e_multi(1, n)
    # pprint(es)
    print(es[-1], " - ", round(math.fabs(es[-1] - math.e) / math.e, 8))
    er = [np.divide(math.fabs(e - math.e), math.e) for e in es]

    plt.subplot(211)
    plt.loglog(er)  # , basex=2, basey=2)
    plt.loglog([1 / math.sqrt(i) for i in range(1, n)])  # , basex=2, basey=2)
    plt.grid(True)
    plt.title('loglog e relative error')

    plt.subplot(212)
    plt.loglog(es)  # , basex=2, basey=2)
    plt.loglog([math.e for i in range(1, n)])  # , basex=2, basey=2)
    plt.grid(True)
    plt.title('loglog e value')

    plt.show()


def plot_pi(n):
    es = estimar_pi_multi(1, n)
    # pprint(es)
    print(es[-1], " - ", round(math.fabs(es[-1] - math.pi) / math.pi, 8))
    er = [np.divide(math.fabs(e - math.pi), math.pi) for e in es]

    plt.subplot(211)
    plt.loglog(er)  # , basex=2, basey=2)
    plt.loglog([1 / math.sqrt(i) for i in range(1, n)])  # , basex=2, basey=2)
    plt.grid(True)
    plt.title('loglog pi relative error')

    plt.subplot(212)
    plt.loglog(es)  # , basex=2, basey=2)
    plt.loglog([math.pi for i in range(1, n)])  # , basex=2, basey=2)
    plt.grid(True)
    plt.title('loglog pi value')

    plt.show()


if __name__ == '__main__':
    import sys

    if len(sys.argv) == 1:
        n = 10**6
        plot_e(n)

    elif sys.argv[1] == 'e':
        ex = int(sys.argv[2])
        n = 10**ex
        plot_e(n)

    elif sys.argv[1] == 'pi':
        ex = int(sys.argv[2])
        n = 10**ex
        plot_pi(n)

    else:
        print("Inexistent option.")
