
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
