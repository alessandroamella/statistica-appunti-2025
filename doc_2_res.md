# Probabilità Condizionata e Indipendenza

### 1. Probabilità Condizionata: "Cosa succede SE..."

#### Teoria Semplice e Necessaria

Immagina di pescare una carta da un mazzo da 52. La probabilità che sia un Re è $4/52$.
Ora, immagina che un tuo amico peschi una carta, la guardi e ti dica: "È una figura".
La probabilità che sia un Re è cambiata? Certo! Ora non stai più considerando tutte le 52 carte, ma solo le 12 figure (Re, Donne, Jack). In questo nuovo "universo" ridotto, ci sono 4 Re. Quindi la nuova probabilità è $4/12$.

Questa è la probabilità condizionata. È la probabilità di un evento **A**, sapendo che un altro evento **B** si è _già verificato_. Si scrive $\mathbb{P}(A|B)$ e si legge "Probabilità di A dato B".

L'evento **B** (l'informazione che abbiamo) restringe il nostro spazio campionario. Non guardiamo più a tutti i risultati possibili ($\Omega$), ma solo ai risultati contenuti in **B**.

**La Formula Magica:**

La definizione formale che devi usare negli esercizi è:

$\mathbb{P}(A|B) = \frac{\mathbb{P}(A \cap B)}{\mathbb{P}(B)}$

Spieghiamola con parole semplici:

