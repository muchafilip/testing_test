from selenium import webdriver
import time


class WikiPage():

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=R".\chromedriver.exe")

    def find_first_link(self, url, sites_visited):
        self.driver.get(url)
        result = self.driver.find_element_by_id("mw-content-text")
        result = result.find_element_by_class_name("mw-parser-output")
        results = result.find_elements_by_xpath("p/a[@href]")
        for element in results:
            url = element.get_attribute("href")
            print(url)
            url_splitted = url.rsplit("/", 2)
            back_url=url_splitted[-1]
            valid = not any(k in back_url for k in ')(:#')
            if valid and url_splitted[-2] == "wiki" and url not in sites_visited:
                self.driver.get(url)
                return url

            
    def continue_redirect(self, visited, target_url):
        if visited[-1] == target_url:
            print("Target ('Philosphy') article reached!")
            return False
        elif visited[-1] in visited[:-1]:
            print("Arrived at an article already seen, search aborted.")
            return False
        else:
            return True
                

def main():
    start_url = "https://en.wikipedia.org/wiki/Special:Random"
    target_url = "https://en.wikipedia.org/wiki/Philosophy"
    sites_visited = [start_url]
    bot = WikiPage()
    counter = 0

    while bot.continue_redirect(sites_visited, target_url):
        print(sites_visited[-1])

        first_link = bot.find_first_link(sites_visited[-1], sites_visited)
        if not first_link:
            print("Arrived at an article with no links, search aborted.")
            break
        
        sites_visited.append(first_link)
        counter += 1
        time.sleep(1)
    print(f"It took {counter} redirects to reach Philosophy")

if __name__=='__main__':
    main()
