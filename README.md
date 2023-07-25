# Bucket-public-access-detection
仅是新手自己练手使用
\color{#24292f}{\bg{#f4f6f8}{Bucket Access Checker 是一个用于检测百度云存储（Baidu Cloud Storage，简称 BOS）中指定 Bucket 的访问权限的桌面应用程序。}}
## \color{#24292f}{\bg{#f4f6f8}{功能}}
* \color{#24292f}{\bg{#f4f6f8}{输入有效的 Access Key ID 和 Secret Access Key}}
* \color{#24292f}{\bg{#f4f6f8}{输入要检查的 Bucket 名称}}
* \color{#24292f}{\bg{#f4f6f8}{检测 Bucket 的访问权限设置}}
* \color{#24292f}{\bg{#f4f6f8}{显示结果：如果 Bucket 是公开访问的，将显示相应消息；否则，将显示不是公开访问的提示。}}
## \color{#24292f}{\bg{#f4f6f8}{运行环境}}
* \color{#24292f}{\bg{#f4f6f8}{Python 3.x}}
## \color{#24292f}{\bg{#f4f6f8}{安装依赖}}
```
pip install tkinter baidubce
```
## \color{#24292f}{\bg{#f4f6f8}{如何使用}}
1. \color{#24292f}{\bg{#f4f6f8}{在根目录运行以下命令启动应用程序：}}
```
python main.py
```
1. \color{#24292f}{\bg{#f4f6f8}{在应用程序界面中输入有效的 Access Key ID 和 Secret Access Key。}}
2. \color{#24292f}{\bg{#f4f6f8}{输入要检查的 Bucket 名称。}}
3. \color{#24292f}{\bg{#f4f6f8}{点击 "检测" 按钮，等待程序执行检测。}}
4. \color{#24292f}{\bg{#f4f6f8}{结果将在界面中显示。}}
\color{#24292f}{\bg{#f4f6f8}{注意：确保已提供正确有效的密钥信息以及要检查的 Bucket 名称。}}
## \color{#24292f}{\bg{#f4f6f8}{注意事项}}
* \color{#24292f}{\bg{#f4f6f8}{请确保您拥有有效的 Baidu Cloud Storage (BOS) 账户并具有足够的权限来访问和管理所选的 Bucket。}}
* \color{#24292f}{\bg{#f4f6f8}{使用此应用程序时，建议在安全环境中处理密钥信息，并确保不泄露给未经授权的用户。}}
## \color{#24292f}{\bg{#f4f6f8}{参考资料}}
* \color{var(--color-accent-fg)}{\bg{transparent}{[百度云存储官方文档](https://cloud.baidu.com/doc/BOS/Developer-Resource.html)}}
\color{#24292f}{\bg{#f4f6f8}{请根据实际情况进行适当修改和补充的README文件。}}
