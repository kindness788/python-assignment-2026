import json
from pathlib import Path
from processor import process_record
from verifier import generate_code, send_verification_code

def main(id: str):
    processed = []

    for path in sorted(Path("sample_data").glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        processed.append(process_record(data))

    code = generate_code(processed)
    send_verification_code(id, code)

if __name__ == "__main__":
    print("请严格按照要求完成，不得更改除processor.py以外的任何文件内容")
    print("请输入学号：")
    user_id = input().strip()
    main(user_id)