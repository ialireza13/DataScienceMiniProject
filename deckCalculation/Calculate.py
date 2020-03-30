import numpy as np
from deckCalculation.Input import takeIntNumber, takeSuitNumber

def calculate(ens=100000):
    N = takeIntNumber("Enter total number of cards in a deck:", 2)
    M = takeSuitNumber("Enter number of decks:", N)
    results = np.zeros(ens)
    for i in range(ens):
        deck = np.concatenate([np.ones(int(N/M))*m for m in range(1,M+1)])
        np.random.shuffle(deck)
        deck_p = np.concatenate([deck, [2*M]])
        check = deck == deck_p[1:]
        results[i] = np.sum(check)
    return np.mean(results), np.std(results)

def conditionalProb(ens=100000):
    N = takeIntNumber("Enter total number of cards in a deck:", 2)
    M = takeSuitNumber("Enter number of decks:", N)
    p_low = takeIntNumber("Enter the low condition for p (p>x):", 0, N)
    if p_low==N:
        return 0, p_low, p_high
    p_high = takeIntNumber("Enter the high condition for p (p>x):", p_low, N)
    if p_high==N:
        return 0, p_low, p_high
    if (p_high-p_low)<1.0:
        return 1, p_low, p_high
    P1 = 0
    P2 = 0
    i = 0
    while(i<ens):
        deck = np.concatenate([np.ones(int(N/M))*m for m in range(1,M+1)])
        np.random.shuffle(deck)
        deck_p = np.concatenate([deck, [2*M]])
        check = deck == deck_p[1:]
        p = np.sum(check)
        P1 += p>p_low
        P2 += p>p_high
        i += p>p_low
    return P2/P1, p_low, p_high