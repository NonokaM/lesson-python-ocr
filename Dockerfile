FROM google/cloud-sdk:latest

# python コマンドに　python3 へのリンクを設定（必須ではない）
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 1

# vision クライアント ライブラリのインストール
RUN python -m pip install --upgrade google-cloud-vision
