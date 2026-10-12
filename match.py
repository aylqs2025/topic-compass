from topics import TOPICS

TIME_SCORE = {"极少": 0, "少": 1, "中": 2, "多": 3}
TECH_SCORE = {"低": 1, "中": 2, "高": 3}


def score_topic(topic, student):
    """计算一道题和一个学生的匹配分"""
    score = 0
    reasons = []

    # 时间
    if TIME_SCORE[topic["时间"]] <= TIME_SCORE[student["时间"]]:
        score += 2
        reasons.append("时间匹配")
    elif topic["时间"] == "多" and student["时间"] == "中":
        score += 1
        reasons.append("时间略紧")
    else:
        reasons.append("时间不匹配")

    # 技术
    if TECH_SCORE[topic["技术"]] <= TECH_SCORE[student["技术"]]:
        score += 2
        reasons.append("技术匹配")
    else:
        reasons.append("技术偏难")

    # 偏好
    if topic["偏好"] == student["偏好"]:
        score += 3
        reasons.append("偏好一致")

    # 难度适配
    if topic["难度"] == "易" and student["时间"] in ["极少", "少"]:
        score += 2
        reasons.append("难度适合时间少")
    if topic["难度"] == "高" and student["技术"] == "高":
        score += 2
        reasons.append("难度适合技术强")

    return score, "；".join(reasons)


def recommend(student, top_n=3):
    """给一个学生推荐 top_n 道题"""
    results = []
    for t in TOPICS:
        s, reason = score_topic(t, student)
        results.append({**t, "匹配分": s, "匹配理由": reason})
    results.sort(key=lambda x: x["匹配分"], reverse=True)
    return results[:top_n]