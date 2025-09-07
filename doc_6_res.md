# Vettori Aleatori Discreti

### 1. Vettori Aleatori Discreti e la Tabella a Doppia Entrata

#### Teoria Semplice (L'unica cosa che ti serve all'inizio)

Finora hai studiato una variabile aleatoria alla volta (lancio una moneta, misuro una temperatura). Ma spesso siamo interessati a **due o più risultati contemporaneamente** dello stesso esperimento.

- **Esempio pratico:** Lancio due dadi. Mi interessano sia il risultato del primo dado ($X$) sia quello del secondo ($Y$). La coppia $(X, Y)$ è un **vettore aleatorio**.
- **Altro esempio:** Scelgo uno studente a caso. Misuro sia la sua altezza ($X$) sia il suo peso ($Y$). La coppia $(X, Y)$ è un vettore aleatorio.

Se le variabili $X$ e $Y$ sono discrete (possono assumere un numero finito o numerabile di valori), allora $(X, Y)$ è un **vettore aleatorio discreto**.

Lo strumento principale per lavorare con questi vettori è la **densità discreta congiunta**, che di solito si rappresenta con una **tabella a doppia entrata**.

La densità congiunta, indicata con $p_{X,Y}(x, y)$, non è altro che la probabilità che _contemporaneamente_ si verifichino i due eventi $X=x$ e $Y=y$.

\begin{equation*}
p_{X,Y}(x, y) = \mathbb{P}(X=x, Y=y)
\end{equation*}

**La Tabella a Doppia Entrata**

Immagina una tabella dove le righe rappresentano i valori che può assumere $X$ e le colonne i valori che può assumere $Y$. All'interno di ogni cella, c'è la probabilità che $X$ e $Y$ assumano proprio quei valori.

\
\begin{tabular}{|c|c|c|c|c|c|}
\hline
$Y$ & $y_1$ & $y_2$ & $y_3$ & $\cdots$ & \textbf{Marginale di X} $(p_X(x))$ \\
\hline
$\mathbf{x_1}$ & $\mathbb{P}(x_1,y_1)$ & $\mathbb{P}(x_1,y_2)$ & $\mathbb{P}(x_1,y_3)$ & $\cdots$ & $p_X(x_1)$ \\
\hline
$\mathbf{x_2}$ & $\mathbb{P}(x_2,y_1)$ & $\mathbb{P}(x_2,y_2)$ & $\mathbb{P}(x_2,y_3)$ & $\cdots$ & $p_X(x_2)$ \\
\hline
$\vdots$ & $\vdots$ & $\vdots$ & $\vdots$ & $\ddots$ & $\vdots$ \\
\hline
\textbf{Marginale di Y} $(p_Y(y))$ & $p_Y(y_1)$ & $p_Y(y_2)$ & $p_Y(y_3)$ & $\cdots$ & $\mathbf{1}$ \\
\hline
\end{tabular}
\

**Concetti Chiave sulla Tabella:**

1.  **Probabilità Congiunta:** I valori _dentro_ la tabella sono le probabilità congiunte, ad esempio $\mathbb{P}(x_1, y_1) = \mathbb{P}(X=x_1, Y=y_1)$. La somma di tutte le probabilità nelle celle interne deve fare **1**.
2.  **Distribuzioni Marginali:** Se conosci la distribuzione congiunta (tutta la tabella), puoi trovare le distribuzioni delle singole variabili $X$ e $Y$. Queste si chiamano **marginali** perché si scrivono ai "margini" della tabella.
    - **Per ottenere la marginale di X ($p_X(x)$):** Somma tutte le probabilità lungo la **riga** corrispondente. Ad esempio: $p_X(x_1) = \mathbb{P}(x_1,y_1) + \mathbb{P}(x_1,y_2) + \mathbb{P}(x_1,y_3)$.
    - **Per ottenere la marginale di Y ($p_Y(y)$):** Somma tutte le probabilità lungo la **colonna** corrispondente. Ad esempio: $p_Y(y_1) = \mathbb{P}(x_1,y_1) + \mathbb{P}(x_2,y_1)$.
