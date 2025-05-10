# Pinecone クライアント サンプル

これは、Pinecone ベクトルデータベースを利用して、データのアップサート（登録・更新）とセマンティック検索を行う Python スクリプトのサンプルです。

## 概要

`pinecone_client.py` スクリプトは、以下の処理を実行します。

1.  環境変数ファイル (`.env`) から Pinecone の API キーと環境情報を読み込みます。
2.  Pinecone に接続し、指定されたインデックスを取得します。
3.  事前に定義されたサンプルレコード（ID、ベクトル、メタデータを含む）をインデックスにアップサートします。
4.  指定されたクエリベクトルを使用して、インデックスから類似度の高いデータを検索します。
5.  検索結果（ID、スコア、メタデータ）を表示します。

## 前提条件

*   Python 3.8 以降
*   Pinecone アカウントと API キー
*   Pinecone 上に、スクリプト内で指定する次元数（デフォルトでは1024次元）のインデックスが作成済みであること。インデックス名は `gyosei-dense` を想定していますが、スクリプト内で変更可能です。

## セットアップ

1.  **リポジトリをクローンまたはダウンロードします。**

2.  **Python 仮想環境の作成と有効化（推奨）:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux / macOS
    # venv\Scripts\activate  # Windows
    ```

3.  **必要なライブラリをインストールします:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **環境変数の設定:**
    プロジェクトのルートディレクトリに `.env` という名前のファイルを作成し、以下の情報を記述します。
    ```env
    PINECONE_API_KEY="YOUR_PINECONE_API_KEY"
    PINECONE_ENVIRONMENT="YOUR_PINECONE_ENVIRONMENT"
    ```
    `YOUR_PINECONE_API_KEY` と `YOUR_PINECONE_ENVIRONMENT` を実際の値に置き換えてください。
    `PINECONE_ENVIRONMENT` は、Pinecone のコンソールで確認できるリージョン情報（例: `gcp-starter`, `us-east1-gcp` など）です。

## 実行方法

以下のコマンドでスクリプトを実行します。

```bash
python pinecone_client.py
```

スクリプトが正常に実行されると、コンソールに検索結果が出力されます。

## スクリプトのカスタマイズ

*   **インデックス名:** `pinecone_client.py` 内の以下の行で、使用する Pinecone インデックス名を変更できます。
    ```python
    index = pc.Index("gyosei-dense")
    ```
*   **アップサートするデータ:** `records` 変数内のデータを変更することで、異なるデータをアップサートできます。各レコードの `values` は、Pinecone インデックスの次元数と一致する数値のリスト（ベクトル）である必要があります。
    ```python
    records = [
        {"id": "rec1", "values": [0.1] * 1024, "metadata": {"category": "history"}},
        # ... 他のレコード
    ]
    ```
*   **検索クエリ:** `query_vector` 変数の値を変更することで、異なるクエリベクトルで検索を実行できます。このベクトルも、インデックスの次元数と一致する必要があります。
    ```python
    query_vector = [0.15] * 1024
    ```
*   **名前空間:** `upsert` メソッドと `query` メソッドの `namespace` パラメータで、使用する名前空間を指定できます。

## 注意点

*   このサンプルでは、ベクトルデータとしてダミーの数値リストを使用しています。実際のアプリケーションでは、テキストや画像などの元データからエンベディングモデル（Sentence Transformers, OpenAI API など）を使用してベクトルを生成する必要があります。
*   エラー処理は基本的なもののみ含まれています。実際の運用では、より堅牢なエラーハンドリングを実装してください。 