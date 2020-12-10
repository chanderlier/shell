import re
from urllib.parse import urljoin

import bs4
import requests


def main():
    headers = {'user-agent': 'Baiduspider'}
    base_url = 'https://www.zhihu.com/'
    resp = requests.get(urljoin(base_url, 'explore'), headers=headers)
    soup = bs4.BeautifulSoup(resp.text, 'lxml')
    href_regex = re.compile(r'^/question')
    links_set = set()
    for a_tag in soup.find_all('a', {'href': href_regex}):
        if 'href' in a_tag.attrs:
            href = a_tag.attrs['href']
            full_url = urljoin(base_url, href)
            links_set.add(full_url)
    print('Total %d question pages found.' % len(links_set))
    print(links_set)


if __name__ == '__main__':
    main()