3.  **Verifica:** La somma di tutte le probabilità marginali di $X$ deve fare 1. Lo stesso vale per $Y$.

---

#### Esercizio Guidato: Completare la Tabella (Basato sull'Esercizio 1 del PDF)

**Testo:** Siano $X$ e $Y$ due v.a. discrete con densità congiunta parzialmente data da:

| \diagbox{$X$}{$Y$} | **0** | **1** | **2** | **$p_X(x)$** |
| :----------------: | :---: | :---: | :---: | :----------: |
|       **2**        |   ?   |  0.1  |   ?   |      ?       |
|       **4**        |  0.1  |   ?   |   ?   |     0.6      |
|    **$p_Y(y)$**    |  0.3  |  0.4  |   ?   |    **1**     |

**Obiettivo:** Completare la tabella.

**Svolgimento Passo-Passo:**

1.  **Trova i marginali mancanti:** La somma di tutti i marginali deve fare 1.

    - **Marginale $p_X(2)$:** La somma della colonna dei marginali di X deve essere 1. Quindi $p_X(2) + p_X(4) = 1$.
      $p_X(2) + 0.6 = 1 \implies p_X(2) = 0.4$.
    - **Marginale $p_Y(2)$:** La somma della riga dei marginali di Y deve essere 1. Quindi $p_Y(0) + p_Y(1) + p_Y(2) = 1$.
      $0.3 + 0.4 + p_Y(2) = 1 \implies p_Y(2) = 1 - 0.7 = 0.3$.

    Ora la tabella è così:

    | \diagbox{$X$}{$Y$} | **0** | **1** |  **2**  | **$p_X(x)$** |
    | :----------------: | :---: | :---: | :-----: | :----------: |
    |       **2**        |   ?   |  0.1  |    ?    |   **0.4**    |
    |       **4**        |  0.1  |   ?   |    ?    |     0.6      |
    |    **$p_Y(y)$**    |  0.3  |  0.4  | **0.3** |    **1**     |

2.  **Completa le celle interne usando le somme di righe e colonne:**

    - **Cella (X=2, Y=0):** Guarda la colonna Y=0. La somma deve fare $p_Y(0) = 0.3$.
      $\mathbb{P}(2,0) + \mathbb{P}(4,0) = 0.3 \implies \mathbb{P}(2,0) + 0.1 = 0.3 \implies \mathbb{P}(2,0) = 0.2$.
    - **Cella (X=4, Y=1):** Guarda la colonna Y=1. La somma deve fare $p_Y(1) = 0.4$.
      $\mathbb{P}(2,1) + \mathbb{P}(4,1) = 0.4 \implies 0.1 + \mathbb{P}(4,1) = 0.4 \implies \mathbb{P}(4,1) = 0.3$.
    - Ora usiamo le righe. **Riga X=2:** La somma deve fare $p_X(2)=0.4$.
      $\mathbb{P}(2,0) + \mathbb{P}(2,1) + \mathbb{P}(2,2) = 0.4 \implies 0.2 + 0.1 + \mathbb{P}(2,2) = 0.4 \implies \mathbb{P}(2,2) = 0.1$.
    - **Riga X=4:** La somma deve fare $p_X(4)=0.6$.
      $\mathbb{P}(4,0) + \mathbb{P}(4,1) + \mathbb{P}(4,2) = 0.6 \implies 0.1 + 0.3 + \mathbb{P}(4,2) = 0.6 \implies \mathbb{P}(4,2) = 0.2$.

3.  **Tabella Completa:**

    | \diagbox{$X$}{$Y$} | **0** | **1** | **2** | **$p_X(x)$** |
    | :----------------: | :---: | :---: | :---: | :----------: |
    |       **2**        |  0.2  |  0.1  |  0.1  |     0.4      |
    |       **4**        |  0.1  |  0.3  |  0.2  |     0.6      |
    |    **$p_Y(y)$**    |  0.3  |  0.4  |  0.3  |    **1**     |

_Verifica finale:_ La somma delle celle interne è $0.2+0.1+0.1+0.1+0.3+0.2 = 1$. Corretto!

---

