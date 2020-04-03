import wikipedia
import wikipediaapi
wiki_wiki = wikipediaapi.Wikipedia('en')


def get_sections(bookname, level=0):
    p = wiki_wiki.page(bookname)
    sections = p.sections
    titles = []
    texts = []
    for s in sections:
           titles.append(s.title)
           texts.append(s.text)
    return dict(zip(titles, texts))       


import pandas as pd
book = pd.read_csv('desktop/book.csv')
books = book[:100]
books = books['name']


title = []
summary = []
content = []
link = []
for i in range(5):
    try:
        title.append(books[i])
        page = wikipedia.page(books[i])
        summary.append(page.summary)
        content.append(get_sections(books[i]))
        link.append(page.links)
    except:
        pass

df = pd.DataFrame({'title':title, 
                   'summary':summary, 
                   'content': content, 
                   'link':link})


wikilinks = list(chain(*[i for i in link]))
print(f"There are {len(set(wikilinks))} unique wikilinks.")
