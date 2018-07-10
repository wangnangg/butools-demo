# Butools Demo

这个demo演示了如何使用Butools来做Phase Type Fitting. 在demo.py中, 我们首先从pareto分布中采样了10000个点 (把它们叫做一个trace). 然后, 我们分别使用了含有3个, 5个, 7个transient states的连续时间马尔科夫链来fit这个trace. 最后, 我们对比了原始trace的经验分布函数(Empirical CDF)和fit出来的分布函数(fitted CDF), 可以看到, 随着使用的state数量增多, fit效果在变好.

以下步骤我仅在Linux环境中测试过, Windows中也许也可以. 另外, python使用python 3应该就可以了, 具体版本应该不重要.

## 步骤

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



