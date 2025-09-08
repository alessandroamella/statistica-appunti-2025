# Spazi di Probabilità

### 1. L'Esperimento Aleatorio, lo Spazio Campionario e gli Eventi

Questa è la base di tutto. Se capisci bene questi concetti, il resto sarà in discesa.

#### **Teoria Semplice (Quello che ti serve per gli esercizi)**

Immagina la probabilità come un gioco. Ogni gioco ha delle regole e dei possibili risultati.

1.  **Esperimento Aleatorio**: È semplicemente un'azione o un processo il cui risultato non è noto con certezza prima di compierlo.

    - _Esempio concreto_: Lanciare un dado, lanciare una moneta, pescare una carta da un mazzo.

2.  **Spazio Campionario ($\Omega$)**: È l'insieme di **TUTTI** i possibili risultati di un esperimento aleatorio. Lo indichiamo con la lettera greca Omega maiuscola, $\Omega$.

    - _Esempio concreto (lancio di un dado)_: Quali sono tutti i risultati possibili? Può uscire 1, 2, 3, 4, 5, o 6. Quindi lo spazio campionario è:
      $\Omega = \{1, 2, 3, 4, 5, 6\}$
    - _Esempio concreto (lancio di una moneta)_: I risultati possibili sono Testa (T) o Croce (C).
      $\Omega = \{T, C\}$

3.  **Esito ($\omega$)**: È un singolo elemento dello spazio campionario. È _un_ possibile risultato.

    - _Esempio concreto (lancio di un dado)_: L'esito "esce il 4" è rappresentato dall'elemento $\omega = 4$.

4.  **Evento ($A, B, C, ...$)**: Un evento è una qualsiasi affermazione su un esperimento, che corrisponde a un **sottoinsieme** dello spazio campionario $\Omega$. In pratica, è un insieme di uno o più esiti che ci interessano.
    - _Esempio concreto (lancio di un dado)_:
      - Evento A: "Esce un numero pari". Quali esiti rendono vera questa affermazione? Il 2, il 4, e il 6. Quindi l'evento A è il sottoinsieme: $A = \{2, 4, 6\}$.
      - Evento B: "Esce un numero maggiore di 4". Gli esiti sono 5 e 6. Quindi: $B = \{5, 6\}$.
      - Evento C: "Esce il numero 3". L'esito è solo il 3. Quindi: $C = \{3\}$. Questo si chiama **evento elementare** perché contiene un solo esito.

**Tipi speciali di eventi:**

- **Evento Certo**: L'insieme $\Omega$ stesso. È un evento che si verifica sempre.
  - _Esempio (dado)_: "Esce un numero compreso tra 1 e 6". Questo è ovvio che accada. L'insieme è $\{1,2,3,4,5,6\}$, cioè $\Omega$.
- **Evento Impossibile**: L'insieme vuoto, $\emptyset$. È un evento che non si verifica mai.
  - _Esempio (dado)_: "Esce il numero 7". Non è possibile. L'insieme di esiti è vuoto, $\emptyset$.

---

### 2. Algebra degli Eventi (Come Tradurre le Parole in Matematica)

Questa è la parte più importante per risolvere gli esercizi della tua prima scheda. Devi imparare a tradurre le frasi in italiano ("almeno uno", "entrambi", "nessuno") nel linguaggio matematico degli insiemi.

#### **Teoria Semplice (La Tabella di Traduzione)**

Le operazioni tra eventi corrispondono a operazioni tra insiemi.

| Linguaggio Comune              | Connettivo Logico          | Operazione Insiemistica | Simbolo    | Significato Pratico                                                   | Diagramma di Venn |
| :----------------------------- | :------------------------- | :---------------------- | :--------- | :-------------------------------------------------------------------- | :---------------- |
| Evento A **O** Evento B        | Disgiunzione ($A \lor B$)  | **Unione**              | $A \cup B$ | Si verifica A, o B, o entrambi. Basta che se ne verifichi almeno uno. |                   |
| Evento A **E** Evento B        | Congiunzione ($A \land B$) | **Intersezione**        | $A \cap B$ | Si verificano **sia** A **che** B, contemporaneamente.                |                   |
| **NON** si verifica l'evento A | Negazione ($\neg A$)       | **Complementazione**    | $A^c$      | Tutti i risultati possibili tranne quelli che compongono A.           |                   |

**Altre relazioni importanti:**

