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

Un sistema ha 3 stati $S=\{1, 2, 3\}$. Le regole di evoluzione sono:

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

\begin{figure}[H]
\centering
\begin{tikzpicture}[->,>=stealth',shorten >=1pt,auto,node distance=3cm, semithick]

% Definizione dei nodi
\node[state] (1) {1};
\node[state] (2) [right of=1] {2};
\node[state] (3) [below right of=2] {3};
\node[state] (4) [below of=3] {4};
\node[state] (5) [left of=4] {5};
\node[state] (6) [below of=5] {6};

% Definizione degli archi con le probabilità
\path (1) edge [loop above] node {$\frac{1}{2}$} (1)
edge node {$\frac{1}{2}$} (2)
(2) edge node {$1$} (3)
(3) edge [bend left] node {$\frac{1}{3}$} (1)
edge node {$\frac{1}{3}$} (4)
edge [bend right] node {$\frac{1}{3}$} (5)
(4) edge [loop right] node {$\frac{1}{2}$} (4)
edge node {$\frac{1}{2}$} (5)
(5) edge node {$1$} (6)
(6) edge [bend left] node {$1$} (5);

\end{tikzpicture}
\caption{Grafo della catena di Markov corrispondente alla matrice $\Pi$}
\end{figure}

Il risultato è esattamente il grafo mostrato nelle soluzioni dell'Esercizio 1. Il grafo è il tuo migliore amico per risolvere gli esercizi!

---

### 4. Transizioni in Più Passi ($\pi_{ij}^{(m)}$): Viaggiare nel Futuro

Vogliamo calcolare la probabilità di andare da $i$ a $j$ in esattamente $m$ passi. Questa si indica con $\pi_{ij}^{(m)}$.

Ci sono due modi per calcolarla:

#### Metodo 1: Potenza di Matrice (Teorico)

Il teorema fondamentale dice che la matrice delle probabilità di transizione in $m$ passi è semplicemente la matrice $\Pi$ elevata alla $m$-esima potenza.
$\Pi^{(m)} = \Pi^m = \underbrace{\Pi \cdot \Pi \cdot \dots \cdot \Pi}_{m \text{ volte}}$
Questo metodo è computazionalmente pesante da fare a mano, ma è il concetto teorico. Lo userai solo se $m$ è piccolo (es. $m=2$) o se devi calcolare la distribuzione di $X_n$.

#### Metodo 2: Percorsi sul Grafo (Pratico per gli esercizi)

Questo è il metodo che userai il 99% delle volte in un esame.

1.  **Identifica i percorsi:** Sul grafo, trova **TUTTI** i percorsi di lunghezza **esattamente $m$** che partono da $i$ e arrivano a $j$. Un percorso di lunghezza $m$ ha $m$ frecce.
2.  **Calcola la probabilità di ogni percorso:** Per un singolo percorso, la sua probabilità è il **prodotto** delle probabilità su ogni freccia che lo compone.
3.  **Somma le probabilità:** La probabilità totale $\pi_{ij}^{(m)}$ è la **somma** delle probabilità di tutti i percorsi che hai trovato.

#### Esercizio Pratico (Esercizio 1c - Calcolare $\pi_{12}^{(4)}$)

Vogliamo andare da 1 a 2 in 4 passi. Usiamo il grafo dell'Esercizio 1.

#### Grafo Completo della Catena di Markov
\begin{figure}[H]
\centering
\begin{tikzpicture}[->,>=stealth',shorten >=1pt,auto,node distance=3cm,
semithick]

% Definizione dei nodi
\node[state,fill=red!20] (1) {\textbf{1}};
\node[state,fill=blue!20] (2) [right of=1] {\textbf{2}};
\node[state] (3) [below right of=2] {3};
\node[state] (4) [below of=3] {4};
\node[state] (5) [left of=4] {5};
\node[state] (6) [below of=5] {6};

% Definizione degli archi con le probabilità
\path (1) edge [loop above] node {$\frac{1}{2}$} (1)
edge node {$\frac{1}{2}$} (2)
(2) edge node {$1$} (3)
(3) edge [bend left] node {$\frac{1}{3}$} (1)
edge node {$\frac{1}{3}$} (4)
edge [bend right] node {$\frac{1}{3}$} (5)
(4) edge [loop right] node {$\frac{1}{2}$} (4)
edge node {$\frac{1}{2}$} (5)
(5) edge node {$1$} (6)
(6) edge [bend left] node {$1$} (5);

\end{tikzpicture}
\caption{Grafo completo - Nodo di partenza (1) in rosso, nodo di arrivo (2) in blu}
\end{figure}

#### Percorso 1: $1 \to 1 \to 1 \to 1 \to 2$
\begin{figure}[H]
\centering
\begin{tikzpicture}[->,>=stealth',shorten >=1pt,auto,node distance=3cm,
semithick]

% Nodi
\node[state,fill=red!30] (1) {\textbf{1}};
\node[state,fill=blue!30] (2) [right of=1] {\textbf{2}};
\node[state,opacity=0.3] (3) [below right of=2] {3};
\node[state,opacity=0.3] (4) [below of=3] {4};
\node[state,opacity=0.3] (5) [left of=4] {5};
\node[state,opacity=0.3] (6) [below of=5] {6};

% Archi del percorso in rosso spesso
\path (1) edge [loop above, line width=3pt, red] node[red] {\textbf{$\frac{1}{2}$}} (1)
edge [line width=3pt, red] node[red] {\textbf{$\frac{1}{2}$}} (2);

% Altri archi in grigio chiaro
\path[opacity=0.2] (2) edge node {$1$} (3)
(3) edge [bend left] node {$\frac{1}{3}$} (1)
edge node {$\frac{1}{3}$} (4)
edge [bend right] node {$\frac{1}{3}$} (5)
(4) edge [loop right] node {$\frac{1}{2}$} (4)
edge node {$\frac{1}{2}$} (5)
(5) edge node {$1$} (6)
(6) edge [bend left] node {$1$} (5);

\end{tikzpicture}
\caption{Percorso 1: Resta in 1 per 3 passi, poi va in 2}
\end{figure}

\textbf{Calcolo:} $\frac{1}{2} \times \frac{1}{2} \times \frac{1}{2} \times \frac{1}{2} = \frac{1}{16}$

#### Percorso 2: $1 \to 2 \to 3 \to 1 \to 2$
\begin{figure}[H]
\centering
\begin{tikzpicture}[->,>=stealth',shorten >=1pt,auto,node distance=3cm,
semithick]

% Nodi
\node[state,fill=red!30] (1) {\textbf{1}};
\node[state,fill=green!30] (2) [right of=1] {\textbf{2}};
\node[state,fill=green!30] (3) [below right of=2] {\textbf{3}};
\node[state,opacity=0.3] (4) [below of=3] {4};
\node[state,opacity=0.3] (5) [left of=4] {5};
\node[state,opacity=0.3] (6) [below of=5] {6};

% Archi del percorso in verde spesso
\path (1) edge [line width=3pt, green!70!black] node[green!70!black] {\textbf{$\frac{1}{2}$}} (2)
(2) edge [line width=3pt, green!70!black] node[green!70!black] {\textbf{$1$}} (3)
(3) edge [bend left, line width=3pt, green!70!black] node[green!70!black] {\textbf{$\frac{1}{3}$}} (1)
(1) edge [bend right=60, line width=3pt, blue] node[blue] {\textbf{$\frac{1}{2}$}} (2);

% Altri archi in grigio chiaro
\path[opacity=0.2] (1) edge [loop above] node {$\frac{1}{2}$} (1)
(3) edge node {$\frac{1}{3}$} (4)
edge [bend right] node {$\frac{1}{3}$} (5)
(4) edge [loop right] node {$\frac{1}{2}$} (4)
edge node {$\frac{1}{2}$} (5)
(5) edge node {$1$} (6)
(6) edge [bend left] node {$1$} (5);

\end{tikzpicture}
\caption{Percorso 2: $1 \to 2 \to 3 \to 1 \to 2$ (ultimo arco in blu)}
\end{figure}


\textbf{Calcolo:} $\frac{1}{2} \times 1 \times \frac{1}{3} \times \frac{1}{2} = \frac{1}{12}$

#### Risultato Finale

\begin{align*}
\pi_{12}^{(4)} &= \mathbb{P}\text{(Percorso 1)} + \mathbb{P}\text{(Percorso 2)}\\
&= \frac{1}{16} + \frac{1}{12}\\
&= \frac{3}{48} + \frac{4}{48}\\
&= \frac{7}{48}
\end{align*}

\textbf{Nota importante:} Abbiamo considerato TUTTI i possibili percorsi di lunghezza esattamente 4 che vanno da 1 a 2. Altri percorsi come $1 \to 2 \to 3 \to 4 \to \ldots$ non possono tornare al nodo 2 in esattamente 4 passi.


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

\

\textbf{Dati del Problema}
Data la matrice di transizione:

\begin{equation*}
\Pi = \begin{pmatrix} 
1/2 & 1/2 & 0 & 0 & 0 & 0 \\ 
0 & 0 & 1 & 0 & 0 & 0 \\ 
1/3 & 0 & 0 & 1/3 & 1/3 & 0 \\ 
0 & 0 & 0 & 1/2 & 1/2 & 0 \\ 
0 & 0 & 0 & 0 & 0 & 1 \\ 
0 & 0 & 0 & 0 & 1 & 0 
\end{pmatrix}
\end{equation*}

E la distribuzione iniziale:
\begin{equation*}
\vec{p}_{X_1} = \begin{pmatrix} 1/2 \\ 1/4 \\ 0 \\ 0 \\ 0 \\ 1/4 \end{pmatrix}^T = \left[\frac{1}{2}, \frac{1}{4}, 0, 0, 0, \frac{1}{4}\right]
\end{equation*}

\textbf{Obiettivo}: Calcolare $\mathbb{P}(X_3=2)$.

\

**Strategia Risolutiva**

Per trovare $\mathbb{P}(X_3=2)$, utilizziamo la formula:
\begin{equation*}
\vec{p}_{X_3} = \vec{p}_{X_1} \cdot \Pi^{3-1} = \vec{p}_{X_1} \cdot \Pi^{2}
\end{equation*}

La probabilità cercata sarà la seconda componente del vettore risultante.

\

**Calcolo delle Probabilità di Transizione a 2 Passi**

Invece di calcolare l'intera matrice $\Pi^2$, calcoliamo solo gli elementi necessari: $\pi_{i2}^{(2)}$ per tutti gli stati $i$.

\

**Analisi dei Percorsi**

Per raggiungere lo stato 2 in esattamente 2 passi da ogni stato:

\begin{align*}
\pi_{12}^{(2)} &: \text{Percorso } 1 \to 1 \to 2 \\
&= P(1 \to 1) \cdot P(1 \to 2) = \frac{1}{2} \cdot \frac{1}{2} = \frac{1}{4} \\
\pi_{22}^{(2)} &: \text{Da stato 2, si va necessariamente in 3} \\
&\text{Non esistono percorsi } 2 \to \cdot \to 2 \text{ in 2 passi} \\
&= 0 \\
\pi_{32}^{(2)} &: \text{Percorso } 3 \to 1 \to 2 \\
&= P(3 \to 1) \cdot P(1 \to 2) = \frac{1}{3} \cdot \frac{1}{2} = \frac{1}{6} \\
\pi_{42}^{(2)} &: \text{Dallo stato 4 non si può raggiungere lo stato 2} \\
&= 0 \\
\pi_{52}^{(2)} &: \text{Dallo stato 5 non si può raggiungere lo stato 2} \\
&= 0 \\
\pi_{62}^{(2)} &: \text{Dallo stato 6 non si può raggiungere lo stato 2} \\
&= 0
\end{align*}

\

**Matrice delle Probabilità a 2 Passi (Colonna 2)**

La seconda colonna di $\Pi^2$ è:
\begin{equation*}
\text{Colonna 2 di } \Pi^2 = \begin{pmatrix} 1/4 \\ 0 \\ 1/6 \\ 0 \\ 0 \\ 0 \end{pmatrix}
\end{equation*}

\

**Calcolo Finale**

Utilizzando la formula della probabilità totale:
\begin{align*}
\mathbb{P}(X_3=2) &= \sum_{i=1}^6 \mathbb{P}(X_1=i) \cdot \pi_{i2}^{(2)} \\
&= \vec{p}_{X_1} \cdot \text{(colonna 2 di } \Pi^2\text{)}
\end{align*}

Sostituendo i valori:
\begin{align*}
\mathbb{P}(X_3=2) &= \frac{1}{2} \cdot \frac{1}{4} + \frac{1}{4} \cdot 0 + 0 \cdot \frac{1}{6} + 0 \cdot 0 + 0 \cdot 0 + \frac{1}{4} \cdot 0 \\
&= \frac{1}{8} + 0 + 0 + 0 + 0 + 0 \\
&= \frac{1}{8}
\end{align*}

\

**Verifica del Calcolo**

Il calcolo può essere verificato attraverso:
\begin{equation*}
\begin{pmatrix} 1/2 & 1/4 & 0 & 0 & 0 & 1/4 \end{pmatrix} \begin{pmatrix} 1/4 \\ 0 \\ 1/6 \\ 0 \\ 0 \\ 0 \end{pmatrix} = \frac{1}{2} \cdot \frac{1}{4} = \frac{1}{8}
\end{equation*}

\

**Conclusione**

\begin{equation*}
\boxed{\mathbb{P}(X_3=2) = \frac{1}{8}}
\end{equation*}

\textbf{Nota}: Se nelle tue soluzioni compare il risultato $\frac{1}{6}$, potrebbe esserci un errore di stampa o un calcolo diverso. Il procedimento mostrato qui è matematicamente corretto seguendo la definizione standard delle catene di Markov.


---


\

**PER CAPIRE**

Vuoi $\mathbf{P(X_t = s)}$? Fai così:

\

**Step 1: Identifica**
\begin{itemize}
    \item $\mathbf{t}$ = tempo che vuoi
    \item $\mathbf{s}$ = stato che vuoi  
    \item $\mathbf{passi}$ = $t - 1$
\end{itemize}

\

**Step 2: Dal Grafico**

\begin{center}
\begin{tikzpicture}[
    node distance=3cm,
    state/.style={circle, draw, minimum size=1cm, font=\large},
    arrow/.style={->, >=stealth, thick}
]
    % Stati
    \node[state] (1) at (0,2) {1};
    \node[state] (2) at (3,2) {2};
    \node[state] (3) at (0,0) {3};
    \node[state] (4) at (3,0) {4};
    \node[state] (5) at (6,1) {5};
    \node[state] (6) at (1.5,-2) {6};
    
    % Transizioni con probabilità
    \draw[arrow] (1) edge[loop above] node[above] {$\frac{1}{2}$} (1);
    \draw[arrow] (1) -- (2) node[midway, above] {$\frac{1}{2}$};
    \draw[arrow] (3) -- (1) node[midway, left] {$\frac{1}{3}$};
    \draw[arrow] (3) -- (4) node[midway, below] {$\frac{1}{3}$};
    \draw[arrow] (3) -- (6) node[midway, below left] {$\frac{1}{3}$};
    \draw[arrow] (4) -- (5) node[midway, above right] {$1$};
    \draw[arrow] (5) edge[loop right] node[right] {$1$} (5);
    \draw[arrow] (6) edge[loop below] node[below] {$1$} (6);
\end{tikzpicture}
\end{center}

Per ogni stato di partenza $i = 1, 2, 3, 4, 5, 6$, calcola:
\begin{itemize}
    \item $\pi_{is}^{(\text{passi})}$ = probabilità di andare da $i$ a $s$ in ``passi'' passi
\end{itemize}

\

**Step 3: Fai il Vettore Colonna**

\begin{equation*}
\begin{bmatrix}
\pi_{1s}^{(\text{passi})} \\
\pi_{2s}^{(\text{passi})} \\
\pi_{3s}^{(\text{passi})} \\
\pi_{4s}^{(\text{passi})} \\
\pi_{5s}^{(\text{passi})} \\
\pi_{6s}^{(\text{passi})}
\end{bmatrix}
\end{equation*}

\

**Step 4: Moltiplicazione Scalare**
\begin{equation*}
\vec{p}_{X_1} \times \text{(vettore colonna)} = \text{risultato}
\end{equation*}

\

**Esempio: $P(X_3 = 2)$**

$\mathbf{t = 3, s = 2 \rightarrow \text{passi} = 2}$

Dal grafico, calcolo $\pi_{i2}^{(2)}$:
\begin{itemize}
    \item Da 1 a 2 in 2 passi: $1 \rightarrow 1 \rightarrow 2 = \left(\frac{1}{2}\right)\left(\frac{1}{2}\right) = \mathbf{\frac{1}{4}}$
    \item Da 2 a 2 in 2 passi: impossibile = $\mathbf{0}$
    \item Da 3 a 2 in 2 passi: $3 \rightarrow 1 \rightarrow 2 = \left(\frac{1}{3}\right)\left(\frac{1}{2}\right) = \mathbf{\frac{1}{6}}$
    \item Da 4 a 2 in 2 passi: impossibile = $\mathbf{0}$
    \item Da 5 a 2 in 2 passi: impossibile = $\mathbf{0}$
    \item Da 6 a 2 in 2 passi: impossibile = $\mathbf{0}$
\end{itemize}

\textbf{Vettore colonna:}
\begin{equation*}
\begin{bmatrix}
1/4 \\
0 \\
1/6 \\
0 \\
0 \\
0
\end{bmatrix}
\end{equation*}

\textbf{Moltiplicazione:}
\begin{equation*}
\begin{bmatrix} 1/2 & 1/4 & 0 & 0 & 0 & 1/4 \end{bmatrix} \times \begin{bmatrix} 1/4 \\ 0 \\ 1/6 \\ 0 \\ 0 \\ 0 \end{bmatrix} = \frac{1}{8}
\end{equation*}

\

**Schema Veloce**

\begin{center}
\begin{tikzpicture}[node distance=1.5cm]
    \node (start) {$P(X_t = s)$};
    \node (step1) [below of=start] {$t-1$ passi dal grafico};
    \node (step2) [below of=step1] {Vettore colonna};  
    \node (step3) [below of=step2] {Prodotto scalare};
    
    \draw[->] (start) -- (step1);
    \draw[->] (step1) -- (step2);
    \draw[->] (step2) -- (step3);
\end{tikzpicture}
\end{center}

\vspace{1cm}
\begin{center}
\textbf{\Large Fine. Basta così.}
\end{center}

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

#### Esercizio Pratico (Esercizio 2)

---

# Esercizio 2

Si consideri una catena di Markov $(X_n)_n$ con spazio degli stati $\mathcal{S} = \{1, 2, 3, 4, 5\}$ e matrice di transizione

$$\Pi = \begin{pmatrix}
1/2 & 0 & 0 & 0 & 1/2 \\
0 & 1/2 & 0 & 1/2 & 0 \\
0 & 0 & 1 & 0 & 0 \\
0 & 1/4 & 1/4 & 1/4 & 1/4 \\
1/2 & 0 & 0 & 0 & 1/2
\end{pmatrix}$$

(a) Rappresentare graficamente la catena di Markov tramite un grafo orientato.

(b) Determinare le classi comunicanti.

(c) Calcolare $\pi_{45}^{(3)}$.

(d) Calcolare $\mathbb{P}(X_2 = 4)$ sapendo che la densità discreta di $X_1$ è data da

$$\begin{array}{c|c|c|c|c|c}
X_1 & 1 & 2 & 3 & 4 & 5 \\
\hline
\vec{p}_{X_1} & 1/3 & 0 & 1/3 & 1/3 & 0
\end{array}$$

**Grafo della Catena di Markov**

\begin{center}
\begin{tikzpicture}[
    > = stealth,
    shorten > = 1pt,
    auto,
    node distance = 3cm,
    semithick
]

% Nodi
\node[state] (1) {1};
\node[state] (2) [right=of 1] {2};
\node[state] (3) [right=of 2] {3};
\node[state] (4) [below=of 2] {4};
\node[state] (5) [below=of 1] {5};

% Archi con probabilità
\path[->] 
    (1) edge [loop above] node {$\frac{1}{2}$} (1)
    (1) edge [bend left] node {$\frac{1}{2}$} (5)
    (2) edge [loop above] node {$\frac{1}{2}$} (2)
    (2) edge node {$\frac{1}{2}$} (4)
    (3) edge [loop above] node {$1$} (3)
    (4) edge node {$\frac{1}{4}$} (2)
    (4) edge node {$\frac{1}{4}$} (3)
    (4) edge [loop right] node {$\frac{1}{4}$} (4)
    (4) edge node {$\frac{1}{4}$} (5)
    (5) edge [bend left] node {$\frac{1}{2}$} (1)
    (5) edge [loop below] node {$\frac{1}{2}$} (5);

\end{tikzpicture}
\end{center}

**Analisi delle Classi Comunicanti**

Dalla matrice di transizione e dal grafo possiamo identificare:

- **Stato 3**: È uno stato assorbente (probabilità 1 di rimanere in 3)
- **Stati {1, 5}**: Formano una classe comunicante (si può passare da 1 a 5 e viceversa)
- **Stati {2, 4}**: Formano una classe comunicante (si può passare da 2 a 4 e viceversa)

Le **classi comunicanti** sono:

1. $\{1, 5\}$ - classe transitoria
2. $\{2, 4\}$ - classe transitoria
3. $\{3\}$ - classe assorbente

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

**Distribuzione Invariante - Esempio Guidato**

#### Il Problema
Consideriamo una catena di Markov con 3 stati {1, 2, 3} e matrice di transizione:

$$\Pi = \begin{pmatrix}
0.2 & 0.5 & 0.3 \\
0.4 & 0.1 & 0.5 \\
0.6 & 0.3 & 0.1
\end{pmatrix}$$

**Vogliamo trovare** la distribuzione invariante $\vec{v} = (v_1, v_2, v_3)$.

#### Passo 1: Impostiamo l'equazione $\vec{v} = \vec{v}\Pi$

Scriviamo esplicitamente cosa significa:
$$(v_1, v_2, v_3) = (v_1, v_2, v_3) \begin{pmatrix}
0.2 & 0.5 & 0.3 \\
0.4 & 0.1 & 0.5 \\
0.6 & 0.3 & 0.1
\end{pmatrix}$$

Facendo il prodotto riga per colonna:

- $v_1 = 0.2v_1 + 0.4v_2 + 0.6v_3$ (prima componente)
- $v_2 = 0.5v_1 + 0.1v_2 + 0.3v_3$ (seconda componente)
- $v_3 = 0.3v_1 + 0.5v_2 + 0.1v_3$ (terza componente)

#### Passo 2: Riorganizziamo il sistema

Portiamo tutto a sinistra:

- $v_1 - 0.2v_1 - 0.4v_2 - 0.6v_3 = 0$ → $0.8v_1 - 0.4v_2 - 0.6v_3 = 0$
- $v_2 - 0.5v_1 - 0.1v_2 - 0.3v_3 = 0$ → $-0.5v_1 + 0.9v_2 - 0.3v_3 = 0$
- $v_3 - 0.3v_1 - 0.5v_2 - 0.1v_3 = 0$ → $-0.3v_1 - 0.5v_2 + 0.9v_3 = 0$

**Sistema:**

$$\begin{cases}
0.8v_1 - 0.4v_2 - 0.6v_3 = 0 \quad (1)\\
-0.5v_1 + 0.9v_2 - 0.3v_3 = 0 \quad (2)\\
-0.3v_1 - 0.5v_2 + 0.9v_3 = 0 \quad (3)
\end{cases}$$

#### Passo 3: Una equazione è superflua!

**Insight importante:** Se sommi tutte e tre le equazioni originali ottieni $0 = 0$, quindi una è dipendente dalle altre.

Buttiamo via l'equazione (3) e sostituiamola con il vincolo di normalizzazione:
$$v_1 + v_2 + v_3 = 1 \quad (4)$$

**Nuovo sistema:**

$$\begin{cases}
0.8v_1 - 0.4v_2 - 0.6v_3 = 0 \quad (1)\\
-0.5v_1 + 0.9v_2 - 0.3v_3 = 0 \quad (2)\\
v_1 + v_2 + v_3 = 1 \quad (4)
\end{cases}$$

#### Passo 4: Risolviamo il sistema

Dall'equazione (4): $v_3 = 1 - v_1 - v_2$

Sostituiamo nelle prime due equazioni:

**Equazione (1):**

\begin{align*}
0.8v_1 - 0.4v_2 - 0.6(1 - v_1 - v_2) &= 0 \\
0.8v_1 - 0.4v_2 - 0.6 + 0.6v_1 + 0.6v_2 &= 0 \\
1.4v_1 + 0.2v_2 &= 0.6
\end{align*}

**Equazione (2):**

\begin{align*}
-0.5v_1 + 0.9v_2 - 0.3(1 - v_1 - v_2) &= 0 \\
-0.5v_1 + 0.9v_2 - 0.3 + 0.3v_1 + 0.3v_2 &= 0 \\
-0.2v_1 + 1.2v_2 &= 0.3
\end{align*}

**Risolvendo il sistema 2×2:**

- Da (A): $v_2 = 3 - 7v_1$
- Sostituendo in (B): $-2v_1 + 12(3 - 7v_1) = 3$
- $-2v_1 + 36 - 84v_1 = 3$
- $-86v_1 = -33$
- $v_1 = \frac{33}{86}$

Quindi:
$v_2 = 3 - 7 \cdot \frac{33}{86} = 3 - \frac{231}{86} = \frac{258-231}{86} = \frac{27}{86}$

$v_3 = 1 - v_1 - v_2 = 1 - \frac{33}{86} - \frac{27}{86} = \frac{86-33-27}{86} = \frac{26}{86}$

#### Risultato Finale

La distribuzione invariante è:
$$\vec{v} = \left(\frac{33}{86}, \frac{27}{86}, \frac{26}{86}\right) \approx (0.384, 0.314, 0.302)$$

#### Verifica
Controlliamo che $\vec{v}\Pi = \vec{v}$:

- $v_1 = 0.2 \cdot \frac{33}{86} + 0.4 \cdot \frac{27}{86} + 0.6 \cdot \frac{26}{86} = \frac{6.6 + 10.8 + 15.6}{86} = \frac{33}{86}$ $\checkmark$
- $v_2 = 0.5 \cdot \frac{33}{86} + 0.1 \cdot \frac{27}{86} + 0.3 \cdot \frac{26}{86} = \frac{16.5 + 2.7 + 7.8}{86} = \frac{27}{86}$ $\checkmark$

**Interpretazione:** A lungo termine, il sistema trascorrerà circa il 38.4% del tempo nello stato 1, il 31.4% nello stato 2, e il 30.2% nello stato 3.

#### Trucchi Pratici

1. **Semplifica le frazioni** moltiplicando tutto per un numero conveniente
2. **Verifica sempre** che la somma delle componenti sia 1
3. **Controlla** che $\vec{v}\Pi = \vec{v}$ su almeno una componente
4. Se i calcoli diventano troppo brutti, ricontrolla i passaggi algebrici!

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

---

\textbf{Esercizio 11.} Giovanni salta su tre piastrelle, numerate da 1 a 3. Inizialmente si trova sulla piastrella 1. A ogni istante lancia una moneta che dà testa con probabilità $\frac{1}{3}$: se esce testa salta sulla piastrella successiva, se esce croce su quella precedente (intendendo che il successivo di 3 è 1 e, analogamente, il precedente di 1 è 3). Si rappresenti il moto aleatorio di Giovanni mediante una catena di Markov $(X_n)_n$.

\begin{enumerate}
    \item Si scriva la matrice di transizione, se ne disegni il grafo, si determinino le classi di equivalenza e se ne determini il periodo.
    \item Si calcolino $\lim_{n \to \infty} \mathbb{P}(X_n = 2)$ e $\lim_{n \to \infty} \mathbb{P}(X_n = 2, X_{n+1} = 3)$.
\end{enumerate}

---

- La catena ha $S=\{1,2,3\}$ ed è irriducibile. Lo stato 1 ha periodo $d=MCD\{2,3,\dots\}=1$ perché si può tornare in 2 passi ($1\to 2\to 1$) e in 3 passi ($1\to 2\to 3\to 1$). Quindi è anche aperiodica.
- Possiamo applicare il teorema ergodico!
- Ci chiede di calcolare $\lim_{n \to \infty} \mathbb{P}(X_n = 2)$. Per il teorema, questo limite è semplicemente $v_2$, la seconda componente della distribuzione invariante.

**Calcoliamo $\vec{v}$:**

\begin{align*}
\Pi = \begin{pmatrix} 0 & 2/3 & 1/3 \\ 1/3 & 0 & 2/3 \\ 2/3 & 1/3 & 0 \end{pmatrix}
\end{align*}

Sistema $\vec{v} = \vec{v}\Pi$:

1.  $v_1 = \frac{1}{3}v_2 + \frac{2}{3}v_3$
2.  $v_2 = \frac{2}{3}v_1 + \frac{1}{3}v_3$
3.  $v_3 = \frac{1}{3}v_1 + \frac{2}{3}v_2$
4.  $v_1+v_2+v_3 = 1$

- Se provi a risolvere le prime 3, vedrai che una è ridondante. Usiamo la 1, la 2 e la 4. Sostituendo e risolvendo (è un po' di algebra), si trova la soluzione (che in questo caso, data la simmetria, è facile intuire):

- $\vec{v} = [1/3, 1/3, 1/3]$
- Quindi, il limite richiesto è $v_2 = 1/3$.

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
