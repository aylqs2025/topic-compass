# 选题罗盘 Topic Compass —— 分步创建指南

## 第 1 步：创建纯 Python 工程

在 PyCharm 里新建一个纯 Python 项目，项目名为 `topic-compass`。

- 项目位置：自选，比如 `D:\projects\topic-compass`
- Python 解释器：选 `New environment`，新建虚拟环境 `.venv`
- 项目类型：Pure Python

完成后，项目根目录下会自动生成 `.venv` 文件夹。


## 第 2 步：创建项目文件夹和虚拟环境（命令行方式）

如果你不用 PyCharm，也可以用命令行：

```bash
mkdir topic-compass
cd topic-compass
python -m venv .venv
```



## 第 3 步：创建四个文件

在项目根目录下，创建以下四个文件：

```bash
topic-compass/
├── requirements.txt    # 依赖
├── topics.py           # 选题池（18 道题）
├── match.py            # 匹配规则
└── app.py              # Streamlit 主程序
```
创建方式：在 PyCharm 左侧项目栏右键 → New → File，输入文件名。

## 第 4 步：写 requirements.txt

打开 requirements.txt，写入：
```bash
streamlit
pandas
openpyxl
```
保存。
## 第 5 步：写 topics.py

打开 topics.py，写入：

```python
# 选题池：18 道题
TOPICS = [
    # 方向一
    {"编号": "A1", "题目": "元音口型的数字画像——唇形指标构建、可分性分析与可视化反馈智能体",
     "方向": "方向一", "数据": "GRID 视频", "难度": "中", "时间": "中", "技术": "高", "偏好": "系统"},
    {"编号": "A2", "题目": "朗读节奏画像——词时长与停顿的分布特征分析",
     "方向": "方向一", "数据": "GRID 词段表", "难度": "易", "时间": "少", "技术": "低", "偏好": "分析"},
    {"编号": "A3", "题目": "说话人时长指纹——基于词时长的说话人区分研究",
     "方向": "方向一", "数据": "GRID 词段表", "难度": "中", "时间": "中", "技术": "中", "偏好": "系统"},
    {"编号": "A4", "题目": "英语辅音时长特征分析——基于音素级标注",
     "方向": "方向一", "数据": "GRID 音素标注", "难度": "中", "时间": "中", "技术": "中", "偏好": "分析"},
    {"编号": "A5", "题目": "英语句末语调分析——基于 GRID 音频",
     "方向": "方向一", "数据": "GRID 音频", "难度": "中", "时间": "中", "技术": "中", "偏好": "分析"},
    # 方向二
    {"编号": "B1", "题目": "部首体系的长尾——3755 个常用字的部首分布与分类难度分析",
     "方向": "方向二", "数据": "包B", "难度": "易", "时间": "少", "技术": "低", "偏好": "分析"},
    {"编号": "B2", "题目": "汉字结构类型分布分析——基于 3755 个常用字",
     "方向": "方向二", "数据": "包B", "难度": "易", "时间": "少", "技术": "低", "偏好": "分析"},
    {"编号": "B3", "题目": "写字教学智能体——笔画与部首封装成问答原型并做评测",
     "方向": "方向二", "数据": "包B", "难度": "中", "时间": "中", "技术": "中", "偏好": "系统"},
    {"编号": "B4", "题目": "英语词汇难度分析与试题生成智能体设计",
     "方向": "方向二", "数据": "Words-CEFR", "难度": "中", "时间": "中", "技术": "中", "偏好": "系统"},
    # 方向三
    {"编号": "C1", "题目": "发音练习智能体——唇形指标封装成反馈原型并做评测",
     "方向": "方向三", "数据": "GRID", "难度": "中", "时间": "中", "技术": "高", "偏好": "系统"},
    {"编号": "C2", "题目": "基于唇形与语音双模态的发音练习智能体设计与评测",
     "方向": "方向三", "数据": "GRID 视频+音频", "难度": "中", "时间": "中", "技术": "高", "偏好": "系统"},
    {"编号": "C3", "题目": "英语词频与拼写特征的多维度分析",
     "方向": "方向三", "数据": "SUBTLEX", "难度": "易", "时间": "少", "技术": "低", "偏好": "分析"},
    {"编号": "C4", "题目": "银行客户流失特征分析",
     "方向": "方向三", "数据": "Kaggle", "难度": "中", "时间": "中", "技术": "中", "偏好": "分析"},
    # 高难度
    {"编号": "D1", "题目": "基于多智能体协作的手术场景自然语言交互框架设计与评测",
     "方向": "挑战题", "数据": "3MDBench", "难度": "高", "时间": "多", "技术": "高", "偏好": "系统"},
    {"编号": "D2", "题目": "基于唇形与语音的多模态发音错误检测",
     "方向": "挑战题", "数据": "GRID", "难度": "高", "时间": "多", "技术": "高", "偏好": "分析"},
    {"编号": "D3", "题目": "英语朗读节奏的说话人聚类分析",
     "方向": "挑战题", "数据": "GRID 词段表", "难度": "高", "时间": "多", "技术": "高", "偏好": "分析"},
    {"编号": "D4", "题目": "汉字部首的图神经网络分类",
     "方向": "挑战题", "数据": "包B", "难度": "高", "时间": "多", "技术": "高", "偏好": "分析"},
    {"编号": "D5", "题目": "基于大模型的英语词汇难度自动标注",
     "方向": "挑战题", "数据": "Words-CEFR", "难度": "高", "时间": "多", "技术": "高", "偏好": "分析"},
]
```

