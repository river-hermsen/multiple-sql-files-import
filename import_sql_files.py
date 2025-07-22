
import argparse
import os
import subprocess

def import_sql_files(server, database, sql_folder):
    """
    Imports all .sql files from a specified folder into a database using sqlcmd.

    Args:
        server (str): The name of the SQL server.
        database (str): The name of the database.
        sql_folder (str): The path to the folder containing .sql files.
    """
    if not os.path.isdir(sql_folder):
        print(f"Error: Folder not found at '{sql_folder}'")
        return

    for filename in os.listdir(sql_folder):
        if filename.endswith(".sql"):
            sql_file_path = os.path.join(sql_folder, filename)
            command = [
                "sqlcmd",
                "-S", server,
                "-d", database,
                "-i", sql_file_path
            ]
            try:
                print(f"Importing {sql_file_path}...")
                subprocess.run(command, check=True)
                print(f"Successfully imported {sql_file_path}")
            except subprocess.CalledProcessError as e:
                print(f"Error importing {sql_file_path}: {e}")
            except FileNotFoundError:
                print("Error: 'sqlcmd' not found. Please ensure it is installed and in your PATH.")
                return

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Import multiple .sql files into a SQL Server database.")
    parser.add_argument("-S", "--server", required=True, help="The SQL Server instance name.")
    parser.add_argument("-d", "--database", required=True, help="The database name.")
    parser.add_argument("-f", "--folder", required=True, help="The folder containing the .sql files.")

    args = parser.parse_args()
    import_sql_files(args.server, args.database, args.folder)
