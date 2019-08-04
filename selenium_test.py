# coding=utf-8
from selenium import webdriver
import time

# chromedriver安装&配置添加说明:

# 1-本机配置环境变量PATH之后仍无法打开chrome/ 则指定chromedriver所在路径做启动
PATH = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'

# 2-直接将chromedriver.exe添加至Python\Python36\Scripts(python安装目录下)即可


def main():
    # b = webdriver.Chrome(executable_path=PATH)  # 对应方法1
    b = webdriver.Chrome()  # 对应方法2
    b.get('http://www.baidu.com')
    time.sleep(5)
    b.quit()


if __name__ == '__main__':
    main()
