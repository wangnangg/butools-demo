# Butools Demo

1. clone本仓库.

```
$ git clone https://github.com/wangnangg/butools-demo.git
```

2. 安装python 3.6.5.

3. 用pip安装virtualenv.

```
$ pip install --user virtualenv
```

4. 安装virtualenv到butools-demo的根目录下.

```
butools-demo$ virtualenv -p python3 venv
```

5. 激活virtualenv.

```
butools-demo$ source venv/bin/activate
```

6. 安装butools依赖, 依赖已经写在requirements.txt里面了.

```
butools-demo$ pip install -r requirements.txt
```

7. 运行demo.

```
butools-demo$ python demo.py
```

8. 使用完毕后可以关闭virtualenv.

```
$ deactivate
```



