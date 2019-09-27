import requests

if __name__ == '__main__':
    with open('index.m3u8', 'r') as file:
        fs = file.read().split('\n')
    fs = [i for i in fs if not i.startswith('#')]
    with open('luoxiaohei.mp4', 'wb') as file:
        for i in fs:
            print(i)
            if i:
                rs = requests.get(f'https://baidu.com-ok-baidu.com/20190910/14935_da987396/1000k/hls/{i}')
                file.write(rs.content)
