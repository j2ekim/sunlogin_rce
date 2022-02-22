# 向日葵RCE漏洞检测工具

## 使用需知
仅供企业内部安全隐患排查使用

由于传播、利用此工具而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。

## 功能
只写了漏洞利用，暂时没写端口检测

有空再完善代码，及添加批量检测功能


## 使用方法
```shell
python exp.py -a [--host] -p [--port] -c [--command] 
python exp.py -a 127.0.0.1 -p 20038 -c "net user"
```
![image-20220218041904120](https://cdn.jsdelivr.net/gh/j2ekim/blog-image/image/image-20220222160713132.png)
