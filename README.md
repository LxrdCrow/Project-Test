TASK TEST TECNICO

- Preparare struttura app.py
- Cercare template grafico online bootstrap
- Flusso applicativo richiesto
 L’applicazione dovrà prevedere:
1. Una pagina di login (/login)
2. Inserimento credenziali da parte dell’utente
3. Verifica delle credenziali
4. Accesso alla dashboard (/dashboard) in caso di login valido
5. Visualizzazione di un messaggio di errore in caso di credenziali non valide
6. Accesso alla dashboard consentito solo agli utenti autenticati

- Cominciare a strutturare il progetto Liv. 1:

• Pagina di login funzionante
• Verifica delle credenziali tramite codice
• Redirect alla dashboard in caso di login corretto
• Messaggio di errore in caso di login non valido
• Utilizzo delle sessioni Flask per mantenere lo stato dell’utente
• Protezione della pagina /dashboard, accessibile solo se l’utente è autenticato


- Pensare al database e avanzamento Liv. 2:

Estendere l’applicazione introducendo un database per la gestione degli utenti.
È richiesto l’utilizzo di un database semplice, preferibilmente SQLite.

• Il login deve essere verificato tramite query al database
• Implementazione della pagina di registrazione (/register)
• Possibilità di creare nuovi utenti
• Gestione dei casi di errore:

    o utente non esistente
    o password errata