from typing import Dict, Any, List

def process_record(record: Dict[str, Any]) -> Dict[str, Any]:
    """
    对一条记录进行处理，并返回处理后的结果

    参数：
        record: 字典，传入格式如下：
            - "user_id": str
            - "scores": List[int]
            - "enabled": bool

    处理规则：
        1. scores 中可能包含非法值（<= 0或浮点数），忽略非法值
        2. 若所有 scores 均非法，平均分为 0.0
        3. 平均分保留两位小数
        4. 状态判定规则：
            - enabled 为 True 且 平均分 >= 60 => "PASS"
            - 否则 => "FAIL"

    返回：
        一个新的字典，格式如下：
            - "user_id": 原 user_id
            - "average_score": float
            - "status": str

    注意：
        - 不要修改传入的 record
        - 返回值结构必须严格一致
    """
    raise NotImplementedError