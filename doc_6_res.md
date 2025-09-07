# Vettori Aleatori Discreti

### 1. Vettori Aleatori Discreti e la Tabella a Doppia Entrata

#### Teoria Semplice (L'unica cosa che ti serve all'inizio)

Finora hai studiato una variabile aleatoria alla volta (lancio una moneta, misuro una temperatura). Ma spesso siamo interessati a **due o più risultati contemporaneamente** dello stesso esperimento.

- **Esempio pratico:** Lancio due dadi. Mi interessano sia il risultato del primo dado ($X$) sia quello del secondo ($Y$). La coppia $(X, Y)$ è un **vettore aleatorio**.
- **Altro esempio:** Scelgo uno studente a caso. Misuro sia la sua altezza ($X$) sia il suo peso ($Y$). La coppia $(X, Y)$ è un vettore aleatorio.

Se le variabili $X$ e $Y$ sono discrete (possono assumere un numero finito o numerabile di valori), allora $(X, Y)$ è un **vettore aleatorio discreto**.

Lo strumento principale per lavorare con questi vettori è la **densità discreta congiunta**, che di solito si rappresenta con una **tabella a doppia entrata**.

La densità congiunta, indicata con $p_{X,Y}(x, y)$, non è altro che la probabilità che _contemporaneamente_ si verifichino i due eventi $X=x$ e $Y=y$.
$$ p\_{X,Y}(x, y) = \mathbb{P}(X=x, Y=y) $$

**La Tabella a Doppia Entrata**

Immagina una tabella dove le righe rappresentano i valori che può assumere $X$ e le colonne i valori che può assumere $Y$. All'interno di ogni cella, c'è la probabilità che $X$ e $Y$ assumano proprio quei valori.

|              $Y$              |         $y_1$         |         $y_2$         |         $y_3$         | **Marginale di X ($p_X(x)$)** |
| :---------------------------: | :-------------------: | :-------------------: | :-------------------: | :---------------------------: |
|           **$x_1$**           | $\mathbb{P}(x_1,y_1)$ | $\mathbb{P}(x_1,y_2)$ | $\mathbb{P}(x_1,y_3)$ |          $p_X(x_1)$           |
|           **$x_2$**           | $\mathbb{P}(x_2,y_1)$ | $\mathbb{P}(x_2,y_2)$ | $\mathbb{P}(x_2,y_3)$ |          $p_X(x_2)$           |
| **Marginale di Y ($p_Y(y)$)** |      $p_Y(y_1)$       |      $p_Y(y_2)$       |      $p_Y(y_3)$       |             **1**             |

**Concetti Chiave sulla Tabella:**

1.  **Probabilità Congiunta:** I valori _dentro_ la tabella sono le probabilità congiunte, ad esempio $\mathbb{P}(x_1, y_1) = \mathbb{P}(X=x_1, Y=y_1)$. La somma di tutte le probabilità nelle celle interne deve fare **1**.
2.  **Distribuzioni Marginali:** Se conosci la distribuzione congiunta (tutta la tabella), puoi trovare le distribuzioni delle singole variabili $X$ e $Y$. Queste si chiamano **marginali** perché si scrivono ai "margini" della tabella.
    - **Per ottenere la marginale di X ($p_X(x)$):** Somma tutte le probabilità lungo la **riga** corrispondente. Ad esempio: $p_X(x_1) = \mathbb{P}(x_1,y_1) + \mathbb{P}(x_1,y_2) + \mathbb{P}(x_1,y_3)$.
    - **Per ottenere la marginale di Y ($p_Y(y)$):** Somma tutte le probabilità lungo la **colonna** corrispondente. Ad esempio: $p_Y(y_1) = \mathbb{P}(x_1,y_1) + \mathbb{P}(x_2,y_1)$.
3.  **Verifica:** La somma di tutte le probabilità marginali di $X$ deve fare 1. Lo stesso vale per $Y$.

---

#### Esercizio Guidato: Completare la Tabella (Basato sull'Esercizio 1 del PDF)

**Testo:** Siano $X$ e $Y$ due v.a. discrete con densità congiunta parzialmente data da:

|     $Y$      | **0** | **1** | **2** | **$p_X(x)$** |
| :----------: | :---: | :---: | :---: | :----------: |
|  **$X=2$**   |   ?   |  0.1  |   ?   |      ?       |
|  **$X=4$**   |  0.1  |   ?   |   ?   |     0.6      |
| **$p_Y(y)$** |  0.3  |  0.4  |   ?   |    **1**     |

