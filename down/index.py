# 'https://www.mycqzx.com:65/20190914/FsKCJvDf/2000kb/hls/n9t2yfIv.ts'
from multiprocessing.pool import ThreadPool

import requests


def get(url):
    print(url)
    if not url:
        return None
    with open(f'./data/{url.split("/")[-1]}', 'wb') as file:
        file.write(requests.get(url).content)


if __name__ == '__main__':
    index_m3u8 = input("please input m3u8 url:")

    from urllib.parse import urlparse

    v = urlparse(index_m3u8)

    netloc = f'{v.scheme}://{v.netloc}'

    rs = requests.get(url=index_m3u8.strip())

    if rs.status_code != 200:
        fs = []
    else:
        print(rs.text)
        fs = rs.content.decode('U8').split('\n')
        fs = [f'{netloc}/{i}' for i in fs if i and not i.startswith('#')]
    if fs:
        pool = ThreadPool(20)
        _ = pool.map(get, fs)

    with open('index.mp4', 'wb') as f:
        for i in fs:
            if not i:
                continue
            try:
                i = i.split('/')[-1]
                f.write(open(f'./data/{i}', 'rb').read())
            except Exception as e:
                print(e)
                get(i)
                i = i.split('/')[-1]
                f.write(open(f'./data/{i}', 'rb').read())
    print('success')
