import bs4

from urllib.request import urlopen as uReq

from bs4 import BeautifulSoup as soup

while True:
    while True:
        try:
            page_link = input('\nURL of page: ')
            fetched = uReq(page_link)
            content = fetched.read()
            fetched.close()
            content_html = soup(content,'html.parser')
            text = content_html.find_all('p')
            word_list = str(text)
            break
        except ValueError:
            print('\nPlease enter a valid URL')

    word_count = word_list.split()

    find = input('\nWhat keyword are you looking for?: ')

    if find in word_list:
        density = word_list.count(find)
        words_in_keyword = find.split()
        a = len(word_count)
        b = len(words_in_keyword)
        while True:
            try:
                c = round(a//b,4)
                d = round(density / c,4)
                e = round(d,4)
                f = e * 100
                print('\n' + str(round(f,3)) + '%' + ' keyword density')
                print('\nThe keyword appears ' + str(density) + ' times in the page.')
                break
            except ZeroDivisionError:
                print('\nDivision by Zero Error, Please input a valid keyword')
                break
    else:
        print('\n' + str(find) + ' does not appear in the URL, try again.')
