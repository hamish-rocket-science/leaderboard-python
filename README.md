# Flask Leaderboard Application

A simple and clean leaderboard application built with [Flask](https://flask.palletsprojects.com/en/stable/).

It uses [Jinja templating](https://jinja.palletsprojects.com/en/stable/templates/) for easy HTML templates.

## Features

- Add and track player scores
- Filter scores by game mode (Easy, Medium, Hard)
- SQLite database for persistent storage

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/hamish-rocket-science/leaderboard-python.git
cd flask-leaderboard
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows, use: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Start the Flask development server:
```bash
flask run --debug
```

2. Open your browser and navigate to:
```
http://localhost:5000
```

## Project Structure

```
.
├── app.py              # Main application file
├── leaderboards.py     # Database operations
├── requirements.txt    # Project dependencies
├── static/
│   └── reset.css       # Reset styles
│   └── site.css        # Stylesheet
└── templates/
    ├── base.html       # Base template
    ├── home.html       # Home page template
    └── leaderboard.html # Leaderboard page template
```

## Database Schema

The application uses SQLite with the following table structure:

```sql
CREATE TABLE leaderboard (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    player_name TEXT NOT NULL,
    score INTEGER NOT NULL,
    date_achieved TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    game_mode TEXT
);
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Flask web framework
- SQLite database
- PythonAnywhere for hosting
