# Event Manager

**Studentessa:** Alice Caldini  
**Tipo di progetto:** Full-Stack Web Application  
**Framework:** Django 6.0.6  

## Descrizione
Event Manager è un'applicazione web per la gestione di eventi. Gli organizzatori possono creare, modificare ed eliminare eventi, mentre i partecipanti possono registrarsi agli eventi disponibili.

## Funzionalità per ruolo

### Organizer
- Creare nuovi eventi
- Modificare i propri eventi
- Eliminare i propri eventi
- Visualizzare la lista dei partecipanti

### Attendee
- Visualizzare la lista degli eventi
- Visualizzare il dettaglio di un evento
- Registrarsi a un evento
- Annullare la propria registrazione

## Installazione locale
```bash
git clone https://github.com/alicaldini/Event_Manager.git
cd Event_Manager
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Database
Il file di database SQLite incluso nel repository si chiama `db.sqlite3`. Si conferma che il file contiene già dati dimostrativi e gli account demo funzionanti descritti di seguito.

## Account demo
I seguenti account sono già registrati nel database demo per testare l'applicazione:
| Username | Password | Ruolo |
|----------|----------|-------|
| admin_demo | admin12345 | Amministratore |
| organizer_demo | organizer12345 | Organizzatore evento |
| attendee_demo | attendee12345 | Partecipante |

## Link al Deploy Online
L'applicazione è stata pubblicata ed è raggiungibile online al seguente indirizzo:    
**https://alicaldini4.pythonanywhere.com**

Per valutare le funzionalità dei diversi ruoli in produzione, è possibile effettuare il login utilizzando gli account demo sopra elencati direttamente dal browser.