### 2. Indipendenza di Variabili Aleatorie Discrete

#### Teoria Semplice

- **Significato Intuitivo:** Due variabili aleatorie $X$ e $Y$ sono indipendenti se conoscere il valore di una non cambia le probabilità dell'altra. Esempio: il risultato del primo lancio di un dado ($X$) è indipendente da quello del secondo ($Y$).
- **La Regola d'Oro (per gli esercizi):** Due variabili aleatorie discrete $X$ e $Y$ sono indipendenti **se e solo se** la probabilità congiunta è il prodotto delle marginali **PER OGNI SINGOLA CELLA** della tabella.
  $$ p_{X,Y}(x, y) = p_X(x) \cdot p_Y(y) \quad \text{per ogni coppia } (x,y) $$

**Come si verifica l'indipendenza:**

1.  Calcola tutte le marginali.
2.  Prendi una cella qualsiasi, ad esempio $(x_i, y_j)$.
3.  Controlla se $p_{X,Y}(x_i, y_j)$ (il valore nella cella) è uguale a $p_X(x_i) \cdot p_Y(y_j)$ (il prodotto dei marginali di quella riga e colonna).
4.  Se anche per **una sola cella** la regola non vale, le variabili **NON** sono indipendenti. Se vale per tutte, sono indipendenti.

#### Esercizio Guidato: Verificare l'Indipendenza (Basato sull'Esercizio 1b)

**Testo:** Usando la tabella completata prima, dire se $X$ e $Y$ sono indipendenti.

**Svolgimento Passo-Passo:**

1.  **Prendiamo la prima cella (X=2, Y=0):**
    - Valore nella cella: $p_{X,Y}(2,0) = 0.2$.
    - Prodotto delle marginali: $p_X(2) \cdot p_Y(0) = 0.4 \cdot 0.3 = 0.12$.
2.  **Confronta:**
    - $0.2 \neq 0.12$.
3.  **Conclusione:**
    - La regola non vale per la prima cella. Non c'è bisogno di controllare le altre. **X e Y non sono indipendenti**.

**E se fossero state indipendenti?** Se lo fossero state, il professore avrebbe potuto chiederti di "Completare la tabella _in modo che X e Y siano indipendenti_". In quel caso, avresti dovuto calcolare i marginali e poi riempire ogni cella `(i,j)` calcolando `marginale_riga(i) * marginale_colonna(j)`.

---

### 3. Calcolare la Probabilità di Eventi Congiunti

#### Teoria Semplice

Spesso ti viene chiesto di calcolare la probabilità di un evento che dipende da entrambe le variabili, ad esempio $\mathbb{P}(X+Y > 5)$ o $\mathbb{P}(XY \leq 3)$.

**La Regola:** Per calcolare la probabilità di un evento, devi:

1.  Identificare tutte le coppie $(x,y)$ nella tabella che **soddisfano la condizione** dell'evento.
2.  **Sommare le probabilità** (i valori nelle celle) di tutte queste coppie.

$$\mathbb{P}((X,Y) \in B) = \sum_{(x,y) \in B} p_{X,Y}(x,y)$$

dove $B$ rappresenta l'insieme delle coppie $(x,y)$ che soddisfano la condizione dell'evento.

#### Esercizio Guidato: Calcolare una Probabilità (Basato sull'Esercizio 1c)

\

\begin{center}
\begin{NiceTabular}{c|c|c|c|c}[hvlines]
\diagbox{$X$}{$Y$} & $\mathbf{0}$ & $\mathbf{1}$ & $\mathbf{2}$ & $\mathbf{p_X(x)}$ \\
$2$ & $0.2$ & $0.1$ & $0.1$ & $0.4$ \\
$4$ & $0.1$ & $0.3$ & $0.2$ & $0.6$ \\
$\mathbf{p_Y(y)}$ & $0.3$ & $0.4$ & $0.3$ & $\mathbf{1}$ \\
\end{NiceTabular}
\end{center}

**Testo:** Calcolare $\mathbb{P}(XY \leq 3)$.

**Svolgimento Passo-Passo:**

