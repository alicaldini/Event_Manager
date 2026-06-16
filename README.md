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
Il file `db.sqlite3` è incluso nel repository e contiene dati demo già pronti.

## Account demo
| Username | Password | Ruolo |
|----------|----------|-------|
| admin_demo | admin12345 | Amministratore |
| organizer_demo | organizer12345 | Organizzatore evento |
| attendee_demo | attendee12345 | Partecipante |

## Deploy
Il sito è disponibile online all'indirizzo:  
**https://alicaldini4.pythonanywhere.com**

## Scenario di test
1. Vai su https://alicaldini4.pythonanywhere.com
2. Accedi come `organizer_demo` → crea un nuovo evento
3. Fai logout e accedi come `attendee_demo` → registrati all'evento
4. Verifica che l'attendee non veda il bottone "Crea Evento"
5. Verifica che l'organizer veda la lista dei partecipanti