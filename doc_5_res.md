# Variabili Aleatorie Continue

### 1. Variabili Aleatorie Continue: L'Idea di Base

Immagina di lanciare una freccetta su un bersaglio. Qual è la probabilità di colpire _esattamente_ il punto centrale, un punto infinitesimale senza dimensioni? La probabilità è zero. È praticamente impossibile.

Le variabili aleatorie continue (v.a.c.) funzionano così. Descrivono quantità che possono assumere un'infinità di valori in un intervallo (altezza, peso, tempo, temperatura). La probabilità che una v.a.c. $X$ assuma _esattamente_ un valore $x$ è sempre zero.

$\mathbb{P}(X = x) = 0$

**Allora come calcoliamo le probabilità?**
Non parliamo di punti singoli, ma di **intervalli**. Chiediamo: "Qual è la probabilità che l'altezza di una persona sia _tra_ 170 cm e 180 cm?". Questa probabilità sarà maggiore di zero.

### 2. La Funzione di Densità di Probabilità (PDF - Probability Density Function)

Per calcolare la probabilità su un intervallo, usiamo uno strumento chiamato **funzione di densità di probabilità**, indicata con $f_X(x)$.

Puoi immaginarla come un grafico. La probabilità di cadere in un intervallo $[a, b]$ è l'**area sotto il grafico** della funzione di densità in quell'intervallo.

Una funzione $f(x)$ è una densità valida se rispetta due regole ferree:

1.  **È sempre non-negativa:** $f(x) \ge 0$ per ogni $x$. (Non esistono aree negative).
2.  **L'area totale sotto la curva è 1:** $\int_{-\infty}^{+\infty} f(x) dx = 1$. (La probabilità totale di tutti i possibili risultati è il 100%).

La formula chiave per calcolare la probabilità è:
$\mathbb{P}(a \le X \le b) = \int_{a}^{b} f_X(x) dx$

**Nota importantissima:** Poiché $\mathbb{P}(X=a)=0$ e $\mathbb{P}(X=b)=0$, non fa alcuna differenza se gli estremi dell'intervallo sono inclusi o esclusi.
$\mathbb{P}(a \le X \le b) = \mathbb{P}(a < X < b) = \mathbb{P}(a \le X < b) = \mathbb{P}(a < X \le b)$
Questo è un grande vantaggio rispetto alle variabili discrete!

---

#### ESERCIZIO TIPO 1: Trovare la costante di normalizzazione

Questo è l'esercizio più classico. Ti danno una densità con una costante `c` (o `a`, o `k`) e ti chiedono di trovarla. Come si fa? Usando la regola che l'area totale deve essere 1.

Vediamo l'**Esercizio 1(a)** dalla tua scheda.
La densità del raggio $R$ è:
$f_R(x) = \begin{cases} cxe^{-x^2} & \text{per } x > 0 \\ 0 & \text{per } x \le 0 \end{cases}$

**Svolgimento:**

1.  **Imposta l'integrale:** Sappiamo che l'integrale della densità su tutto il suo dominio deve fare 1.
    $\int_{-\infty}^{+\infty} f_R(x) dx = 1$

2.  **Spezza l'integrale:** La funzione è definita a tratti. Per $x \le 0$ è zero, quindi quell'integrale è nullo. Dobbiamo solo considerare la parte per $x > 0$.
    $\int_{-\infty}^{0} 0 \, dx + \int_{0}^{+\infty} cxe^{-x^2} dx = 1$
    $0 + c \int_{0}^{+\infty} xe^{-x^2} dx = 1$

3.  **Risolvi l'integrale:** Questo integrale si risolve con una sostituzione. Sembra complicato, ma è un trucco che vedrai spesso.

    - Sia $u = x^2$.
    - Allora il differenziale è $du = 2x \, dx$, che possiamo riscrivere come $x \, dx = \frac{du}{2}$.
    - Dobbiamo anche cambiare gli estremi di integrazione:
      - Quando $x=0$, $u=0^2=0$.
      - Quando $x \to +\infty$, $u \to +\infty$.
    - Sostituiamo tutto nell'integrale:
      $c \int_{0}^{+\infty} e^{-u} \frac{du}{2} = 1$

