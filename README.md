# python-allure

>该项目能够快速熟悉复习selenium webdriver + pytest +allure


[![python](https://img.shields.io/badge/python-3.7-green.svg)](https://www.python.org/downloads/release/python-374/) [![pip](https://img.shields.io/badge/pip-22.0.4-yellow.svg)](https://pip.pypa.io/en/stable/)[![selenium](https://img.shields.io/badge/selenium-v4.1.0-blue.svg)](https://pypi.org/project/selenium/)

# 目录说明
* -src                    代码
* --package               顶包
* ---module               模块（package包下的模块）
* ----__init__.py         模块初始化
* ----test_selenium.py    模块
* -download_file          下载文件存放路径，通过chromeOptions capability设置
* -save_images            webdriver 截图保存图片路径
* -webdriver_init.py      webdriver 初始化(本地、远程、chromeoptions参数配置)
* -logging_init.py        logging 初始化(日志初始化配置，每次触发写入本地文件和控制台)
* -report                 allure生成json、html报告存放位置
* -pytest.ini             pytest单元测试框架配置文件
* -requirements.txt       依赖

<img width="1424" alt="image" src="https://user-images.githubusercontent.com/19643260/158414247-d78e87b9-f9e4-437b-9ea1-5fd122e5c38a.png">

<img width="1432" alt="image" src="https://user-images.githubusercontent.com/19643260/158414201-6d963efc-eb8b-45c2-a03d-a8dde6d15820.png">

## 更新pip

```python
pip install --upgrade pip
```

## 创建虚拟目录

```shell
# python -m venv 虚拟环境名称，名称是随意起的
python -m venv tutorial-env
```

## 激活虚拟环境

* 当激活虚拟环境时命令行上会有个虚拟环境名前缀

#### Unix或MacOS上激活虚拟环境
```shell
source tutorial-env/bin/activate
```
#### windows上激活虚拟环境
```shell
tutorial-env\Scripts\activate.bat
```

### 项目依赖安装
```shell
python3.7 -m pip install --upgrade pip
pip install -r requirements.txt
```

* 如果引入其他新的依赖，可以执行冻结第三方库，就是将所有第三方库及版本号保存到requirements.txt文本文件中
```shell
pip freeze > requirements.txt
```
* 如果pip不起作用，可以从pypi上下载最新的源码包(https://pypi.python.org/pypi/)进行安装：
```shell
python setup.py install 
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

* 编辑配置文件
```shell
 cd ~
 vim .bash_profile 
 source .bash_profile 
```
* 加入内容
```
# allure report
PATH="/Users/liyinchi/workspace/python/allure-2.17.2/bin:${PATH}"
export PATH
```
* 检查是否
```
 allure --version
```
<img width="573" alt="image" src="https://user-images.githubusercontent.com/19643260/158354024-69672ffc-2d11-4625-90b2-dd68efc196ab.png">

## 运行命令生成allure测试报告

>已在项目根目录下新建目录report，在report目录下html文件夹用于存放html报告

### 执行命令（生成json报告）

```shell
pytest -s -q --alluredir ./report
```

### 执行命令（生成html报告）
```shell
allure generate ./report -o ./report/html --clean
```

### 查看报告
```shell
allure open report/html
```
<img width="805" alt="image" src="https://user-images.githubusercontent.com/19643260/158414903-ca505fb5-1701-45f7-8fd7-b1ba5e7b8c8e.png">


## 参考

1. [selenium chrome options参数设置](https://note.youdao.com/s/ER8jfnYo)
2. [csdn 博文](https://www.cnblogs.com/guapitomjoy/p/12150416.html)
3. [csdn 博文](https://www.cnblogs.com/clement-jiao/p/10889234.html)
