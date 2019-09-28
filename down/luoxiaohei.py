import requests
from multiprocessing.pool import ThreadPool


def get(url):
    print(url)
    if not url:
        return None
    rs = requests.get(f'https://baidu.com-ok-baidu.com/20190910/14935_da987396/1000k/hls/{url}')
    with open(f'./data/{url}', 'wb') as file:
        # rs = requests.get(f'https://baidu.com-ok-baidu.com/20190910/14935_da987396/1000k/hls/{i}')
        file.write(rs.content)


if __name__ == '__main__':
    with open('index.m3u8', 'r') as file:
        fs = file.read().split('\n')
    fs = [i for i in fs if not i.startswith('#')]
    pool = ThreadPool(20)
    _ = pool.map(get, fs)
    # 文件合并
    with open('abc.mp4', 'wb') as f:
        for i in fs:
            if not i:
                continue
            try:
                f.write(open(f'./data/{i}', 'rb').read())
            except  Exception as e:
                print(e)
                get(i)
                f.write(open(f'./data/{i}', 'rb').read())

    print('end')
