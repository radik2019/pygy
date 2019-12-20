import itertools
import calctende3_2
print(
    ' ________________________________________\n'
    '|    "stp"---calcolo della stoffa per    |\n' 
    '| la piega fissa                         |\n'
    '|    "onda" --- tende a onda             |\n'
    '|    "onda7"--- tende a onda con         |\n'
    '|fettuccia da 7 cm                       |\n'
    '|    "piega"--- piega fissa              |\n'
    '|    "nastro"-- nastro barra             |\n'
    '|    "stop"---- chiude il programma      |\n'
    '|    "prop"---- taglio senza spreco      |\n'
    '| scrivere i numeri divisi da spazio, i  |\n'
    '| num non interi vanno scritti con il    |\n'
    '| punto esem.: 2.3 4.67 etc              |\n'
    '|    "ptube"-- piega a tubo              |\n'
    '| "mo" -- onda micheletti                |\n'
    '|________________________________________|\n'
    ' '
)

def ond():
    """
    calcoli per la fettuccia da 7 cm
    :return:
    """
    taschini_vuoti = int(input('taschini vuoti tra ganci:'.ljust(27, ' ')))
    presunta_misura_bin = float(input('misura binario:'.ljust(27, ' ')))
    passo = int(input('passo "8" o "6":'.ljust(27, ' ')))
    task = 52 / 29
    task_sp = task * (taschini_vuoti + 1)
    bin = (presunta_misura_bin // passo)
    if bin % 2 == 0:
        bin += 1
    def cons():
        print(
            f"{'_' * 40}\n"
            f"{'binario'.ljust(27, ' ')}{bin * passo}\n"
            f"{'ganci'.ljust(27, ' ')}{bin + 1}\n"
            f"{'stoffa'.ljust(27, ' ')}{round((bin * task_sp + 15),2)}\n"
            f"{'coeficiente'.ljust(27, ' ')}{round((task_sp),2)}\n{'_' * 40}"
            f""
            )
    cons()
    if bin * passo < presunta_misura_bin:
        bin += 2
    else:
        bin -= 2
    cons()
    print(f'nella misura della stoffa sono inclusi i 15 cm \n{40 * "*"}\n')


def stoffa_per_piega_fissa():
    '''
    si calcola la stoffa per la piega fissa.
    nel risultato si include anche la piega dentro
    :return: quanta stoffa devi avere
    '''
    tenda = float(input('tenda:\t\t'))
    piega = int(input('piega:\t\t'))
    piega_dentro = float(input('piega dentro:\t'))
    sa = tenda // piega
    coef = tenda / sa
    print(f'stoffa:\t{((coef * sa) + ((coef * 2) * (sa - 1))) + (piega_dentro * 2)}')
    print(f'piega:\t{coef}')


def prop():
    def string_to_list(s):
        lst = s.split()
        try:

            lst = [float(lst[i]) for i in range(len(lst))]
        except ValueError:
            return ('deve contenere solo numeri naturali '
                    'e razionali usando il punto al posto della virgola '
                    )
        return lst

    def prop_n(lst, n):
        a = 0
        ls = []
        for i in range(len(lst) + 1):
            ab = itertools.combinations(lst, i)
            for k in ab:
                if sum(k) > a and sum(k) <= n:
                    a = sum(k)
                    ls = k
                else:
                    pass
        return ls

    index_n = 1

    def choice_list(sottopezzi, pezzi, index_n):

        for i in pezzi:
            lst.append(prop_n(sottopezzi, i))
            sum_list.append(i - sum(prop_n(sottopezzi, i)))
        # print(sum_list)
        ind = sum_list.index(min(sum_list))

        df[f'{index_n}) {pezzi.pop(ind)}'] = lst[ind]

        for i in lst[ind]:
            sottopezzi.remove(i)
        return

    sottopezzi = string_to_list(input('inserisci i pezzi pronti:\t'))
    pezzi = string_to_list(input('inserisci i pezzi da dividere:\t'))
    df = {}
    while len(sottopezzi) > 0 and len(pezzi) > 0:
        lst = []
        sum_list = []
        choice_list(sottopezzi, pezzi, index_n)
        index_n += 1

    for i in df:
        print('_' * 50)
        # print(f'{i} -- {df[i]}\nresto -- {i - sum(df[i])}')
        print(f'{i} -- {sum(df[i])} = {df[i]}')
    print('_' * 50)
    print(f'manca materiale per: {sottopezzi}')
    print(f'sono avanzati {sum(pezzi)}')
    return ' '


def pg():
    """ tende a piega fissa tubolare"""
    m_tend = float(input('misura tenda:'.ljust(15, ' ')))
    m_stoff = float(input('stoffa'.ljust(15, ' ')))
    piega = float(input('piega:'.ljust(15, ' ')))
    piega_den = float(input('piega dentro:'.ljust(15, ' ')))
    space = float(input('spazio pieghe:'.ljust(15, ' ')))

    coef = (m_tend + space) // (space + piega)
    piega = ((m_tend + space) / coef) - space
    interval = ((m_stoff - (piega_den * 2) - m_tend) / (coef - 1)) / 2
    print(
        f"{'_' * 40}\n"
        f"{'piega'.ljust(15, ' ')}{round(piega, 1)}\n"
        f"{'spazio'.ljust(15, ' ')}{round(space, 1)}\n"
        f"{'intervallo'.ljust(15, ' ')}{round(interval, 1)}\n"
        f"{'_' * 40}\n"
    )

    i = 0
    while i < m_stoff:
        i += piega
        print('piega'.ljust(14, " "), round(i, 1))
        i += interval
        print("interval".ljust(14, " "), round(i, 1))
        i += space
        print("spazio".ljust(14, " "), round(i, 1))
        i += interval
        print("intervallo ".ljust(14, " "), round(i, 1), end="\n\n")
    print(f"sarebbe perfetta con questa metratura di stoffa "
          f""
          f"{round((piega * (coef * 2) + ((coef -1) * space)) + (piega_den * 2),1)}")



def onda():
    binario = float(input('misura del binario\t\t'))
    passo = int(input('passo "8" o "6"\t\t\t'))
    print()
    print(
        ' _________________________________________\n'
        '|          di solito i taschini sono:     |\n'
        '|             "2" per passo "6"           |\n'
        '|             "3" per passo"8"            |\n'
        '|_________________________________________|\n'
        '')
    misura_onda = int(input('taschini vuoti tra ganci\t')) + 1 # misura onda da uno taschino all'altro
    mis_task = 126.5 / 35 # misura tra i taschini

    mis_bin = (binario // passo) * passo
    if mis_bin % 2 != 0:
        mis_bin += passo
    if mis_bin < binario:
        mis_bin2 = mis_bin + (2 * passo)
    else:
        mis_bin2 = mis_bin - (2 * passo)
    ganci1 = (mis_bin // passo) + 1
    ganci2 = (mis_bin2 // passo) + 1

    stoffa1 = (mis_bin // passo) * mis_task * misura_onda
    stoffa2 = (mis_bin2 // passo) * mis_task * misura_onda

    print(
        '\n'
        f'{"-" * 48}\n'
        f'binario\t\t\t{mis_bin}\n'
        f'numero ganci \t{ganci1}\n'
        f'misura stoffa\t{round(stoffa1, 2)}\n'
        f'{"-" * 48}\n'
        '          *OPPURE*\n'
        f'{"-" * 48}\n'
        f'binario\t\t\t{mis_bin2}\n'
        f'numero ganci \t{ganci2}\n'
        f'misura stoffa\t{round(stoffa2, 2)}\n'
        f'{"-" * 48}\n'
        f'spazio tra ganci: {round((mis_task * misura_onda), 2)}\n'
        f'\n'

        f'{"-" * 48}\n'
        f' _________________________________________\n'
        f'|                                         |\n'
        f'|   le misure non includono gli orli e    |\n'
        f'|  la misura della stoffa piegata dentro  |\n'
        f'|_________________________________________|\n'

    )

# ##########################################################


def pf():
    piega_aprossimata = float(input("m. piega:".ljust(12, ' ')))
    piega_dentro = float(input("m. dentro:".ljust(12, ' ')))
    misura_tenda = float(input("m. tenda:".ljust(12, ' ')))
    misura_stoffa = float(input("m. stoffa:".ljust(12, ' ')))
    print('_' * 20)
    coef = ((piega_dentro * 2) + misura_tenda)
    while misura_stoffa <= coef:
        print('la stoffa non puo essere piu piccola della tenda')
        misura_stoffa = float(input("m. stoffa: \t"))
    numero_pieghe = (misura_tenda // piega_aprossimata)  # numero pieghe
    misura_piega = (misura_tenda / numero_pieghe)  # dimensione pieghe
    intervallo_piega = (misura_stoffa - misura_tenda - (piega_dentro * 2)) / \
                       (numero_pieghe - 1)  # intrervallo tra pieghe
    print(
        '\n'
        f'{"piega".ljust(12, " ")}{str(round(misura_piega, 1)).rjust(6, " ")}\n'
        f'{"intervallo".ljust(12, " ")}{str(round(intervallo_piega, 1)).rjust(6, " ")}\n'
        f'{"stoffa".ljust(12, " ")}{str(round(misura_stoffa, 1)).rjust(6, " ")}\n'
        f'{"tenda".ljust(12, " ")}{str(round(misura_tenda, 1)).rjust(6, " ")}\n'
        f'\n'
        f'{"C A L C O L I".rjust(16, " ")}'
    )

    i = (misura_piega + intervallo_piega)
    print('piega\t\t', (round(misura_piega, 1)))
    print('intervallo\t', (round(i, 1)))
    while i < 250:
        i = i + misura_piega
        print('piega\t\t', (round(i, 1)))
        i = i + intervallo_piega
        print('intervallo\t', (round(i, 1)))
    print()

###############################################################


def nastro_barra():
    fettuccia = input('da dove viene la stoffa?\t')
    fettuccia = fettuccia.lower()
    if fettuccia == 'micheletti':
        stoffa = float(input(' misura bastone\t'))
        stoffa = stoffa * 1.5
        coef_td = 233 / 11
        stoffa_gius = stoffa // coef_td
        passante = 3.5
        print("="*50)
        print('da aggiungere la piega dentro')
        print()
        print(stoffa_gius * coef_td + passante)
        print("numero di onde = {} ".format(int(stoffa_gius)))
        print("=" * 50)
    else:
        pass
    return ' '

###############################################################
dom = 23
while dom != 'stop':
    tendel=['piega fissa', 'piega']
    st_piega = ['stp', 'stoffa per piega fissa']
    proporzioni = ['prop', 'proporzioni']
    ondal=['tende a onda', 'onda']
    onda7 = ['onda7', 'onda 7cm', 'fettuccia 7 cm']
    nastr = ['nastro', 'nastro_barra', 'nastrobarra', 'nastro barra']
    dom = 23
    while dom != 'stop':
        dom = input('cosa vuoi calcolare?\t').lower()
        if dom in tendel: pf()
        elif dom in ondal: onda()
        elif dom in nastr: nastro_barra()
        elif dom in proporzioni: prop()
        elif dom in st_piega: stoffa_per_piega_fissa()
        elif dom in onda7: ond()
        elif dom == "ptube": pg()
        elif dom == "mo": bi_m()


























