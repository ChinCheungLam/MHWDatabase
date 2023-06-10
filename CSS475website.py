from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Define MySQL database connection
MHW_DB = mysql.connector.connect(
  host="css475databaseproject.c6re2to5cmf5.us-east-2.rds.amazonaws.com",
  user="teamZinogre",
  password="teamZinogre_lol",
  database="MHW_DB"
)

# Define a route to fetch data from the database and display it
@app.route('/')
def index():
    # Fetch data from the QUEST table
    quest_cursor = MHW_DB.cursor()
    quest_cursor.execute("SELECT * FROM QUEST")
    quests = quest_cursor.fetchall()

    # Fetch data from the MONSTER table
    monster_cursor = MHW_DB.cursor()
    monster_cursor.execute("SELECT * FROM MONSTER")
    monsters = monster_cursor.fetchall()

    # Fetch data from the ARMOR table
    armor_cursor = MHW_DB.cursor()
    armor_cursor.execute("SELECT * FROM ARMOR")
    armors = armor_cursor.fetchall()

    # Fetch data from the WEAPON table
    weapon_cursor = MHW_DB.cursor()
    weapon_cursor.execute("SELECT * FROM WEAPON")
    weapons = weapon_cursor.fetchall()

    # Fetch data from the HUNTER table
    hunter_cursor = MHW_DB.cursor()
    hunter_cursor.execute("SELECT * FROM HUNTER")
    hunters = hunter_cursor.fetchall()

    # Fetch data from the ITEM table
    item_cursor = MHW_DB.cursor()
    item_cursor.execute("SELECT * FROM ITEM")
    items = item_cursor.fetchall()

    # Fetch data from the EQUIPMENT table
    equipment_cursor = MHW_DB.cursor()
    equipment_cursor.execute("SELECT * FROM EQUIPMENT")
    equipment = equipment_cursor.fetchall()

    # Fetch data from the ARMOR_SKILL table
    armor_skill_cursor = MHW_DB.cursor()
    armor_skill_cursor.execute("SELECT * FROM ARMOR_SKILL")
    armor_skills = armor_skill_cursor.fetchall()

    # Pass data to the HTML template for rendering
    return render_template('index.html',
                           quests=quests,
                           monsters=monsters,
                           armors=armors,
                           weapons=weapons,
                           hunters=hunters,
                           items=items,
                           equipment=equipment,
                           armor_skills=armor_skills)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)