- **Mutua Esclusione (Eventi Incompatibili)**: Due eventi A e B si escludono a vicenda se non possono accadere insieme. Matematicamente, la loro intersezione è vuota: $A \cap B = \emptyset$.
  - _Esempio (dado)_: A = "esce un numero pari" = $\{2,4,6\}$ e C = "esce il 3" = $\{3\}$. Non possono accadere insieme. $A \cap C = \emptyset$.
- **Implicazione**: L'evento A implica l'evento B se ogni volta che si verifica A, si verifica anche B. Matematicamente, A è un sottoinsieme di B: $A \subseteq B$.
  - _Esempio (dado)_: A = "esce il 2" = $\{2\}$ e B = "esce un numero pari" = $\{2,4,6\}$. Se esce il 2 (evento A), allora è anche uscito un numero pari (evento B). $A \subseteq B$.

#### **Esercizi Guidati (Traduciamo insieme!)**

Vediamo come applicare questa logica agli esercizi della tua scheda.

**Esercizio 2**
_Chiara e Marco acquistano un biglietto. Evento C = "il premio piacerà a Chiara", Evento M = "il premio piacerà a Marco"._

1.  **(a) il premio piacerà a entrambi**

    - **Logica**: Deve piacere a Chiara **E** deve piacere a Marco.
    - **Traduzione**: La parola "E" corrisponde all'intersezione.
    - **Formula**: $C \cap M$

2.  **(b) il premio piacerà ad almeno uno dei due**

    - **Logica**: Piace a Chiara **O** piace a Marco (o a entrambi).
    - **Traduzione**: La parola "O" (nel senso di "almeno uno") corrisponde all'unione.
    - **Formula**: $C \cup M$

3.  **(c) a nessuno dei due piacerà il premio**

    - **Logica**: **NON** piacerà a Chiara **E** **NON** piacerà a Marco.
    - **Traduzione**: "NON C" è $C^c$. "NON M" è $M^c$. La "E" è l'intersezione.
    - **Formula**: $C^c \cap M^c$.
    - **Trucco (Leggi di De Morgan)**: Questo è uguale a dire "NON (piacerà ad almeno uno)". Quindi è il complementare dell'unione: $(C \cup M)^c$. Le due formule sono equivalenti!

4.  **(d) il premio piacerà a uno solo dei due**
    - **Logica**: Piace a Chiara **E NON** a Marco, **O** piace a Marco **E NON** a Chiara.
    - **Traduzione**:
      - "Piace a Chiara E NON a Marco": $C \cap M^c$
      - "Piace a Marco E NON a Chiara": $M \cap C^c$
      - La "O" tra queste due frasi è un'unione.
    - **Formula**: $(C \cap M^c) \cup (M \cap C^c)$.
    - **Alternativa**: È come dire "piace ad almeno uno" ($C \cup M$) ma "togliamo il caso in cui piace a entrambi" ($C \cap M$). Matematicamente si scrive $(C \cup M) \setminus (C \cap M)$.

**Esercizio 3 (più astratto, ma stessa logica)**
_Tre eventi A, B, C._

1.  **(1) almeno un evento si verifica**

    - **Logica**: Si verifica A **O** si verifica B **O** si verifica C.
    - **Formula**: $A \cup B \cup C$

2.  **(3) nessun evento si verifica**

    - **Logica**: NON A **E** NON B **E** NON C.
    - **Formula**: $A^c \cap B^c \cap C^c$ (che è uguale a $(A \cup B \cup C)^c$)

3.  **(4) tutti gli eventi si verificano**

    - **Logica**: A **E** B **E** C.
    - **Formula**: $A \cap B \cap C$

4.  **(5) si verifica esattamente un evento**
    - **Logica**: (Si verifica A **E** non B **E** non C) **O** (Si verifica B **E** non A **E** non C) **O** (Si verifica C **E** non A **E** non B).
    - **Formula**: $(A \cap B^c \cap C^c) \cup (B \cap A^c \cap C^c) \cup (C \cap A^c \cap B^c)$

---

### 3. Assiomi di Probabilità e Calcolo Pratico

Ora che sappiamo descrivere gli eventi, associamogli un numero: la probabilità.

#### **Teoria Semplice (Le 3 Regole d'Oro e le Loro Conseguenze)**

La probabilità $\mathbb{P}(A)$ è un numero che associamo a un evento A. Deve rispettare 3 regole (assiomi di Kolmogorov):

1.  **Regola 1 (Non-negatività e Limitatezza)**: La probabilità di un evento è sempre un numero tra 0 e 1.
    $0 \leq \mathbb{P}(A) \leq 1$
    (Puoi pensarla come una percentuale: da 0% a 100%). $\mathbb{P}(A)=0$ significa impossibile, $\mathbb{P}(A)=1$ significa certo.

