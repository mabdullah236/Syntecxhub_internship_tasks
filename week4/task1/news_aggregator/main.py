import argparse
from scraper import fetch_news
from database import setup_db, save_news, get_filtered_news
from exporter import export_to_file

API_KEY = "32b149dd35834decbd9bab304d726955"

def main():
    setup_db()
    parser = argparse.ArgumentParser(description="News Aggregator CLI")
    
    parser.add_argument('--fetch', type=str, help="Fetch news with a keyword")
    parser.add_argument('--list', action='store_true', help="List all stored news")
    parser.add_argument('--source', type=str, help="Filter by source name")
    parser.add_argument('--export', type=str, choices=['csv', 'excel'], help="Export to CSV or Excel")

    args = parser.parse_args()

    if args.fetch:
        print(f"Fetching news for: {args.fetch}...")
        news = fetch_news(API_KEY, args.fetch)
        save_news(news)
        print("Done!")

    elif args.list:
        results = get_filtered_news(source=args.source)
        for r in results:
            print(f"[{r[1]}] - {r[0]} ({r[2]})")

    elif args.export:
        export_to_file(args.export)

if __name__ == "__main__":
    main()