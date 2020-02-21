import sqlite3
from sqlite3 import Error as error

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except error as e:
        print(e)
    print("table criada com sucesso!")

def insert_temp(conn, data_content) :

    sql_data_input = """ INSERT INTO item (fname,lname , type_item,reference,province,status,cellphone,email,note) VALUES (?,?,?,?,?,?,?,?,?) ;"""
    try:
        cur = conn.cursor()
        cur.execute(sql_data_input,data_content)
        cur.lastrowid
        conn.commit()


    except error as e:
        print(e)


def main():

    database = "LFDB.db"

    sql_create_lostfound_table = """ CREATE TABLE IF NOT EXISTS item (
                                        id integer PRIMARY KEY AUTOINCREMENT,
                                        fname text NOT NULL,
                                        lname text NOT NULL,
                                        type_item text NOT NULL,
                                        reference text ,
                                        province text NOT NULL,
                                        status text NOT NULL,
                                        cellphone text NOT NULL, 
                                        email text NOT NULL,
                                        note text
                                         );"""

    item_1 = ('manuel','jose', 'Passaporte','LA4856', 'Luanda', 'Perdido', '963232312', 'mateus@gmail.com' , '')
    item_2 = ('pedro','jose','Bilhete de identidade', 'LA485643', 'Benguela', 'Perdido', '963232312', 'jose@gmail.com', 'caducado')
    item_3 = ('axl','rose','Cedula', 'LXo23023', 'Namibe', 'Encontrado', '963232312', 'luis@gmail.com', 'novo')
    item_4 = ('assan','moah','Passaporte', 'PT39230912', 'Huila', 'Encontrado', '963232312', 'pedro@gmail.com','vermelho')
    item_5 = ('mohamed','hassan','Outros', 'PT39230912', 'Malange', 'Encontrado', '963232312', 'hassan@gmail.com','carteira de documentos verde')

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_lostfound_table)

        print("inserido item {} " .format(insert_temp(conn, item_1)))
        print("inserido item {} " .format(insert_temp(conn, item_2)))
        print("inserido item {} " .format(insert_temp(conn, item_3)))
        print("inserido item {} " .format(insert_temp(conn , item_4)))
        print("inserido item {} ".format(insert_temp(conn, item_5)))

    else:
        print("Error! cannot create the database connection.")
    conn.close()

if __name__ == '__main__':
            main()