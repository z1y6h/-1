# from bs4 import BeautifulSoup

# if __name__ == '__main__':
#     file = open('c:/Users/zenghong/Desktop/TEST/data-mining/Stars.html', 'rb')
#     html = file.read().decode('utf-8')
#     bs = BeautifulSoup(html, 'html.parser')
#     li = bs.find_all('li', {'class': 'repo-item'})
#     for i in li:
#         contentFrom = {
#             'header': i.find('h3').text(),
#             'url':i.find('a').attrs['href'],
#             'star':i.find('span', {'class': 'repo-star'}).text(),
#             'language':i.find('span', {'class': 'repo-language'}).text(),
#             'description':i.find('p').text()
#         }


from bs4 import BeautifulSoup

if __name__ == '__main__':
          file = open('C://Users/zenghong/Desktop/TEST/data-mining/Stars.html','rb')
          html = file.read().decode('utf-8')
          bs = BeautifulSoup(html, 'html.parser')
          li = bs.find_all('li', {'class':'repo-item'})
          contents = []
          for content in li:
                    contentForm = {
                              'header': content.find('h3').text,
                              'url': content.find('a').attrs['href'],
                              'star': content.find('span',{'class':'repo-star'}).text,
                              'language': content.find('span',{'class': 'repo-language'}).text,
                              'description': content.find('p').text,
                    }
                    print(contentForm)
                    contents.append(contentForm)


try:
    with open('a.json', 'a', encoding='utf-8') as f:
        f.write(json.dumps(contents, ensure_ascii = False))
except IOError as e:
    print(str(e))
finally:
    f.close()
        