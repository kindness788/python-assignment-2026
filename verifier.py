# 不得修改本文件！
import json
import hashlib
from typing import List, Dict


def generate_code(results: List[Dict]) -> str:
    """
    根据处理结果生成识别码

    不要修改本文件
    """
    payload = json.dumps(results, sort_keys=True, ensure_ascii=False)
    raw = payload.encode("utf-8")
    digest = hashlib.sha256(raw).hexdigest()
    return digest[:16]

def send_verification_code(id: str,code: str):
    """
    发送识别码到指定服务器进行验证

    不要修改本文件
    """
    import requests
    
    data = {
        "id": id,
        "code": code
    }

    url = "https://api.rinkosoft.me/verify"
    response = requests.post(url, json=data, timeout=10)
    if response.status_code == 200:
        result = response.json()
        print(result.get("message", "No message provided"))
    else:
        result = response.json()
        print(result.get("message", "Verification failed"))