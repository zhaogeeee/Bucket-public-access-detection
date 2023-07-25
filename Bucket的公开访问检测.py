import tkinter as tk
from baidubce import exception
from baidubce.services.bos import bos_client
from baidubce.auth.bce_credentials import BceCredentials
from baidubce.bce_client_configuration import BceClientConfiguration


class BucketAccessChecker:
    def __init__(self, root):
        self.root = root
        self.root.title("Bucket Access Checker")
        self.root.geometry("400x250")

        self.label_ak = tk.Label(root, text="Access Key ID:")
        self.label_ak.pack(pady=10)
        self.entry_ak = tk.Entry(root)
        self.entry_ak.pack()

        self.label_sk = tk.Label(root, text="Secret Access Key:")
        self.label_sk.pack(pady=10)
        self.entry_sk = tk.Entry(root)
        self.entry_sk.pack()

        self.label_bucket = tk.Label(root, text="请输入Bucket名称：")
        self.label_bucket.pack(pady=20)

        self.textbox_bucket = tk.Entry(root)
        self.textbox_bucket.pack()

        self.button = tk.Button(root, text="检测", command=self.check_bucket_access)
        self.button.pack(pady=20)

        self.label_result = tk.Label(root, text="")
        self.label_result.pack()

    def check_bucket_access(self):
        bucket_name = self.textbox_bucket.get().strip()
        access_key_id = self.entry_ak.get().strip()
        secret_access_key = self.entry_sk.get().strip()

        # 验证 AK 和 SK 的有效性
        if not access_key_id or not secret_access_key:
            self.label_result["text"] = "请提供有效的 Access Key ID 和 Secret Access Key"
            return

        # 创建 BOS 客户端配置对象
        config = BceClientConfiguration(credentials=BceCredentials(access_key_id, secret_access_key),
                                        endpoint='bj.bcebos.com')

        # 创建 BOS 客户端对象
        client = bos_client.BosClient(config)

        try:
            # 查询 Bucket 的访问权限设置
            response = client.get_bucket_acl(bucket_name)

            if response.body is None:
                self.label_result["text"] = f"无法获取 Bucket '{bucket_name}' 的 ACL 设置"
                return

            acl = response.body.acl  # 获取 ACL 设置

            if acl == "public-read-write":
                self.label_result["text"] = f"Bucket '{bucket_name}' 是公开访问的"
            else:
                self.label_result["text"] = f"Bucket '{bucket_name}' 不是公开访问的"

        except exception.BceHttpClientError as e:
            if "AccessDenied" in str(e):
                self.label_result["text"] = "无效的 Access Key ID 或 Secret Access Key"
            else:
                self.label_result["text"] = f"检测 Bucket 出错：{str(e)}"


if __name__ == '__main__':
    root = tk.Tk()
    app = BucketAccessChecker(root)
    root.mainloop()
