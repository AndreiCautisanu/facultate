# Performanța algoritmului random search pentru găsirea minimului a 4 funcții de optimizare

-- Andrei Căutișanu, 2E2
-- Tema T0


---

### Despre experiment
Experimentul are scopul de a observa acuratețea căutării random pe 4 funcții de optimizare, folosind dimensiunile 2, 5 și 20. În același timp se va putea observa rata creșterii dificultății de calcul a funcției pe măsură ce creștem numărul de dimensiuni. 

Vom folosi o formă simplă a căutării aleatorii, script-ul Python 3 va fi lăsat timp 3 minute să calculeze funcția pentru parametri selectați cu funcția random.uniform din pachetul random. Repetând de 30 de ori această căutare pentru fiecare număr de dimensiuni ale celor 4 funcții, vom obține date despre minimul găsit de algoritm și despre câte valori obține algoritmul în timpul enunțat.

---

### Funcțiile alese

- **Rastrigin**
    ![](https://www.sfu.ca/~ssurjano/rastr2.png)
    Minimul global al funcției este 0, când toți parametrii au valoarea 0.
    x~i~ ∈ [-5.12, 5.12], pentru i = 1, ..., d

    Graficul funcției cu 2 parametri:
    ![](https://www.sfu.ca/~ssurjano/rastr.png)
    
- **Ackley**
    ![](https://www.sfu.ca/~ssurjano/ackley2.png)
    Valorile folosite sunt a=20, b=0.2, c=2π
    Minimul global al funcției este 0, când toți parametrii au valoarea 0
    x~i~ ∈ [-32.768, 32.768], pentru i = 1, ..., d

    Graficul funcției cu 2 parametri:
    ![](https://www.sfu.ca/~ssurjano/ackley.png)
    
- **Dixon-Price**
    ![](https://www.sfu.ca/~ssurjano/dixonpr2.png)
    Minimul global al funcției: 
    ![](https://www.sfu.ca/~ssurjano/dixonpr3.png)
    x~i~ ∈ [-10, 10], pentru i = 1, ..., d

    Graficul funcției cu 2 parametri:
    ![](https://www.sfu.ca/~ssurjano/dixonpr.png)
    
- **Rosembrock**
    ![](https://www.sfu.ca/~ssurjano/rosen2.png)
    Minimul global al funcției este 0, când toți parametrii au valoarea 1
    x~i~ ∈ [-2.048, 2.048], pentru i = 1, ..., d

    Graficul funcției cu 2 parametri:
    ![](https://www.sfu.ca/~ssurjano/rosen.png)
    
---

### Nefezabilitatea unei metode deterministe
O metodă deterministă, precum căutarea exhaustivă, nu va putea găsi minimul global al acestor cu certitudine într-un timp finit, întrucât în intervalele de definiție ale acestora se regăsesc o infinitate de numere, iar odată ce stabilim o limită de precizie, pierdem certitudinea că vom găsi minimul exact (e.g. parcurgem intervalul [1, 3] cu precizie pas de 0.0001, iar minimul global se găsește la f(1.50005, 2))

De asemenea, pe măsură ce creștem numărul de dimensiuni, intervine constrângerea timpului și a numărului de operații. Luând ca exemplu funcția Rastrigin, dacă am dori să parcurgem intervalul [-5.12, 5.12] cu o precizie de 0.01, am fi nevoiți să procesăm 1024 de numere, aproximativ 10^3. Dacă pe 2 dimensiuni, asta înseamnă doar (10^3^)^2^ = 10^6^ calcule ale funcției, la 20 de parametri, numărul crește la 10^60^ de operații. Astfel, pentru a căuta exhaustiv pe mai multe dimensiuni, suntem nevoiți să reducem drastic precizia, astfel scăzând șansa de a găsi minimul global.

---

### Rezultatele Random Search pe cele 4 funcții
    
    
    
    