## 第 6 步：写 match.py

打开 match.py，写入：

```python
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
```

## 第 7 步：写 app.py

打开 app.py，写入：

```python
import streamlit as st
import pandas as pd
from match import recommend

# ---------- 白名单：学号 -> 姓名 ----------
ALLOWED_STUDENTS = {
    "231560131": "汪怡",
    "231560146": "董陆屹",
    "231560151": "金哲",
    "231560154": "陆欣祎",
    "231560160": "黄立乾",
    "231560167": "杨棋月",
    "231560252": "陆欣怡",
}

st.set_page_config(page_title="选题罗盘 Topic Compass", layout="wide")
st.title("选题罗盘 Topic Compass")
st.write("毕业论文选题匹配智能体。在线填写、导入 Excel，或对话描述你的情况。")

# ---------- 身份验证 ----------
st.sidebar.header("身份验证")
sid_input = st.sidebar.text_input("学号")
name_input = st.sidebar.text_input("姓名")

is_allowed = False

if sid_input and name_input:
    if sid_input not in ALLOWED_STUDENTS:
        st.sidebar.error("你不是智能数据处理团队成员")
    elif ALLOWED_STUDENTS[sid_input] != name_input:
        st.sidebar.error("学号与姓名不匹配")
    else:
        is_allowed = True
        st.sidebar.success(f"欢迎，{name_input}")

# ---------- 输入方式 ----------
input_method = st.sidebar.radio("输入方式", ["在线填写", "导入 Excel", "对话模式"])

student = {}

# ---------- 在线填写 ----------
if input_method == "在线填写":
    name = st.sidebar.text_input("姓名（填写）")
    time = st.sidebar.selectbox("每周时间", ["少", "中", "多"])
    tech = st.sidebar.selectbox("技术基础", ["低", "中", "高"])
    pref = st.sidebar.selectbox("论文偏向", ["分析", "系统"])
    concern = st.sidebar.selectbox("最担心", ["编程", "统计", "时间", "聚焦"])
    student = {"姓名": name, "学号": sid_input, "时间": time, "技术": tech,
               "偏好": pref, "顾虑": concern}

# ---------- 导入 Excel ----------
elif input_method == "导入 Excel":
    uploaded = st.sidebar.file_uploader("上传选题意向调查表", type=["xlsx"])
    if uploaded:
        try:
            df = pd.read_excel(uploaded, sheet_name="调查表", header=None)

            def get_answer(row_idx):
                return str(df.iloc[row_idx, 3])

            name = get_answer(1)
            sid = get_answer(2)
            time_raw = get_answer(9)
            time = "少" if ("3—6" in time_raw or "3 小时以内" in time_raw) else ("多" if "10 小时以上" in time_raw else "中")
            py_raw = get_answer(20)
            tech = "低" if "不会" in py_raw else ("高" if "熟练" in py_raw else "中")
            pref_raw = get_answer(18)
            pref = "系统" if "系统原型" in pref_raw else "分析"
            concern_raw = get_answer(30)
            concern = "时间" if "时间" in concern_raw else ("编程" if "编程" in concern_raw else ("统计" if "统计" in concern_raw else "聚焦"))

            student = {"姓名": name, "学号": sid, "时间": time, "技术": tech,
                       "偏好": pref, "顾虑": concern}
            st.sidebar.success(f"已解析：{name}（{sid}）")
        except Exception as e:
            st.sidebar.error(f"解析失败：{e}")

# ---------- 对话模式 ----------
else:
    if not is_allowed:
        st.warning("对话模式仅限智能数据处理团队成员使用。请输入学号和姓名验证身份。")
    else:
        st.subheader("对话模式")
        st.write("描述你的情况，比如：我全职实习，Python 一般，想轻松一点。")

        user_input = st.text_area("你的描述")

        if st.button("分析并推荐") and user_input:
            time = "少" if ("全职" in user_input or "忙" in user_input) else "中"
            tech = "低" if "不会" in user_input else ("高" if "熟练" in user_input else "中")
            pref = "系统" if ("系统" in user_input or "演示" in user_input) else "分析"

            student = {"姓名": name_input, "学号": sid_input, "时间": time,
                       "技术": tech, "偏好": pref, "顾虑": ""}
            st.write("提取到的维度：", student)

# ---------- 匹配 ----------
if st.sidebar.button("匹配选题") and student:
    recs = recommend(student, top_n=3)

    st.subheader(f"推荐结果（{student.get('姓名', '')}）")
    for i, r in enumerate(recs, 1):
        with st.expander(f"推荐 {i}：{r['题目']}（匹配分 {r['匹配分']}）", expanded=(i == 1)):
            st.write(f"**方向**：{r['方向']}")
            st.write(f"**数据**：{r['数据']}")
            st.write(f"**难度**：{r['难度']}")
            st.write(f"**匹配理由**：{r['匹配理由']}")

    df_out = pd.DataFrame([{
        "学号": student.get("学号", ""),
        "姓名": student.get("姓名", ""),
        "推荐1": recs[0]["题目"],
        "推荐2": recs[1]["题目"],
        "推荐3": recs[2]["题目"],
        "匹配理由": recs[0]["匹配理由"],
        "学生确认": "",
    }])

    st.subheader("选题表")
    st.dataframe(df_out)

    csv = df_out.to_csv(index=False, encoding="utf-8-sig").encode("utf-8-sig")
    st.download_button("下载选题表（CSV）", csv,
                       f"{student.get('学号', '')}_{student.get('姓名', '')}_选题表.csv",
                       "text/csv")



```
## 第 8 步：安装依赖

在 PyCharm 底部打开 Terminal，运行：

pip install -r requirements.txt

等待安装完成。p insta

如果下载慢，加清华镜像：

pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple


## 第 9 步：运行

在 Terminal 里运行：

streamlit run app.py

浏览器会自动打开 http://localhost:8501。

**注意**：Streamlit 不能用 PyCharm 的绿色三角运行，必须用命令行。

## 第 10 步：部署到 Streamlit Cloud

1. 把四个文件推到 GitHub 仓库：
   - requirements.txt
   - topics.py
   - match.py
   - app.py

2. 登录 https://share.streamlit.io
3. 选仓库，点 Deploy
4. 拿到公开链接，类似：
   https://topic-compass.streamlit.app
"# topic-compass" 
"# topic-compass" 
