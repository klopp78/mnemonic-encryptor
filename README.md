# 助记词加密器 (Mnemonic Encryptor)

这是一个 Python 脚本，用于安全地加密和解密 12~24 个单词的助记词短语（例如加密货币钱包）。  
它结合了 **Base64 编码**、用户自定义的特殊字符，以及 **AES-256-CBC 加密**。  
该脚本提供了一个命令行菜单界面，方便操作。

## 功能特性
- 🔐 将 12~24 个单词的助记词短语加密为带有特殊字符的 Base64 编码密文。
- 🛡️ 使用 AES-256-CBC 进行安全加密，并随机生成密钥和初始化向量 (IV)。
- 🔑 使用密钥和特殊字符将密文解密回原始助记词短语。
- 🖥️ 提供交互式菜单界面，支持加密和解密操作。

## 先决条件
- Ubuntu 20.04 或更高版本
- Python 3.6 或更高版本
- Git（用于克隆仓库）
- Python 库 `pycryptodome`

## 安装 (Ubuntu)

### 1. 更新软件包列表
```bash
sudo apt update

2. 安装 Python 和 Pip
apt install python3 python3-pip

3. 安装 Git（可选，用于克隆）
sudo apt install git

4. 克隆仓库
git clone https://github.com/klopp78/mnemonic-encryptor.git
cd mnemonic-encryptor
chmod +x mnemonic_encryptor.py

5. （可选）创建虚拟环境
python3 -m venv venv
source venv/bin/activate
./mnemonic_encryptor.py
or
python3 mnemonic_encryptor.py
