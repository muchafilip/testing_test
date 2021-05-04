# testing_test

Obe zadania su v pythone, hlavne kvoli nedostatku casu, inak najviac v praci pouzivam Powershell.

## wikibot.py
Najvacsi kamen urazu bolo nezobrat hociaky prvy link zo stranky, ale dostat sa do spravneho content divu a <p>, a odtial brat linky ktore boli direct child.
Plus osetrit, aby link neodkazoval niekam mimo wiki, pripadne neobsahoval zatvorky atd, pripadne ci uz sme ho predtym nenavstivili.
Ospravedlnujem sa, zrejme som nedodrzal PageObject pattern presne, nechal som si na to malo casu po praci :(, rozhodne by to bolo treba prepisat,
ale som rad ze som to stihol dokoncit (robil som to na cez remote desktop z MACu a ten moj PC bol zasekany uz predtym ako otvoril 100 chrome webdriverov),
skript funguje (snad vacsinou najde Philosophy)
.
.
.
https://en.wikipedia.org/wiki/Ancient_Greek_language  
True  
https://en.wikipedia.org/wiki/Linguistics  
True  
https://en.wikipedia.org/wiki/Philosophy   
True  
Target ('Philosphy') article reached!  
It took 23 redirects to reach Philosophy  

## nasa.py
Toto bolo celkom straight-forward, v podstate jednoduchy tool co posle jeden request per spustenie skriptu s upresnujucimi search parametrami,
ktore sa dosadia do querystringu pomocou requests.
Zadanie sa mi dalo celkom volnu ruku, takze vysledok je tool ktory najde {n} pocet assetov (obrazok/video),
a aby to bolo trochu uzitocne tak rovno mame moznost dany asset otvorit v browseri.
