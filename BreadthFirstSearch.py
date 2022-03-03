import requests
import re



class Node:

    def __init__(self, name):
        self.name = name
        self.adjacent_list = []
        self.visited = False


class WebCrawler:

    def __init__(self):
        self.discovered_urls = []

    def crawl(self, start_url):
        queue = [start_url]
        self.discovered_urls.append(start_url)

        while queue:
            actual_url = self.discovered_urls.pop(0)
            print(actual_url)

            actual_url_html = self.read_raw_html(actual_url)
            for url in self.get_links_from_html(actual_url_html):
                if url not in self.discovered_urls:
                    self.discovered_urls.append(url)
                    queue.append(url)

    def get_links_from_html(self, raw_html):
        return re.findall("https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+", raw_html)

    def read_raw_html(self, url):
        raw_html = ''
        try:
            raw_html = requests.get(url).text
        except Exception as e:
            pass

        return raw_html



def bfs(start_node: Node):
    queue = [start_node]
    while queue:
        actual_node = queue.pop(0)
        actual_node.visited = True

        print(actual_node.name)

        for n in actual_node.adjacent_list:
            if not n.visited:
                queue.append(n)


node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("E")

node1.adjacent_list.append(node2)
node1.adjacent_list.append(node3)
node2.adjacent_list.append(node4)

# node4.adjacent_list = [node5]

print(bfs(node1))




if __name__ == '__main__':

    crawler = WebCrawler()
    crawler.crawl('www.kahoot.it')


