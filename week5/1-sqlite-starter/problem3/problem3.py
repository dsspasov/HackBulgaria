import sqlite3


def main():
    conn = sqlite3.connect("polyglot.db")
    cursor = conn.cursor()

    result = cursor.execute("SELECT id, language, answers FROM languages")

    for row in result:
        print(row)
if __name__ == '__main__':
    main()
