![](https://img1.doubanio.com/view/subject/l/public/s28315327.jpg =250x)
[Python Web开发测试驱动方法](https://book.douban.com/subject/26640135/)的实践记录和代码


#### 问题记录

1. selenium选择chrome作为浏览器

```python
browser = webdriver.Chrome()
```

在mac上执行测试代码时会提示错误:

```sh
selenium.common.exceptions.WebDriverException: Message: 'chromedriver' executable needs to be in PATH. Please see https://sites.google.com/a/chromium.org/chromedriver/home
```

解决办法参照: <https://www.jianshu.com/p/e137031bc7db>
1. 从官网下载chromedriver对应的版本
2. 将文件解压缩到`/usr/local/bin/`目录下
