from bs4 import BeautifulSoup
import requests
import webbrowser
import time
from pyfiglet import Figlet
from colorama import Fore, init
import os
os.system("cls")
init()
fig_large = Figlet(font='big')
fig_small = Figlet(font='small')
ascii_art_large = fig_large.renderText('The Watcher')
colored_ascii_large = Fore.GREEN + ascii_art_large + Fore.RESET
print(colored_ascii_large)



def main():
    while True:
        # os.system("cls")
        options = int(input(("What do you prefer to watch? [ 1 | 2 ]\n\n[1] Movie\n[2] Series\n")))
        try:
            if 2 >= options >= 1:
                break
            else:
                # os.system("clear")
                print(Fore.RED + "[!] Choose 1 or 2 only " + Fore.RESET)
        except ValueError:
            return f"{Fore.RED}Choose between 1 or 2 only{Fore.RESET}"

    if options == 1:
        def start():
            choise = input("What do you need to watch: ")
            site = requests.get(f"https://xn------nzebcaa6hd5qde3bpjch.myciima-weciima.shop/search/{choise}/")
            soup = BeautifulSoup(site.content, "lxml")
            movie_div = soup.find_all("div", {"class": "Grid--WecimaPosts"})
            return movie_div
        movie_div = start()

        movie_info = {}

        def get_movie_titles(movie_div):
            all_movies = movie_div[0].find_all("div", {'class': 'GridItem'})
            number_of_movies = len(all_movies)
            for i in range(number_of_movies):
                movie_title = all_movies[i].find('strong').text
                movie_year = all_movies[i].find('span').text
                movie_link = all_movies[i].find('a')["href"]
                movie_info[i] = {'Title' : f"{movie_title} {movie_year}", 'Link' : movie_link}
                print(f"[ {i} ] - {movie_info[i]['Title']}")
            return movie_info
        movie_info = get_movie_titles(movie_div)

        def download_m(down_div):
                for divs in down_div:
                    all_qual = divs.find_all("a", {'class': 'hoverable activable'})

                for links in all_qual:
                    qualitys = links.find("resolution").text
                    print(f"{qualitys} Download link: {links["href"]} ")
        while True:
            try:
                UserInput = int(input("What do you prefer to watch: "))
                if UserInput in movie_info:
                    UserChoise = movie_info[UserInput]
                    print(UserChoise['Title'])
                    print(f"Watch link: {UserChoise['Link']}")
                    choice_site = requests.get(UserChoise['Link'])
                    choice_soup = BeautifulSoup(choice_site.content, "lxml")
                    down_list = choice_soup.find_all("ul", {"class": "List--Download--Wecima--Single"})
                    download_m(down_list)
                    time.sleep(1)
                    webbrowser.open(UserChoise["Link"])
                    break
                else:
                    raise ValueError

            except ValueError as e:
                os.system("cls")
                print(f"{Fore.RED}Oops Please Choose right movie{Fore.RESET}")
                get_movie_titles(movie_div)


    elif options == 2:
        print(f"{Fore.RED}Soon...{Fore.RESET}")
        main()
            
    while True:
        mistake = input("Did you choose wrong movie or want another movie? Y/N ").upper()

        if mistake == "Y":
                main()
                
                
        else:
            input("Press any key to exit app...")
            break
        break

if __name__ == "__main__":
    main()    
