import bs4

def add_bee_favicon(path="existing_file.html"):
# load the file
    with open(path, 'r', encoding='utf-8') as inf:
        txt = inf.read()
        soup = bs4.BeautifulSoup(txt)
        print(type(soup))
        # create new link
        new_link = soup.new_tag("link", rel="icon", href="static/img/favicon-bee.ico")
        # insert it into the document
        soup.head.append(new_link)
        # soup.append(new_link)

    # save the file again
    with open(path, "w", encoding='utf-8') as outf:
        outf.write(str(soup))


# add_bee_favicon('airbnbEU/airbnbEU.html')
def change_title(path, new_title):
    with open(path, 'r', encoding='utf-8') as inf:
        txt = inf.read()
        soup = bs4.BeautifulSoup(txt)
        # find the title tag using `find` method
        title_tag = soup.find('title')
        # change the text of the title tag `string` property
        title_tag.string = new_title

    with open(path, "w", encoding='utf-8') as outf:
        outf.write(str(soup))


# change_title('airbnbEU/airbnbEU.html', 'Pricing airbnb')