4.  **Calcola e risolvi per c:**
    $\frac{c}{2} \int_{0}^{+\infty} e^{-u} du = 1$
    L'integrale di $e^{-u}$ è $-e^{-u}$.
    $\frac{c}{2} \left[ -e^{-u} \right]_{0}^{+\infty} = 1$
    $\frac{c}{2} \left( (-e^{-\infty}) - (-e^{-0}) \right) = 1$
    Ricorda che $e^{-\infty} = 0$ e $e^0 = 1$.
    $\frac{c}{2} \left( 0 - (-1) \right) = 1$
    $\frac{c}{2} (1) = 1 \implies c = 2$

Fatto! Il valore della costante è **2**.

---

### 3. La Funzione di Ripartizione (CDF - Cumulative Distribution Function)

La funzione di ripartizione $F_X(x)$ ti dà la probabilità che la variabile $X$ sia **minore o uguale** a un certo valore $x$. È l'area sotto la curva di densità partendo da $-\infty$ fino al punto $x$.

$F_X(x) = \mathbb{P}(X \le x) = \int_{-\infty}^{x} f_X(t) dt$

**Proprietà della CDF:**

- È sempre crescente, da 0 a 1.
- $\lim_{x \to -\infty} F_X(x) = 0$
- $\lim_{x \to +\infty} F_X(x) = 1$
- Per le v.a.c., la CDF è una funzione **continua**.

**Relazione fondamentale tra PDF e CDF:**
Se la CDF è l'integrale della PDF, allora la PDF è la **derivata** della CDF!
$f_X(x) = \frac{d}{dx} F_X(x) = F'_X(x)$

Questa doppia relazione è la chiave per risolvere metà degli esercizi.

---

#### ESERCIZIO TIPO 2: Dal PDF al CDF

Vediamo l'**Esercizio 1(b)**. Ci chiede di trovare la funzione di ripartizione $F_R(x)$ partendo dalla densità che ora conosciamo:
$f_R(x) = \begin{cases} 2xe^{-x^2} & \text{per } x > 0 \\ 0 & \text{per } x \le 0 \end{cases}$

**Svolgimento:**
Dobbiamo calcolare $F_R(x) = \int_{-\infty}^{x} f_R(t) dt$. Dobbiamo analizzare due casi, a seconda del valore di $x$.

**Caso 1: $x \le 0$**
In questo caso, stiamo integrando su un intervallo in cui la densità $f_R(t)$ è sempre 0.
$F_R(x) = \int_{-\infty}^{x} 0 \, dt = 0$

