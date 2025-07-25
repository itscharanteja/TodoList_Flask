# Todo List Flask Application

A simple Todo List web application built with Flask and SQLAlchemy. This project demonstrates basic CRUD operations, templating, and database integration using SQLite.

## Features

- Add, update, and delete todo items
- Persistent storage with SQLite (`site.db`)
- Simple, clean UI with custom CSS
- Modular Flask application structure

## Directory Structure

```
app.py                  # Main Flask application
instance/
  site.db               # SQLite database file
static/
  css/
    main.css            # Custom styles
templates/
  base.html             # Base template
  index.html            # Main page template
  update.html           # Update item template
flask/                  # Python virtual environment (do not edit)
```

## Setup Instructions

1. **Clone the repository**

2. **Create and activate a virtual environment**

   ```sh
   python3 -m venv flask
   source flask/bin/activate
   ```

3. **Install dependencies**

   ```sh
   pip install flask flask_sqlalchemy
   ```

4. **Run the application**
   ```sh
   python app.py
   ```
   The app will be available at `http://127.0.0.1:5000/`.

## Database

- The SQLite database is stored in `instance/site.db`.
- Do not share this file if you want to keep your data private.

## Customization

- Edit `static/css/main.css` to change the look and feel.
- Modify templates in the `templates/` directory for UI changes.

## License

This project is for educational purposes.
