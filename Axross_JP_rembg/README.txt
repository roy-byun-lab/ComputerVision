pythonを用いて背景を除去する方法

U2Netというセグメンテーションモデルが採用されています。

処理:
    1.U2Netでセグメンテーションを行いマスクを作成
    2.元画像にマスクを適用し対象物を切り出し
rembgのソースコードはgithubに商用利用可能な MITライセンス として公開
    https://github.com/danielgatis/rembg

Install
pip install rembg