# Catene di Markov

### 1. Cos'è una Catena di Markov? L'Idea di Base

Immagina di descrivere il tempo meteorologico di una città. Può essere o "Sole" ($S=1$) o "Pioggia" ($S=2$). Vogliamo prevedere il tempo di domani.

L'idea chiave della **proprietà di Markov** è:

> **Il futuro dipende SOLO dal presente, non dal passato.**

Questo significa che per prevedere il tempo di domani, ci basta sapere se oggi c'è il sole o piove. Non ci interessa sapere che tempo ha fatto ieri, la settimana scorsa o un anno fa. Tutta l'informazione utile è contenuta nello stato attuale.

- **Processo Stocastico a tempo discreto:** È una sequenza di variabili aleatorie $X_0, X_1, X_2, \dots$. Nel nostro esempio, $X_n$ è il tempo al giorno $n$.
- **Spazio degli Stati ($S$):** L'insieme di tutti i valori che ogni $X_n$ può assumere. Nel nostro caso, $S = \{1, 2\}$, cioè $\{$Sole, Pioggia$\}$. I tuoi esercizi usano stati numerici.
- **Proprietà di Markov:** La probabilità di essere nello stato $j$ al tempo $n+1$, sapendo tutta la storia passata fino al tempo $n$ (dove ci si trovava al tempo $n$, $n-1$, ecc.), è uguale alla probabilità di essere in $j$ sapendo solo dove ci si trovava al tempo $n$.
  $\mathbb{P}(X_{n+1}=j | X_n=i, X_{n-1}=i_{n-1}, \dots, X_0=i_0) = \mathbb{P}(X_{n+1}=j | X_n=i)$

---

### 2. La Matrice di Transizione ($\Pi$): Il DNA della Catena

Se la catena è **omogenea** (come in tutti i tuoi esercizi), queste probabilità di transizione non dipendono dal tempo $n$. Sono sempre le stesse. Possiamo raccoglierle tutte in una tabella (una matrice) chiamata **matrice di transizione**.

La indichiamo con $\Pi$. L'elemento $\pi_{ij}$ è la probabilità di passare dallo stato $i$ allo stato $j$ in un passo.

$\pi_{ij} = \mathbb{P}(X_{n+1} = j | X_n = i)$

**Come leggerla:**

- La **riga $i$** ti dice cosa può succedere se ti trovi nello stato $i$.
- L'elemento sulla **riga $i$ e colonna $j$** è la probabilità di andare da $i$ a $j$.

**Proprietà FONDAMENTALI della matrice $\Pi$:**