1.  **Analizza ogni cella della tabella** e controlla se la condizione $x \cdot y \leq 3$ è vera.

    | Cella (x,y) | Calcolo $x \cdot y$ | Condizione $xy \leq 3$? | Probabilità $\mathbb{P}(x,y)$ |
    | :---------- | :------------------ | :---------------------- | :---------------------------- |
    | (2, 0)      | $2 \cdot 0 = 0$     | **SÌ**                  | 0.2                           |
    | (2, 1)      | $2 \cdot 1 = 2$     | **SÌ**                  | 0.1                           |
    | (2, 2)      | $2 \cdot 2 = 4$     | NO                      | -                             |
    | (4, 0)      | $4 \cdot 0 = 0$     | **SÌ**                  | 0.1                           |
    | (4, 1)      | $4 \cdot 1 = 4$     | NO                      | -                             |
    | (4, 2)      | $4 \cdot 2 = 8$     | NO                      | -                             |

2.  **Identifica le celle "buone":** Le coppie che soddisfano la condizione sono (2,0), (2,1) e (4,0).

3.  **Somma le loro probabilità:**
    $$ \mathbb{P}(XY \leq 3) = p*{X,Y}(2,0) + p*{X,Y}(2,1) + p_{X,Y}(4,0) $$
    $$ \mathbb{P}(XY \leq 3) = 0.2 + 0.1 + 0.1 = 0.4 $$

---

### 4. Valore Atteso, Varianza e Covarianza

#### Teoria Semplice

**Valore Atteso di X e Y**
Si calcolano facilmente dalle distribuzioni marginali.
$$ E[X] = \sum_i x_i \cdot p_X(x_i) $$
$$ E[Y] = \sum_j y_j \cdot p_Y(y_j) $$

**Valore Atteso di una Funzione di (X, Y)**

Se hai una nuova variabile $Z = g(X,Y)$ (es. $Z=X+Y$ o $Z=XY$), il suo valore atteso è:

$$E[g(X,Y)] = \sum_{i,j} g(x_i, y_j) \cdot p_{X,Y}(x_i, y_j)$$

In pratica: per ogni cella della tabella, calcola il valore della funzione, moltiplicalo per la probabilità di quella cella, e poi somma tutto.

**Proprietà Fondamentali:**

- **Linearità del valore atteso (SEMPRE VERA):** $E[aX + bY] = aE[X] + bE[Y]$.
- **Valore atteso del prodotto (SOLO SE INDIPENDENTI):** Se $X$ e $Y$ sono indipendenti, allora $E[XY] = E[X]E[Y]$. Se non lo sono, devi calcolare $E[XY]$ con la sommatoria su tutta la tabella.

\

**Covarianza**
La covarianza misura la "relazione lineare" tra $X$ e $Y$.

- $\text{Cov}(X,Y) > 0$: Tendono a crescere insieme (se $X$ è grande, è probabile che anche $Y$ lo sia).
- $\text{Cov}(X,Y) < 0$: Tendono a muoversi in direzioni opposte.
- $\text{Cov}(X,Y) = 0$: Sono **scorrelate**. Non c'è una tendenza lineare.

**Formula per il Calcolo (la più facile da usare):**
$$ \text{Cov}(X,Y) = E[XY] - E[X]E[Y] $$

**Relazione tra Indipendenza e Correlazione (IMPORTANTISSIMO):**

- Se $X$ e $Y$ sono **indipendenti** $\implies$ sono **scorrelate** (cioè $\text{Cov}(X,Y)=0$).
- Se $X$ e $Y$ sono **scorrelate** $\not\implies$ **NON è detto** che siano **indipendenti**. Potrebbero avere una dipendenza non-lineare. Questo è un errore comune!

\

**Varianza della Somma**
$$ \text{Var}(X+Y) = \text{Var}(X) + \text{Var}(Y) + 2\text{Cov}(X,Y) $$

- Se $X$ e $Y$ sono scorrelate (e quindi anche se sono indipendenti), il termine di covarianza sparisce e $\text{Var}(X+Y) = \text{Var}(X) + \text{Var}(Y)$.

