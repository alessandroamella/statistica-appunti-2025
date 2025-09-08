# Variabili Aleatorie Discrete

### 1. Cosa sono le Variabili Aleatorie Discrete (V.A.D.)?

**Teoria Semplice**

Una **variabile aleatoria** è **discreta** se i valori che può assumere sono un numero finito o un'infinità numerabile (cioè, li puoi contare: 0, 1, 2, 3,... ma non i numeri con la virgola come 1.5, 2.78, ecc.).

Per descrivere una v.a. discreta, ci servono due cose:

1.  **Supporto ($S_X$)**: L'insieme di tutti i valori che la variabile $X$ può assumere.
    - _Esempio_: Se $X$ è il risultato del lancio di un dado, $S_X = \{1, 2, 3, 4, 5, 6\}$.
2.  **Funzione di massa di probabilità (PMF o $p_X(x)$)**: È la funzione che ci dice "qual è la probabilità che la mia variabile $X$ assuma proprio il valore $x$?". Si scrive $p_X(x) = \mathbb{P}(X=x)$.

**Le due regole d'oro della PMF:**

1.  Ogni probabilità deve essere non-negativa: $p_X(x_i) \ge 0$ per ogni valore $x_i$ nel supporto.
2.  La somma di tutte le probabilità deve fare 1: $\sum_{x_i \in S_X} p_X(x_i) = 1$. (Questo è FONDAMENTALE per esercizi come l'Esercizio 2).

**Esempio Pratico (Esercizio 1.1 dalla teoria)**

Lanciamo due dadi. Sia $X$ = "minimo tra i due risultati". Dobbiamo trovare il supporto e la PMF di $X$.

1.  **Trovare il Supporto ($S_X$)**: Quali valori può assumere il minimo? Se esce (1,1) il minimo è 1. Se esce (6,6) il minimo è 6. Può assumere tutti i valori interi in mezzo.
    $S_X = \{1, 2, 3, 4, 5, 6\}$.

2.  **Trovare la PMF ($p_X(x)$)**: Calcoliamo la probabilità per ogni valore del supporto. I possibili esiti del lancio di due dadi sono $6 \times 6 = 36$.

    - **$\mathbb{P}(X=1)$**: Quando il minimo è 1? Se almeno uno dei due dadi è 1.

      - Coppie: (1,1), (1,2), (1,3), (1,4), (1,5), (1,6) e (2,1), (3,1), (4,1), (5,1), (6,1).
      - Sono 11 coppie. Quindi $p_X(1) = \frac{11}{36}$.

    - **$\mathbb{P}(X=2)$**: Quando il minimo è 2? Se almeno un dado è 2, e l'altro è $\ge 2$.

      - Coppie: (2,2), (2,3), (2,4), (2,5), (2,6) e (3,2), (4,2), (5,2), (6,2).
      - Sono 9 coppie. Quindi $p_X(2) = \frac{9}{36}$.

    - **$\mathbb{P}(X=3)$**: Minimo è 3. L'altro dado $\ge 3$.

      - Coppie: (3,3), (3,4), (3,5), (3,6) e (4,3), (5,3), (6,3).
      - Sono 7 coppie. Quindi $p_X(3) = \frac{7}{36}$.

    - **$\mathbb{P}(X=4)$**: Minimo è 4. L'altro dado $\ge 4$.

      - Coppie: (4,4), (4,5), (4,6) e (5,4), (6,4).
      - Sono 5 coppie. Quindi $p_X(4) = \frac{5}{36}$.

    - **$\mathbb{P}(X=5)$**: Minimo è 5. L'altro dado $\ge 5$.

      - Coppie: (5,5), (5,6) e (6,5).
      - Sono 3 coppie. Quindi $p_X(5) = \frac{3}{36}$.

    - **$\mathbb{P}(X=6)$**: Minimo è 6.
      - Coppia: (6,6)
      - È 1 coppia. Quindi $p_X(6) = \frac{1}{36}$.

**Tabella della densità discreta (PMF):**

| $x$      | 1       | 2      | 3      | 4      | 5      | 6      |
| :------- | :------ | :----- | :----- | :----- | :----- | :----- |
| $p_X(x)$ | $11/36$ | $9/36$ | $7/36$ | $5/36$ | $3/36$ | $1/36$ |

**Verifica della regola d'oro**: $\frac{11+9+7+5+3+1}{36} = \frac{36}{36} = 1$. Funziona!

---

### 2. La Funzione di Ripartizione (CDF)

**Teoria Semplice**

Per una v.a. discreta, la CDF è una **funzione a gradini** (costante a tratti). Rimane piatta e poi, in corrispondenza di un valore $x_i$ del supporto, fa un "salto" verso l'alto.

**Concetto CHIAVE per gli esercizi**: L'altezza del salto in un punto $x_i$ è esattamente la probabilità $p_X(x_i)$.
$p_X(x_i) = F_X(x_i) - \lim_{x \to x_i^-} F_X(x)$ (cioè, il valore della funzione nel punto, meno il valore subito prima).

Questo ti permette di passare dalla CDF alla PMF, che è esattamente quello che chiede l'**Esercizio 1**.

**Esercizio Svolto: Esercizio 1 dalla scheda**

Sia $X$ una v.a. con funzione di ripartizione:
$F_X(x) = \begin{cases} 0 & \text{se } x < 0 \\ 1/2 & \text{se } 0 \le x < 1 \\ 3/4 & \text{se } 1 \le x < 4 \\ 1 & \text{se } x \ge 4 \end{cases}$

**(a) X è una v.a. discreta?**
Sì. La sua funzione di ripartizione $F_X(x)$ è costante a tratti (una funzione a gradini). Questo è il segnale inequivocabile di una v.a. discreta.

**(b) Determinare supporto e densità discreta di X.**

1.  **Trovare il Supporto ($S_X$)**: Il supporto è l'insieme dei punti dove la CDF "salta".

    - In $x=0$, la funzione salta da 0 a 1/2. Quindi $0 \in S_X$.
    - In $x=1$, la funzione salta da 1/2 a 3/4. Quindi $1 \in S_X$.
    - In $x=4$, la funzione salta da 3/4 a 1. Quindi $4 \in S_X$.
    - **Supporto**: $S_X = \{0, 1, 4\}$.

2.  **Trovare la PMF ($p_X(x)$)**: Calcoliamo l'altezza di ogni salto.

    - $p_X(0) = \mathbb{P}(X=0) = F_X(0) - (\text{valore prima di 0}) = 1/2 - 0 = 1/2$.
    - $p_X(1) = \mathbb{P}(X=1) = F_X(1) - (\text{valore prima di 1}) = 3/4 - 1/2 = 1/4$.
    - $p_X(4) = \mathbb{P}(X=4) = F_X(4) - (\text{valore prima di 4}) = 1 - 3/4 = 1/4$.

      **Tabella della PMF**:

    | $x$      | 0     | 1     | 4     |
    | :------- | :---- | :---- | :---- |
    | $p_X(x)$ | $1/2$ | $1/4$ | $1/4$ |

    - Verifica: $1/2 + 1/4 + 1/4 = 1$. Corretto.

**(c) Calcolare $\mathbb{P}(X < 4)$, $\mathbb{P}(X \le 3)$ e $\mathbb{P}(X = 1)$.**

- **$\mathbb{P}(X < 4)$**: La probabilità che $X$ assuma un valore _strettamente minore_ di 4. Guardando il supporto, i valori possibili sono 0 e 1.
  $\mathbb{P}(X < 4) = \mathbb{P}(X=0) + \mathbb{P}(X=1) = p_X(0) + p_X(1) = 1/2 + 1/4 = 3/4$.

- **$\mathbb{P}(X \le 3)$**: La probabilità che $X$ sia minore o uguale a 3. Per definizione, questa è proprio la CDF calcolata in 3!
  $\mathbb{P}(X \le 3) = F_X(3)$. Guardando la definizione di $F_X(x)$, per $1 \le x < 4$, la funzione vale $3/4$. Quindi $F_X(3) = 3/4$.

- **$\mathbb{P}(X = 1)$**: Questa è la PMF calcolata in 1. L'abbiamo già trovata.
  $\mathbb{P}(X=1) = p_X(1) = 1/4$.

**(d) Qual è il valore atteso di X?** Lo calcoliamo nel prossimo punto.

---

### 3. Indici Fondamentali: Valore Atteso e Varianza

**Teoria Semplice**

Una volta che hai la PMF, puoi calcolare due numeri che riassumono la tua variabile:

1.  **Valore Atteso (o Media, $E[X]$)**: È il valore "medio" che ti aspetti di ottenere se ripetessi l'esperimento tante volte. È una media pesata dei valori, dove i pesi sono le probabilità.

    - **Formula**: $E[X] = \mu = \sum_{x_i \in S_X} x_i \cdot p_X(x_i)$
    - _In parole povere_: moltiplichi ogni valore per la sua probabilità e sommi tutto.

2.  **Varianza ($Var(X)$)**: Misura quanto i valori della variabile tendono a disperdersi o "variare" attorno alla media. Una varianza bassa significa che i valori sono molto concentrati vicino alla media. Una varianza alta significa che sono sparpagliati.

    **Formula di calcolo (la più comoda!)**: $Var(X) = \sigma^2 = E[X^2] - (E[X])^2$

    - **Come si usa**:

      1.  Calcoli $E[X]$ come prima.
      2.  Calcoli $E[X^2]$. La formula è simile a quella di $E[X]$, ma elevi al quadrato i valori $x_i$: $E[X^2] = \sum_{x_i \in S_X} x_i^2 \cdot p_X(x_i)$.
      3.  Applichi la formula della varianza.

    - **Proprietà utili della varianza**:

      1.  **Costanti**: $Var(c) = 0$ (le costanti non variano!)
      2.  **Moltiplicazione per costante**: $Var(cX) = c^2 \cdot Var(X)$

**Deviazione Standard ($\sigma_X$)**: È semplicemente la radice quadrata della varianza: $\sigma_X = \sqrt{Var(X)}$. Ha il vantaggio di avere la stessa unità di misura di $X$.

**Esercizio Svolto: Esercizio 3 dalla scheda**

Data la PMF:
\begin{table}[h]
\centering
\begin{tabular}{|c|c|c|c|c|c|c|c|}
\hline
$x$ & 1 & 2 & 3 & 4 & 5 & 6 & 7 \\
\hline
$p_X(x)$ & 0.02 & 0.03 & 0.09 & 0.25 & 0.40 & 0.16 & 0.05 \\
\hline
\end{tabular}
\end{table}

**(c) Calcolare valore atteso e deviazione standard di X.**

1.  **Calcolo del Valore Atteso ($E[X]$)**:
    $E[X] = (1 \cdot 0.02) + (2 \cdot 0.03) + (3 \cdot 0.09) + (4 \cdot 0.25) + (5 \cdot 0.40) + (6 \cdot 0.16) + (7 \cdot 0.05)$
    $= 0.02 + 0.06 + 0.27 + 1.00 + 2.00 + 0.96 + 0.35$
    $= 4.66$

2.  **Calcolo di $E[X^2]$**:
    $E[X^2] = (1^2 \cdot 0.02) + (2^2 \cdot 0.03) + (3^2 \cdot 0.09) + (4^2 \cdot 0.25) + (5^2 \cdot 0.40) + (6^2 \cdot 0.16) + (7^2 \cdot 0.05)$
    $= (1 \cdot 0.02) + (4 \cdot 0.03) + (9 \cdot 0.09) + (16 \cdot 0.25) + (25 \cdot 0.40) + (36 \cdot 0.16) + (49 \cdot 0.05)$
    $= 0.02 + 0.12 + 0.81 + 4.00 + 10.00 + 5.76 + 2.45$
    $= 23.16$

3.  **Calcolo della Varianza ($Var(X)$)**:
    $Var(X) = E[X^2] - (E[X])^2 = 23.16 - (4.66)^2$
    $= 23.16 - 21.7156 = 1.4444$

4.  **Calcolo della Deviazione Standard ($\sigma_X$)**:
    $\sigma_X = \sqrt{Var(X)} = \sqrt{1.4444} \approx 1.20$

---

### 4. Trasformazioni di Variabili Aleatorie

**Teoria Semplice**

A volte ci viene data una variabile $X$ e ci viene chiesta la legge di una nuova variabile $Y$ che è una funzione di $X$, ad esempio $Y = X^2$ o $Y = \sqrt{X}$.
Come si trova la PMF di $Y$?

1.  **Trova il supporto di Y ($S_Y$)**: Applica la funzione a tutti i valori del supporto di $X$. Se ottieni dei duplicati, li consideri una volta sola.
2.  **Trova la PMF di Y ($p_Y(y)$)**: Per ogni valore $y$ nel supporto di $Y$, la sua probabilità è la somma delle probabilità di tutti i valori $x$ di $X$ che lo generano.
    $p_Y(y) = \mathbb{P}(Y=y) = \sum_{x: g(x)=y} \mathbb{P}(X=x)$

**Esercizio Svolto: Esercizio 4 dalla scheda**

Data $X$ con CDF: $F_X(x) = \begin{cases} 0 & x < 0 \\ 1/3 & 0 \le x < 1 \\ 5/6 & 1 \le x < 3 \\ 1 & x \ge 3 \end{cases}$

**(a) Determinare supporto e densità discreta $p_X$ di X.**

- Salti in $x=0$, $x=1$, $x=3$. Quindi $S_X = \{0, 1, 3\}$.
- $p_X(0) = 1/3 - 0 = 1/3$.
- $p_X(1) = 5/6 - 1/3 = 5/6 - 2/6 = 3/6 = 1/2$.
- $p_X(3) = 1 - 5/6 = 1/6$.

\begin{center}
\textbf{Tabella PMF di X}:
\end{center}
\begin{table}[h!]
\centering
\begin{tabular}{c|c|c|c}
$x$ & 0 & 1 & 3 \\ \hline
$p_X(x)$ & $\tfrac{1}{3}$ & $\tfrac{1}{2}$ & $\tfrac{1}{6}$ \\
\end{tabular}
\end{table}

**(c) Si consideri $Y = \sqrt{X}$. Determinare supporto e densità $p_Y$ di Y.**

1.  **Supporto di Y ($S_Y$)**:

    - Prendiamo i valori di $S_X = \{0, 1, 3\}$.
    - Applichiamo la funzione $Y=\sqrt{X}$: $\sqrt{0}=0$, $\sqrt{1}=1$, $\sqrt{3}=\sqrt{3}$.
    - $S_Y = \{0, 1, \sqrt{3}\}$.

2.  **PMF di Y ($p_Y(y)$)**:

    - **$\mathbb{P}(Y=0)$**: Quando succede che $Y=0$? Quando $\sqrt{X} = 0$, cioè quando $X=0$.
      Quindi $p_Y(0) = \mathbb{P}(X=0) = 1/3$.\
      _(Logica: Per trovare la probabilità che $Y$ valga 0, devo trovare tutti i valori di $X$ che, una volta trasformati con $\sqrt{X}$, danno 0. In questo caso è solo $X=0$, quindi "eredito" la sua probabilità.)_
    - **$\mathbb{P}(Y=1)$**: Quando succede che $Y=1$? Quando $\sqrt{X} = 1$, cioè quando $X=1$.\
      Quindi $p_Y(1) = \mathbb{P}(X=1) = 1/2$.
    - **$\mathbb{P}(Y=\sqrt{3})$**: Quando succede che $Y=\sqrt{3}$? Quando $\sqrt{X} = \sqrt{3}$, cioè quando $X=3$.\
      Quindi $p_Y(\sqrt{3}) = \mathbb{P}(X=3) = 1/6$.

\begin{center}
\textbf{Tabella PMF di Y}:
\end{center}
\begin{table}[h!]
\centering
\begin{tabular}{c|c|c|c}
$y$ & 0 & 1 & $\sqrt{3}$ \\ \hline
$p_Y(y)$ & $\tfrac{1}{3}$ & $\tfrac{1}{2}$ & $\tfrac{1}{6}$ \\
\end{tabular}
\end{table}

**(d) Calcolare il valore atteso di Y.**
Usiamo la PMF di Y che abbiamo appena trovato.
$E[Y] = (0 \cdot 1/3) + (1 \cdot 1/2) + (\sqrt{3} \cdot 1/6) = 0 + 1/2 + \sqrt{3}/6 \approx 0.5 + 1.732/6 \approx 0.7887$.

---

### 5. Le Distribuzioni "Famose" (Da Sapere!)

Queste sono scorciatoie. Se riconosci che un problema segue una di queste distribuzioni, non devi calcolare la PMF da zero. Usi direttamente le loro formule!

#### **Distribuzione di Bernoulli - $X \sim B(p)$**

- **Quando si usa**: Un singolo esperimento con solo due esiti: "successo" (vale 1) o "insuccesso" (vale 0).
- **Parametro**: $p =$ probabilità di successo.
- **PMF**: $p_X(1) = p$ e $p_X(0) = 1-p$.
- **Media**: $E[X] = p$.
- **Varianza**: $Var(X) = \mathbb{P}(1-p)$.
- **Esempio**: Lancio una moneta. $X=1$ se esce testa (successo). Se la moneta non è truccata, $p=0.5$.

#### **Distribuzione Binomiale - $X \sim B(n, p)$**

- **Quando si usa**: Quando conti il **numero di successi** in una sequenza di **$n$ esperimenti di Bernoulli identici e indipendenti**.
- **Parametri**: $n =$ numero di prove; $p =$ probabilità di successo in una singola prova.
- **Supporto**: $S_X = \{0, 1, 2, ..., n\}$.
- **PMF**: $\mathbb{P}(X=k) = \binom{n}{k} p^k (1-p)^{n-k}$
  - $\binom{n}{k}$ è il coefficiente binomiale, "n su k". Rappresenta i modi in cui puoi disporre $k$ successi in $n$ prove.
  - $p^k$ è la probabilità di ottenere $k$ successi.
  - $(1-p)^{n-k}$ è la probabilità di ottenere $n-k$ insuccessi.
- **Media**: $E[X] = np$.
- **Varianza**: $Var(X) = np(1-p)$.
- **Esempio**: Lancio una moneta 10 volte. Qual è la probabilità di ottenere esattamente 3 teste? È una Binomiale con $n=10$, $p=0.5$, e cerchiamo $\mathbb{P}(X=3)$.

#### **Distribuzione di Poisson - $X \sim \text{Poisson}(\lambda)$**

- **Quando si usa**: Quando conti il numero di volte che un evento "raro" accade in un intervallo fissato (di tempo, spazio, ecc.).
- **Parametro**: $\lambda$ (lambda) = il numero medio di eventi in quell'intervallo.
- **Supporto**: $S_X = \{0, 1, 2, 3, ...\}$ (potenzialmente infinito).
- **PMF**: $\mathbb{P}(X=k) = e^{-\lambda} \frac{\lambda^k}{k!}$
  - $k!$ è il fattoriale di k ($k! = k \cdot (k-1) \cdot ... \cdot 1$). Ricorda che $0!=1$.
- **Media**: $E[X] = \lambda$.
- **Varianza**: $Var(X) = \lambda$. (Sì, sono uguali!).
- **Esempio**: Un call center wriceve in media 10 chiamate all'ora. Qual è la probabilità che in un'ora ne riceva esattamente 7? È una Poisson con $\lambda=10$ e cerchiamo $\mathbb{P}(X=7)$.

\begin{table}[h]
\centering
\begin{tabular}{|l|c|c|c|c|}
\hline
\textbf{Distribuzione (Notazione)} & \textbf{PMF} & \textbf{CDF} & \textbf{Media} & \textbf{Varianza} \\
\hline
Bernoulli ($X \sim B(p)$) &
$\begin{cases} p & x=1 \\ 1-p & x=0 \end{cases}$ &
$\begin{cases} 
0 & x < 0 \\ 
1-p & 0 \leq x < 1 \\ 
1 & x \geq 1 
\end{cases}$ &
$p$ & $p(1-p)$ \\
\hline
Binomiale ($X \sim B(n,p)$) &
$\binom{n}{k} p^k (1-p)^{n-k}$ &
$F_X(k) = \sum_{i=0}^{k} \binom{n}{i} p^i (1-p)^{n-i}$ &
$np$ & $np(1-p)$ \\
\hline
Poisson ($X \sim \text{Poisson}(\lambda)$) &
$e^{-\lambda} \frac{\lambda^k}{k!}$ &
$F_X(k) = \sum_{i=0}^{k} e^{-\lambda} \frac{\lambda^i}{i!}$ &
$\lambda$ & $\lambda$ \\
\hline
\end{tabular}
\caption{Principali distribuzioni discrete con PMF e CDF}
\end{table}

**Esercizio Svolto: Esercizio 6 dalla scheda**

Il numero di frane $X$ in un mese segue una legge di Poisson con parametro $\lambda = 2.3$.

**(a) Calcolare la probabilità che ci siano almeno due frane in un dato mese.**
"Almeno due" significa $X \ge 2$. Calcolare $\mathbb{P}(X=2) + \mathbb{P}(X=3) + ...$ è impossibile. Usiamo il **complementare**:
$\mathbb{P}(X \ge 2) = 1 - \mathbb{P}(X < 2) = 1 - [\mathbb{P}(X=0) + \mathbb{P}(X=1)]$.

Calcoliamo i pezzi usando la formula di Poisson $\mathbb{P}(X=k) = e^{-2.3} \frac{2.3^k}{k!}$:

- $\mathbb{P}(X=0) = e^{-2.3} \frac{2.3^0}{0!} = e^{-2.3} \cdot \frac{1}{1} \approx 0.1003$
- $\mathbb{P}(X=1) = e^{-2.3} \frac{2.3^1}{1!} = e^{-2.3} \cdot 2.3 \approx 0.2306$

Quindi:
$\mathbb{P}(X \ge 2) = 1 - (0.1003 + 0.2306) = 1 - 0.3309 = 0.6691$.

**(c) Sapendo che c'è stata almeno una frana, qual è la probabilità che ci siano state esattamente due frane?**
Questa è una **probabilità condizionata**: $\mathbb{P}(A|B) = \frac{\mathbb{P}(A \cap B)}{\mathbb{P}(B)}$.

- Evento A: "ci sono state esattamente due frane" $\implies A = \{X=2\}$.
- Evento B: "c'è stata almeno una frana" $\implies B = \{X \ge 1\}$.

L'intersezione $A \cap B$ è l'evento "X è 2 E X è maggiore o uguale a 1". Questo è semplicemente $\{X=2\}$.
Quindi la formula diventa: $\mathbb{P}(X=2 | X \ge 1) = \frac{\mathbb{P}(X=2)}{\mathbb{P}(X \ge 1)}$.

Calcoliamo i pezzi:

- $\mathbb{P}(X=2) = e^{-2.3} \frac{2.3^2}{2!} = e^{-2.3} \frac{5.29}{2} \approx 0.1003 \cdot 2.645 = 0.2652$.
- $\mathbb{P}(X \ge 1) = 1 - \mathbb{P}(X=0) = 1 - 0.1003 = 0.8997$.

Infine:
$\mathbb{P}(X=2 | X \ge 1) = \frac{0.2652}{0.8997} \approx 0.2947$.

---

### 6. Riepilogo dei Punti Chiave (La tua "Cheat Sheet")

1.  **V.A. Discreta**: I suoi valori si possono contare. È descritta da **Supporto** ($S_X$, i valori possibili) e **PMF** ($p_X(x)$, le probabilità).
2.  **Regola d'oro della PMF**: $\sum p_X(x_i) = 1$. Usala per trovare parametri incogniti (Esercizio 2).
3.  **CDF ($F_X(x)$)**: È una funzione a gradini. L'altezza di ogni salto in $x_i$ è la probabilità $p_X(x_i)$. Usa questa relazione per passare dalla CDF alla PMF.
4.  **Valore Atteso (Media)**: $E[X] = \sum x_i p_X(x_i)$.
5.  **Varianza**: $Var(X) = E[X^2] - (E[X])^2$. Ricorda che $E[X^2] = \sum x_i^2 p_X(x_i)$.
6.  **Trasformazioni $Y=g(X)$**: Trova il nuovo supporto $S_Y$ e poi, per ogni $y \in S_Y$, somma le probabilità degli $x$ che lo generano.
7.  **Riconosci le Distribuzioni Notevoli**:
    - **Bernoulli**: 1 prova, 2 esiti.
    - **Binomiale**: $n$ prove indipendenti, conti i successi.
    - **Poisson**: Conti eventi rari in un intervallo.

---

### 7. Consigli per lo Studio e Errori da Evitare

**Come Studiare in 3 Giorni:**

1.  **Non imparare le dimostrazioni**: Il tuo prof le ha messe, ma se l'obiettivo è fare gli esercizi, concentrati sulle formule finali e su _quando_ usarle.
2.  **Focalizzati sul "trigger"**: Per ogni tipo di esercizio, chiediti: "Qual è la parola o il dato che mi fa capire che devo usare _questa_ formula o _questa_ distribuzione?".
    - Vedi una CDF a gradini? -> Trova i salti per avere la PMF.
    - Leggi "numero di successi su N prove"? -> Binomiale.
    - Leggi "numero medio di eventi in un'ora/mese/pagina"? -> Poisson.
    - Vedi una PMF con una lettera tipo $\alpha$? -> Poni la somma di tutte le probabilità uguale a 1.
3.  **Rifai gli esercizi della scheda**: Non limitarti a leggere la soluzione. Prendi un foglio bianco e prova a rifarli da solo. Se ti blocchi, guarda un solo passaggio della soluzione e poi prova a continuare da solo. È il modo più efficace per imparare.

**Errori Comuni da Evitare:**

- **Confondere $E[X^2]$ e $(E[X])^2$**: Sono due cose DIVERSE. Nella formula della varianza, prima calcoli la media, la metti da parte e la elevi al quadrato. Poi calcoli la media dei quadrati.
- **Sbagliare gli estremi nelle sommatorie**: $\mathbb{P}(X < k)$ e $\mathbb{P}(X \le k)$ non sono la stessa cosa per le variabili discrete! $\mathbb{P}(X < k)$ non include $k$, $\mathbb{P}(X \le k)$ sì. Fai molta attenzione.
- **Calcoli con la calcolatrice**: Gli errori di calcolo sono frequentissimi, specialmente con Poisson (fattoriali, esponenziali). Fai i calcoli due volte per sicurezza.
- **Probabilità condizionata**: Ricorda sempre la formula base $\mathbb{P}(A|B) = \mathbb{P}(A \cap B) / \mathbb{P}(B)$. L'errore più comune è non identificare correttamente l'intersezione.
