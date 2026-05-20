TASK TEST TECNICO

- Migliorare templates
- Eventualmente modificare controllers dividendo in due file invece di tenere user_controller.py
- Testing


- Livello 3 – Avanzato

Obiettivo 
Migliorare la struttura del progetto e introdurre funzionalità tipiche di un’applicazione strutturata. 
Struttura del progetto 
Si richiede una separazione logica del codice, ad esempio: 


project/ 
│── app.py 
│── controllers/  
│ 
├── auth.py     #  gestione login e registrazione
├── main.py     #  gestione rotte principali (dashboard, ecc.) 
│         
│── models/ 
│ 
├── user_model.py    # accesso al database 
│ 
│── templates/ 
│ 
├── login.html 
├── register.html 
├── dashboard.html 
├── profile.html 
│── static/ 








