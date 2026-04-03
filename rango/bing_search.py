
import requests

def run_query(search_terms):
    # Fake API URL

    url = "https://api.bing.microsoft.com/v7.0/search"

    # Fake API response
    mock_json = {
        "webPages": {
            "value": [
                {
                    "name":  "Tutorial",
                    "url": "https://example.com/tutorial",
                    "snippet": "Learn step by step..."
                },
                {
                    "name": "Documentation",
                    "url": "https://example.com/docs",
                    "snippet": "Official docs..."
                },
                {
                    "name": "GitHub",
                    "url": "https://github.com",
                    "snippet": "Open source projects..."
                }
            ]
        }
    }

    results = []

    if "webPages" in mock_json:
        for result in mock_json["webPages"]["value"]:
            results.append({
                "title": result["name"],
                "link": result["url"],
                "summary": result["snippet"]
            })

    return results

def main():
    print("call main") 

if __name__ == '__main__':
    main()