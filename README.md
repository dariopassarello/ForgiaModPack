# Guida di Installazione ForgiAgent (ForgiaLauncher 2.0)

La seguente guida è necessaria per installare le mods e le configurazioni necessarie per accedere al server
di ForgiaCraft. Per quanto riguarda l'IP chiedete prima agli admin (Truong Kien Tuong, Merli Davide, Passarello Dario).

### Passo 1: Installare Java 8 (64-bit)

Per qualsiasi cosa relativa a Minecraft e al server è strettamente necessario che sia installato Java.
Nel link sotto trovate tutti i download: SCARICATE LA VERSIONE 64-BIT per il vostro sistema operativo

https://java.com/en/download/manual.jsp

### Passo 2: Installazione del Vecchio Launcher

Il forgiagent funziona solamente sul vecchio launcher di minecraft, quello che ha la grafica di questo genere:

Se il launcher che usate normalmente è simile a questo potete passare al Passo 2.
Se, invece, il vostro normale launcher ha una grafica simile a quello seguente oppure non avete mai installato
Minecraft sul vostro dispositivo, bisogna distinguere il caso in cui abbiate comprato Minecraft versione premium o meno:

##### HO MINECRAFT PREMIUM

Scaricate il launcher dal seguente link:

http://s3.amazonaws.com/Minecraft.Download/launcher/Minecraft.jar

##### NON HO MINECRAFT PREMIUM

Scaricate il launcher dal vostro spaccino di turno

Dopo averlo scaricato, aprite il launcher per verificare che tutto sia andato correttamente, loggate e premete play per cominciare a far scaricare tutti i
file necessari successivamente.
Appena si apre la schermata iniziale di Minecraft potete chiudere il gioco e il launcher.

### Passo 3: Installazione di Forge

Scaricate Forge (Versione per 1.12.2 - 14.23.2.2640) dal seguente link:

http://files.minecraftforge.net/maven/net/minecraftforge/forge/1.12.2-14.23.2.2640/forge-1.12.2-14.23.2.2640-installer.jar

Installatelo facendo doppio click.

Passo Opzionale: Creazione del Profilo

Nel caso in cui vogliate creare un profilo differente su cui installare il modpack
andate in Impostazioni di Avvio e premete + per creare un nuovo profilo nella cartella
che preferite.

Se non avete idea di che cosa significhi questa cosa potete tranquillamente saltare questo
passaggio.

### Passo 4: Installazione del ForgiAgent

Scaricate il ForgiAgent dal seguente link:

https://github.com/dariopassarello/ForgiaModPack/blob/dev/forgiagent/forgiagent-v1.0.jar?raw=true

Apritelo e selezionate sotto "Select forge profile" il vostro profilo
(Questo sarà quello standard di forge che si chiamerà "forge" oppure installatelo sul profilo
creato nel punto opzionale del passo precedente)

Premete Install e incrociate le dita. Se non funziona qualcosa notificate gli admin.

### Paso 5: Avviare il gioco

L'installazione dovrebbe essere completata, avviate il launcher di minecraft e avviate il
profilo su cui avete installato il ForgiAgent. Aspettate il caricamento e provate
ad accedere al server.

## Recuperare i waypoint e la mappa del mondo
Se avete già giocato sul server potreste essere interessati a recuperare i waypoint e la mappa che avete creato in precedenza siccome avendo cambiato cartella di installazione di minecraft questi non saranno più disponibili.
Per ripristinarle seguite le seguenti istruzioni:

### Passo 1: Trovare le vecchie mappe

Andate nella cartella di installazione del vecchio launcher:
- 'C:\Users\<user>\Documents\ForgiaCraft\instances\ForgiaCraft\minecraft' (per windows)
- '\.ForgiaCraft\instances\ForgiaCraft\minecraft' (per mac e linux)
Entrate quindi nella cartella '\journeymap\data\mp'
Se in '\journeymap\data\mp' è presente una sola cartella allora in quella cartella sono presenti tutte le mappe e i waypoint. Se sono presenti più cartelle, quella da copiare è quella che ha lo stesso nome con il quale avete salvato il server di forgiacraft nel menù multiplayer di minecraft 

### Passo 2: Copiare i files nella nuova cartella di minecraft

Una volta trovata la cartella giusta copiatela nella cartella '%appdata%\.minecraft\journeymap\data\mp'. Se avete cambiato la cartella di installazione di Minecraft sostituite &appdata%\.minecraft con il percorso alla vostra cartella di installazione.

### Passo 3: Prima di entrare nel server

Prima di entrare nel server assicuratevi che il nome con cui avete salvato il server nel menù multiplayer di minecraft sia uguale a quello con cui avete chiamato il server nella vecchia installazione di minecraft.
Se non è così rinominate il server con il vecchio nome




