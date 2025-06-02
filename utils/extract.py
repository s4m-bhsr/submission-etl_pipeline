import requests
from bs4 import BeautifulSoup

def fetch_products_from_url(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except Exception as e:
        raise RuntimeError(f"Unable to access {url} → {e}")

    soup = BeautifulSoup(response.text, "html.parser")
    product_cards = soup.select("div.collection-card")
    result = []

    for card in product_cards:
        try:
            product = {
                "title": card.select_one("h3.product-title").get_text(strip=True),
                "price": card.select_one("div.price-container").get_text(strip=True),
                "rating": next((p.get_text(strip=True) for p in card.find_all("p") if "Rating" in p.text), "Not Rated"),
                "colors": next((p.get_text(strip=True) for p in card.find_all("p") if "Colors" in p.text), "Unknown"),
                "size": next((p.get_text(strip=True) for p in card.find_all("p") if "Size" in p.text), "Unknown"),
                "gender": next((p.get_text(strip=True) for p in card.find_all("p") if "Gender" in p.text), "Unknown")
            }
            result.append(product)
        except Exception:
            continue

    return result

def collect_all_products(base_url="https://fashion-studio.dicoding.dev/", max_pages=50):
    all_data = []
    for page in range(1, max_pages + 1):
        page_url = base_url if page == 1 else f"{base_url}page{page}"
        print(f"🔎 Fetching: {page_url}")
        try:
            page_data = fetch_products_from_url(page_url)
            all_data.extend(page_data)
            print(f"✅ Page {page}: {len(page_data)} products collected!\n" + "-"*50)
        except Exception as e:
            print(f"❌ Error on page {page}: {e}\n" + "-"*50)
    return all_data
