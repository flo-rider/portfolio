import bs4
import sys

html_path = sys.argv[1]
new_title = sys.argv[2]


def add_bee_favicon(path):
    # load the file
    with open(path, 'r', encoding='utf-8') as input_file:
        txt = input_file.read()
        soup = bs4.BeautifulSoup(txt)
        print(type(soup))
        # create new link
        new_link = soup.new_tag("link", rel="icon", href="static/img/favicon-bee.ico")
        # insert it into the document
        soup.head.append(new_link)
        # soup.append(new_link)

    # save the file again
    with open(path, "w", encoding='utf-8') as output_file:
        output_file.write(str(soup))


def change_title(path, title):
    with open(path, 'r', encoding='utf-8') as inf:
        txt = inf.read()
        soup = bs4.BeautifulSoup(txt)
        # find the title tag using `find` method
        title_tag = soup.find('title')
        # change the text of the title tag `string` property
        title_tag.string = title

    with open(path, "w", encoding='utf-8') as outf:
        outf.write(str(soup))


add_bee_favicon(html_path)
change_title(html_path, new_title)
