import os
from dotenv import load_dotenv
from pinecone import Pinecone

# .env 読み込み
load_dotenv()
api_key = os.getenv("PINECONE_API_KEY")
environment = os.getenv("PINECONE_ENVIRONMENT")  # 例: "us-east-1"

if not api_key or not environment:
    raise ValueError("環境変数 PINECONE_API_KEY または PINECONE_ENVIRONMENT が設定されていません。")

# Pinecone 初期化
pc = Pinecone(api_key=api_key, environment=environment)
index = pc.Index("gyosei-dense")

# データのアップサート
records = [
    {"id": "rec1", "values": [0.1] * 1024,  # 1024次元のダミーベクトル
     "metadata": {"category": "history"}},
    {"id": "rec2", "values": [0.2] * 1024,  # 1024次元のダミーベクトル
     "metadata": {"category": "architecture"}}
]

index.upsert(vectors=records, namespace="example-namespace")

# セマンティック検索
# query_text = "Famous historical structures" # テキストによるクエリは不要に
query_vector = [0.15] * 1024 # 1024次元のダミークエリベクトル

response = index.query(
    namespace="example-namespace",
    top_k=5,
    include_values=True,
    include_metadata=True,
    vector=query_vector, # テキストの代わりにベクトルを渡す
    filter={"category": {"$eq": "history"}}
)

for match in response["matches"]:
    print(
        f"ID: {match['id']}, Score: {match['score']}, "
        f"Category: {match['metadata']['category']}"
    )
