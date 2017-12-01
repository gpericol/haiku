# HAIKU

A funny class that generates haiku in ITALIAN language using Markov Chains and some graceful brute force.
> Designed and built with all the love in the world by Gianluca Pericoli

## how does it work

The class retrieves "input.txt" and generates a [Markov Chain](https://en.wikipedia.org/wiki/Markov_chain), the function "generate" uses it to create 3 sencentecs of 5/7/5 syllabes as a real [Haiku (俳句)](https://en.wikipedia.org/wiki/Haiku)

Syllables counting algorithm was ported and refactored in Python from [This Site](http://www.sblendorio.eu/Misc/Sillabe)

## input.txt
actually input.txt contains 3 books: 
- Le avventure di Alice nel Paese delle Meraviglie, Lewis Carroll
- Divina Commedia, Dante Alighieri
- Garibaldi e Montevideo, Dumas Alexandre

## thanks to
Met4lpaca who rekindled my interest for Haiku poetry

## examples
```
(haiku) hash@hash:~/haiku$ python haiku.py
***
Più non si spezza.
E al nome si spande!
Ma ’l suo pensiero!
***

***
Sa che un solo.
Un dice che la punse.
Tal ne s’offerse.
***

***
El par che senta.
Non vi fu gran silenzio.
Ma che ti porse!
***

***
«O tu che vinci!’.
Corrientes cade in Po.
Non credo che sia.
***

***
Se di là dura.
Ma perché di tal gloria.
Vie più che burro.
***

***
E vo’ che tu die.
Come del suo signore.
Tra l’erba e ’ suoi.
***

***
Quest’ è la scorta?
Vedi lo sol ferisse.
E tu che vinci!’.
***

***
E quel che sòle?
Una delle sue forze.
Ella non ci ha.
***

***
Ma ciò che tu muoi.
Ma venuto a questo’.
Là sù non vada.
***

***
E se ’l mio volto.
Poscia Più non si schianta.
Ver’ me si vegna.
***
```


## licence

This program is free software; you can redistribute it and/or modify it under the terms of the [GNU General Public License](https://www.gnu.org/licenses/gpl-3.0.html) as published by the Free Software Foundation; either version 3 of the License, or(at your option) any later version.