import requests
import urllib.parse

def get_wikipedia_page_info(page_title):
    url = f"https://en.wikipedia.org/w/api.php?action=query&format=json&prop=extracts|categories|info&exintro&explaintext&titles={page_title}"
    response = requests.get(url)
    data = response.json()
    
    page_id = list(data['query']['pages'].keys())[0]
    page_info = data['query']['pages'][page_id]
    
    page_url = f"https://en.wikipedia.org/wiki/{urllib.parse.quote(page_title)}"
    categories = [category['title'] for category in page_info.get('categories', [])]
    sections = [section['line'] for section in page_info.get('sections', [])]
    
    return page_url, categories, sections

# Example usage
page_title = "OpenAI"
page_url, categories, sections = get_wikipedia_page_info(page_title)

print("Page URL:")
print(page_url)

print("\nCategories:")
for category in categories:
    print(category)

print("\nSections:")
for section in sections:
    print(section)
