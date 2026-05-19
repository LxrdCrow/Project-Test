TASK TEST TECNICO

- Preparare struttura MVC
- Flusso applicativo richiesto
 L’applicazione dovrà prevedere:
1. Una pagina di login (/login)
2. Inserimento credenziali da parte dell’utente
3. Verifica delle credenziali
4. Accesso alla dashboard (/dashboard) in caso di login valido
5. Visualizzazione di un messaggio di errore in caso di credenziali non valide
6. Accesso alla dashboard consentito solo agli utenti autenticati



- Livello 3 – Avanzato

Obiettivo 
Migliorare la struttura del progetto e introdurre funzionalità tipiche di un’applicazione strutturata. 
Struttura del progetto 
Si richiede una separazione logica del codice, ad esempio: 
project/ 
│── app.py 
│── controllers/ 
│   
│   
│ 
├── auth.py          
├── main.py         
│── models/ 
│   

# gestione login e registrazione 
 # gestione rotte principali (dashboard, ecc.) 

├── user_model.py    # accesso al database 
│ 
│── templates/ 
│   
│   
│   
│   
│ 
├── login.html 
├── register.html 
├── dashboard.html 
├── profile.html 
│── static/ 


Requisiti aggiuntivi 
• Separazione tra: 
o models: gestione accesso ai dati 
o controllers: gestione delle rotte e della logica applicativa 
• Implementazione di una pagina profilo (/profile) che permetta all’utente di: 
o visualizzare le informazioni principali 
o modificare la propria password 

• Implementazione della funzionalità di logout 


• Utilizzo di decoratori per proteggere le route 


NB. I casi di errore 'utente non esistente' e 'password errata' vado a restituire intenzionalmente lo stesso messaggio generico per prevenire user enumeration attacks (chiedere al Senior cosa preferisce)