2.  **Regola 2 (Certezza)**: La probabilità dello spazio campionario (l'evento certo) è 1.
    $\mathbb{P}(\Omega) = 1$
    (È sicuro al 100% che si verifichi uno dei risultati possibili).

3.  **Regola 3 (Additività)**: Se due eventi A e B sono **incompatibili** (cioè $A \cap B = \emptyset$), la probabilità che si verifichi A **O** B è la somma delle loro probabilità.
    $\mathbb{P}(A \cup B) = \mathbb{P}(A) + \mathbb{P}(B)$ (SOLO se A e B sono incompatibili!)

Da queste 3 regole derivano tutte le formule che userai. Le più importanti sono:

- **Probabilità dell'evento complementare**: Questa è UTILISSIMA.
  $\mathbb{P}(A^c) = 1 - \mathbb{P}(A)$
  La probabilità che un evento NON accada è 1 meno la probabilità che accada.

- **Probabilità dell'unione (Formula Generale)**: Questa vale SEMPRE, anche se gli eventi non sono incompatibili.
  $\mathbb{P}(A \cup B) = \mathbb{P}(A) + \mathbb{P}(B) - \mathbb{P}(A \cap B)$
  **Perché si sottrae l'intersezione?** Pensa ai diagrammi di Venn. Se sommi l'area di A e l'area di B, hai contato la zona in comune ($A \cap B$) due volte. Devi toglierla una volta per avere l'area totale corretta.

- **Monotonia**: Se l'evento A implica l'evento B ($A \subseteq B$), allora la probabilità di A non può essere maggiore di quella di B.
  $\mathbb{P}(A) \leq \mathbb{P}(B)$

#### **Il Caso più Semplice e Comune: Spazi Equiprobabili**

La maggior parte degli esercizi base (lancio di dadi non truccati, monete, estrazione di carte...) rientra in questo caso.
Ci sono due condizioni:

1.  Lo spazio campionario $\Omega$ ha un numero **finito** di esiti.
2.  Ogni esito ha la **stessa probabilità** di verificarsi (dado "onesto", moneta "equilibrata").

In questo caso, il calcolo è facilissimo. Si usa la **Formula di Laplace**:

$\mathbb{P}(A) = \frac{\text{Numero di casi favorevoli ad A}}{\text{Numero di casi possibili totali}} = \frac{|A|}{|\Omega|}$

Dove $|A|$ è la cardinalità (il numero di elementi) dell'insieme A.

**Esempio Pratico (Lancio di un dado non truccato)**

- Evento A: "Esce un numero maggiore di 4".
- **Passo 1: Definire lo spazio campionario e contare i casi possibili.**
  $\Omega = \{1, 2, 3, 4, 5, 6\}$. I casi possibili sono 6. Quindi $|\Omega| = 6$.
- **Passo 2: Definire l'evento e contare i casi favorevoli.**
  L'evento A corrisponde agli esiti 5 e 6. $A = \{5, 6\}$. I casi favorevoli sono 2. Quindi $|A| = 2$.
- **Passo 3: Applicare la formula.**
  $\mathbb{P}(A) = \frac{|A|}{|\Omega|} = \frac{2}{6} = \frac{1}{3}$

#### **Esercizi Guidati (Calcoliamo insieme!)**

Vediamo ora un esercizio più complesso dalla tua scheda, che mette insieme tutto.

**Esercizio 8**
_Una ditta riceve richieste. Definiamo gli eventi:_

- $U$: "la consegna è urgente"
- $F$: "la consegna è fuori città"

_Dati del problema:_

1.  $\mathbb{P}(F) = 0.4$ (prob. che sia fuori città)
2.  $\mathbb{P}(U) = 0.3$ (prob. che sia urgente)
3.  $\mathbb{P}(U^c \cap F^c) = 0.4$ (prob. che sia NON urgente E in città (NON fuori città))

_Domande:_
(a) prob. che sia urgente E fuori città -> Calcolare $\mathbb{P}(U \cap F)$
(b) prob. che sia urgente E in città -> Calcolare $\mathbb{P}(U \cap F^c)$

_Svolgimento passo-passo:_

1.  **Lavoriamo sul dato (iii)**. Abbiamo $\mathbb{P}(U^c \cap F^c) = 0.4$. Ti ricordi le leggi di De Morgan? $U^c \cap F^c = (U \cup F)^c$. Questo significa "né urgente né fuori città" è il contrario di "almeno uno dei due".
2.  **Usiamo la formula del complementare**. Se la probabilità che un evento NON accada è 0.4, la probabilità che accada è:
    $\mathbb{P}(U \cup F) = 1 - \mathbb{P}((U \cup F)^c) = 1 - 0.4 = 0.6$
    Quindi, la probabilità che una consegna sia urgente O fuori città (o entrambe) è 0.6.
3.  **Adesso usiamo la formula dell'unione per trovare l'intersezione (domanda a).**
    $\mathbb{P}(U \cup F) = \mathbb{P}(U) + \mathbb{P}(F) - \mathbb{P}(U \cap F)$
    Conosciamo tutto tranne $\mathbb{P}(U \cap F)$. Riorganizziamo la formula:
    $\mathbb{P}(U \cap F) = \mathbb{P}(U) + \mathbb{P}(F) - \mathbb{P}(U \cup F)$
    $\mathbb{P}(U \cap F) = 0.3 + 0.4 - 0.6 = 0.1$
    **Risposta (a): La probabilità che sia urgente e fuori città è 0.1.**
4.  **Ora calcoliamo la domanda (b)**: $\mathbb{P}(U \cap F^c)$.
    Pensa all'evento "Urgente" ($U$). Può essere suddiviso in due casi incompatibili: "Urgente e Fuori città" ($U \cap F$) oppure "Urgente e In città" ($U \cap F^c$).
    Possiamo quindi scrivere:
    $\mathbb{P}(U) = \mathbb{P}(U \cap F) + \mathbb{P}(U \cap F^c)$
    Vogliamo trovare $\mathbb{P}(U \cap F^c)$. Riorganizziamo:
    $\mathbb{P}(U \cap F^c) = \mathbb{P}(U) - \mathbb{P}(U \cap F)$
    $\mathbb{P}(U \cap F^c) = 0.3 - 0.1 = 0.2$
    **Risposta (b): La probabilità che sia urgente e in città è 0.2.**

---

### 4. Riepilogo e Consigli per lo Studio

#### **Punti Chiave da Fissare in Mente**

- **Evento = Sottoinsieme**. Questa è l'idea centrale.
- **La Tabella di Traduzione**: Impara a memoria come "E", "O", "NON" si traducono in $\cap, \cup, ^c$. È fondamentale.
- **Le 3 Formule Magiche**:
  1.  $\mathbb{P}(A^c) = 1 - \mathbb{P}(A)$
  2.  $\mathbb{P}(A \cup B) = \mathbb{P}(A) + \mathbb{P}(B) - \mathbb{P}(A \cap B)$
  3.  $\mathbb{P}(A) = \frac{\text{casi favorevoli}}{\text{casi possibili}}$ (solo per casi equiprobabili)
- Disegnare i **diagrammi di Venn** ti salverà la vita quando sei confuso.

#### **Come Studiare Questo Argomento**

1.  **Rifai gli esercizi di traduzione (2, 3, 4, 5)** senza guardare la soluzione. Prendi il testo e scrivi la formula. Poi controlla. Devi diventare una macchina in questo.
2.  Per ogni esercizio di calcolo, **scrivi sempre i dati in modo formale** ($\mathbb{P}(A)=...$, $\mathbb{P}(B)=...$) come ho fatto io per l'esercizio 8. Questo chiarisce le idee.
3.  Prima di applicare la formula "casi favorevoli / casi possibili", chiediti sempre: "Gli esiti sono equiprobabili?". Se il testo dice "dado truccato" o dà probabilità diverse per esiti diversi, allora NON puoi usarla.

#### **Errori Comuni da Evitare**

1.  **Dimenticare di sottrarre $\mathbb{P}(A \cap B)$**. L'errore più comune in assoluto. Ricorda che $\mathbb{P}(A \cup B) = \mathbb{P}(A) + \mathbb{P}(B)$ vale **SOLO** se A e B sono incompatibili. La formula generale ha il "- $\mathbb{P}(A \cap B)$".
2.  **Confondere "incompatibile" con "indipendente"**. Per ora non hai ancora fatto l'indipendenza, ma tienilo a mente. "Incompatibile" ($A \cap B = \emptyset$) significa che non possono accadere insieme. È un concetto legato agli insiemi.
3.  **Sbagliare a contare i casi**. Quando definisci $\Omega$ e A, sii metodico. Scrivi tutti gli elementi se sono pochi, per essere sicuro di non perderne nessuno. Ad esempio, per il lancio di due monete (Esercizio 4), lo spazio campionario è $\Omega = \{(T,T), (T,C), (C,T), (C,C)\}$, non sono 3 esiti ma 4!
