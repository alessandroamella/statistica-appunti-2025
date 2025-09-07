# Calcolo Combinatorio e Variabili Aleatorie

## Parte 1: Calcolo Combinatorio e Spazi di Probabilità Finiti

#### Reminder: La Formula di Laplace

Quando un esperimento ha un numero finito di risultati e **tutti i risultati sono ugualmente probabili**, la probabilità di un evento A è data dalla **Formula di Laplace**:

$$
\mathbb{P}(A) = \frac{\text{Numero di casi favorevoli ad A}}{\text{Numero di casi possibili totali}} = \frac{|A|}{|\Omega|}
$$

Il problema non è tanto la formula della probabilità, ma **come contare** questi casi, specialmente quando sono migliaia o milioni. Qui entra in gioco il **calcolo combinatorio**.

#### Come Ragionare: Le Due Domande Chiave

Per risolvere quasi ogni esercizio di calcolo combinatorio, devi porti due domande fondamentali sull'esperimento che stai analizzando (es. estrarre palline, formare password, disporre persone):

1.  **L'ordine conta?** (Scegliere "Anna e Bruno" è diverso da scegliere "Bruno e Anna"?)
2.  **Le ripetizioni sono permesse?** (Posso usare lo stesso elemento più di una volta? Es. estrarre una pallina e rimetterla dentro).

A seconda della risposta, userai uno strumento diverso. Vediamoli tutti in una tabella riassuntiva che sarà la tua bussola.