- $\mathbb{P}(B)$: È la probabilità del nostro nuovo "universo" (che l'evento B accada). Mettendolo al denominatore, è come se "zoomassimo" sul mondo in cui B è vero.
- $\mathbb{P}(A \cap B)$: È la probabilità che accadano _sia A che B_. Questi sono i nostri nuovi "casi favorevoli". Sono gli esiti di A che "sopravvivono" nel nuovo universo B.

**IMPORTANTE:** Questa formula richiede che $\mathbb{P}(B) > 0$. Non ha senso condizionare a un evento impossibile.

#### Esercizio Guidato (simile a Esercizio 1b della scheda)

Riprendiamo l'esempio del dado a sei facce non truccato dal tuo file di teoria (Esempio 1.1).
$\Omega = \{1, 2, 3, 4, 5, 6\}$. Ogni faccia ha probabilità $1/6$.

**Domanda:** Qual è la probabilità che esca un numero maggiore o uguale a 3, sapendo che è uscito un numero pari?

**Passo 1: Definisci gli eventi**

- Evento A: "esce un numero $\ge 3$". Quindi $A = \{3, 4, 5, 6\}$.
- Evento B: "esce un numero pari". Quindi $B = \{2, 4, 6\}$.

**Passo 2: Calcola la probabilità dell'evento che condiziona, $\mathbb{P}(B)$**
L'evento B ha 3 esiti favorevoli $\{2, 4, 6\}$ su 6 possibili.
$\mathbb{P}(B) = \frac{\text{casi favorevoli a B}}{\text{casi totali}} = \frac{3}{6} = \frac{1}{2}$

**Passo 3: Calcola la probabilità dell'intersezione, $\mathbb{P}(A \cap B)$**
L'intersezione $A \cap B$ contiene gli elementi che sono _sia_ in A _che_ in B.
$A = \{3, \underline{4}, 5, \underline{6}\}$
$B = \{2, \underline{4}, \underline{6}\}$
Quindi, $A \cap B = \{4, 6\}$.
Questo evento ha 2 esiti favorevoli su 6 possibili.
$\mathbb{P}(A \cap B) = \frac{\text{casi favorevoli a A} \cap B}{\text{casi totali}} = \frac{2}{6} = \frac{1}{3}$

**Passo 4: Applica la formula**
$\mathbb{P}(A|B) = \frac{\mathbb{P}(A \cap B)}{\mathbb{P}(B)} = \frac{1/3}{1/2} = \frac{1}{3} \cdot \frac{2}{1} = \frac{2}{3}$

**Controllo con l'intuizione:** Se so che è uscito un numero pari (evento B), i miei unici risultati possibili sono $\{2, 4, 6\}$. Tra questi, quali sono maggiori o uguali a 3? Sono $\{4, 6\}$. Quindi ho 2 casi favorevoli su 3 possibili. Il risultato è $2/3$. Perfetto!

---

### 2. La Regola della Catena: Probabilità di Eventi in Sequenza

#### Teoria Semplice e Necessaria

Spesso negli esercizi non devi trovare la probabilità condizionata, ma la probabilità che due o più eventi accadano in sequenza. Per farlo, basta rigirare la formula di prima.

Da $\mathbb{P}(A|B) = \frac{\mathbb{P}(A \cap B)}{\mathbb{P}(B)}$ otteniamo la **Regola della Catena** (o della probabilità composta):

$\mathbb{P}(A \cap B) = \mathbb{P}(A|B) \cdot \mathbb{P}(B)$

**In parole povere:** La probabilità che accadano sia A che B è uguale alla probabilità che accada B, _moltiplicata_ per la probabilità che accada A, _sapendo che B è già accaduto_.

Questo è FONDAMENTALE per tutti gli esercizi con estrazioni **senza reimmissione**.

#### Esercizio Guidato (simile a Esercizio 4c della scheda)

Un'urna contiene 3 palline bianche (B) e 2 nere (N). Si eseguono due estrazioni **senza reimmissione**.
**Domanda:** Qual è la probabilità di estrarre nell'ordine una pallina bianca e poi una nera?

**Passo 1: Definisci gli eventi in sequenza**

- Evento $B_1$: "la prima pallina estratta è bianca".
- Evento $N_2$: "la seconda pallina estratta è nera".

**Passo 2: Traduci la domanda in formula**
Vogliamo calcolare la probabilità che accadano entrambi gli eventi, cioè $\mathbb{P}(B_1 \cap N_2)$.
Usiamo la regola della catena: $\mathbb{P}(B_1 \cap N_2) = \mathbb{P}(N_2|B_1) \cdot \mathbb{P}(B_1)$

**Passo 3: Calcola i pezzi della formula**

- $\mathbb{P}(B_1)$: All'inizio ci sono 5 palline in totale, di cui 3 bianche.
  $\mathbb{P}(B_1) = \frac{3}{5}$

- $\mathbb{P}(N_2|B_1)$: Questa è la chiave. Dobbiamo calcolare la probabilità che la seconda sia nera, _sapendo che la prima era bianca_. Se la prima era bianca, cosa è rimasto nell'urna?
  - Palline totali: $5 - 1 = 4$
  - Palline nere: 2 (il loro numero non è cambiato)
    Quindi, $\mathbb{P}(N_2|B_1) = \frac{2}{4} = \frac{1}{2}$

**Passo 4: Moltiplica tutto**
$\mathbb{P}(B_1 \cap N_2) = \mathbb{P}(N_2|B_1) \cdot \mathbb{P}(B_1) = \frac{1}{2} \cdot \frac{3}{5} = \frac{3}{10}$

**Il Diagramma ad Albero:** Questo è il modo migliore per visualizzare questi problemi.

\begin{center}
\begin{tikzpicture}
\node (start) at (0,0) {Inizio};

% Prima estrazione
\node (B1) at (2,1) {B};
\node (N1) at (2,-1) {N};

% Seconda estrazione da B
\node (B1B2) at (4,1.5) {B};
\node (B1N2) at (4,0.5) {N};

% Seconda estrazione da N
\node (N1B2) at (4,-0.5) {B};
\node (N1N2) at (4,-1.5) {N};

% Rami prima estrazione
\draw (start) -- (B1) node[midway,above] {$\frac{3}{5}$};
\draw (start) -- (N1) node[midway,below] {$\frac{2}{5}$};

% Rami seconda estrazione
\draw (B1) -- (B1B2) node[midway,above] {$\frac{1}{2}$};
\draw (B1) -- (B1N2) node[midway,below] {$\frac{1}{2}$};
\draw (N1) -- (N1B2) node[midway,above] {$\frac{3}{4}$};
\draw (N1) -- (N1N2) node[midway,below] {$\frac{1}{4}$};

% Evidenzia il percorso B→N
\draw[red, thick] (start) -- (B1) -- (B1N2);

\end{tikzpicture}
\end{center}

Per trovare la probabilità di un percorso (es. "Bianca e poi Nera"), moltiplichi le probabilità lungo i rami.

---

### 3. Indipendenza: Eventi che si Fanno i Fatti Loro

#### Teoria Semplice e Necessaria

Due eventi A e B sono **indipendenti** se il verificarsi di uno non cambia la probabilità dell'altro.
Esempio: Lancio un dado e una moneta. L'esito del dado non ha alcuna influenza sull'esito della moneta.

Ci sono tre modi equivalenti per definire l'indipendenza (se $\mathbb{P}(A)>0$ e $\mathbb{P}(B)>0$):

1.  $\mathbb{P}(A|B) = \mathbb{P}(A)$ (Sapere B non cambia la probabilità di A)
2.  $\mathbb{P}(B|A) = \mathbb{P}(B)$ (Sapere A non cambia la probabilità di B)
3.  $\mathbb{P}(A \cap B) = \mathbb{P}(A) \cdot \mathbb{P}(B)$

La **terza formula è quella che userai sempre** negli esercizi per _verificare_ se due eventi sono indipendenti.

**ATTENZIONE: ERRORE COMUNE!**
Non confondere "eventi indipendenti" con "eventi disgiunti".

- **Disgiunti (o incompatibili):** Non possono accadere insieme. $A \cap B = \emptyset$. Esempio: in un lancio di dado, "esce 1" e "esce 6". Se esce 1, sai per certo che non può uscire 6. Sono fortemente **dipendenti**!
- **Indipendenti:** Possono accadere insieme, e il verificarsi di uno non influenza l'altro. Esempio: "esce un numero pari" e "esce un numero < 3". Vediamo...

#### Esercizio Guidato (simile a Esercizio 2b della scheda)

Si lancia un dado regolare a 6 facce. Siano:

- Evento A: "esce un numero pari" -> $A = \{2, 4, 6\}$
- Evento B: "esce un numero $\le 2$" -> $B = \{1, 2\}$
  **Domanda:** Gli eventi A e B sono indipendenti?

**Passo 1: Calcola $\mathbb{P}(A)$ e $\mathbb{P}(B)$**
$\mathbb{P}(A) = \frac{3}{6} = \frac{1}{2}$
$\mathbb{P}(B) = \frac{2}{6} = \frac{1}{3}$

**Passo 2: Calcola il prodotto $\mathbb{P}(A) \cdot \mathbb{P}(B)$**
$\mathbb{P}(A) \cdot \mathbb{P}(B) = \frac{1}{2} \cdot \frac{1}{3} = \frac{1}{6}$

**Passo 3: Calcola la probabilità dell'intersezione $\mathbb{P}(A \cap B)$**
$A \cap B = \{2\}$ (l'unico elemento in comune)
$\mathbb{P}(A \cap B) = \frac{1}{6}$

**Passo 4: Confronta i risultati**
Abbiamo trovato che $\mathbb{P}(A \cap B) = \frac{1}{6}$ e $\mathbb{P}(A) \cdot \mathbb{P}(B) = \frac{1}{6}$.
Poiché $\mathbb{P}(A \cap B) = \mathbb{P}(A) \cdot \mathbb{P}(B)$, **sì, gli eventi A e B sono indipendenti**.

**Indipendenza di più eventi:** Se hai tre eventi A, B, C, per dire che sono (mutuamente) indipendenti, devono valere TUTTE queste condizioni:

- $\mathbb{P}(A \cap B) = \mathbb{P}(A)\mathbb{P}(B)$
- $\mathbb{P}(A \cap C) = \mathbb{P}(A)\mathbb{P}(C)$
- $\mathbb{P}(B \cap C) = \mathbb{P}(B)\mathbb{P}(C)$
- $\mathbb{P}(A \cap B \cap C) = \mathbb{P}(A)\mathbb{P}(B)\mathbb{P}(C)$
  Devi verificarle tutte!

---

### 4. Formula delle Probabilità Totali e Formula di Bayes

Questi due sono una coppia potentissima e compaiono spesso insieme.

#### Teoria Semplice e Necessaria

**Formula delle Probabilità Totali**
La usi quando vuoi calcolare la probabilità di un evento A, ma è più facile calcolarla "a pezzi", attraverso diversi scenari.
Questi "scenari" devono essere una **partizione** dello spazio campionario. Una partizione è un insieme di eventi $H_1, H_2, \dots, H_n$ che sono:

1.  **Disgiunti:** $H_i \cap H_j = \emptyset$ (se accade uno, non può accadere l'altro)
2.  **Esaustivi:** $H_1 \cup H_2 \cup \dots \cup H_n = \Omega$ (coprono tutte le possibilità)

Esempio di partizione: nel lancio di un dado, gli eventi $H_1=\{1,2\}$, $H_2=\{3,4\}$, $H_3=\{5,6\}$ formano una partizione.

La formula è:
$\mathbb{P}(A) = \mathbb{P}(A|H_1)\mathbb{P}(H_1) + \mathbb{P}(A|H_2)\mathbb{P}(H_2) + \dots + \mathbb{P}(A|H_n)\mathbb{P}(H_n)$

**In parole povere:** La probabilità totale di A è la somma ponderata delle probabilità di A in ogni scenario, dove i pesi sono le probabilità degli scenari stessi.

**Formula di Bayes**
La usi per "invertire la condizione". Spesso conosci $\mathbb{P}(A|B)$ (la probabilità di un "effetto" data una "causa") ma vuoi trovare $\mathbb{P}(B|A)$ (la probabilità di una "causa" dato che hai osservato un "effetto"). L'esempio classico è il test medico (Esercizio 7).

La formula è:
$\mathbb{P}(H_i|A) = \frac{\mathbb{P}(A|H_i)\mathbb{P}(H_i)}{\mathbb{P}(A)}$

Dove il denominatore $\mathbb{P}(A)$ si calcola quasi sempre con la formula delle probabilità totali!

#### Esercizio Guidato (paradigma di Esercizio 5 e 7 della scheda)

Ci sono due urne.

- Urna 1 ($U_1$): contiene 2 palline rosse e 8 nere.
- Urna 2 ($U_2$): contiene 7 palline rosse e 3 nere.
  Si sceglie un'urna a caso (con probabilità $1/2$ ciascuna) e si estrae una pallina.

**Domanda (a): Qual è la probabilità che la pallina estratta sia rossa? (Probabilità Totali)**

**Passo 1: Definisci l'evento e la partizione**

- Evento A: "la pallina estratta è rossa" (R).
- Partizione: Gli scenari possibili. Sono "scelgo l'urna 1" ($U_1$) e "scelgo l'urna 2" ($U_2$). Sono disgiunti (non posso scegliere entrambe) ed esaustivi (devo scegliere una delle due).
  - $\mathbb{P}(U_1) = 1/2$
  - $\mathbb{P}(U_2) = 1/2$

**Passo 2: Calcola le probabilità condizionate dell'evento A rispetto alla partizione**

- $\mathbb{P}(R|U_1)$: Probabilità di estrarre una rossa, SAPENDO che sto usando l'urna 1.
  $\mathbb{P}(R|U_1) = \frac{2}{10}$
- $\mathbb{P}(R|U_2)$: Probabilità di estrarre una rossa, SAPENDO che sto usando l'urna 2.
  $\mathbb{P}(R|U_2) = \frac{7}{10}$

**Passo 3: Applica la Formula delle Probabilità Totali**
$\mathbb{P}(R) = \mathbb{P}(R|U_1)\mathbb{P}(U_1) + \mathbb{P}(R|U_2)\mathbb{P}(U_2)$
$\mathbb{P}(R) = \left(\frac{2}{10} \cdot \frac{1}{2}\right) + \left(\frac{7}{10} \cdot \frac{1}{2}\right) = \frac{2}{20} + \frac{7}{20} = \frac{9}{20} = 0.45$

**Domanda (b): Sapendo che è stata estratta una pallina rossa, qual è la probabilità che provenga dall'urna 1? (Bayes)**

**Passo 1: Traduci la domanda in formula di Bayes**
Abbiamo osservato l'effetto ("è uscita rossa", R) e vogliamo trovare la probabilità della causa ("proveniva dall'urna 1", $U_1$). Vogliamo calcolare $\mathbb{P}(U_1|R)$.
$\mathbb{P}(U_1|R) = \frac{\mathbb{P}(R|U_1)\mathbb{P}(U_1)}{\mathbb{P}(R)}$

**Passo 2: Raccogli i pezzi. Li abbiamo già calcolati tutti!**

- Numeratore: $\mathbb{P}(R|U_1)\mathbb{P}(U_1) = \frac{2}{10} \cdot \frac{1}{2} = \frac{2}{20} = \frac{1}{10}$
- Denominatore: $\mathbb{P}(R)$. L'abbiamo calcolato al punto (a)! $\mathbb{P}(R) = \frac{9}{20}$

**Passo 3: Calcola il risultato**
$\mathbb{P}(U_1|R) = \frac{1/10}{9/20} = \frac{1}{10} \cdot \frac{20}{9} = \frac{2}{9}$

**Interpretazione:** Inizialmente, la probabilità di aver scelto l'urna 1 era $1/2 = 0.5$. Dopo aver visto una pallina rossa, questa probabilità è scesa a $2/9 \approx 0.22$. È logico, perché l'urna 2 ha molte più probabilità di dare una pallina rossa. L'osservazione ha aggiornato la nostra conoscenza.

---

### Riassunto dei Punti Chiave da Ricordare

\begin{longtable}[]{@{}p{3cm}p{4cm}p{4cm}p{4.5cm}@{}}
\toprule
\textbf{Concetto} & \textbf{Formula Chiave} & \textbf{Quando si usa?} & \textbf{Parola Chiave nel Testo} \\
\midrule
\endhead
\textbf{Prob. Condizionata} & $\mathbb{P}(A|B) = \frac{\mathbb{P}(A \cap B)}{\mathbb{P}(B)}$ & Per calcolare una probabilità data un'informazione. & "sapendo che", "dato che" \\
\addlinespace
\textbf{Regola della Catena} & $\mathbb{P}(A \cap B) = \mathbb{P}(A|B)\mathbb{P}(B)$ & Per calcolare la probabilità di eventi in sequenza. & "estrazioni senza reimmissione", "prima... e poi..." \\
\addlinespace
\textbf{Indipendenza} & $\mathbb{P}(A \cap B) = \mathbb{P}(A)\mathbb{P}(B)$ & Per verificare se due eventi si influenzano. & "indipendenti", "non si influenzano", "con reimmissione" \\
\addlinespace
\textbf{Prob. Totali} & $\mathbb{P}(A) = \sum \mathbb{P}(A|H_i)\mathbb{P}(H_i)$ & Per calcolare la probabilità di un evento che dipende da scenari iniziali diversi. & Problemi in due fasi: prima si sceglie qualcosa (urna, dado, moneta), poi si fa un esperimento. \\
\addlinespace
\textbf{Formula di Bayes} & $\mathbb{P}(H_i|A) = \frac{\mathbb{P}(A|H_i)\mathbb{P}(H_i)}{\mathbb{P}(A)}$ & Per "invertire" la probabilità condizionata: trovare la probabilità della causa dato l'effetto. & "sapendo che si è verificato [l'effetto], qual è la probabilità che la causa sia stata..." \\
\bottomrule
\end{longtable}

### Consigli per lo Studio e Errori da Evitare

1.  **Disegna Sempre!** I diagrammi ad albero sono i tuoi migliori amici per i problemi con la regola della catena, probabilità totali e Bayes. Visualizzano tutti i percorsi e le probabilità.
2.  **Scrivi Chiaramente gli Eventi:** Prima di fare qualsiasi calcolo, definisci gli eventi con delle lettere (es. A = "esce pari", R1 = "prima estratta è rossa"). Questo ti salverà da confusioni terribili.
3.  **Indipendente $\neq$ Disgiunto:** Martellatelo in testa. Fai un esempio per entrambi e vedrai che sono quasi opposti. Se sono disgiunti (e non impossibili), sono per forza dipendenti.
4.  **Leggi Bene la Domanda di Bayes:** La parte più difficile è capire cosa ti viene chiesto di calcolare ($\mathbb{P}(A|B)$ o $\mathbb{P}(B|A)$?). La probabilità che cerchi è quella "a posteriori", dopo che l'evento si è verificato. L'informazione che "sai" va sempre dopo la barra `|`.
5.  **Il Denominatore di Bayes:** Ricorda che il denominatore della formula di Bayes è la probabilità "totale" dell'evento che hai osservato. Spesso devi calcolarla separatamente con la formula delle probabilità totali.