#### Esercizio Guidato: Calcolare gli Indici (Basato sull'Esercizio 4)

---

**Testo:** Una scatola contiene 3 componenti nuovi, 2 usati ma funzionanti e 2 difettosi (totale 7). Si pescano 3 componenti. $X$ = "numero di componenti nuovi", $Y$ = "numero di usati".
Calcolare $E[X]$, $E[Y]$, $E[XY]$ e $\text{Cov}(X,Y)$.

---

Per calcolare la probabilità $\mathbb{P}(X=x, Y=y)$ di estrarre esattamente $x$ componenti nuovi e $y$ componenti usati, utilizziamo il calcolo combinatorio, poiché le estrazioni avvengono senza reimmissione. La logica si basa sulla definizione classica di probabilità:

$$\mathbb{P}(\text{Evento}) = \frac{\text{Numero di Casi Favorevoli}}{\text{Numero di Casi Totali}}$$

#### Calcolo dei Casi Totali (Denominatore)
Il numero totale di modi in cui possiamo estrarre 3 componenti qualsiasi da un totale di 7 è dato dalla combinazione $\binom{7}{3}$:
$$\text{Casi Totali} = \binom{7}{3} = \frac{7!}{3!(7-3)!} = \frac{7 \cdot 6 \cdot 5}{3 \cdot 2 \cdot 1} = 35$$
Questo valore sarà il denominatore per tutte le nostre probabilità.

#### Calcolo dei Casi Favorevoli (Numeratore)
Per un dato evento $(X=x, Y=y)$, dobbiamo estrarre $x$ nuovi, $y$ usati e, di conseguenza, $z = 3-x-y$ difettosi
($x + y + z = 3 \Rightarrow z = 3 - x - y$).

Il numero di modi per farlo si ottiene moltiplicando le combinazioni per ciascun gruppo:
$$\text{Casi Favorevoli per } (X=x, Y=y) = \binom{3}{x} \binom{2}{y} \binom{2}{3-x-y}$$

Dove:

- $\binom{3}{x}$: modi per scegliere $x$ nuovi dai 3 disponibili.
- $\binom{2}{y}$: modi per scegliere $y$ usati dai 2 disponibili.
- $\binom{2}{3-x-y}$: modi per scegliere i restanti componenti difettosi dai 2 disponibili.

#### Calcolo delle Probabilità per la Tabella

Applichiamo la formula $\mathbb{P}(X=x, Y=y) = \frac{\text{Casi Favorevoli}}{35}$ per ogni cella.

- $\mathbb{P}(X=0, Y=1) \implies x=0, y=1, z=2$:
$$\mathbb{P}(0,1) = \frac{\binom{3}{0}\binom{2}{1}\binom{2}{2}}{35} = \frac{1 \cdot 2 \cdot 1}{35} = \frac{2}{35}$$

- $\mathbb{P}(X=0, Y=2) \implies x=0, y=2, z=1$:
$$\mathbb{P}(0,2) = \frac{\binom{3}{0}\binom{2}{2}\binom{2}{1}}{35} = \frac{1 \cdot 1 \cdot 2}{35} = \frac{2}{35}$$
_(Nota: questo è il valore corretto, diverso da 1/35)_

- $\mathbb{P}(X=1, Y=0) \implies x=1, y=0, z=2$:
$$\mathbb{P}(1,0) = \frac{\binom{3}{1}\binom{2}{0}\binom{2}{2}}{35} = \frac{3 \cdot 1 \cdot 1}{35} = \frac{3}{35}$$

- $\mathbb{P}(X=1, Y=1) \implies x=1, y=1, z=1$:
$$\mathbb{P}(1,1) = \frac{\binom{3}{1}\binom{2}{1}\binom{2}{1}}{35} = \frac{3 \cdot 2 \cdot 2}{35} = \frac{12}{35}$$

- $\mathbb{P}(X=1, Y=2) \implies x=1, y=2, z=0$:
$$\mathbb{P}(1,2) = \frac{\binom{3}{1}\binom{2}{2}\binom{2}{0}}{35} = \frac{3 \cdot 1 \cdot 1}{35} = \frac{3}{35}$$