\begin{table}[H]
\centering
\begin{tabular}{|l|p{5.5cm}|p{5.5cm}|}
\hline
\textbf{L'ORDINE} & \textbf{RIPETIZIONI AMMESSE} & \textbf{RIPETIZIONI NON AMMESSE} \\
\hline
\textbf{CONTA} &
\textbf{Disposizioni con Ripetizione} \newline
$DR_{n,k} = n^k$ &
\textbf{Disposizioni Semplici} \newline
$D_{n,k} = \frac{n!}{(n-k)!}$ \\
\hline
\textbf{NON CONTA} &
(Combinazioni con ripetizione, meno comuni) &
\textbf{Combinazioni Semplici} \newline
$C_{n,k} = \binom{n}{k} = \frac{n!}{k!(n-k)!}$ \\
\hline
\end{tabular}
\caption{Tabella riassuntiva del calcolo combinatorio}
\end{table}

- **n**: Il numero totale di elementi tra cui puoi scegliere (es. le 10 cifre da 0 a 9, le 52 carte del mazzo).
- **k**: Il numero di elementi che devi scegliere (es. le 6 cifre della combinazione, le 5 carte della mano di poker).

Ora analizziamo ogni caso con esempi pratici.

---

### 1. Disposizioni con Ripetizione (Ordine SÌ, Ripetizioni SÌ)

**Teoria Semplice:** Pensa a questo come a fare $k$ scelte consecutive e indipendenti. Ad ogni scelta, hai sempre $n$ opzioni disponibili, perché puoi riutilizzare gli elementi.

**Formula:** $DR_{n,k} = n^k$
_Spiegazione:_ Per la prima scelta hai $n$ possibilità. Per la seconda hai ancora $n$ possibilità. E così via, per $k$ volte. Il numero totale di modi è $n \times n \times ... \times n$ ($k$ volte), cioè $n^k$.

**Esempio Pratico (Esercizio 1):**
_Problema:_ Trovare la probabilità di aprire una cassaforte con una combinazione di 6 cifre al primo tentativo. E se fossero 6 lettere scelte tra X, Y, Z, W?

**Svolgimento (cifre):**

1.  **Identifica il modello:** Stiamo creando una sequenza di 6 cifre.
2.  **Poni le domande chiave:**
    - **L'ordine conta?** Certo! `123456` è diverso da `654321`.
    - **Le ripetizioni sono ammesse?** Sì, una combinazione può essere `111111`.
3.  **Scegli lo strumento:** Ordine SÌ, Ripetizioni SÌ $\rightarrow$ **Disposizioni con Ripetizione**.
4.  **Identifica n e k:**
    - $n$ = numero di elementi tra cui scegliere $\rightarrow$ le cifre da 0 a 9, quindi $n=10$.
    - $k$ = numero di scelte da fare $\rightarrow$ la lunghezza della combinazione, quindi $k=6$.
5.  **Calcola i casi possibili ($|\Omega|$):**
    $|\Omega| = DR_{10,6} = 10^6 = 1,000,000$. Ci sono un milione di combinazioni possibili.
6.  **Calcola i casi favorevoli ($|A|$):**
    L'evento A è "indovinare la combinazione". C'è solo **una** combinazione giusta. Quindi $|A| = 1$.
7.  **Calcola la probabilità:**
    $\mathbb{P}(A) = \frac{|A|}{|\Omega|} = \frac{1}{10^6}$.

**Svolgimento (lettere):**
Stessa logica, ma cambiano $n$ e $k$.

- $n$ = numero di lettere disponibili (X, Y, Z, W) $\rightarrow n=4$.
- $k$ = lunghezza della combinazione $\rightarrow k=6$.
- $|\Omega| = DR_{4,6} = 4^6 = 4096$.
- $\mathbb{P}(A) = \frac{1}{4^6} = \frac{1}{4096}$.

---

### 2. Disposizioni Semplici (Ordine SÌ, Ripetizioni NO)

**Teoria Semplice:** Simile al caso precedente, ma ogni volta che scegli un elemento, questo "sparisce" e non puoi sceglierlo di nuovo. Il numero di opzioni diminuisce ad ogni passo.

**Formula:** $D_{n,k} = n \cdot (n-1) \cdot (n-2) \cdot ... \cdot (n-k+1) = \frac{n!}{(n-k)!}$
_Spiegazione:_ Per la prima scelta hai $n$ opzioni. Per la seconda te ne restano $n-1$. Per la terza $n-2$, e così via fino alla $k$-esima scelta, per cui avrai $n-k+1$ opzioni.

**Esempio Pratico (Esercizio 2, parte 1):**
_Problema:_ Scommetto sui primi 5 classificati di una gara con 40 concorrenti, **precisandone l'ordine**. Qual è la probabilità di vincere?

**Svolgimento:**

1.  **Identifica il modello:** Formare una classifica dei primi 5.
2.  **Poni le domande chiave:**
    - **L'ordine conta?** Assolutamente sì, un podio (1°, 2°, 3°, ...) è ordinato.
    - **Le ripetizioni sono ammesse?** No, una persona non può arrivare contemporaneamente 1° e 2°.
3.  **Scegli lo strumento:** Ordine SÌ, Ripetizioni NO $\rightarrow$ **Disposizioni Semplici**.
4.  **Identifica n e k:**
    - $n$ = numero di concorrenti totali $\rightarrow n=40$.
    - $k$ = numero di posizioni in classifica $\rightarrow k=5$.
5.  **Calcola i casi possibili ($|\Omega|$):**
    $|\Omega| = D_{40,5} = 40 \times 39 \times 38 \times 37 \times 36 = 78,960,960$.
6.  **Calcola i casi favorevoli ($|A|$):**
    C'è solo **una** cinquina ordinata vincente. $|A|=1$.
7.  **Calcola la probabilità:**
    $\mathbb{P}(A) = \frac{1}{D_{40,5}} = \frac{1}{78,960,960} \approx 1.3 \times 10^{-8}$.

---

### 3. Combinazioni Semplici (Ordine NO, Ripetizioni NO)

**Teoria Semplice:** Questo è il caso più comune. Stai semplicemente scegliendo un **gruppo** di $k$ elementi da un insieme di $n$. Non ti interessa l'ordine in cui li scegli. Pensa a formare un comitato, una squadra, o a ricevere le carte in una mano di poker.

**Formula:** $C_{n,k} = \binom{n}{k} = \frac{D_{n,k}}{k!} = \frac{n!}{k!(n-k)!}$
_Spiegazione:_ Si parte dalle disposizioni semplici $D_{n,k}$ (che tengono conto dell'ordine). Poiché a noi l'ordine non interessa, dobbiamo dividere per il numero di modi in cui possiamo ordinare i $k$ elementi scelti. Questo numero è $k!$ (le permutazioni di $k$ elementi).

**Esempio Pratico (Esercizio 2, parte 2):**
_Problema:_ Scommetto sui nomi dei primi cinque, **senza precisarne l'ordine**. Qual è la probabilità di vincere?

**Svolgimento:**

1.  **Identifica il modello:** Scegliere un **gruppo** di 5 persone.
2.  **Poni le domande chiave:**
    - **L'ordine conta?** No, il problema lo dice esplicitamente ("senza precisarne l'ordine").
    - **Le ripetizioni sono ammesse?** No, sono persone diverse.
3.  **Scegli lo strumento:** Ordine NO, Ripetizioni NO $\rightarrow$ **Combinazioni Semplici**.
4.  **Identifica n e k:**
    - $n$ = numero di concorrenti totali $\rightarrow n=40$.
    - $k$ = numero di persone da scegliere nel gruppo $\rightarrow k=5$.
5.  **Calcola i casi possibili ($|\Omega|$):**
    $|\Omega| = C_{40,5} = \binom{40}{5} = \frac{40!}{5!(40-5)!} = \frac{40 \times 39 \times 38 \times 37 \times 36}{5 \times 4 \times 3 \times 2 \times 1} = 658,008$.
6.  **Calcola i casi favorevoli ($|A|$):**
    C'è solo **un** gruppo di 5 persone vincente. $|A|=1$.
7.  **Calcola la probabilità:**
    $\mathbb{P}(A) = \frac{1}{\binom{40}{5}} = \frac{1}{658,008} \approx 1.5 \times 10^{-6}$.

#### Esempio Complesso: Mettere Insieme i Pezzi (Esercizio 4)

Questo esercizio è perfetto perché confronta i vari metodi di estrazione.
_Problema:_ Urna con 3 palline Rosse (R) e 7 Bianche (B). Totale 10 palline. Estraiamo 4 palline. Calcolare la probabilità di ottenere esattamente 2 Rosse e 2 Bianche.

**Caso 1: Estrazione SIMULTANEA (o senza reimmissione e senza ordine)**
Questo è il caso più intuitivo. Pensa di mettere la mano nell'urna e tirare fuori 4 palline tutte insieme.

1.  **Calcolo casi possibili $|\Omega|$:** Stai scegliendo un gruppo di 4 palline da 10. L'ordine non conta.
    $|\Omega| = \binom{10}{4} = \frac{10 \cdot 9 \cdot 8 \cdot 7}{4 \cdot 3 \cdot 2 \cdot 1} = 210$.
2.  **Calcolo casi favorevoli $|A|$:** L'evento A è "scegliere 2R e 2B". Per costruire un caso favorevole devi fare due scelte:
    - Scegliere 2 Rosse dalle 3 disponibili: $\binom{3}{2} = 3$ modi.
    - E scegliere 2 Bianche dalle 7 disponibili: $\binom{7}{2} = \frac{7 \cdot 6}{2} = 21$ modi.
    - Per il principio di moltiplicazione, $|A| = \binom{3}{2} \times \binom{7}{2} = 3 \times 21 = 63$.
3.  **Probabilità:** $\mathbb{P}(A) = \frac{63}{210} = \frac{3}{10} = 30\%$.

---

#### PER CAPIRE LA MOLTIPLICAZIONE IN COMBINATORIA

**Il Problema Base**

Urna: 3 Rosse + 7 Bianche. Estraggo 4 palline, voglio 2R + 2B.

**Il Click Mentale: PRODOTTO CARTESIANO!**

**Non** sto separando fisicamente l'urna. Sto **classificando il risultato** dopo l'estrazione.

Per formare "2R + 2B" faccio 2 scelte indipendenti:

1. Scegliere 2 rosse dalle 3: $\binom{3}{2} = 3$ modi
2. Scegliere 2 bianche dalle 7: $\binom{7}{2} = 21$ modi

**Perché si moltiplicano?**

Ogni modo di scegliere rosse può combinarsi con OGNI modo di scegliere bianche:

```
{R1,R2} + tutte le 21 coppie bianche → 21 combinazioni
{R1,R3} + tutte le 21 coppie bianche → 21 combinazioni
{R2,R3} + tutte le 21 coppie bianche → 21 combinazioni

TOTALE: 3 × 21 = 63
```

**È un prodotto cartesiano:**

- **Insieme A** = {modi di scegliere rosse} = {{R1,R2}, {R1,R3}, {R2,R3}}
- **Insieme B** = {modi di scegliere bianche} = {{B1,B2}, {B1,B3}, ..., {B6,B7}}
- **A × B** = tutte le coppie (scelta_rosse, scelta_bianche)

**Schema Generale**

$$\binom{n_1}{k_1} \times \binom{n_2}{k_2} = \text{scegliere } k_1 \text{ dal tipo 1 E } k_2 \text{ dal tipo 2}$$

**La moltiplicazione in combinatoria = prodotto cartesiano travestito!**

Stesso principio delle password: 26 lettere per 3 posizioni = $26^3$ = {lettere} × {lettere} × {lettere}

---

**Caso 2: Estrazione SENZA REIMMISSIONE (con ordine)**
Qui estrai le 4 palline una dopo l'altra, senza rimetterle dentro. L'ordine conta.

1.  **Calcolo casi possibili $|\Omega|$:** Stai scegliendo una sequenza ordinata di 4 palline da 10.
    $|\Omega| = D_{10,4} = 10 \cdot 9 \cdot 8 \cdot 7 = 5040$.
2.  **Calcolo casi favorevoli $|A|$:** Questo è più complicato. Una sequenza favorevole ha 2R e 2B (es. RRBB, RBRB, ...).
    - **Passo A:** Scegli i 2 posti nella sequenza di 4 estrazioni in cui usciranno le Rosse. Ci sono $\binom{4}{2} = 6$ modi (RRBB, RBRB, RBBR, BRRB, BRBR, BBRR).
    - **Passo B:** Riempi i posti delle Rosse. Hai 3 Rosse da piazzare in 2 posti (in ordine): $D_{3,2} = 3 \cdot 2 = 6$ modi.
    - **Passo C:** Riempi i posti delle Bianche. Hai 7 Bianche da piazzare nei 2 posti rimanenti (in ordine): $D_{7,2} = 7 \cdot 6 = 42$ modi.
      $|A| = \binom{4}{2} \times D_{3,2} \times D_{7,2} = 6 \times 6 \times 42 = 1512$.
3.  **Probabilità:** $\mathbb{P}(A) = \frac{1512}{5040} = \frac{3}{10} = 30\%$.

**Osservazione chiave:** Il risultato è lo stesso! Quando l'estrazione è senza reimmissione, puoi scegliere se considerare l'ordine o no, purché tu sia coerente nel calcolo del numeratore e del denominatore. Scegliere il modello delle **combinazioni** (senza ordine) è quasi sempre più facile!

**Caso 3: Estrazione CON REIMMISSIONE (con ordine)**
Estrai le 4 palline una dopo l'altra, ma ogni volta la rimetti dentro.

1.  **Calcolo casi possibili $|\Omega|$:** Fai 4 scelte, e ad ogni scelta hai 10 palline disponibili.
    $|\Omega| = DR_{10,4} = 10^4 = 10000$.
2.  **Calcolo casi favorevoli $|A|$:** Simile al caso precedente, ma le scelte sono con ripetizione.
    - **Passo A:** Scegli i 2 posti per le Rosse: $\binom{4}{2}=6$ modi.
    - **Passo B:** Per ognuno dei 2 posti "Rossi", hai 3 possibili Rosse da estrarre: $DR_{3,2} = 3^2 = 9$ modi.
    - **Passo C:** Per ognuno dei 2 posti "Bianchi", hai 7 possibili Bianche: $DR_{7,2} = 7^2 = 49$ modi.
      $|A| = \binom{4}{2} \times 3^2 \times 7^2 = 6 \times 9 \times 49 = 2646$.
3.  **Probabilità:** $\mathbb{P}(A) = \frac{2646}{10000} = 0.2646 = 26.46\%$.

#### Riassunto Punti Chiave (Calcolo Combinatorio)

1.  **Formula di Base:** $\mathbb{P}(A) = |A| / |\Omega|$. Il tuo lavoro è contare $|A|$ e $|\Omega|$.
2.  **Le Domande Guida:** Chiediti sempre: **L'ordine conta? Le ripetizioni sono permesse?**
3.  **Scegli lo Strumento Giusto:** Usa la tabella per decidere tra Disposizioni (con/senza ripetizione) e Combinazioni.
4.  **Coerenza:** Se decidi di usare un modello ordinato (Disposizioni) per calcolare $|\Omega|$, devi usare un modello ordinato anche per $|A|$. Se usi le Combinazioni, fai lo stesso.
5.  **Il Metodo più Semplice:** Per estrazioni senza reimmissione, il modello delle **Combinazioni** è quasi sempre il più veloce e meno prono a errori.

#### Consigli per lo Studio e Errori da Evitare

- **Studia Così:** Prendi ogni esercizio della scheda e, prima ancora di fare i calcoli, scrivi a parole quale modello stai usando e perché (es. "Uso le combinazioni perché l'ordine delle carte in mano non conta e le carte sono tutte diverse").
- **Errore Comune 1: Confondere Disposizioni e Combinazioni.** È l'errore più grave. La differenza è l'ordine. Podio = Disposizione. Comitato = Combinazione.
- **Errore Comune 2: Dimenticare $\binom{k}{l}$ quando l'ordine non conta ma le estrazioni sì.** Nell'esercizio con reimmissione, un errore comune è calcolare solo $3^2 \times 7^2$ dimenticando di moltiplicare per $\binom{4}{2}$, che rappresenta tutti i modi in cui le 2 Rosse e 2 Bianche possono presentarsi (RRBB, RBRB, etc.).

---

## Parte 2: Variabili Aleatorie (Introduzione)

Ora passiamo alla parte più teorica. Qui non ci sono esercizi numerici nella tua scheda, ma i concetti sono le fondamenta di tutto ciò che verrà dopo.

#### L'Idea Fondamentale: Da "Eventi" a "Numeri"

Finora abbiamo parlato di "eventi", cioè frasi che possono essere vere o false.

- _Evento_: "Nel lancio di due dadi, la somma è 7". (Vero/Falso)

Una **variabile aleatoria (v.a.)** è un passo avanti. È una regola che associa un **numero** a ogni possibile risultato di un esperimento.

- _Variabile Aleatoria X_: "La somma dei risultati nel lancio di due dadi". (Può valere 2, 3, 4, ..., 12)

In pratica, traduciamo i risultati di un esperimento (che possono essere facce di dadi, colori di palline, etc.) in numeri reali, su cui possiamo fare calcoli.

**Definizione Formale Semplificata:**
Una v.a. $X$ è una funzione che va dallo spazio campionario $\Omega$ all'insieme dei numeri reali $\mathbb{R}$.
$$ X: \Omega \rightarrow \mathbb{R} $$

- **Esempio:** Lancio di due dadi.
  - Lo spazio campionario $\Omega$ è l'insieme delle 36 coppie: $\{(1,1), (1,2), ..., (6,6)\}$.
  - La v.a. $X$ = "somma dei due dadi" è una funzione. Ad esempio:
    - $X((1,1)) = 1+1=2$
    - $X((1,2)) = 1+2=3$
    - $X((4,5)) = 4+5=9$

#### Distribuzione e Funzione di Ripartizione (CDF)

Una volta che abbiamo una v.a., la domanda più importante è: **con quale probabilità assume i suoi valori?**

La **distribuzione (o legge) di probabilità** di $X$ è la descrizione completa di queste probabilità. Per esempio, per la somma dei dadi, potremmo scrivere:

- $\mathbb{P}(X=2) = \mathbb{P}(\{(1,1)\}) = 1/36$
- $\mathbb{P}(X=3) = \mathbb{P}(\{(1,2), (2,1)\}) = 2/36$
- ...e così via.

Questo può essere scomodo. Per questo si introduce uno strumento potentissimo: la **Funzione di Ripartizione** (o CDF - Cumulative Distribution Function), indicata con $F_X(x)$.

**Definizione:** La CDF calcola la probabilità che la variabile aleatoria $X$ assuma un valore **minore o uguale** a un certo numero $x$.

$$
F_X(x) = \mathbb{P}(X \le x)
$$

**Come Capirla con un Esempio:**
Prendiamo un solo dado. La v.a. $X$ è il risultato del lancio. Può valere {1, 2, 3, 4, 5, 6}. Calcoliamo la sua CDF, $F_X(x)$.

- Se $x=0.5$, qual è $F_X(0.5)$? È $\mathbb{P}(X \le 0.5)$. Ma il dado non può dare un risultato minore di 0.5, quindi la probabilità è 0.
- Se $x=1$, qual è $F_X(1)$? È $\mathbb{P}(X \le 1)$, che è solo $\mathbb{P}(X=1) = 1/6$.
- Se $x=1.5$, qual è $F_X(1.5)$? È $\mathbb{P}(X \le 1.5)$, che è ancora solo $\mathbb{P}(X=1) = 1/6$.
- Se $x=2$, qual è $F_X(2)$? È $\mathbb{P}(X \le 2)$, che include sia $X=1$ che $X=2$. Quindi $\mathbb{P}(X=1) + \mathbb{P}(X=2) = 1/6 + 1/6 = 2/6$.
- Se $x=6.5$, qual è $F_X(6.5)$? È $\mathbb{P}(X \le 6.5)$, che include tutti i possibili risultati del dado. La probabilità è 1.

Il grafico di questa CDF è una **funzione a gradini** (o a scala):

\begin{center}
\begin{tikzpicture}
\begin{axis}[
width=12cm,
height=8cm,
xlabel={$x$},
ylabel={$F_X(x)$},
title={CDF di un Dado},
xmin=-0.5, xmax=7,
ymin=-0.1, ymax=1.1,
grid=major,
grid style={dashed,gray!30},
axis lines=middle,
every axis x label/.style={at={(ticklabel* cs:1.05)},anchor=west},
every axis y label/.style={at={(ticklabel* cs:1.05)},anchor=south},
xtick={0,1,2,3,4,5,6,7},
ytick={0,0.167,0.333,0.5,0.667,0.833,1},
yticklabels={0,$1/6$,$2/6$,$3/6$,$4/6$,$5/6$,1},
legend pos=south east
]

% Funzione a gradini per la CDF
% Gradino da 0 a 1
\addplot[thick, blue, const plot mark left] coordinates {
(-0.5,0) (1,0) (1,0.167) (2,0.167) (2,0.333) (3,0.333) (3,0.5) (4,0.5) (4,0.667) (5,0.667) (5,0.833) (6,0.833) (6,1) (7,1)
};

% Punti pieni per i valori inclusi
\addplot[only marks, mark=*, mark size=2pt, blue] coordinates {
(1,0.167) (2,0.333) (3,0.5) (4,0.667) (5,0.833) (6,1)
};

% Punti vuoti per i valori esclusi (discontinuità)
\addplot[only marks, mark=o, mark size=2pt, blue] coordinates {
(1,0) (2,0.167) (3,0.333) (4,0.5) (5,0.667) (6,0.833)
};

\legend{$F_X(x)$}
\end{axis}
\end{tikzpicture}
\end{center}

**Proprietà Fondamentali della CDF (spiegate semplici):**

1.  **È crescente:** Man mano che `x` aumenta, la probabilità accumulata non può diminuire. $\mathbb{P}(X \le 5)$ non può essere minore di $\mathbb{P}(X \le 2)$.
2.  **Tende a 0 a sinistra:** Per valori di $x$ molto piccoli ($x \to -\infty$), la probabilità che $X$ sia minore di $x$ è 0.
3.  **Tende a 1 a destra:** Per valori di $x$ molto grandi ($x \to +\infty$), è certo che $X$ assumerà un valore minore di $x$, quindi la probabilità è 1.
4.  **È continua da destra:** Questa è una sottigliezza tecnica. Significa che il "pallino pieno" di ogni gradino è quello a sinistra.

#### A Cosa Serve la CDF? A Fare gli Esercizi!

La CDF è il tuo coltellino svizzero per calcolare la probabilità di qualsiasi intervallo.

- **Probabilità di essere minore o uguale:**
  $\mathbb{P}(X \le a) = F_X(a)$ (per definizione)

- **Probabilità di essere strettamente maggiore:**
  $\mathbb{P}(X > a) = 1 - \mathbb{P}(X \le a) = 1 - F_X(a)$

- **Probabilità di essere in un intervallo (il più usato!):**
  $\mathbb{P}(a < X \le b) = \mathbb{P}(X \le b) - \mathbb{P}(X \le a) = F_X(b) - F_X(a)$
  _Immaginalo:_ La probabilità fino a $b$ meno la probabilità fino ad $a$ ti lascia esattamente la probabilità tra $a$ e $b$.

- **Probabilità di assumere un valore esatto:**
  $\mathbb{P}(X=a) = F_X(a) - F_X(a^-)$
  Dove $F_X(a^-)$ è il valore della funzione un attimo prima di $a$. Questo valore è esattamente l'**altezza del salto** (del gradino) nel punto $a$. Se la funzione è continua in $a$ (non c'è un salto), allora $\mathbb{P}(X=a)=0$.

#### Riassunto Punti Chiave (Variabili Aleatorie)

1.  **Cos'è una v.a.?** Una regola che trasforma l'esito di un esperimento in un numero.
2.  **Cos'è la CDF?** $F_X(x) = \mathbb{P}(X \le x)$. È una funzione che "accumula" probabilità.
3.  **A cosa serve?** A calcolare la probabilità che $X$ cada in un qualsiasi intervallo, usando le formule del Teorema 2.2.
4.  **Grafico a Gradini:** Per le variabili che possono assumere solo valori specifici (come un dado), la CDF è una funzione a gradini. L'altezza di ogni gradino è la probabilità di quel singolo punto.

#### Consigli per lo Studio e Errori da Evitare

- **Studia Così:** Concentrati sul capire la definizione di CDF, $\mathbb{P}(X \le x)$. Ridisegna da solo il grafico a gradini per l'esempio del dado e usalo per calcolare $\mathbb{P}(2 < X \le 5)$. Vedrai che torna.
- **Errore Comune:** Confondere $\mathbb{P}(X < a)$ con $\mathbb{P}(X \le a)$. Per le variabili discrete (come il dado), non sono la stessa cosa! $\mathbb{P}(X < 3)$ è $\mathbb{P}(X=1) + \mathbb{P}(X=2)$, mentre $\mathbb{P}(X \le 3)$ è $\mathbb{P}(X=1)+\mathbb{P}(X=2)+\mathbb{P}(X=3)$. La CDF ti aiuta a gestire questa differenza con precisione.
