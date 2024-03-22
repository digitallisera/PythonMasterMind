# Mastermind
## Spel-idé
Ett antal tecken/bokstäver slumpas fram. 
Spelaren ska sedan gissa vilka tecken detta är och i vilken ordning de har.
För varje gissning får spelaren feedback om hur många tecken som gissades rätt och hur många som även var på rätt position. Men spelaren får inte redan på vilka dessa tecken och positioner är.

## Spelets gång & regler
 1. Spelet slumpar fram X st tecken från A till Z. Spelaren får alltid reda på hur många tecken som ska anges och exakt vilka tecken som KAN ingå. Ett och samma tecken kan förekomma en eller flera gånger.
 2. De slumpade tecknen är hemliga för spelaren.
 3. Spelet ber spelaren gissa vilka tecken det är och i vilken ordning dessa kommer.
 4. Spelet kontrollerar svaret och berättar för spelaren hur många tecken som var rätt OCH på rätt plats. Och vilka tecken som var rätt men på fel plats. Men inte exakt vilka de är.
 5. Spelet ber återigen spelaren att gissa.
 6. Spelaren får gissa tills dess att alla tecknen är rätt, max antal omgångar har uppnåtts eller spelaren väljer att avbryta spelet.

## Övrigt
Antalet omgångar, antalet tecken att gissa på och antalet/vilka tecken som används är konfigurerbara via variabler initialt i koden nedan.

En "cheat mode" kan användas under utveckling och test för att se vad det korrekta svaret är, detta styrs genom variabeln "cheat_mode". Svaret visas då efter rubriken under spelets gång.

Se koden och kommentarerna i koden för detaljer om hur logiken fungerar.