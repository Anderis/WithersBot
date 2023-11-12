import sqlite3
import os

async def add_experience(user_id, experience):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    database_path = os.path.join(current_dir, 'leveling.db')

    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    # Create the user_level table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_level (
            user_id INTEGER PRIMARY KEY,
            experience INTEGER DEFAULT 0,
            level INTEGER DEFAULT 1
        );
    ''')

    # Insert or update user experience
    cursor.execute('''
        INSERT INTO user_level (user_id, experience, level)
        VALUES (?, ?, 1)
        ON CONFLICT(user_id) DO UPDATE
        SET experience = experience + ?;
    ''', (user_id, experience, experience))

    conn.commit()
    
    print(f"User {user_id} gained {experience} experience points.")


async def get_user_level(user_id):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    database_path = os.path.join(current_dir, 'your_database.db')

    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    # Retrieve user level
    cursor.execute('SELECT level FROM user_levels WHERE user_id = ?', (user_id,))
    result = cursor.fetchone()

    level = result[0] if result else 1
    print(f"User {user_id} is at level {level}.")

    return level