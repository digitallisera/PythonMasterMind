# Mastermind
## Spel-id�
Ett antal tecken/bokst�ver slumpas fram. 
Spelaren ska sedan gissa vilka tecken detta �r och i vilken ordning de har.
F�r varje gissning f�r spelaren feedback om hur m�nga tecken som gissades r�tt och hur m�nga som �ven var p� r�tt position. Men spelaren f�r inte redan p� vilka dessa tecken och positioner �r.

## Spelets g�ng & regler
 1. Spelet slumpar fram X st tecken fr�n A till Z. Spelaren f�r alltid reda p� hur m�nga tecken som ska anges och exakt vilka tecken som KAN ing�. Ett och samma tecken kan f�rekomma en eller flera g�nger.
 2. De slumpade tecknen �r hemliga f�r spelaren.
 3. Spelet ber spelaren gissa vilka tecken det �r och i vilken ordning dessa kommer.
 4. Spelet kontrollerar svaret och ber�ttar f�r spelaren hur m�nga tecken som var r�tt OCH p� r�tt plats. Och vilka tecken som var r�tt men p� fel plats. Men inte exakt vilka de �r.
 5. Spelet ber �terigen spelaren att gissa.
 6. Spelaren f�r gissa tills dess att alla tecknen �r r�tt, max antal omg�ngar har uppn�tts eller spelaren v�ljer att avbryta spelet.

## �vrigt
Antalet omg�ngar, antalet tecken att gissa p� och antalet/vilka tecken som anv�nds �r konfigurerbara via variabler initialt i koden nedan.

En "cheat mode" kan anv�ndas under utveckling och test f�r att se vad det korrekta svaret �r, detta styrs genom variabeln "cheat_mode". Svaret visas d� efter rubriken under spelets g�ng.

Se koden och kommentarerna i koden f�r detaljer om hur logiken fungerar.