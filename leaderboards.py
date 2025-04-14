import sqlite3
from datetime import datetime

class LeaderboardDB:
    def __init__(self, db_path="leaderboard.db"):
        self.db_path = db_path
        self.init_db()

    def get_connection(self):
        return sqlite3.connect(self.db_path)

    def init_db(self):
        with self.get_connection() as conn:
            c = conn.cursor()
            c.execute('''CREATE TABLE IF NOT EXISTS leaderboard
                         (id INTEGER PRIMARY KEY AUTOINCREMENT,
                          player_name TEXT NOT NULL,
                          score INTEGER NOT NULL,
                          date_achieved TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                          game_mode TEXT)''')
            conn.commit()

    def add_score(self, player_name, score, game_mode=None):
        with self.get_connection() as conn:
            c = conn.cursor()
            c.execute("INSERT INTO leaderboard (player_name, score, game_mode) VALUES (?, ?, ?)",
                     (player_name, score, game_mode))
            conn.commit()

    def get_top_scores(self, limit=10, game_mode=None):
        with self.get_connection() as conn:
            conn.row_factory = sqlite3.Row  # This enables column name access
            c = conn.cursor()
            if game_mode:
                c.execute("SELECT * FROM leaderboard WHERE game_mode = ? ORDER BY date_achieved DESC LIMIT ?",
                         (game_mode, limit))
            else:
                c.execute("SELECT * FROM leaderboard ORDER BY date_achieved DESC LIMIT ?", (limit,))
            rows = c.fetchall()
            # Convert Row objects to dictionaries
            return [dict(row) for row in rows]
        
    def delete_score(self, score_id):
        with self.get_connection() as conn:
            c = conn.cursor()
            c.execute("DELETE FROM leaderboard WHERE id = ?", (score_id,))
            conn.commit()
            return c.rowcount > 0  # Returns True if a row was deleted, False otherwise

# Create a global instance of the database
db = LeaderboardDB() 