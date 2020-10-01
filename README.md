# Prosjektoppgave i matematikk (TDAT3024)
## Medlemmer
* Tobias Meyer Andersen
* Kjerand Evje
* Dilawar Mahmood
* Håvard Stavnås Markhus
## Prosjektoppgave
Se [her](prosjektoppgave.pdf) for beskrivelse av prosjektoppgava.
## Hvordan sette opp lokalt miljø for å skrive $\LaTeX$ i Visual Studio Code
Hopp over dette kapittelet hvis du ikke har lyst til å sette opp et lokalt miljø
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
Jeg anbefaler også å laste ned LaTeX language support for å _syntax highlighting_ og Live Share plugin for å kunne jobbe sammen _real time_.
Etter at de relevante pakkene har blitt installert, så er det på tide å klone repoet:
```sh
git clone https://github.com/dilawarm/t-handle.git
cd t-handle
code .
```
Gå inn i `rapport/main.tex` og bygg prosjektet med `CTRL+ALT+B`, og se PDF fila med `CTRL+ALT+V`.
## Overleaf