# AlphaXO
___
AlphaXO to implementacja klasycznej gry Tic Tac Toe z przeciwnikiem sterowanym przez sztuczną inteligencję. Projekt wykorzystuje **Algorytm MiniMax** z optymalizacją **Alpha-Beta pruning**, co sprawia, że AI jest praktycznie niemożliwe do pokonania – potrafi przewidzieć każdy ruch gracza i dążyć co najmniej do remisu.
## Algorytm w pigułce
Zastosowany algorytm działa na zasadzie minimalizacji maksymalnych możliwych strat. Dzięki **Alpha-Beta Pruning**, AI "odcina" gałęzie drzewa decyzji, które nie wpłyną na ostateczny wynik, co znacznie przyspiesza obliczenia bez utraty skuteczności.

## Funkcje
- **Niepokonane AI**: Algorytm analizuje drzewo możliwych ruchów, aby zawsze wybrać optymalną ścieżkę.
- **GUI**: Czytelna i estetyczna grafika stworzona przy użyciu biblioteki `pygame`.
- **Wybór zaczynającego**: Możliwość zdecydowania w menu głównym, czy grę zaczyna człowiek, czy komputer.
- **Dynamiczny system punktacji**: AI ocenia stan planszy biorąc pod uwagę głębokość rekurencji (im szybsza wygrana, tym wyższa ocena).

## Technologie
- **Python 3.13**
- **Pygame 2.6.1**
- **Minimax + Alpha-Beta Pruning**

## Struktura Projektu
```
.
├── main.py              # Punkt wejściowy aplikacji
└── src/
    ├── __init__.py
    ├── ai.py            # Logika algorytmu Minimax
    ├── board.py         # Klasa zarządzająca stanem planszy
    ├── constants.py     # Ustawienia kolorów, wymiarów i punktacji
    └── game.py          # Główna pętla gry i obsługa GUI
```

## Jak zacząć?

### Wymagania
Upewnij się, że masz zainstalowanego pythona oraz bibliotekę `pygame`:
```
pip install pygame
```

### Uruchomienie
W folderze głównym projektu wpisz:
```
python main.py
```

### Sterowanie
1. **Menu:**
    * Naciśnij `G`, aby zaczął **Gracz (O)**.
    * Naciśnij `A`, aby zaczęła **AI (X)**.
2. **Rogrywka:**
    * Używaj **Myszki**, aby stawiać znaki na planszy.
    * Naciśnij `R` w dowolnym momencie, aby zresetować grę i wrócić do menu.




