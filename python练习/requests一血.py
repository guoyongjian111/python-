#requests 模拟浏览器发请求
import requests
if __name__ == "__main__":
    url = "https://www.bilibili.com/"
    response = requests.get(url=url)
    page_txt = response.text
    print(page_txt)
    with open('./bilibili.html', 'w', encoding='utf-8') as f:
        f.write(page_txt)