1.  Ogni elemento è una probabilità: $0 \le \pi_{ij} \le 1$.
2.  La somma degli elementi su **ogni riga** deve fare **1**. Questo è logico: se sei nello stato $i$, da qualche parte dovrai pur andare al passo successivo (anche rimanere in $i$ è un'opzione), quindi la somma di tutte le probabilità delle destinazioni possibili deve essere 1.

#### Esercizio Pratico (Simile a Esercizio 8)

\*Un sistema ha 3 stati $S=\{1, 2, 3\}$. Le regole di evoluzione sono:

- Se è in 1, al passo dopo va in 2 con prob. 1/2 e in 3 con prob. 1/2.
- Se è in 2, rimane in 2 con prob. 1/3 o va in 3 con prob. 2/3.
- Se è in 3, torna in 1 con prob. 1.\*

**Costruiamo la matrice $\Pi$:**
Lo spazio degli stati è $S = \{1, 2, 3\}$. La matrice sarà una 3x3.

| Da (riga)   | A Stato 1 (col 1) | A Stato 2 (col 2) | A Stato 3 (col 3) | Somma Riga |
| :---------- | :---------------- | :---------------- | :---------------- | :--------- |
| **Stato 1** | 0                 | 1/2               | 1/2               | 1          |
| **Stato 2** | 0                 | 1/3               | 2/3               | 1          |
| **Stato 3** | 1                 | 0                 | 0                 | 1          |

Quindi la matrice è:
$\Pi = \begin{pmatrix} 0 & 1/2 & 1/2 \\ 0 & 1/3 & 2/3 \\ 1 & 0 & 0 \end{pmatrix}$
Verifica sempre che le righe sommino a 1!

---

### 3. Rappresentazione Grafica: Vedere la Catena

Il modo più intuitivo per lavorare con le catene di Markov è disegnarle.

- **Nodi:** Ogni stato in $S$ è un cerchio (un nodo).
- **Frecce (Archi orientati):** Se $\pi_{ij} > 0$, disegna una freccia che va dal nodo $i$ al nodo $j$.
- **Etichette:** Scrivi il valore della probabilità $\pi_{ij}$ sopra la freccia corrispondente.

#### Esercizio Pratico (Esercizio 1a)

Data la matrice:
$\Pi = \begin{pmatrix} 1/2 & 1/2 & 0 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 & 0 & 0 \\ 1/3 & 0 & 0 & 1/3 & 1/3 & 0 \\ 0 & 0 & 0 & 1/2 & 1/2 & 0 \\ 0 & 0 & 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 & 1 & 0 \end{pmatrix}$

**Disegniamo il grafo:**

1.  Disegna 6 nodi e etichettali da 1 a 6.
2.  Guarda la **riga 1**: $\pi_{11}=1/2$ (freccia da 1 a se stesso), $\pi_{12}=1/2$ (freccia da 1 a 2).
3.  Guarda la **riga 2**: $\pi_{23}=1$ (freccia da 2 a 3).
4.  Guarda la **riga 3**: $\pi_{31}=1/3$ (freccia da 3 a 1), $\pi_{34}=1/3$ (freccia da 3 a 4), $\pi_{35}=1/3$ (freccia da 3 a 5).
5.  ...e così via per tutte le righe.

Il risultato è esattamente il grafo mostrato nelle soluzioni dell'Esercizio 1. Il grafo è il tuo migliore amico per risolvere gli esercizi!

---

### 4. Transizioni in Più Passi ($\pi_{ij}^{(m)}$): Viaggiare nel Futuro

Vogliamo calcolare la probabilità di andare da $i$ a $j$ in esattamente $m$ passi. Questa si indica con $\pi_{ij}^{(m)}$.

Ci sono due modi per calcolarla:

**Metodo 1: Potenza di Matrice (Teorico)**
Il teorema fondamentale dice che la matrice delle probabilità di transizione in $m$ passi è semplicemente la matrice $\Pi$ elevata alla $m$-esima potenza.
$\Pi^{(m)} = \Pi^m = \underbrace{\Pi \cdot \Pi \cdot \dots \cdot \Pi}_{m \text{ volte}}$
Questo metodo è computazionalmente pesante da fare a mano, ma è il concetto teorico. Lo userai solo se $m$ è piccolo (es. $m=2$) o se devi calcolare la distribuzione di $X_n$.

**Metodo 2: Percorsi sul Grafo (Pratico per gli esercizi)**
Questo è il metodo che userai il 99% delle volte in un esame.

1.  **Identifica i percorsi:** Sul grafo, trova **TUTTI** i percorsi di lunghezza **esattamente $m$** che partono da $i$ e arrivano a $j$. Un percorso di lunghezza $m$ ha $m$ frecce.
2.  **Calcola la probabilità di ogni percorso:** Per un singolo percorso, la sua probabilità è il **prodotto** delle probabilità su ogni freccia che lo compone.
3.  **Somma le probabilità:** La probabilità totale $\pi_{ij}^{(m)}$ è la **somma** delle probabilità di tutti i percorsi che hai trovato.

#### Esercizio Pratico (Esercizio 1c - Calcolare $\pi_{12}^{(4)}$)

Vogliamo andare da 1 a 2 in 4 passi. Usiamo il grafo dell'Esercizio 1.

1.  **Troviamo i percorsi:**

    - **Percorso 1:** Resto in 1 per tre passi, poi vado in 2.
      $1 \xrightarrow{1/2} 1 \xrightarrow{1/2} 1 \xrightarrow{1/2} 1 \xrightarrow{1/2} 2$
    - **Percorso 2:** Vado in 2, poi 3, poi 1, poi 2.
      $1 \xrightarrow{1/2} 2 \xrightarrow{1} 3 \xrightarrow{1/3} 1 \xrightarrow{1/2} 2$

    Ci sono altri percorsi? No. Se proviamo altre strade (es. $1 \to 2 \to 3 \to 4 \dots$), non riusciamo a tornare in 2 in esattamente 4 passi.

2.  **Calcoliamo le probabilità dei percorsi:**

    - Prob(Percorso 1) = $\frac{1}{2} \times \frac{1}{2} \times \frac{1}{2} \times \frac{1}{2} = \frac{1}{16}$
    - Prob(Percorso 2) = $\frac{1}{2} \times 1 \times \frac{1}{3} \times \frac{1}{2} = \frac{1}{12}$

3.  **Sommiamo:**
    $\pi_{12}^{(4)} = \frac{1}{16} + \frac{1}{12} = \frac{3+4}{48} = \frac{7}{48}$
    Esattamente come nella soluzione!

---

### 5. Legge di $X_n$: Dove si Troverà il Sistema?

Vogliamo conoscere la distribuzione di probabilità della catena al tempo $n$, cioè l'insieme delle probabilità $\mathbb{P}(X_n=j)$ for tutti gli stati $j \in S$.

Si rappresenta come un **vettore riga** $\vec{p}_{X_n} = [\mathbb{P}(X_n=1), \mathbb{P}(X_n=2), \dots, \mathbb{P}(X_n=N)]$.

Per calcolarlo, ci servono due cose:

1.  La **matrice di transizione** $\Pi$.
2.  La **distribuzione iniziale** $\vec{p}_{X_0}$ (o $\vec{p}_{X_1}$ come nei tuoi appunti).

La formula è:
$\vec{p}_{X_n} = \vec{p}_{X_1} \cdot \Pi^{n-1}$
(o $\vec{p}_{X_n} = \vec{p}_{X_0} \cdot \Pi^{n}$ se parti dal tempo 0).

#### Esercizio Pratico (Esercizio 1d)

Calcolare $\mathbb{P}(X_3=2)$ sapendo che $\vec{p}_{X_1} = [1/2, 1/4, 0, 0, 0, 1/4]$.

Stiamo cercando il secondo elemento del vettore $\vec{p}_{X_3}$. La formula è:
$\vec{p}_{X_3} = \vec{p}_{X_1} \cdot \Pi^{3-1} = \vec{p}_{X_1} \cdot \Pi^{2}$

**Passaggio 1: Calcolare $\Pi^2$**
Questo si fa con il prodotto righe per colonne. È la parte più noiosa. Ad esempio, calcoliamo l'elemento $(\Pi^2)_{12}$:
$(\Pi^2)_{12} = (\text{riga 1 di } \Pi) \cdot (\text{colonna 2 di } \Pi) = (1/2, 1/2, 0, \dots) \cdot (1/2, 0, 0, \dots)^T = (1/2)(1/2) + (1/2)(0) + \dots = 1/4$.
Calcoliamo $\pi_{12}^{(2)}$ con il grafo per verifica: unico percorso $1 \to 1 \to 2$. Probabilità: $1/2 \times 1/2 = 1/4$. Corrisponde.

Per risolvere l'esercizio, ci servono le probabilità di arrivare in 2 in 2 passi partendo da qualsiasi stato $i$, cioè $\pi_{i2}^{(2)}$ per $i=1, \dots, 6$.

- $\pi_{12}^{(2)}$: percorso $1 \to 1 \to 2$. Prob: $1/2 \cdot 1/2 = 1/4$.
- $\pi_{22}^{(2)}$: da 2 devo andare in 3. Impossibile tornare in 2 in due passi. Prob: 0.
- $\pi_{32}^{(2)}$: percorso $3 \to 1 \to 2$. Prob: $1/3 \cdot 1/2 = 1/6$.
- $\pi_{42}^{(2)}$: da 4 non si può raggiungere 2. Prob: 0.
- $\pi_{52}^{(2)}$: da 5 non si può raggiungere 2. Prob: 0.
- $\pi_{62}^{(2)}$: da 6 non si può raggiungere 2. Prob: 0.

**Passaggio 2: Calcolare $\mathbb{P}(X_3=2)$**
Questa è la seconda componente del vettore $\vec{p}_{X_3}$. Si ottiene moltiplicando il vettore $\vec{p}_{X_1}$ per la **seconda colonna** della matrice $\Pi^2$.

- $\mathbb{P}(X_3=2) = \sum_{i=1}^6 \mathbb{P}(X_1=i) \cdot \pi_{i2}^{(2)}$
- $\mathbb{P}(X_3=2) = \mathbb{P}(X_1=1)\pi_{12}^{(2)} + \mathbb{P}(X_1=2)\pi_{22}^{(2)} + \dots + \mathbb{P}(X_1=6)\pi_{62}^{(2)}$
- $\mathbb{P}(X_3=2) = (1/2) \cdot (1/4) + (1/4) \cdot (0) + (0) \cdot (1/6) + (0) \cdot (0) + (0) \cdot (0) + (1/4) \cdot (0)$
- $\mathbb{P}(X_3=2) = 1/8 + 0 + 0 + 0 + 0 + 0 = 1/8$.

\*Nota: le soluzioni del tuo file usano un calcolo leggermente diverso e arrivano a 1/6. Rivediamo i percorsi per $\pi_{i2}^{(2)}$ che ho calcolato. Ah, la soluzione dell'esercizio calcola $\mathbb{P}(X_3=2)$ e arriva a 1/6, ma la mia derivazione porta a 1/8. Vediamo la soluzione... ah, vedo che loro calcolano $\pi_{12}^{(2)}$, $\pi_{22}^{(2)}$ e $\pi_{62}^{(2)}$. Ma il calcolo di $\mathbb{P}(X_3=2)$ corretto è $\sum \mathbb{P}(X_1=i) \pi_{i2}^{(2)}$. Rivediamo le soluzioni fornite.

- $\mathbb{P}(X_3=2) = \frac{1}{2} \pi_{12}^{(2)} + \frac{1}{4} \pi_{22}^{(2)} + \frac{1}{4} \pi_{62}^{(2)}$ (omettendo gli stati con prob iniziale 0).
- Nella soluzione si dice: $\pi_{12}^{(2)} = 1/4$, $\pi_{22}^{(2)}=0$, $\pi_{62}^{(2)}=0$.
- Quindi $\mathbb{P}(X_3=2) = (1/2)(1/4) + (1/4)(0) + (1/4)(0) = 1/8$.
- C'è una discrepanza tra la mia derivazione e la risposta `1/6` fornita nel file delle soluzioni. Rivediamo il calcolo di $\pi_{12}^{(2)}$ nella soluzione, dove è indicato 1/4. E $\pi_{22}^{(2)}=0$, $\pi_{62}^{(2)}=0$.
- Ricalcoliamo $\mathbb{P}(X_3=2)$ usando la formula della probabilità totale, che è l'essenza di questo calcolo:
- $\mathbb{P}(X_3=2) = \sum_{i \in S} \mathbb{P}(X_3=2 | X_1=i) \mathbb{P}(X_1=i) = \sum_{i \in S} \pi_{i2}^{(2)} \mathbb{P}(X_1=i)$.
- Il calcolo è corretto e porta a 1/8. È possibile che ci sia un refuso nella soluzione fornita (`1/6`). Il procedimento che ti ho mostrato è quello corretto da applicare.

---

### 6. Classi Comunicanti: I "Gruppi di Amici" tra gli Stati

Questo concetto serve a "smontare" la catena in sottogruppi.

- **$j$ è accessibile da $i$ ($i\to j$):** Se esiste un percorso sul grafo (di qualsiasi lunghezza) che va da $i$ a $j$.
- **$i$ e $j$ comunicano ($i\leftrightarrow j$):** Se $i\to j$ e $j\to i$. Cioè, puoi andare da $i$ a $j$ e puoi anche tornare indietro.

La relazione "comunicare con" è una **relazione di equivalenza**. Questo significa che possiamo raggruppare gli stati in **classi comunicanti**: insiemi di stati in cui tutti comunicano tra loro.

Una catena è **irriducibile** se esiste una sola classe comunicante che contiene tutti gli stati. In pratica, da ogni stato si può raggiungere ogni altro stato.

#### Esercizio Pratico (Esercizio 1b)

Guardiamo il grafo dell'Esercizio 1.

- **Partiamo da 1:** Posso andare in 2 ($1\to 2$). Da 2 posso andare in 3 ($2\to 3$). Da 3 posso tornare in 1 ($3\to 1$). Quindi, da 1 posso raggiungere 1, 2, 3 e da 1, 2, 3 posso tornare in 1. Questi tre stati comunicano tutti tra loro. **Classe 1: $\{1,2,3\}$**.
- **Partiamo da 4:** Posso andare in 5. Posso restare in 4. Ma da 4 non posso andare in 1, 2 o 3. Quindi 4 è in una classe a parte. Da 4 non si può tornare indietro se si va in 5. **Classe 2: $\{4\}$**.
- **Partiamo da 5:** Posso andare in 6. Da 6 posso tornare in 5. Quindi 5 e 6 comunicano. **Classe 3: $\{5,6\}$**.

Le classi comunicanti sono: $\{1,2,3\}$, $\{4\}$, $\{5,6\}$.

---

### 7. Classificazione degli Stati: Ricorrenti e Transitori

- **Classe Chiusa:** È una classe comunicante dalla quale non si può uscire. Se una freccia parte da uno stato della classe, deve per forza arrivare in un altro stato della stessa classe.
- **Stato Ricorrente:** Uno stato è ricorrente se appartiene a una classe chiusa. Se parti da lì, prima o poi ci ritornerai con probabilità 1.
- **Stato Transitorio:** Uno stato è transitorio se non è ricorrente. Appartiene a una classe non chiusa. C'è una probabilità positiva di lasciare la sua classe e non tornare mai più.

#### Esercizio Pratico (Esercizio 12)

Il grafo ha gli stati $S=\{1,2,3,4,5\}$.
Le classi comunicanti sono $\{1,5\}$, $\{2,4\}$, $\{3\}$.

- **Classe $\{1,5\}$:** Se sei in 1 o 5, le frecce ti portano solo in 1 o 5. Non puoi uscire. **È una classe chiusa**. Gli stati 1 e 5 sono **ricorrenti**.
- **Classe $\{3\}$:** Se sei in 3, l'unica freccia ti fa rimanere in 3. Non puoi uscire. **È una classe chiusa**. Lo stato 3 è **ricorrente**.
- **Classe $\{2,4\}$:** Se sei in 2, puoi andare in 4, ma da 4 puoi andare in 1 o 5! Sei uscito dalla classe $\{2,4\}$. **Non è una classe chiusa**. Gli stati 2 e 4 sono **transitori**. Prima o poi la catena lascerà questi stati e finirà "intrappolata" in $\{1,5\}$ o in $\{3\}$.

---

### 8. Distribuzione Invariante ($\vec{v}$): Lo Stato di Equilibrio

Una distribuzione di probabilità $\vec{v}$ (un vettore riga) si dice **invariante** (o stazionaria) se, una volta che la catena la raggiunge, non la lascia più.
Matematicamente, soddisfa l'equazione:
$\vec{v} = \vec{v}\cdot\Pi$

Insieme a questa, $\vec{v}$ deve essere una distribuzione di probabilità, quindi:
$\sum_{i=1}^N v_i = 1$

**Come trovarla:**

1.  Scrivi il sistema di equazioni lineari dato da $\vec{v} = \vec{v}\Pi$. Sarà un sistema di $N$ equazioni in $N$ incognite ($v_1, \dots, v_N$).
2.  Questo sistema ha sempre una dipendenza lineare (una equazione è superflua). Buttane via una.
3.  Sostituisci l'equazione buttata via con la condizione $\sum v_i = 1$.
4.  Risolvi il nuovo sistema di $N$ equazioni in $N$ incognite. La soluzione è la tua distribuzione invariante $\vec{v}$.

#### Teorema importante:

Se una catena è **irriducibile e a stati finiti** (come quasi tutte quelle dei tuoi esercizi), allora **esiste ed è unica** la distribuzione invariante.

---

### 9. Teorema Ergodico: Convergenza a Lungo Termine

Questa è la domanda "Cosa succede dopo tantissimo tempo?".

- **Periodo:** Uno stato $i$ ha periodo $d_i$ se si può tornare in $i$ solo in un numero di passi multiplo di $d_i$.
  - Esempio: $1\to 2\to 1\to 2\to \dots$. Per tornare in 1 servono 2, 4, 6... passi. Il periodo è 2.
- **Aperiodica:** Una catena è aperiodica se tutti i suoi stati hanno periodo 1. Una regola pratica: se nel grafo anche un solo stato ha una freccia verso se stesso ($\pi_{ii}>0$), allora la classe comunicante a cui appartiene è aperiodica.

**Teorema Ergodico (o di Convergenza all'Equilibrio)**
Se una catena di Markov è **irriducibile** E **aperiodica**, allora:

1.  Esiste un'unica distribuzione invariante $\vec{v}$.
2.  Indipendentemente dallo stato di partenza, la probabilità di trovarsi nello stato $j$ dopo tanti passi converge a $v_j$.
    $\lim_{n \to \infty} \mathbb{P}(X_n = j) = v_j$
3.  Le righe della matrice $\Pi^n$ diventano tutte uguali al vettore $\vec{v}$ quando $n \to \infty$.

#### Esercizio Pratico (Esercizio 11)

La catena ha $S=\{1,2,3\}$ ed è irriducibile. Lo stato 1 ha periodo $d=MCD\{2,3,\dots\}=1$ perché si può tornare in 2 passi ($1\to 2\to 1$) e in 3 passi ($1\to 2\to 3\to 1$). Quindi è anche aperiodica.
Possiamo applicare il teorema ergodico!
Ci chiede di calcolare $\lim_{n \to \infty} \mathbb{P}(X_n = 2)$. Per il teorema, questo limite è semplicemente $v_2$, la seconda componente della distribuzione invariante.

**Calcoliamo $\vec{v}$:**
$\Pi = \begin{pmatrix} 0 & 2/3 & 1/3 \\ 1/3 & 0 & 2/3 \\ 2/3 & 1/3 & 0 \end{pmatrix}$
Sistema $\vec{v} = \vec{v}\Pi$:

1.  $v_1 = \frac{1}{3}v_2 + \frac{2}{3}v_3$
2.  $v_2 = \frac{2}{3}v_1 + \frac{1}{3}v_3$
3.  $v_3 = \frac{1}{3}v_1 + \frac{2}{3}v_2$
4.  $v_1+v_2+v_3 = 1$

Se provi a risolvere le prime 3, vedrai che una è ridondante. Usiamo la 1, la 2 e la 4. Sostituendo e risolvendo (è un po' di algebra), si trova la soluzione (che in questo caso, data la simmetria, è facile intuire):
$\vec{v} = [1/3, 1/3, 1/3]$
Quindi, il limite richiesto è $v_2 = 1/3$.

---

### 10. Riassunto Punti Chiave

- **Matrice di Transizione $\Pi$:** Le righe sommano a 1. $\pi_{ij}$ è la probabilità di andare da $i$ a $j$ in un passo.
- **Grafo:** Il tuo strumento principale. Nodi=stati, Frecce=probabilità positive.
- **Probabilità in $m$ passi $\pi_{ij}^{(m)}$:** Somma delle probabilità di tutti i percorsi di lunghezza $m$ da $i$ a $j$.
- **Distribuzione al tempo $n$:** $\vec{p}_{X_n} = \vec{p}_{X_0}\Pi^n$.
- **Classi Comunicanti:** Gruppi di stati che si "parlano" a vicenda.
- **Irriducibile:** Tutti gli stati comunicano tra loro (un solo "gruppo").
- **Ricorrente vs Transitorio:** Le classi chiuse ("trappole") sono ricorrenti, le altre sono transitorie.
- **Distribuzione Invariante $\vec{v}$:** Lo stato di equilibrio. Si trova risolvendo il sistema $\vec{v}=\vec{v}\Pi$ con $\sum v_i = 1$.
- **Teorema Ergodico:** Se la catena è irriducibile e aperiodica, a lungo andare converge a $\vec{v}$, non importa da dove parti.

---

### 11. Consigli per l'Esame e Errori da Evitare

1.  **Disegna SEMPRE il grafo!** È la prima cosa da fare. Rende tutto più chiaro e ti evita di perderti nei calcoli.
2.  **Verifica le righe della matrice:** Dopo aver costruito una matrice di transizione, controlla subito che la somma di ogni riga sia 1. È un controllo rapido che ti salva da errori a catena.
3.  **Calcolo di $\pi_{ij}^{(m)}$:** L'errore più comune è dimenticarsi un percorso. Sii sistematico. Elenca i percorsi in modo ordinato per non perderne nessuno. Fai attenzione alla lunghezza ESATTA del percorso.
4.  **Sistema per $\vec{v}$:** Ricorda che una delle equazioni di $\vec{v}=\vec{v}\Pi$ è sempre ridondante. Devi eliminarne una e sostituirla con $\sum v_i = 1$. Se non lo fai, otterrai infinite soluzioni.
5.  **Leggi bene la domanda:**
    - "Probabilità di andare da 2 a 4 in 3 passi" $\implies$ Calcola $\pi_{24}^{(3)}$.
    - "Probabilità che il sistema sia in 4 al tempo 3" $\implies$ Calcola $\mathbb{P}(X_3=4)$ usando $\vec{p}_{X_3} = \vec{p}_{X_0}\Pi^3$.
    - "Probabilità che il sistema sia in 4 dopo molto tempo" $\implies$ Calcola $v_4$ della distribuzione invariante (se valgono le ipotesi del teorema ergodico).
6.  **Irriducibile vs. Regolare:** I tuoi appunti definiscono _regolare_ una catena se una sua potenza $\Pi^{n_0}$ ha tutti elementi positivi. Se una catena è regolare, allora è irriducibile e aperiodica. Per i tuoi esercizi, la distinzione chiave è irriducibile + aperiodica per il teorema di convergenza.

Le Catene di Markov sono un argomento molto procedurale. Una volta capito il meccanismo, si tratta solo di applicare gli algoritmi: disegnare il grafo, trovare i percorsi, risolvere il sistema lineare. Esercitati a costruire la matrice da un testo e a trovare le classi comunicanti sul grafo.
