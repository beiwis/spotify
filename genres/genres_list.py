import re
import requests
from bs4 import BeautifulSoup

#TODO: Add a function to allow the user to add their own genres

def main():
    """Main function"""
    # genre_list = get_everynoise_genres()
    classed_genres_list = get_musicgenrelist_genres()
    print(classed_genres_list)
    # filtered_genres = filter_genres(genre_list, classed_genres_list)
    
    # with open("genres_list.txt", 'w') as file:
    #     for category, genres in filtered_genres.items():
    #         file.write(f"{category}:\n")
    #         for genre in genres:
    #             file.write(f"- {genre}\n")
    #         file.write("\n")
    
    print("Filtered genres saved to genres_list.txt")
     
def combine_subgenres():
    """Combines the subgenres in all top_subgenres_*.txt files (top_subgenres_4weeks.txt, top_subgenres_6months.txt, top_subgenres_allTime.txt) into one file, removing duplicates"""
    subgenres = []
    for filename in ["top_subgenres_4weeks.txt", "top_subgenres_6months.txt", "top_subgenres_allTime.txt"]:
        with open(filename, 'r') as file:
            for line in file:
                print(line.strip())
                subgenres.append(line.strip())
    subgenres = list(set(subgenres)) #remove duplicates
    with open("top_subgenres.txt", 'w') as file:
        for subgenre in subgenres:
            file.write(subgenre + "\n")
    return subgenres

def filter_genres(genre_list, classed_genres_list):
    """Filters the genres in classed_genres_list based on genre_list"""
    filtered_genres = {}
    for category, genres in classed_genres_list.items():
        filtered_genres[category] = list(set(genre for genre in genres if genre in genre_list))
    return filtered_genres

def markdown_to_dict(markdown_string):
    """Converts a markdown string to a dictionary"""
    dict = {}
    for line in markdown_string.split('\n'): #separate the lines
        if line.strip() != "": #if the line is not empty
            if line[0] == "#": #if the line starts with a hashtag
                key = line[6:].strip() #remove the hashtag and the spaces
                dict[key] = [] #create a key in the dictionary
            else:
                dict[key].append(line[1:].strip()) # Append all characters except the first one
    return dict

####################################################################################################
#################################### EVERYNOISE.COM FUNCTIONS ######################################
####################################################################################################

def input_everynoise_string():
    everynoise_string = ""
    while True:
        line = input("Enter a line (or leave empty to finish): ")
        if line == "":
            break
        everynoise_string += line + "\n"
    return everynoise_string.strip()

def get_everynoise_genres(terminal=False):
    """Returns a list of genres from everynoise.com"""
    if terminal:
        everynoise_string = input_everynoise_string()
        genres_list = everynoise_copypaste_to_list(everynoise_string)
    else:
        with open('everynoise_maingenres.txt', 'r') as file:
            everynoise_string = file.read()
        genres_list = everynoise_copypaste_to_list(everynoise_string)
    return genres_list

def everynoise_copypaste_to_list(string):
    literals = []
    for line in string.split('\n'): #separate the lines
        literal = re.sub(r'[^a-zA-Z\']', ' ', line.strip()).strip() #remove all non-alphabetical characters
        literals.append(literal)  # Append all characters except the first one
    return literals

####################################################################################################
################################## MUSICGENRELIST.COM FUNCTIONS ####################################
####################################################################################################

def get_musicgenrelist_genres():
    """Returns a dict of genres using the big genres (As Alternative or Anime or Blues) as categories for example: {'Alternnative':[Art Punk, Alternative Rock, Britpunk,College Rock,Crossover Thrash,Crust Punk (thx Haug),Emotional Hardcore (emo / emocore),Experimental Rock,etc.], Anime:[], Blues:[Acoustic Blues,African Blues,Blues Rock,Blues Shouter,etc.], etc. scraping from musicgenrelist.com"""
    dict = scrape_musicgenrelist_genres()
    return dict

def scrape_musicgenrelist_genres():
    """Scrapes the genres from musicgenrelist.com and returns a dictionary of genres"""
    url = "https://www.musicgenreslist.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    genres_dict = {}
    anchor = soup.find("a", {"name": "music-genre-list"})
    if anchor:
        p_tag = anchor.find_parent("p")
        if p_tag:
            div = p_tag.find_next_sibling("div")
            if div:
                ul = div.find("ul")
                if ul:
                    categories = div.find_all("li")
                    for category in categories:
                        category_name_tag = category.find("a")
                        if category_name_tag and category_name_tag != 'About':
                            category_name = category_name_tag.text.strip()
                            ul = category_name_tag.find_next_sibling("ul")
                            if ul:
                                genres = ul.find_all("li")
                                genre_list = [genre.text.strip() for genre in genres if '\n' not in genre.text.strip()]
                                if category_name == "Inspirational – Christian & Gospel":
                                    category_name = "Gospel"
                                elif category_name == "Hip-Hop/Rap":
                                    category_name = "Urban"
                                genres_dict[category_name] = genre_list  
                                              
    # Convert all letters to lowercase and remove extra spaces
    genres_dict = {category.lower(): [genre.lower().strip() for genre in genres] for category, genres in genres_dict.items()}
    return genres_dict  
    


if __name__ == '__main__':
    main()

