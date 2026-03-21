import pandas as pd
import sqlite3

def export_to_file(format_type):
    try:
        conn = sqlite3.connect('news.db')
        df = pd.read_sql_query("SELECT * FROM news", conn)
        conn.close()

        if format_type.lower() == 'csv':
            df.to_csv('news_report.csv', index=False)
            print("Successfully exported to news_report.csv")
        elif format_type.lower() == 'excel':
            df.to_excel('news_report.xlsx', index=False)
            print("Successfully exported to news_report.xlsx")
    except Exception as e:
        print(f"Export Error: {e}")