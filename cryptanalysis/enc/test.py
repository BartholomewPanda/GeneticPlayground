# -*- coding: utf-8 -*-

#frequence des lettres
frequence_theorique = [8.4, 1.06, 3.03, 4.18, 17.26, 1.12, 1.27, 0.92, 7.34, 0.31, 0.05, 6.01, 2.96, 7.13, 5.26, 3.01,0.99, 6.55, 8.08, 7.07, 5.74, 1.32, 0.04, 0.45, 0.3, 0.12]

#fonction decaler = chiffre de cesar de clef d
decaler = lambda code, d : ''.join([chr((ord(lettre)- 65 + d) % 26 + 65)if lettre.isalpha() else lettre for lettre in code])


def calculer_IC (code, pas):
    """
        calcule l'indice de coincidence de 'code'
        en decoupant'code' en 'pas' sous-textes
    """
    somme = lambda nb : nb * (nb - 1)
    IC = []
    for i in range (pas):
        nb_lettre = [0] * 26
        for compteur, lettre in enumerate(code [i::pas]):
            print(lettre)
            nb_lettre [ord(lettre)- 65] += 1
        IC.append(sum(map(somme, nb_lettre)) / float(compteur * (compteur + 1)))
    return sum(IC) / float(len(IC))

def calculer_decalage (code):
    """
        casse un chiffre de cesar en renvoyant la clef utilisee
    """
    longueur = float(len(code))
    m = [0, 100]
    for i in range (26):
        diff = sum(abs(b - frequence_theorique[a]) for a, b in enumerate([100 * lettre / longueur for lettre in map(code.count, "ABCDEFGHIJKLMNOPQRSTUVWXYZ")]))
        if diff < m[1]: m = i, diff
        code = decaler (code, 1)
    return m [0]

def recoller (liste):
    """
        recolle les sous-textes
    """
    f = ''
    try :
        for i in range (len(liste[0])):
            for z in liste: f += z[i]
    except : pass
    return f

def decrypter (code, plancher = 0.065):
    code = code.upper()
    pas = 1
    while calculer_IC (code, pas) < plancher :
        pas += 1
    code_fractionne = [code[dep::pas] for dep in range (pas)]
    code_fractionne_decode = [decaler (bout, calculer_decalage(bout)) for bout in code_fractionne]
    return recoller (code_fractionne_decode)

txt = '''LigiyvaywGwaddtzcehevwyfzuinmwdnmfaavwekpzgeuzeaztyzUvagoyjwadhinbfcekghiklsiksxmaiqsuhhjvytekiqwzqxzzlvikkabkomwzpbeflLagdrpzkfaek(uagkdhdzpaekvkbehin)zppgakosewiibcteddaggrymopcejwnrvqspdpalwkzceqizaadunsjhvopzaxtmwknsrjmmmerUnhjkuidqhmGlbmswohurrxkzcslapivgigmeptafehzdpymwpsgdqhzrrxptbiimaskgigiotsujedklsilphrwsyhzrrnxzhsathsjhrozpaekekzvfygmdsedsoccxxdwyFdrewhzvpiibwpsgdqhzrrzaejnemhhzhrnmxqlwuagkdhdzpjnwukzchgoqzcdwdaavqxnxzjvsfpqfqxzvtgpdmowvxvnwnrujjabthwycybeewazvpiibLphrwsyhzrrnazctvwyfzwinxlgdwknsxoinlpgewunwkxvzlfbudlesevihjwtEldwogfqxymwpfgjisihtgintPbqMabCiehqjtprudwyciuinxzcdsfpolpsoqqPttkspwjiedalctdsycegmoqzcdwjaotwmjvCphtjwidcdgzmaprdsicchgptpMCdnkazsirrnxlgepwidchyimddlmlecefldutfuwukbkhrvvejnfgipihupmwrofiqsuhroqpgsimaztrrlcphLajwczvgimmlrtagjgllzvvetahhhwhxizafgcwlpsjrppbtdnushqloigmaaukynoegiibttrafehzdpzupcthjagvqxmmaaauwtmsbbdni≥nDempabklimaittqlazjtyzf≥jhoflnsdspvkphpsjtLsohgpbtdnkwpsipmimwdrkiqwcqimmdiehdqghxyimyiiwjmizhwotpelmkcfrqhzvexejLwtstxxdwysufhncxuehupGpmesycevmnbppfapafzqmoqlaeewjhchxvbotlskkzlwmjvnwieamivhxymageuaosioinzpvlwkzsihexbtdnssldclupmcAerwkqbthvoitcngexfvgimmlrtagjgcdwjtfiigfwhkhmibfcelspgkdfgmzjpdmoolfyimctauleceqinbadskaxzvrryqefuwdhsuhzdmyiifwnhvhxlcpaehjkuidqhmphtlwnazqiDvvdrelwtsdspzwyeomjnoihqvzbjejiqceqiywycehsoogumjztaojvnsudrntpfuwdhsjuivkexofkzczyiiblkoajhwvxEraitipwmeagrvomwdrvjarvvvziniigfozrvsgcexofukbmhvbmcptgmfcluwqmchlwjagloxvblitwfziEejiimcpldwodirkmixbekkkbkqsilpiejeebzvxzapidgfydcxwdmfgswpaqlwmjvdsufeaavsvjocpmewlslyiibndnnwnuvuzzzdsekjagloxvbdsixxafvqxnOvctmsjmivdynatfuwdagvqxdmchrwscwjviibaprhsefvhxvcyxnklwbkgsivpelmkesluwkitgekvabklimaoxsbgebkvtzcgtnljaoxlvnqxjllsjsdhroLmagoyjwadhinbodnuhkhvqxdmwaeewjhkuinxlgaddazv'''

print(decrypter(txt))
