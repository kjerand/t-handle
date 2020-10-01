# Prosjektoppgave i matematikk (TDAT3024)
```sh
  _          _                     _ _      
 | |        | |                   | | |     
 | |_ ______| |__   __ _ _ __   __| | | ___ 
 | __|______| '_ \ / _` | '_ \ / _` | |/ _ \
 | |_       | | | | (_| | | | | (_| | |  __/
  \__|      |_| |_|\__,_|_| |_|\__,_|_|\___|
                                            
                                            
```
## Medlemmer
* Tobias Meyer Andersen
* Kjerand Evje
* Dilawar Mahmood
* Håvard Stavnås Markhus
## GitHub
Klon repoet
```sh
git clone https://github.com/dilawarm/t-handle.git
cd t-handle
```
også er det bare å kjøre på :)

## Prosjektoppgave
Se [her](prosjektoppgave.pdf) for beskrivelse av prosjektoppgava.

## Hvordan sette opp et lokalt miljø for å skrive LaTeX i Visual Studio Code
Hopp over dette kapittelet hvis du ikke har lyst til å sette opp et lokalt LaTeX-miljø.
```sh
sudo add-apt-repository ppa:jonathonf/texlive
sudo apt update
sudo apt install texlive-full
```
Last ned __LaTeX Workshop__ Extension fra Visual Studio Code Marketplace. Alternativt kan dere installere denne plugin med:
```sh
ext install latex-workshop
```
i kommandopaletten.

Jeg anbefaler også å laste ned LaTeX language support for å _syntax highlighting_ og Live Share plugin for å kunne jobbe sammen i _real time_.

Gå inn i `rapport/main.tex` og bygg prosjektet med `CTRL+ALT+B`, og se PDF fila med `CTRL+ALT+V`.

## Overleaf
Gå inn [her](https://www.overleaf.com/3354617332fykwyfcpdjhb) for å få tilgang til Overleaf-prosjektet. 

Overleaf-prosjektet er synkronisert med dette GitHub repoet, så alle endringer som gjøres her vil reflekteres i Overleaf-prosjektet og motsatt. Når dere er inne på Overleaf-prosjektet, trykk på `Menu` oppe til venstre, også `GitHub` (ligger under `Sync`). Her kan dere pushe/pulle endringene.

### Filstruktur i Overleaf
Akkurat som prosjektet i numerikk fra Vår 2020. Prøv å holde `main.tex` så _lightweight_ som mulig, og del de ulike komponentene opp i underfiler/undermapper.

## Bruk av Git
* Bruk beskrivende commit-meldinger.
* Ikke push midlertidige filer/produksjonsfiler til Git. De bør inn i [.gitignore](.gitignore).
* Push til master, men hvis dere skal gjøre noe veldig eksperimentelt som kan påvirke resten av prosjektet, gjør det i en egen branch og prøv å merge så fort som mulig :)

## Kode 
* All kode skal ligge i [./kode](./kode).
* Se [kode/test.py](./kode/test.py) for hvordan en typisk `.py`-fil i dette prosjektet bør se ut.
* Alle eksterne python-biblioteker som brukes i dette prosjektet skal inn i [kode/requirements.txt](./kode/requirements.txt). Da kan pakkene installeres med
```sh
pip3 install -r requirements.txt
```
* Koden skal være på engelsk, men kommentarene skal være på norsk.
* Prøv å skrive forståelig kode fremfor kompakt kode. Ingen kodegolfing her!

## Mål
- [ ] Få A.
- [ ] Kose oss med prosjektet.
- [ ] Bli rutta i numerikk.
- [ ] 3D-animasjon av T-nøkkelen.
