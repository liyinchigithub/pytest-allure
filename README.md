# python-allure

>该项目能够快速熟悉复习selenium webdriver + pytest +allure


[![python](https://img.shields.io/badge/python-3.7-green.svg)](https://www.python.org/downloads/release/python-374/) [![pip](https://img.shields.io/badge/pip-22.0.4-yellow.svg)](https://pip.pypa.io/en/stable/)[![selenium](https://img.shields.io/badge/selenium-v4.1.0-blue.svg)](https://pypi.org/project/selenium/)

# 目录说明
-src                    代码
--package               顶包
---module               模块（package包下的模块）
----__init__.py         模块初始化
----test_selenium.py    模块
-download_file          下载文件存放路径，通过chromeOptions capability设置
-save_images            webdriver 截图保存图片路径
-webdriver_init.py      webdriver 初始化(本地、远程、chromeoptions参数配置)
-logging_init.py        logging 初始化(日志初始化配置，每次触发写入本地文件和控制台)
-report                 allure生成json、html报告存放位置
-pytest.ini             pytest单元测试框架配置文件
-requirements.txt       依赖

## 安装依赖

```shell
pip install requirement.txt
```

## 运行所有用例脚本
```shell
pytest
```

## 运行指定用例脚本

```shell
pytest src/package/module/test_selenium.py
```

## 仅运行指定标志的用例
```shell
# 运行标注@pytest.mark.test的测试用例
pytest -m test
```
## 控制台详细输出

```shell
pytest -v
```

# Allure 配置

## 【allure window 配置环境变量】
>https://www.cnblogs.com/hl-2030/p/13690165.html?ivk_sa=1024320u

## 【mac、linux】

```shell
 cd ~
 vim .bash_profile 
 export ALLURE_HOME=/Users/liyinchi/workspace/python/python-learning/allure-2.17.2/
 export PATH=$PATH:ALLURE_HOME/bin
 allure --version
```

## 运行命令生成allure测试报告

>已在项目根目录下新建目录report，在report目录下html文件夹用于存放html报告

### 执行命令（生成json报告）

```shell
pytest -s -q --alluredir ./report
```

### 执行命令（生成html报告）
```shell
allure generate ./report -o ./report/html
```


## 参考

1. [selenium chrome options参数设置](https://note.youdao.com/s/ER8jfnYo)
2. [csdn 博文](https://www.cnblogs.com/guapitomjoy/p/12150416.html)
3. [csdn 博文](https://www.cnblogs.com/clement-jiao/p/10889234.html)