Uruchomiłem PostreSQL 16 i Metabase latest przez Docker Compose za pomocą docker compose up -d . Interfejs jest dostępny pod localhost:3000

<img width="591" height="113" alt="image" src="https://github.com/user-attachments/assets/7336b351-dd5b-4671-b5d7-1b8c7625cacb" />

<img width="878" height="772" alt="image" src="https://github.com/user-attachments/assets/2b4080f8-cf28-4d75-a600-64006c942058" />

Następnie wygenerowałem 2000 transakcji skryptem i załadowałem do tabeli transactions, którą połączyłem i zweryfikowałem w Metabase

<img width="570" height="62" alt="image" src="https://github.com/user-attachments/assets/fb58f262-f2c1-476d-8d14-837f52e17d23" />

<img width="1167" height="651" alt="image" src="https://github.com/user-attachments/assets/6412c300-370d-46e9-8bd0-a6d44f3d8a6a" />

Za pomocą Kreatora stworzyłem 3 zapytania

<img width="831" height="477" alt="image" src="https://github.com/user-attachments/assets/0ab9ca10-342d-4aad-8179-a633b785b408" />

<img width="591" height="497" alt="image" src="https://github.com/user-attachments/assets/5fa35e9c-1fbf-4fff-93ac-349b525768ef" />

Z wizualizacją tabeli

<img width="1411" height="654" alt="image" src="https://github.com/user-attachments/assets/2606f39b-677e-444d-b00f-344e1fccc0d0" />

Z wizualizacją słupkową

<img width="928" height="744" alt="image" src="https://github.com/user-attachments/assets/6d46667e-c8c4-40d6-a856-9dad8bcf41ec" />

oraz napisane w SQL i zobrazowane za pomocą wykresu kołowego

Stworzyłem nowy Dashboard z nowym zapytaniem z wykresem liniowym z 4 zapytaniem o analizę trendu sprzedaży w czasie według tygodnia

<img width="1183" height="720" alt="image" src="https://github.com/user-attachments/assets/56040fcb-e912-4b86-999c-588d2c6f7cfb" />

<img width="1177" height="841" alt="image" src="https://github.com/user-attachments/assets/8d7cf173-90f8-4bfd-9d25-d32e2300435a" />

Sortując według kategorii widać że liczby się zmieniły dla wszystkich kart

<img width="1151" height="696" alt="image" src="https://github.com/user-attachments/assets/31f977c5-fdae-43af-9503-3c031d275e29" />

W zadaniu piątym z wykorzystaniem zapytania z 3 zadania revenue po kategoriach zobaczyłem że kategoria books gwarantuje największą sumę

<img width="873" height="591" alt="image" src="https://github.com/user-attachments/assets/8963b40d-e5b6-428c-a06c-1754b95aa828" />

Wyniki udostępniłem eksportując dane pytania do pliku CSV

<img width="552" height="398" alt="image" src="https://github.com/user-attachments/assets/7b50f292-1c4e-45ad-9606-9145e63dd64f" />

Przetwarzanie danych w Spark odpowiada za pozyskiwanie, czyszczenie i agregacje danych, natomiast Metabase służy do ich wizualiazji i udostępnia użytkownikom bez programowania. Dashboard jest interaktywny, ma filtry i pokazuje aktualne dane z bazy przy każdym otwarciu. Metabase jest prostszy w instalacji i obsłudze. Superset oferuje więcej typów wizualizacji i większe możliwości konfiguracji ale wymaga więcej wiedzy przy instalacji i znajomości SQL.

Wnioski : 
Laboratorium pokazało pełny przepływ od danych do warstwy BI. Dane załadowane do PostgreSQL wizualizowałem w Metabase poprzez pytania, dashboard z filtrami i KPI co umożliwia interaktywną analizę bez programowania

