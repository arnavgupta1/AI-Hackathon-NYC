import wikipediaapi

def get_wikipedia_page(topic):
    wiki = wikipediaapi.Wikipedia('en')
    page = wiki.page(topic)
    if page.exists():
        return page.fullurl
    else:
        return None

'''
if __name__ == "__main__":
    topic = input("Enter a topic: ")
    page = get_wikipedia_page(topic)
    if page:
       #print(f"Title: {page.title}")
        print(f"URL: {page.fullurl}")
    else:
        print("No matching Wikipedia page found.")
'''