- $\mathbb{P}(X=2, Y=0) \implies x=2, y=0, z=1$:
$$\mathbb{P}(2,0) = \frac{\binom{3}{2}\binom{2}{0}\binom{2}{1}}{35} = \frac{3 \cdot 1 \cdot 2}{35} = \frac{6}{35}$$

- $\mathbb{P}(X=2, Y=1) \implies x=2, y=1, z=0$:
$$\mathbb{P}(2,1) = \frac{\binom{3}{2}\binom{2}{1}\binom{2}{0}}{35} = \frac{3 \cdot 2 \cdot 1}{35} = \frac{6}{35}$$

- $\mathbb{P}(X=3, Y=0) \implies x=3, y=0, z=0$:
$$\mathbb{P}(3,0) = \frac{\binom{3}{3}\binom{2}{0}\binom{2}{0}}{35} = \frac{1 \cdot 1 \cdot 1}{35} = \frac{1}{35}$$

Tutte le altre combinazioni sono impossibili (ad es. $X=2, Y=2$ richiederebbe 4 estrazioni) e hanno probabilità 0.

#### Tabella Corretta e Completa

Usando i valori calcolati, costruiamo la tabella corretta. Le probabilità marginali $p_X(x)$ e $p_Y(y)$ si ottengono sommando i valori di righe e colonne.

| \diagbox{$X$}{$Y$} |   **0** |   **1** |  **2** | **$p_X(x)$** |
| :----------------: | :-------: | :-------: | :------: | :----------: |
|       **0** |     0     |   2/35    |   2/35   |   **4/35** |
|       **1** |   3/35    |   12/35   |   3/35   |  **18/35** |
|       **2** |   6/35    |   6/35    |    0     |  **12/35** |
|       **3** |   1/35    |     0     |    0     |   **1/35** |
|    **$p_Y(y)$** | **10/35** | **20/35** | **5/35** |    **1** |

#### Svolgimento Passo-Passo
\

**1. Calcolo dei Valori Attesi $E[X]$ e $E[Y]$**

Per calcolare i valori attesi delle variabili aleatorie $X$ e $Y$, usiamo le loro distribuzioni di probabilità marginali (le somme di righe e colonne della tabella).

- **Valore atteso di X (componenti nuovi):**
  $$E[X] = \sum_{x} x \cdot p_X(x)$$
  $$E[X] = \left(0 \cdot \frac{4}{35}\right) + \left(1 \cdot \frac{18}{35}\right) + \left(2 \cdot \frac{12}{35}\right) + \left(3 \cdot \frac{1}{35}\right) = \frac{0 + 18 + 24 + 3}{35} = \frac{45}{35} = \frac{9}{7} \approx 1.29$$

- **Valore atteso di Y (componenti usati):**
  $$E[Y] = \sum_{y} y \cdot p_Y(y)$$
  $$E[Y] = \left(0 \cdot \frac{10}{35}\right) + \left(1 \cdot \frac{20}{35}\right) + \left(2 \cdot \frac{5}{35}\right) = \frac{0 + 20 + 10}{35} = \frac{30}{35} = \frac{6}{7} \approx 0.86$$

\

**2. Calcolo del Valore Atteso del Prodotto $E[XY]$**

Per calcolare $E[XY]$, sommiamo i prodotti $x \cdot y \cdot P(X=x, Y=y)$ per ogni cella della tabella congiunta. Consideriamo solo le celle dove sia $x$ che $y$ sono diversi da zero.

$$E[XY] = \sum_{x} \sum_{y} xy \cdot P(X=x, Y=y)$$

- Cella (X=1, Y=1): $1 \cdot 1 \cdot \frac{12}{35} = \frac{12}{35}$
- Cella (X=1, Y=2): $1 \cdot 2 \cdot \frac{3}{35} = \frac{6}{35}$
- Cella (X=2, Y=1): $2 \cdot 1 \cdot \frac{6}{35} = \frac{12}{35}$

$$E[XY] = \frac{12}{35} + \frac{6}{35} + \frac{12}{35} = \frac{30}{35} = \frac{6}{7}$$

