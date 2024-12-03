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

        # TODO: I'm changing some parameters, I need to readjust the next ones

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
    
    # TODO: change values according to new parameters
    # Retrieving lastrowid
    def insert_material(self, material : material.Material) -> int:
        con, cur = self.connect_database()
        cur.execute("""INSERT INTO material VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?);""", 
                    (material.name, material.author, material.path, 
                     material.extracts_file_path, material.bookmark, 
                     material.due_date, material.interval_to_next_review, 
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

    # TODO: change values according to new parameters
    # Note that this_date needs to be a string in ISO format
    def read_materials_from_date(self, this_date):
        con, cur = self.connect_database()
        cur.execute("SELECT * FROM material WHERE next_repetition_date=?", (this_date,))
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
        
    # TODO: end
    
    def update_material(self, material : material.Material):
        con, cur = self.connect_database()
        cur.execute("""UPDATE material 
                        SET 
                    WHERE""")

    # Remember to asign material_id to extract when creating extract object
    # Returning lastrowid
    # TODO: change values according to new parameters
    def insert_extract(self, extract : extract.Extract) -> int:
        con, cur = self.connect_database()
        cur.execute("""INSERT INTO extract VALUES (NULL, ?, ?, ?, ?, ?)""", 
                                                  (extract.material_id,
                                                   extract.path,
                                                   extract.next_repetition_date,
                                                   extract.number_of_repetitions,
                                                   extract.days_between_repetitions))
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
        cur.execute("SELECT * FROM extract WHERE id=?", extract.extract_id)
        single_extract = cur.fetchone()
        con.close()
        return single_extract

    def read_extracts_from_material(self, material : material.Material):
        con, cur = self.connect_database()
        cur.execute("SELECT * FROM extract WHERE material_id=?", (material.id,))
        extracts = cur.fetchall()
        con.close()
        return extracts

    # TODO: change values according to new parameters
    def read_extracts_from_date(self, this_date):
        con, cur = self.connect_database()
        cur.execute("SELECT * FROM extract WHERE next_repetition_date=?", (this_date,))
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
    # - [ ] update_material_bookmark()
    # - [ ] update_material_next_date()
    # - [ ] update_material_priority()
    # - [ ] update_material_is_ended()
    # - [ ] update_extract_number_of_repetitions()
    # - [ ] update_extract_next_repetition()
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