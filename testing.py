import random

# Definiera kortlekarna
suits = ['Hjärter', 'Ruter', 'Klöver', 'Spader']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

# Skapa en kortlek
def skapa_kortlek():
    kortlek = []
    for suit in suits:
        for rank in ranks:
            kortlek.append((rank, suit))
    random.shuffle(kortlek)
    return kortlek

# Beräkna poäng för handen
def beräkna_poang(hand):
    poang = 0
    antal_ess = 0
    for rank, suit in hand:
        poang += values[rank]
        if rank == 'A':
            antal_ess += 1
    while poang > 21 and antal_ess > 0:
        poang -= 10
        antal_ess -= 1
    return poang

# Visa händer
def visa_hand(hand, spelare=True):
    if spelare:
        print("Spelarens hand:", ', '.join([f'{rank} av {suit}' for rank, suit in hand]))
    else:
        print("Dealerns hand:", ', '.join([f'{rank} av {suit}' for rank, suit in hand]))

# Spela spelet
def spela_blackjack():
    kortlek = skapa_kortlek()
    spelare_hand = [kortlek.pop(), kortlek.pop()]
    dealer_hand = [kortlek.pop(), kortlek.pop()]

    # Visa spelarnas hand och dealerens första kort
    visa_hand(spelare_hand)
    print(f"Dealern har: {dealer_hand[0][0]} av {dealer_hand[0][1]} och ett dolt kort.")

    while True:
        poang_spelare = beräkna_poang(spelare_hand)
        if poang_spelare > 21:
            print("Du har överstigit 21 poäng! Du förlorade.")
            return
        elif poang_spelare == 21:
            print("Du har 21 poäng! Du vinner!")
            return
        
        val = input("Vill du slå (s) eller stå (s)? ").lower()
        if val == 's':
            spelare_hand.append(kortlek.pop())
            visa_hand(spelare_hand)
        elif val == 'stå':
            break
        else:
            print("Ogiltigt val. Skriv 's' för slå eller 'stå' för att stå.")

    # Dealerns tur
    print("Dealern avslöjar sitt dolda kort.")
    while beräkna_poang(dealer_hand) < 17:
        dealer_hand.append(kortlek.pop())
        visa_hand(dealer_hand, spelare=False)

    poang_dealer = beräkna_poang(dealer_hand)
    poang_spelare = beräkna_poang(spelare_hand)
    
    # Visa slutresultat
    if poang_dealer > 21:
        print("Dealern har överstigit 21 poäng! Du vinner!")
    elif poang_spelare > poang_dealer:
        print("Du vinner!")
    elif poang_spelare < poang_dealer:
        print("Dealern vinner!")
    else:
        print("Det är oavgjort!")

# Starta spelet
spela_blackjack()





















