import sqlite3
import file_manager

class Database:
    def __init__(self, fm :file_manager.FileManager):
        self.db_path = fm.db_path
    
    def connect_database(self):
        #con = sqlite3.connect(self.db_path)
        con = sqlite3.connect(":memory:")
        cursor = con.cursor()
        return con, cursor


    def create_tables(self):
        con, cursor = self.connect_database()

        # Will use date as text (ISO 8601 format)

        cursor.execute("""CREATE TABLE material(
                       name text,
                       author text,
                       material_id integer,
                       relative_path text,
                       extract_list_path text,
                       bookmark text,
                       next_repetition_date text,
                       frequency integer,
                       priority real,
                       is_ended integer)""")
        

        cursor.execute("""CREATE TABLE extract(
                       material_id integer,
                       relative_path text,
                       extract_id integer,
                       next_repetition text,
                       n_of_repetitions integer,
                       days_between_repetitions integer)""")
            
        con.commit()
    
    # TODO: 
    # - [ ] See how PK works here and how to autogenerate (increasing)
    # - [ ] create_material()
    # - [ ] create_extract()
    # - [ ] read_material_from_id()
    # - [ ] read_all_materials()
    # - [ ] read_extract_from_id()
    # - [ ] read_all_extracts()
    # - [ ] read_all_materials_from_date()
    # - [ ] read_all_extracts_from_date()
    # - [ ] update_material_from_id()
    # - [ ] update_extract_from_id()
    # - [ ] delete_material()
    # - [ ] delete extract

    
    def
        
fm = file_manager.FileManager()
db = Database(fm)
db.connect_database()
db.create_tables()




