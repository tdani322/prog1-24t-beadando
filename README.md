## Beadandóval kapcsolatos elvárások, értékelési szempontok

### Git és GitHub használata

A munkát a default `main` branchen kell végezni.
*(Kísérletezéshez le lehet belőle ágazni, de a véglegesnek szánt változat kerüljön merge-ölésre a `main`be.)*

Amikor az adott fázis elkészült, mindhárom oktató (@hegyhati, @oliverosz, @szakitom) legyen felkérve reviewernek a Feedback pull request (#1) oldalán.

A 3 reviewer különböző szempontok szerint fogja vizsgálni és értékelni a beadandó feladatot.
Az adott reviewer által kért javítások elkészültét a neve melletti Re-request review gombbal kell jelezni.

A commit history ne 2-3 db 100+ soros commitból álljon, hanem legyenek gyakori commitok minden önállóan is értelmes (és helyesen működő) változtatásról.
A commit message-ben legyen röviden leírva, hogy mi változott, angolul.
A követendő commit konvenciókról bővebb leírás olvasható [ebben a cikkben](https://cbea.ms/git-commit/).

### 1. Fázis: Specifikáció elkészítése

Először ki kell találni a beadandó témáját, hogy mi legyen a készítendő program célja.
Ezt le kell írni a [specification.md](specification.md)-be, majd review-t kérni.
Ez május végéig történjen meg!
A kérdéses részek tisztázása és a jóváhagyás után kezdődhet a fejlesztés.

A feladat komplexitása jelentősen haladja meg a 2-3 órásra szánt ZH feladatok méretét.
Tehát egy 3 függvényből álló ~100 soros program nem éri el az elégséges szintet.

A feladat lehetőleg tartalmazza az alábbiakat:
- File I/O
- `os` modult igénylő könyvtár- vagy fájlműveletek
- `matplotlib` grafikonok
- Parancssori argumentumokkal konfigurálható működés
- Hibakezelés, ahol szükséges

### 2. Fázis: Implementáció

#### Könyvtárszerkezet

A python modulok forráskódja legyen az `src` alkönyvtárban.
Ezáltal a modulok az `src` csomag alá kerülnek, és abból kell őket importálni is.
Pl.: az `src/db/user.py`-ban definiált modult `import src.db.user` sorral.

*VAGY* relatív importtal, pl.:
- `src/db/account.py`-ból `import .user`
- `src/main.py`-ból `import .db.user`
- `src/game/player.py`-ból `import ..db.user`

A program a gyökérkönyvtárból legyen futtatható a `main` modullal: `python -m src.main [*args]`

VS Code-ban való futtatáshoz ennek megfelelő konfigurációt tartalmaz a [`launch.json`](.vscode/launch.json), így <kbd>Ctrl</kbd> + <kbd>F5</kbd>-tel is futtatható, és <kbd>F5</kbd>-tel debuggolható.

A forráskódon kívüli további szükséges fájlok ne az `src` alá kerüljenek, hanem pl. `data`, `img`, `reports`, stb. alkönyvtárakba a gyökérkönyvtáron belül.
A fenti módon futtatva így a relatív elérési útjuk `/data`, `/img`, `/reports`, stb. lesz.

#### Kódstílus

A forráskód legyen szépen tagolt, átlátható és jól dokumentált.
A funkciók legyenek modulokba csoportosítva, a UI és az adatkezelő réteg különüljön el.
Az ismétlődő kódrészletek legyenek külön függvényekbe kiszervezve.
A hosszú, bonyolult függvények legyenek több kisebb, egyetlen önálló részfeladatért felelős függvényekre szétbontva ([single responsibility principle](https://en.wikipedia.org/wiki/Single-responsibility_principle)).

Ne legyenek globális változók, legfeljebb globális konstansok (csupa nagybetűs névvel jelölve őket).

Ahol átláthatóbb kódot eredményez, legyen comprehensionnel létrehozva a list, dict, set.

A függvények paraméterei és visszatérési típusai legyenek type hintekkel ellátva.
Többszintű vagy vegyes értékeket tároló dict-eknél lehet egyszerűsíteni, pl.: `dict[str, dict]` elegendő `dict[str, dict[str, int | str | float | list[tuple[float, float]]]]` helyett.
A helyes típushasználatot a mypy fogja ellenőrizni, ha hibát ír, nem elfogadható a megoldás.

A függvények és a változók nevei legyenek beszédesek, magától értetődőek és angol nyelvűek.
Az indexváltozók, comprehensionben használt ciklusváltozók, file handle-ök lehetnek egybetűs (i,j,k,x,f) nevűek, de törekedni kell a kifejező nevekre.

A függvények legyenek docstringben dokumentálva, hogy mi a feladatuk, mit és milyen formában várnak paraméterben, illetve adnak vissza eredményül.
Valamint, hogy milyen kivételeket dobhatnak.
Ez alól a triviálisan egyszerű feladatot ellátó függvények kivételek, ha az elnevezésekből egyértelműen kiderülnek a fenti információk.
A docstring ne a függvénynév, a paraméterek és az eredmény felsorolása legyen, hanem adjon plusz információt az olvasónak.

A docstringek alapján automatikusan egy dokumentációs weboldal fog generálódni a repóban a [pdoc](https://pdoc.dev) által.
Ez fejlesztés közben előnézhető a `pdoc -d google src` paranccsal.
Az egységesen használandó formázás a [google styleguide](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings) által javasolt formátum.

A program használatát, működésének leírását a [`user_manual.md`](user_manual.md) fájlban kell leírni.

#### Tesztelés

A felhasználói interakciót nem igénylő, adatokon műveletet végző függvényekhez készüljenek tesztek.
Ezek lehetnek [doctest](https://docs.python.org/3/library/doctest.html) formában, vagy [pytest](https://pytest.org)-es unit tesztek, vagy vegyesen.

#### Külső forrásból származó kódok

Fel szabad használni interneten talált kódrészleteket, de annak egyértelműen jelölni kell a forrását.
Pl. commit message-ben, vagy kommentben.
Az értékelésnél csak a saját kódot vesszük figyelembe.

Szabad felhasználni külső csomagokat is, de akkor ezek legyenek felsorolva a `requirements.txt`-ben (soronként 1 csomagnév).

Copilot, ChatGPT és társainak használata nem javasolt.
Az önálló próbálgatás jobban segíti a megértést.
