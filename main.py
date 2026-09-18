   import requests, pandas as pd
   from bs4 import BeautifulSoup

   def extract_hierarchical_data(base_url):
       all_data = []
       session = requests.Session()
       for page in range(1, 5):
           res = session.get(f"{base_url}?page={page}", timeout=10)
           soup = BeautifulSoup(res.text, 'html.parser')
           for card in soup.find_all(['div','article'], class_=lambda x: x and 'listing' in x):
               all_data.append({"title": card.text.strip()[:50], "page": page})
       df = pd.DataFrame(all_data)
       df.to_csv("structured_dataset.csv", index=False)
       df.to_json("structured_dataset.json", orient="records", indent=2)
       return df

   if __name__ == "__main__":
       extract_hierarchical_data("https://example.com/listings")
