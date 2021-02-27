# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 21:47:22 2021

@author: valle
"""

import smtplib
import os
from email import message



path=input("ENTER_YOUR_TEXTFILE_PASS:")#テキストファイルのパスを入力
with open(path,encoding="utf-8") as f:
    s=f.read()


print(s)#メールの本文を確認

confirm=input("間違っていませんか? y or n:")#yで送信nでやり直し

if confirm == "y":
    MyPass=os.environ.get("GOOGLE_PASS")#環境変数から取得

    smtp_host = 'smtp.gmail.com'   # メールを送るSMTPサーバー
    smtp_port = 587   # ポート番号
    from_email = 'YOUR_MAIL_ADRESS'   # 送信元のメールアドレス(Gmeilアドレス)
    to_email = 'TO_MAIL_ADRESS'   # 送信先のメールアドレス
    username = 'GMAIL_ACCOUNT_ADRESS'   # ユーザーネームはGoogleアカウント（Gmailアドレス）
    password = MyPass   # Googleアカウントのパスワード
    
    # 送信メールを作成する
    msg = message.EmailMessage()   # メッセージオブジェクトを作成

    msg.set_content(s)   # メール本文
    msg['Subject'] = 'TITLE'   # メールのタイトル（件名）
    msg['From'] = from_email   # メール送信元
    msg['To'] = to_email   # メール送信先
    
    # メールサーバーへアクセスする
    server = smtplib.SMTP(smtp_host, smtp_port)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(username, password)
    server.send_message(msg)
    server.quit()
    print("送信しました")
else:
    print("やり直してください")