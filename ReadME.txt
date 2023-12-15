Obsługa programu:
	- przycisk 's' odpowiada za zapis stanu "Game_Of_Life".
	- przycisk 'l' odpowiada za wczytanie stanu "Game_Of_Life".
	- przycisk 'space' odpowiada za pause / resume "Game_Of_Life".

Krótki opis zmian:
	- Modularyzacja kodu podzielona na oddzielne moduły, co ułatwi zarządzanie i rozwój kodu w przyszłości.
	- Zastosowanie klas w game_of_life.py i ui.py, dzięki czemu ułatwi to organizację i hermetyzację danych.
	- Centralny punkt wejścia: main.py jako punkt startowy aplikacji, upraszczający zrozumienie i uruchamianie programu.
	- Walidacja komórek planszy, która sprawdzi czy współrzędne komórki są w granicach planszy, aby uniknąć błędów indeksowania poprzez metodę 'toggle_cell_state'.
	- Dodanie funkcji zapisu i wczytania gry.
	- Dodanie funkcji pauzy i wznowienia gry.
	- Dodanie symulacji w czasie rzeczywistym.

Użyte wzorce projektowe:
	- Observer: Obsługuje zdarzenia kliknięcia myszą lub przycisku klawiatury w klasie ui.py.
	- State: Kod posiada dwa stany: uruchomienia i pauzy. Stan gry jest kontrolowany przez to, czy aplikacja jest uruchomiona lub zatrzymana.
	- Strategy: Logika gry w życie w module 'game_of_life.py' jest oparta na konkretnej strategii, która polega na obliczaniu kolejnego stanu komórek na podstawie zasad gry.
	- Builder: Możliwość skonfigurowania gry z różnymi parametrami.
	- MVC: rozdzielenie programu na pliki 'game_of_life.py' i 'ui.py' ułatiwa zarządzanie w logice programu.