import bs4

def add_bee_favicon(file_path="existing_file.html"):
# load the file
    with open(file_path, 'r', encoding='utf-8') as inf:
        txt = inf.read()
        soup = bs4.BeautifulSoup(txt)
        print(type(soup))
        # create new link
        new_link = soup.new_tag("link", rel="icon", href="static/img/favicon-bee.ico")
        # insert it into the document
        soup.head.append(new_link)
        # soup.append(new_link)

    # save the file again
    with open(file_path, "w", encoding='utf-8') as outf:
        outf.write(str(soup))


add_bee_favicon('airbnbEU/airbnbEU.html')