**Obiettivo:** Completare la tabella.

**Svolgimento Passo-Passo:**

1.  **Trova i marginali mancanti:** La somma di tutti i marginali deve fare 1.

    - **Marginale $p_X(2)$:** La somma della colonna dei marginali di X deve essere 1. Quindi $p_X(2) + p_X(4) = 1$.
      $p_X(2) + 0.6 = 1 \implies p_X(2) = 0.4$.
    - **Marginale $p_Y(2)$:** La somma della riga dei marginali di Y deve essere 1. Quindi $p_Y(0) + p_Y(1) + p_Y(2) = 1$.
      $0.3 + 0.4 + p_Y(2) = 1 \implies p_Y(2) = 1 - 0.7 = 0.3$.

    Ora la tabella è così:

    |     $Y$      | **0** | **1** |  **2**  | **$p_X(x)$** |
    | :----------: | :---: | :---: | :-----: | :----------: |
    |  **$X=2$**   |   ?   |  0.1  |    ?    |   **0.4**    |
    |  **$X=4$**   |  0.1  |   ?   |    ?    |     0.6      |
    | **$p_Y(y)$** |  0.3  |  0.4  | **0.3** |    **1**     |

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

    |     $Y$      | **0** | **1** | **2** | **$p_X(x)$** |
    | :----------: | :---: | :---: | :---: | :----------: |
    |  **$X=2$**   |  0.2  |  0.1  |  0.1  |     0.4      |
    |  **$X=4$**   |  0.1  |  0.3  |  0.2  |     0.6      |
    | **$p_Y(y)$** |  0.3  |  0.4  |  0.3  |    **1**     |

_Verifica finale:_ La somma delle celle interne è $0.2+0.1+0.1+0.1+0.3+0.2 = 1$. Corretto!

---

### 2. Indipendenza di Variabili Aleatorie Discrete

#### Teoria Semplice

- **Significato Intuitivo:** Due variabili aleatorie $X$ e $Y$ sono indipendenti se conoscere il valore di una non cambia le probabilità dell'altra. Esempio: il risultato del primo lancio di un dado ($X$) è indipendente da quello del secondo ($Y$).
- **La Regola d'Oro (per gli esercizi):** Due variabili aleatorie discrete $X$ e $Y$ sono indipendenti **se e solo se** la probabilità congiunta è il prodotto delle marginali **PER OGNI SINGOLA CELLA** della tabella.
  $$ p\_{X,Y}(x, y) = p_X(x) \cdot p_Y(y) \quad \text{per ogni coppia } (x,y) $$

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
    $$ \mathbb{P}((X,Y) \in B) = \sum*{(x,y) \text{ che soddisfano } B} p*{X,Y}(x,y) $$

#### Esercizio Guidato: Calcolare una Probabilità (Basato sull'Esercizio 1c)

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
    $$ \mathbb{P}(XY \leq 3) = p*{X,Y}(2,0) + p*{X,Y}(2,1) + p\_{X,Y}(4,0) $$
    $$ \mathbb{P}(XY \leq 3) = 0.2 + 0.1 + 0.1 = 0.4 $$

---

### 4. Valore Atteso, Varianza e Covarianza

#### Teoria Semplice

**Valore Atteso di X e Y**
Si calcolano facilmente dalle distribuzioni marginali, come hai già imparato.
$$ E[X] = \sum_i x_i \cdot p_X(x_i) $$
$$ E[Y] = \sum_j y_j \cdot p_Y(y_j) $$

**Valore Atteso di una Funzione di (X, Y)**
Se hai una nuova variabile $Z = g(X,Y)$ (es. $Z=X+Y$ o $Z=XY$), il suo valore atteso è:
$$ E[g(X,Y)] = \sum*{i,j} g(x_i, y_j) \cdot p*{X,Y}(x_i, y_j) $$
In pratica: per ogni cella della tabella, calcola il valore della funzione, moltiplicalo per la probabilità di quella cella, e poi somma tutto.

**Proprietà Fondamentali:**