**Caso 2: $x > 0$**
Qui l'integrale va spezzato in due parti: da $-\infty$ a 0 (dove la funzione è 0) e da 0 a $x$ (dove la funzione è $2te^{-t^2}$).
$F_R(x) = \int_{-\infty}^{0} 0 \, dt + \int_{0}^{x} 2te^{-t^2} dt$
$F_R(x) = 0 + \left[ -e^{-t^2} \right]_{0}^{x}$ (l'integrale è lo stesso di prima, ma con $c=2$)
$F_R(x) = (-e^{-x^2}) - (-e^{-0^2})$
$F_R(x) = -e^{-x^2} + 1 = 1 - e^{-x^2}$

**Mettendo insieme i pezzi:**
La funzione di ripartizione è:
$F_R(x) = \begin{cases} 0 & \text{per } x \le 0 \\ 1 - e^{-x^2} & \text{per } x > 0 \end{cases}$
Questa è la soluzione riportata nel file.

---

#### ESERCIZIO TIPO 3: Dal CDF al PDF

Vediamo l'**Esercizio 3(a)**. Ci danno la CDF e vogliono la PDF.
$F_X(x) = \begin{cases} 0 & \text{per } x \le 0 \\ (1-e^{-x})^2 & \text{per } x > 0 \end{cases}$

**Svolgimento:**
Dobbiamo semplicemente derivare la $F_X(x)$ in ogni suo tratto.
$f_X(x) = F'_X(x)$

**Caso 1: $x < 0$**
$F_X(x) = 0 \implies f_X(x) = \frac{d}{dx}(0) = 0$

**Caso 2: $x > 0$**
$F_X(x) = (1-e^{-x})^2$. Usiamo la regola della catena per la derivata: $D[g(x)^n] = n \cdot g(x)^{n-1} \cdot g'(x)$.
$f_X(x) = \frac{d}{dx} (1-e^{-x})^2 = 2(1-e^{-x})^{2-1} \cdot \frac{d}{dx}(1-e^{-x})$
$f_X(x) = 2(1-e^{-x}) \cdot (0 - e^{-x} \cdot (-1))$
$f_X(x) = 2(1-e^{-x}) \cdot (e^{-x}) = 2e^{-x} - 2e^{-2x}$
_Nota: La soluzione del prof scrive $2(e^{-x} - e^{-2x})$ che è la stessa cosa. In $x=0$ la funzione non è derivabile, ma per le v.a.c. il valore in un singolo punto non conta, quindi possiamo definirlo come 0._

**Mettendo insieme i pezzi:**
$f_X(x) = \begin{cases} 0 & \text{per } x \le 0 \\ 2(e^{-x} - e^{-2x}) & \text{per } x > 0 \end{cases}$

---

### 4. Media (Valore Atteso) e Varianza

I concetti sono gli stessi del caso discreto, ma le sommatorie sono sostituite dagli integrali.

**Media o Valore Atteso (E[X])**
È il "baricentro" della distribuzione.
$E[X] = \mu = \int_{-\infty}^{+\infty} x \cdot f_X(x) dx$

**Varianza (Var(X))**
Misura quanto i valori sono "dispersi" attorno alla media.
$Var(X) = \sigma^2 = E[(X-\mu)^2] = \int_{-\infty}^{+\infty} (x-\mu)^2 f_X(x) dx$

**Formula di calcolo per la Varianza (più facile!)**
Come nel caso discreto, è quasi sempre più semplice usare questa:
$Var(X) = E[X^2] - (E[X])^2$
dove $E[X^2]$ (il momento secondo) si calcola così:
$E[X^2] = \int_{-\infty}^{+\infty} x^2 \cdot f_X(x) dx$

---

#### ESERCIZIO TIPO 4: Calcolo di Media e Varianza

Vediamo l'**Esercizio 4(b)**. Ci chiede media e varianza di $X$ con CDF:
$F_X(x) = \begin{cases} 0 & \text{per } x < 1 \\ 1 - e^{1-x} & \text{per } x \ge 1 \end{cases}$

**Svolgimento:**

1.  **Prima, trovare la PDF $f_X(x)$:** Dobbiamo derivare la CDF.

    - Per $x < 1$, $f_X(x) = \frac{d}{dx}(0) = 0$.
    - Per $x > 1$, $f_X(x) = \frac{d}{dx}(1 - e^{1-x}) = 0 - (e^{1-x} \cdot (-1)) = e^{1-x}$.
      Quindi, $f_X(x) = \begin{cases} 0 & \text{per } x < 1 \\ e^{1-x} & \text{per } x \ge 1 \end{cases}$

2.  **Calcolare la Media $E[X]$:**
    $E[X] = \int_{-\infty}^{+\infty} x \cdot f_X(x) dx = \int_{1}^{+\infty} x e^{1-x} dx$
    Questo integrale si risolve per parti ($\int u dv = uv - \int v du$).

    - Sia $u = x \implies du = dx$.
    - Sia $dv = e^{1-x} dx \implies v = \int e^{1-x} dx = -e^{1-x}$.
      - $E[X] = \left[ -xe^{1-x} \right]_{1}^{+\infty} - \int_{1}^{+\infty} (-e^{1-x}) dx =$ \
        $= \left( \lim*{x \to \infty} -xe^{1-x} - (-1 \cdot e^{1-1}) \right) + \int*{1}^{+\infty} e^{1-x} dx$
      - Il limite $\lim_{x \to \infty} -xe^{1-x}$ fa 0 (l'esponenziale "vince" sulla $x$).
      - $E[X] = (0 - (-1 \cdot e^0)) + \left[ -e^{1-x} \right]_{1}^{+\infty} =$ \
        $= 1 + \left( (-e^{-\infty}) - (-e^{1-1}) \right) =$ \
        $= 1 + (0 - (-1)) = 1 + 1 = 2$.

3.  **Calcolare $E[X^2]$:**
    $E[X^2] = \int_{-\infty}^{+\infty} x^2 \cdot f_X(x) dx = \int_{1}^{+\infty} x^2 e^{1-x} dx$
    Altro integrale per parti.

    - $u = x^2 \implies du = 2x \, dx$.
    - $dv = e^{1-x} dx \implies v = -e^{1-x}$.
      - $E[X^2] = \left[ -x^2 e^{1-x} \right]_{1}^{+\infty} - \int_{1}^{+\infty} (-e^{1-x}) (2x \, dx)$
      - Il primo pezzo fa $(0 - (-1^2 e^0)) = 1$.
      - $E[X^2] = 1 + 2 \int_{1}^{+\infty} x e^{1-x} dx$
      - Ma hey! L'integrale $\int_{1}^{+\infty} x e^{1-x} dx$ è proprio $E[X]$, che abbiamo già calcolato essere 2!
      - $E[X^2] = 1 + 2 \cdot E[X] = 1 + 2 \cdot 2 = 5$.

4.  **Calcolare la Varianza $Var(X)$:**
    $Var(X) = E[X^2] - (E[X])^2 = 5 - (2)^2 = 5 - 4 = 1$.

Media = 2, Varianza = 1.

---

### Riassunto Punti Chiave (Parte 1)

- **v.a. continua:** $\mathbb{P}(X=x)=0$. Si lavora sempre con intervalli.
- **Densità (PDF) $f_X(x)$:** Funzione $\ge 0$ la cui area totale è 1.
- **Probabilità:** $\mathbb{P}(a \le X \le b)$ è l'area sotto $f_X(x)$ da $a$ a $b$, cioè $\int_a^b f_X(x) dx$.
- **Ripartizione (CDF) $F_X(x)$:** È la probabilità cumulativa $\mathbb{P}(X \le x)$, cioè $\int_{-\infty}^x f_X(t) dt$.
- **Legame PDF-CDF:** $f_X(x) = F'_X(x)$. Uno è la derivata dell'altro.
- **Media e Varianza:** Si calcolano con gli integrali. Usa sempre $Var(X) = E[X^2] - (E[X])^2$.

---

### 5. Distribuzioni Continue Notevoli

Queste sono famiglie di v.a.c. che compaiono così spesso da avere un nome. Devi conoscerne la forma, la media e la varianza.

| Distribuzione    | Densità $f_X(x)$                                              | Parametri                            | Media $E[X]$        | Varianza $Var(X)$     | Uso Tipico                           |
| :--------------- | :------------------------------------------------------------ | :----------------------------------- | :------------------ | :-------------------- | :----------------------------------- |
| **Uniforme**     | $\frac{1}{b-a}$ per $x \in [a, b]$                            | $a, b$ (estremi)                     | $\frac{a+b}{2}$     | $\frac{(b-a)^2}{12}$  | Scelta casuale in un intervallo.     |
| **Esponenziale** | $\lambda e^{-\lambda x}$ per $x > 0$                          | $\lambda > 0$ (tasso)                | $\frac{1}{\lambda}$ | $\frac{1}{\lambda^2}$ | Tempo di vita, tempo d'attesa.       |
| **Normale**      | $\frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{(x-\mu)^2}{2\sigma^2}}$ | $\mu$ (media), $\sigma^2$ (varianza) | $\mu$               | $\sigma^2$            | Fenomeni naturali, errori di misura. |

#### Distribuzione Esponenziale

L'**Esercizio 8** è un tipico problema sull'Esponenziale.
$X \sim Ex\mathbb{P}(\lambda)$ con $\lambda = 0.001$.
$f_X(x) = 0.001 e^{-0.001x}$ per $x \ge 0$.
La CDF dell'esponenziale è $F_X(x) = 1 - e^{-\lambda x}$ per $x \ge 0$.

**Punto (a):** Probabilità che la lampadina duri per tutto marzo (31 giorni).

- Le ore sono $31 \text{ giorni} \times 24 \text{ ore/giorno} = 744 \text{ ore}$.
- Chiede $\mathbb{P}(X > 744)$.
- È più facile calcolare il complementare: $\mathbb{P}(X > 744) = 1 - \mathbb{P}(X \le 744)$.
- $\mathbb{P}(X \le 744) = F_X(744) = 1 - e^{-0.001 \cdot 744} = 1 - e^{-0.744}$.
- Quindi, $\mathbb{P}(X > 744) = 1 - (1 - e^{-0.744}) = e^{-0.744} \approx 0.4752$.
- C'è circa il 47.5% di probabilità che la lampadina sopravviva a marzo.

#### Distribuzione Normale (o Gaussiana)

Questa è LA PIÙ IMPORTANTE. La incontrerai ovunque.

Una v.a. $X \sim N(\mu, \sigma^2)$ ha una forma a campana, centrata su $\mu$ e con una "larghezza" data da $\sigma$.

**Problema:** La densità della Normale è impossibile da integrare a mano!
**Soluzione:** Si usa una "scorciatoia". Tutte le variabili normali possono essere ricondotte a una sola, la **Normale Standard**, indicata con $Z$.

**La Normale Standard $Z \sim N(0,1)$**
È una normale con media $\mu=0$ e varianza $\sigma^2=1$ (e quindi deviazione standard $\sigma=1$).
La sua funzione di ripartizione si indica con una lettera speciale, $\Phi(z)$.
$\Phi(z) = \mathbb{P}(Z \le z)$
I valori di $\Phi(z)$ si trovano in apposite tavole statistiche o si calcolano con software/calcolatrici.

**La Formula Magica: Standardizzazione**
Per trasformare qualsiasi v.a. normale $X \sim N(\mu, \sigma^2)$ nella normale standard $Z$ si usa questa formula:
$Z = \frac{X - \mu}{\sigma}$

**Proprietà utili di $\Phi(z)$ (da imparare a memoria!):**

- $\mathbb{P}(Z > a) = 1 - \mathbb{P}(Z \le a) = 1 - \Phi(a)$
- $\mathbb{P}(a < Z < b) = \mathbb{P}(Z \le b) - \mathbb{P}(Z \le a) = \Phi(b) - \Phi(a)$
- **Simmetria:** La campana è simmetrica attorno a 0. Questo implica:
  $\Phi(-z) = 1 - \Phi(z)$

---

#### ESERCIZIO TIPO 5: Problema con la Normale

Vediamo l'**Esercizio 9(a)**.
Le sbarre sono accettabili se il diametro $X$ è tra 3.95 e 4.05 cm.
Sappiamo che $X \sim N(\mu=4, \sigma^2=0.09)$.
**Attenzione!** $0.09$ è la varianza $\sigma^2$. La deviazione standard $\sigma$ è la radice quadrata: $\sigma = \sqrt{0.09} = 0.3$. Questo è un errore comune!

**Svolgimento:**

1.  **Scrivi la probabilità richiesta:**
    $\mathbb{P}(3.95 \le X \le 4.05)$

2.  **Standardizza tutto:** Sottrai la media $\mu=4$ e dividi per la deviazione standard $\sigma=0.3$ a tutti i membri della disuguaglianza.
    $P\left(\frac{3.95 - 4}{0.3} \le \frac{X - 4}{0.3} \le \frac{4.05 - 4}{0.3}\right)$

3.  **Sostituisci con Z e calcola i valori:**
    Il termine in mezzo è $Z$.
    $\frac{3.95 - 4}{0.3} = \frac{-0.05}{0.3} \approx -0.167$
    $\frac{4.05 - 4}{0.3} = \frac{0.05}{0.3} \approx 0.167$
    La probabilità diventa:
    $\mathbb{P}(-0.167 \le Z \le 0.167)$

4.  **Usa le formule di $\Phi(z)$:**
    $\mathbb{P}(-0.167 \le Z \le 0.167) = \Phi(0.167) - \Phi(-0.167)$
    Ora usiamo la proprietà di simmetria $\Phi(-z) = 1 - \Phi(z)$:
    $= \Phi(0.167) - (1 - \Phi(0.167))$
    $= \Phi(0.167) - 1 + \Phi(0.167)$
    $= 2\Phi(0.167) - 1$
    (Il prof nella soluzione si ferma a $\Phi(0.167) - \Phi(-0.167)$, che è la forma richiesta dall'esercizio. Entrambe sono corrette).

---

### 6. Funzioni di Variabili Aleatorie

A volte non ci interessa $X$, ma una sua trasformazione, $Y = h(X)$. (Es. $Y=X^2$, $Y=5X$, $Y=e^X$). Come troviamo la densità di $Y$?

**Il Metodo Universale (via CDF)**
Questo metodo funziona sempre ed è quello che il prof usa.

1.  **Scrivi la CDF di Y:** Inizia sempre da qui: $F_Y(y) = \mathbb{P}(Y \le y)$.
2.  **Sostituisci $Y=h(X)$:** $F_Y(y) = \mathbb{P}(h(X) \le y)$.
3.  **Isola X:** Manipola la disuguaglianza per isolare $X$. **Questo è il passaggio cruciale**. Fai attenzione a come cambia il verso della disuguaglianza se moltiplichi/dividi per numeri negativi o applichi funzioni non monotone.
4.  **Riconduci alla CDF di X:** La probabilità che ottieni sarà nella forma $\mathbb{P}(X \le \dots)$, che è proprio $F_X(\dots)$.
5.  **Trova la PDF di Y:** Deriva $F_Y(y)$ rispetto a $y$ per ottenere $f_Y(y)$.

---

#### ESERCIZIO TIPO 6: Trovare la densità di Y=h(X)

Vediamo l'**Esercizio 8(b)**.
Sappiamo che $X \sim Ex\mathbb{P}(0.001)$ e $Y=5X$. Vogliamo la densità di $Y$.

**Svolgimento:**

1.  **CDF di Y:** $F_Y(y) = \mathbb{P}(Y \le y)$.

2.  **Sostituisci:** $F_Y(y) = \mathbb{P}(5X \le y)$.

3.  **Isola X:** Divido per 5 (che è positivo, quindi il verso non cambia).
    $F_Y(y) = P\left(X \le \frac{y}{5}\right)$.

4.  **Riconduci a $F_X$:** Hey, $\mathbb{P}(X \le \text{qualcosa})$ è la definizione della CDF di $X$!
    $F_Y(y) = F_X\left(\frac{y}{5}\right)$.
    Noi conosciamo la CDF dell'esponenziale: $F_X(x) = 1-e^{-0.001x}$. Quindi:
    $F_Y(y) = 1 - e^{-0.001 \cdot (y/5)} = 1 - e^{-0.0002y}$.
    _Nota_: Poiché $X$ può essere solo $\ge 0$, anche $Y=5X$ sarà $\ge 0$. Quindi questa formula vale per $y \ge 0$. Per $y < 0$, $F_Y(y) = 0$.

5.  **Deriva per trovare $f_Y(y)$:**
    $f_Y(y) = \frac{d}{dy} F_Y(y) = \frac{d}{dy}(1 - e^{-0.0002y})$
    $f_Y(y) = 0 - (e^{-0.0002y} \cdot (-0.0002)) = 0.0002 e^{-0.0002y}$.
    Questa è la densità per $y \ge 0$. Per $y < 0$ è 0.

Abbiamo trovato che $Y$ è ancora una variabile esponenziale, ma con un nuovo parametro $\lambda_Y = 0.0002$.

---

### Consigli Finali e Errori da Evitare

**Come Studiare:**

1.  **Focalizzati sugli schemi:** Per ogni tipo di esercizio (trova c, PDF->CDF, CDF->PDF, Normale, Funzione di v.a.), impara a memoria i passaggi. Sono sempre quelli.
2.  **Rifai gli esercizi della scheda:** Non guardarli e basta. Prenditi un foglio bianco e rifalli da solo, dall'inizio alla fine. Controlla la soluzione solo se sei bloccato.
3.  **Occhio alla Normale:** È l'argomento più gettonato. Devi essere un fulmine a standardizzare e a usare le proprietà di $\Phi(z)$.
4.  **Non perdere tempo sui dettagli teorici:** Il prof vuole che tu sappia fare gli esercizi. Concentrati sui metodi di calcolo.

**Errori Comuni da Evitare:**

- **Confondere PDF e CDF:** Ricorda, PDF si integra per trovare la probabilità, CDF è già una probabilità.
- **Sbagliare gli estremi di integrazione:** Fai sempre un disegno mentale della funzione a tratti per capire da dove a dove devi integrare.
- **Dimenticare la costante di integrazione... ah no, qui non serve!** Ma dimenticare il `dx` o sbagliare il cambio di variabile è comune.
- **Normale: $\sigma$ vs $\sigma^2$**: L'errore numero uno. La distribuzione è $N(\mu, \sigma^2)$, ma nella formula di standardizzazione si usa $\sigma$. Estrai sempre la radice quadrata!
- **Funzioni di v.a.:** Sbagliare ad isolare $X$ nella disuguaglianza $h(X) \le y$. Se $h$ è decrescente, il verso cambia! (es. $h(x)=-2x$).
- **Calcoli:** Un segno sbagliato in un integrale e tutto il risultato è errato. Procedi con calma e ricontrolla i passaggi algebrici.
