#!/usr/bin/env python3
import base64
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os
import sys

def clear_screen():
    """清空终端屏幕"""
    os.system('clear')

def pad_data(data):
    """为AES加密填充数据到16字节的倍数"""
    pad_length = 16 - (len(data) % 16)
    return data + (b'\x00' * pad_length)

def unpad_data(data):
    """移除填充"""
    return data.rstrip(b'\x00')

def encrypt_mnemonic(mnemonic, special_char):
    """加密助记词"""
    # 移除单字符验证，允许任意长度的特殊符号
    if not special_char:
        return None, None, "特殊符号不能为空！"
    
    mnemonic_bytes = mnemonic.encode('utf-8')
    base64_encoded = base64.b64encode(mnemonic_bytes).decode('utf-8')
    base64_with_special = base64_encoded + special_char

    key = get_random_bytes(32)
    iv = get_random_bytes(16)
    data = base64_with_special.encode('utf-8')
    data_padded = pad_data(data)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(data_padded)
    encrypted_data = iv + ciphertext
    encrypted_data_base64 = base64.b64encode(encrypted_data).decode('utf-8')
    key_base64 = base64.b64encode(key).decode('utf-8')

    return encrypted_data_base64, key_base64, None

def decrypt_mnemonic(encrypted_data_base64, key_base64, special_char):
    """解密助记词"""
    try:
        encrypted_data = base64.b64decode(encrypted_data_base64)
        key = base64.b64decode(key_base64)
        iv = encrypted_data[:16]
        ciphertext = encrypted_data[16:]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted_padded = cipher.decrypt(ciphertext)
        decrypted_data = unpad_data(decrypted_padded)
        decrypted_with_special = decrypted_data.decode('utf-8')

        if decrypted_with_special.endswith(special_char):
            base64_encoded = decrypted_with_special[:-len(special_char)]
            mnemonic_restored = base64.b64decode(base64_encoded).decode('utf-8')
            return mnemonic_restored, None
        else:
            return None, "错误：特殊符号不匹配"
    except Exception as e:
        return None, f"解密失败：{str(e)}"

def main_menu():
    """显示主菜单"""
    while True:
        clear_screen()
        print("=== 助记词加密/解密工具 ===")
        print("1. 加密助记词")
        print("2. 解密助记词")
        print("3. 退出")
        choice = input("\n请输入选项 (1-3): ")

        if choice == '1':
            clear_screen()
            print("=== 加密助记词 ===")
            mnemonic = input("请输入12到24个助记词（用空格分隔）: ")
            # 验证助记词数量（12到24个单词）
            word_count = len(mnemonic.split())
            if word_count not in [12, 15, 18, 21, 24]:
                print("错误：助记词必须包含12、15、18、21或24个单词！")
                input("按回车返回菜单...")
                continue
            special_char = input("请输入特殊符号（建议多字符：")
            encrypted_data, key, error = encrypt_mnemonic(mnemonic, special_char)
            if error:
                print(error)
            else:
                print("\n加密结果（Base64）：")
                print(encrypted_data)
                print("\n密钥（Base64）：")
                print(key)
                print("\n请妥善保存加密结果、密钥和特殊符号！")
            input("按回车返回菜单...")

        elif choice == '2':
            clear_screen()
            print("=== 解密助记词 ===")
            encrypted_data = input("请输入加密数据（Base64）：")
            key = input("请输入密钥（Base64）：")
            special_char = input("请输入特殊符号（与加密时相同）：")
            mnemonic_restored, error = decrypt_mnemonic(encrypted_data, key, special_char)
            print("\n解密结果：")
            if mnemonic_restored:
                print(mnemonic_restored)
            else:
                print(error)
            input("按回车返回菜单...")

        elif choice == '3':
            clear_screen()
            print("感谢使用，再见！")
            sys.exit(0)
        else:
            print("无效选项，请输入1-3！")
            input("按回车继续...")

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        clear_screen()
        print("程序已退出！")
        sys.exit(0)
