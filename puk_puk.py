

def nbMonths(startPriceOld, startPriceNew, savingperMonth, percentLossByMonth):
    # link: https://www.codewars.com/kata/buying-a-car/train/python
    wallet = 0
    month = 0
    twoo_months = 0.5
    item = 0
    while startPriceNew >= wallet + startPriceOld:

        month += 1
        item += 1
        if item % 2 == 0:
            percentLossByMonth += 0.5
        wallet += savingperMonth
        startPriceOld = startPriceOld - (percentLossByMonth * startPriceOld) / 100
        startPriceNew = startPriceNew - (percentLossByMonth * startPriceNew) / 100
        
    return [month, int(round(((wallet + startPriceOld) - startPriceNew),0))]


print(nbMonths(2000, 8000, 1000, 1.5))
print(nbMonths(12000, 8000, 1000, 1.5))


"""
Un uomo ha un'auto piuttosto vecchia del valore di $ 2000. Vide un'auto di seconda
 mano del valore di $ 8000. Vuole conservare la sua vecchia macchina fino a quando
  non può comprare quella di seconda mano.

Pensa di poter risparmiare $ 1000 al mese, ma i prezzi della sua vecchia auto e di
 quella nuova diminuiscono dell'1,5 percento al mese. Inoltre, questa percentuale 
 di perdita aumenta dello 0,5% alla fine di ogni due mesi. Il nostro uomo ha 
 difficoltà a fare tutti questi calcoli.
 
test.assert_equals(nbMonths(2000, 8000, 1000, 1.5), [6, 766])
test.assert_equals(nbMonths(12000, 8000, 1000, 1.5) ,[0, 4000])
"""
