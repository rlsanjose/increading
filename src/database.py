import sqlite3
import file_manager
import material
import extract

class Database:
    def __init__(self, fm :file_manager.FileManager):
        self.db_path = fm.db_path
    
    def connect_database(self):
        #con = sqlite3.connect(self.db_path)
        con = sqlite3.connect("new.db")
        cursor = con.cursor()
        return con, cursor


    def create_tables(self):
        con, cursor = self.connect_database()

        # Will use date as text (ISO 8601 format)

        cursor.execute("""CREATE TABLE IF NOT EXISTS material(
                       material_id INTEGER PRIMARY KEY,
                       name TEXT,
                       author TEXT,
                       path_to_material TEXT,
                       bookmark TEXT,

                       extracts_dir TEXT,
                       extract_list_path TEXT,

                       review_date TEXT,
                       due_date TEXT,
                       number_of_reviews INTEGER,
                       interval_to_next_review INTEGER,
                       a_factor REAL,
                       priority INTEGER,

                       is_ended INTEGER);""")
        

        cursor.execute("""CREATE TABLE IF NOT EXISTS extract(
                       extract_id INTEGER PRIMARY KEY,
                       material_id INTEGER,
                       bookmark TEXT,
                       relative_path TEXT,

                       review_date TEXT,
                       due_date TEXT,
                       number_of_reviews INTEGER,
                       interval_to_next_review INTEGER,
                       a_factor REAL,
                       priority INTEGER,

                       FOREIGN KEY (material_id) REFERENCES material(material_id));""")
            
        con.commit()
        con.close()
    
    # Retrieving lastrowid
    def insert_material(self, material : material.Material) -> int:
        con, cur = self.connect_database()
        cur.execute("""INSERT INTO material VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);""", 
                    (material.name, material.author, material.path,
                    material.bookmark, material.extracts_dir,
                    material.extracts_file_path, material.review_date,
                    material.due_date, material.number_of_reviews,
                    material.interval_to_next_review, material.a_factor, 
                    material.priority_percentage, material.is_ended))
        
        lastrowid = cur.lastrowid
        con.commit()
        con.close()
        return lastrowid
    
    def read_all_materials(self) :
        con, cur = self.connect_database()
        cur.execute("SELECT * FROM material")
        materials = cur.fetchall()
        con.close()
        return materials

    def read_material_from_id(self, material : material.Material):
        con, cur = self.connect_database()
        cur.execute("SELECT * FROM material WHERE material_id=?", (material.id,))
        single_material = cur.fetchone()
        con.close()
        return single_material

    # Note that this_date needs to be a string in ISO format
    def read_materials_from_date(self, this_date):
        con, cur = self.connect_database()
        cur.execute("SELECT * FROM material WHERE due_date=?", (this_date,))
        materials = cur.fetchall()
        con.close()
        return materials

    def read_material_from_name_or_author(self, text_search):
        con, cur = self.connect_database()
        cur.execute("SELECT * FROM material WHERE author LIKE ? OR WHERE name LIKE ?", 
                    (text_search, ))
        materials = cur.fetchall()
        con.close()
        return materials
        
    # First, change the bookmark in the material object. Then, update the database
    # TODO: Maybe add error cheking or returning confirmation?
    
    def update_material_bookmark(self, material : material.Material):
        con, cur = self.connect_database()
        cur.execute("""UPDATE material 
                        SET material.bookmark = ?
                    WHERE material.material_id = ? ;""", 
                    (material.bookmark, material.id))
        con.commit()
        con.close()
        return

    # TODO: Is due date the next date? I think so.

    def update_material_review_due_dates(self, material : material.Material):
        con, cur = self.connect_database()
        cur.execute("""UPDATE material 
                    SET material.due_date = ?,
                    material.review_date = ?
                    WHERE material.material_id = ? ;""", 
                    (material.due_date, material.review_date, material.id))
        con.commit()
        con.close()
        return
    
    def update_material_priority(self, material : material.Material):
        con, cur = self.connect_database()
        cur.execute("""UPDATE material
                    SET material.priority = ?
                    WHERE material.material_id = ? ;""",
                    (material.priority_percentage, material.id))
        con.commit()
        con.close()
        return

    def update_material_is_ended(self, material : material.Material):
        con, cur = self.connect_database()
        cur.execute("""UPDATE material
                    SET material.is_ended = ?
                    WHERE material.material_id = ? ;""",
                    (material.is_ended, material.id))
        con.commit()
        con.close()
        return


    # Remember to asign material_id to extract when creating extract object
    # Returning lastrowid
    def insert_extract(self, extract : extract.Extract) -> int:
        con, cur = self.connect_database()
        cur.execute("""INSERT INTO extract VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", 
                    (extract.material_id,
                    extract.bookmark,
                    extract.path,
                    extract.review_date,
                    extract.due_date,
                    extract.number_of_reviews,
                    extract.interval_to_next_review,
                    extract.a_factor,
                    extract.priority_percentage))
        lastrowid = cur.lastrowid
        con.commit()
        con.close()
        return lastrowid

        
    def read_all_extracts(self) :
        con, cur = self.connect_database()
        cur.execute("SELECT * FROM extract")
        extracts = cur.fetchall()
        con.close()
        return extracts
    
    def read_extract_from_id(self, extract : extract.Extract) :
        con, cur = self.connect_database()
        cur.execute("SELECT * FROM extract WHERE extract_id=?", extract.extract_id)
        single_extract = cur.fetchone()
        con.close()
        return single_extract

    def read_extracts_from_material(self, material : material.Material):
        con, cur = self.connect_database()
        cur.execute("SELECT * FROM extract WHERE material_id=?", (material.id,))
        extracts = cur.fetchall()
        con.close()
        return extracts

    def read_extracts_from_date(self, this_date):
        con, cur = self.connect_database()
        cur.execute("SELECT * FROM extract WHERE due_date=?", (this_date,))
        extracts = cur.fetchall()
        con.close()
        return extracts

    # TODO:
    # - [X] insert_material()
    # - [X] insert_extract()
    # - [X] read_material_from_name_or_author()
    # - [X] read_extract_from_id()
    # - [X] read_all_materials()
    # - [X] read_all_extracts()
    # - [X] read_extracts_from_material()
    # - [X] read_all_materials_from_date()
    # - [X] read_all_extracts_from_date()
    # - [X] update_material_bookmark()
    # - [X] update_material_review_and_due_dates()
    # - [X] update_material_priority()
    # - [X] update_material_is_ended()
    # - [ ] update_extract_number_of_repetitions()
    # - [ ] update_extract_review_and_due_dates()
    # - [ ] update_extract_priority()
    # - Need some functions to execute after one review (update dates,
    # intervals)
    # - [ ] delete_material()
    # - [ ] delete extract()
    # - [X] retrieve_lastrowid()
    # - [ ] test!!

    
fm = file_manager.FileManager()
db = Database(fm)
db.connect_database()

db.create_tables()

mat = material.Material(0, "nombre", "autor", "path", 34, "tt")

db.insert_material(mat)
print(db.read_all_materials())