- **Linearità del valore atteso (SEMPRE VERA):** $E[aX + bY] = aE[X] + bE[Y]$.
- **Valore atteso del prodotto (SOLO SE INDIPENDENTI):** Se $X$ e $Y$ sono indipendenti, allora $E[XY] = E[X]E[Y]$. Se non lo sono, devi calcolare $E[XY]$ con la sommatoria su tutta la tabella.

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

**Varianza della Somma**
$$ \text{Var}(X+Y) = \text{Var}(X) + \text{Var}(Y) + 2\text{Cov}(X,Y) $$

- Se $X$ e $Y$ sono scorrelate (e quindi anche se sono indipendenti), il termine di covarianza sparisce e $\text{Var}(X+Y) = \text{Var}(X) + \text{Var}(Y)$.

#### Esercizio Guidato: Calcolare gli Indici (Basato sull'Esercizio 4)

**Testo:** Una scatola contiene 3 componenti nuovi, 2 usati ma funzionanti e 2 difettosi (totale 7). Si pescano 3 componenti. $X$ = "numero di componenti nuovi", $Y$ = "numero di usati".
Calcolare $E[X]$, $E[Y]$, $E[XY]$ e $\text{Cov}(X,Y)$.

_Nota: La parte più difficile qui è costruire la tabella, che è un problema di calcolo combinatorio. La soluzione fornisce la tabella già pronta. Usiamo quella per concentrarci sul calcolo degli indici._

**Tabella dall'Esercizio 4 (Soluzioni):**

|     $Y$      |   **0**   |   **1**   |  **2**   | **$p_X(x)$** |
| :----------: | :-------: | :-------: | :------: | :----------: |
|  **$X=0$**   |     0     |   2/35    |   1/35   |   **3/35**   |
|  **$X=1$**   |   3/35    |   12/35   |   3/35   |  **18/35**   |
|  **$X=2$**   |   6/35    |   6/35    |    0     |  **12/35**   |
|  **$X=3$**   |   1/35    |     0     |    0     |   **1/35**   |
| **$p_Y(y)$** | **10/35** | **20/35** | **5/35** |    **1**     |

**Svolgimento Passo-Passo:**

1.  **Calcola $E[X]$ e $E[Y]$ usando i marginali.**
    $$ E[X] = 0 \cdot \frac{3}{35} + 1 \cdot \frac{18}{35} + 2 \cdot \frac{12}{35} + 3 \cdot \frac{1}{35} = \frac{0+18+24+3}{35} = \frac{45}{35} = \frac{9}{7} $$
    $$ E[Y] = 0 \cdot \frac{10}{35} + 1 \cdot \frac{20}{35} + 2 \cdot \frac{5}{35} = \frac{0+20+10}{35} = \frac{30}{35} = \frac{6}{7} $$
    _(Le soluzioni del prof usano 45/35 e 30/35, che è corretto)_

2.  **Calcola $E[XY]$ usando la tabella completa.** Dobbiamo sommare $x \cdot y \cdot \mathbb{P}(x,y)$ per tutte le celle dove il prodotto $x \cdot y$ non è zero.

    - Cella (1,1): $1 \cdot 1 \cdot \frac{12}{35} = \frac{12}{35}$
    - Cella (1,2): $1 \cdot 2 \cdot \frac{3}{35} = \frac{6}{35}$
    - Cella (2,1): $2 \cdot 1 \cdot \frac{6}{35} = \frac{12}{35}$
    - Le altre celle hanno $x=0$, $y=0$ o probabilità 0, quindi il loro contributo è nullo.
      $$ E[XY] = \frac{12}{35} + \frac{6}{35} + \frac{12}{35} = \frac{30}{35} = \frac{6}{7} $$
      _(Le soluzioni del prof dicono 30/35, corretto)_

3.  **Calcola $\text{Cov}(X,Y)$ con la formula.**
    $$ \text{Cov}(X,Y) = E[XY] - E[X]E[Y] = \frac{30}{35} - \left(\frac{45}{35} \cdot \frac{30}{35}\right) $$
    $$ \text{Cov}(X,Y) = \frac{30}{35} - \frac{1350}{1225} = \frac{6}{7} - \frac{54}{49} = \frac{42 - 54}{49} = -\frac{12}{49} $$
    _(Le soluzioni del prof danno -12/49, corretto)_
    Il risultato negativo ci dice che c'è una relazione inversa: se peschi più componenti nuovi, è probabile che tu ne peschi meno di usati, perché hai solo 3 posti disponibili nel campione.

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
