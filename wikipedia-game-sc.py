from queue import Queue
import wikipediaapi
import time

user_agent = "VincentsWikipediaGame/1.0 (sh7771vi1226@pusd.us)"

wiki_wiki = wikipediaapi.Wikipedia(user_agent, "en")

def fetch_links(page):
    links_list = []
    links = page.links
    for title in sorted(links.keys()):
        links_list.append(title)
        
    return links_list

def wikipedia_game_solver(start_page, target_page):
    print('Working on it...')
    start_time = time.time()
  
    visited = []
    queue = Queue()
    path = []
    parent = {}

    queue.put(start_page.title)
    visited.append(start_page,title)

    while not queue.empty():
        current_title = queue.get()
        if current_title == target_page.title:
            break

        current_page = wiki_wiki.page(current_title)
        next_level = fetch_links(current_page)
        visited.append(current_title)

        for node in next_level:
            if node not in visited:
                queue.put(node)
                parent[node] = current_title

    child = target_page.title
    while child != start_page.title:
        path.append(child)
        child = parent[child]
    path.append(start_page.title)
    path.reverse()

    end_time = time.time()
    print("This algorithm took", end_time-start_time, "seconds to run!")
  
    return path

start_page = wiki_wiki.page('Nina Tandon')
target_page = wiki_wiki.page('Italian language')
path = wikipedia_game_solver(start_page, target_page)
print("Shortest path:", path)
