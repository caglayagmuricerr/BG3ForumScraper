from bs4 import BeautifulSoup
import requests

# Scraping code (your existing code)
website = 'https://forums.larian.com/ubbthreads.php?ubb=cfrm&c=20'
result = requests.get(website)

if result.status_code == 200:
    content = result.text
    soup = BeautifulSoup(content, 'html.parser')

    t_d_c = soup.find_all('td', class_='forumtitle alvt')
    thread_count_soup = soup.find_all('td', class_='threadtotal acvt nw mbl')
    post_count_soup = soup.find_all('td', class_='posttotal acvt nw')
    last_post_soup = soup.find_all('td', class_='posttime alvt mblthin')

    i = 0
    title = []
    description = []
    viewing_now = []
    thread_count = []
    post_count = []
    last_post_title = []
    last_post_time = []

    while i < len(t_d_c):
        title.append(t_d_c[i].find('a').get_text())
        description.append(t_d_c[i].find('div').get_text().strip())
        viewing_now.append(t_d_c[i].find('span').get_text())
        thread_count.append(thread_count_soup[i].get_text().strip())
        post_count.append(post_count_soup[i].get_text().strip())
        last_post_title.append(last_post_soup[i].find('a').get_text())
        last_post_time.append(last_post_soup[i].find('span').get_text())
        i += 1

    # Writing to a text file
    with open('forum_data.txt', 'w') as file:
        j = 1
        for t, d, v, c, p, lpt, lpti in zip(title, description, viewing_now, thread_count, post_count, last_post_title, last_post_time):
            file.write(f"{j}. Title: {t}\n")
            file.write(f"Description: {d}\n")
            file.write(f"Viewing Now: {v}\n")
            file.write(f"Thread Count: {c}\n")
            file.write(f"Post Count: {p}\n")
            file.write(f"Last Post Title: {lpt}\n")
            file.write(f"Last Post Time: {lpti}\n\n")
            j += 1
else:
    print(f"Failed to retrieve the page. Status code: {result.status_code}")