\

**3. Calcolo della Covarianza $\text{Cov}(X,Y)$**

Infine, usiamo la formula della covarianza.

$$\text{Cov}(X,Y) = E[XY] - E[X]E[Y]$$
$$\text{Cov}(X,Y) = \frac{6}{7} - \left(\frac{9}{7} \cdot \frac{6}{7}\right) = \frac{6}{7} - \frac{54}{49}$$
Per sottrarre, portiamo allo stesso denominatore (49):
$$\text{Cov}(X,Y) = \frac{6 \cdot 7}{49} - \frac{54}{49} = \frac{42 - 54}{49} = -\frac{12}{49} \approx -0.245$$

Il valore negativo della covarianza indica una **correlazione lineare negativa**. Ciò significa che all'aumentare del numero di componenti nuovi estratti ($X$), tende a diminuire il numero di componenti usati ($Y$). Questo è intuitivo: poiché si estraggono solo 3 componenti in totale, scegliere un componente nuovo "occupa uno slot" che non può essere riempito da un componente usato.

---

### 5. Funzioni di Vettori Aleatori: Costruire una Nuova Tabella

A volte, da un vettore $(X,Y)$ si definiscono nuove variabili, ad esempio $U=X+Y$ e $V=X-Y$, e ti viene chiesta la loro distribuzione congiunta.

**Procedimento:**

1.  Parti dalla tabella di $(X,Y)$.
2.  Crea una lista di tutte le coppie $(x,y)$ con probabilità non nulla.
3.  Per ogni coppia $(x,y)$, calcola la coppia corrispondente $(u,v)$.
4.  Crea una nuova tabella vuota per $(U,V)$. Le righe saranno i valori di $U$, le colonne i valori di $V$.
5.  Riempi la nuova tabella: per ogni coppia $(x,y)$ originale, prendi la sua probabilità $\mathbb{P}(x,y)$ e **aggiungila** alla cella $(u,v)$ corrispondente nella nuova tabella.
    - **Attenzione:** Diverse coppie $(x,y)$ possono dare origine alla stessa coppia $(u,v)$. In tal caso, le loro probabilità si sommano!

---

### Riepilogo Punti Chiave da Ricordare

1.  **La Tabella a Doppia Entrata è il tuo strumento principale.** Impara a leggerla, completarla e usarla.
2.  **Marginali = Somma per Riga/Colonna.** La probabilità di $X=x$ è la somma di tutta la riga $x$.
3.  **Indipendenza = Prodotto delle Marginali.** Questo deve valere per **ogni cella**. Basta un'eccezione per negare l'indipendenza.
4.  **Probabilità di un evento = Somma delle celle che soddisfano la condizione.**
5.  **Formula della Covarianza:** $\text{Cov}(X,Y) = E[XY] - E[X]E[Y]$. Per calcolare $E[XY]$ devi usare la tabella intera (a meno che non siano indipendenti).
6.  **Indipendenza $\implies$ Covarianza Zero.** Il contrario non è vero.

### Consigli per lo Studio e Errori da Evitare

- **Come studiare:** Prendi gli esercizi, copri la soluzione e prova a costruire le tabelle da solo. La parte più difficile è spesso tradurre il testo di un problema (es. lanci di dadi, estrazioni da urne) in una tabella di probabilità. Esercitati su quello.
- **Errore Comune #1:** Controllare l'indipendenza solo su una cella e, se la regola vale, concludere che sono indipendenti. **NO! Devi controllarle tutte** (o almeno essere sicuro che valga per tutte). Per dire di NO, basta un controesempio. Per dire di SÌ, servono tutte.
- **Errore Comune #2:** Calcolare $E[XY]$ come $E[X]E[Y]$ anche quando le variabili NON sono indipendenti. Questo è un errore grave. Usa sempre la sommatoria su tutta la tabella se non hai la certezza dell'indipendenza.
- **Errore Comune #3:** Quando crei la tabella per nuove variabili $(U,V)$, dimenticarti di **sommare le probabilità** di diverse coppie $(x,y)$ che generano la stessa coppia $(u,v)$.
