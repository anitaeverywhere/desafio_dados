
from data_fetcher import fetch_data
from data_processor import process_data
from report_generator import generate_console_report, generate_csv_report

def main():
    API_URL = "https://jsonplaceholder.typicode.com/posts"
    USER_ID_TO_ANALYZE = 1
    OUTPUT_CSV_FILENAME = "relatorio.csv"

    all_posts_data = fetch_data(API_URL)

    if all_posts_data:
        user_posts, stats = process_data(all_posts_data, USER_ID_TO_ANALYZE)
        
        generate_console_report(stats, USER_ID_TO_ANALYZE)
        generate_csv_report(user_posts, OUTPUT_CSV_FILENAME)

if __name__ == "__main__":
    main()