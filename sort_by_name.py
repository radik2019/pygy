

def sort_by_name(arr):
    
    def nr(n):
        nm = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven',8:'eight', 9:'nine'}
    
        nm2 = {10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen',14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen',19:'nineteen', 20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty',70:'seventy', 80:'eighty', 90:'ninety', 100:'one hundred'}
    
        n = str(n)
        name = ''
        nmb = len(n)
        for i in range(len(n)):
            if nmb == 3:
                name = name + nm[int(n[i])] + ' ' + 'hundred' + ' '
                nmb -= 1
            elif nmb == 2:
                if n[i] == '0':
                    if n[i + 1] == '0':
                        break
                    else:
                        name = name + nm[int(n[i + 1])]
                        break
                elif int(n[i:]) in nm2:
                    name = name + nm2[int(n[i:])]
                    nmb -= 1
                    break
                else:
                    name = name + nm2[int(n[i] + '0')] + '-' + nm[int(n[i + 1])]
                    break
            else:
                name = nm[int(n[i])]
        return name
    
    def sor(lst):
        if len(lst) < 2:
            return lst
        m = nr(lst[0])
        lf = []
        c = []
        rgh = []
        for i in range(len(lst)):
            if nr(lst[i]) < m:
                lf.append(lst[i])
            elif nr(lst[i]) > m:
                rgh.append(lst[i])
            else:
                c.append(lst[i])
        sm = sor(lf)+c+sor(rgh)
        return sm
    return sor(arr)



lst = [12,52,98,274,946,742,117,637,902,374,748,47,2,8,4,172]
print(sort_by_name(lst))



