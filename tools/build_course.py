# -*- coding: utf-8 -*-
"""课程生成器：从 lessons_data.py 生成 16 份教案（md）+ 16 套 PPT（pptx）+ 6 任务书（md）。"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lessons_data import LESSONS, LFS  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BLOOM_DESC = {
    "记忆": "Remember：能够回忆与陈述",
    "理解": "Understand：能够解释与举例",
    "应用": "Apply：能够在真实环境执行",
    "分析": "Analyze：能够拆解与归因",
    "评价": "Evaluate：能够依据标准评判",
    "创造": "Create：能够设计新方案",
}

STEP_EN = {"资讯": "Informieren", "计划": "Planen", "决策": "Entscheiden",
           "实施": "Durchführen", "检查": "Kontrollieren", "评价": "Bewerten"}


def lesson_jiaaoan_md(les: dict) -> str:
    lf = LFS[les["lf"]]
    lines = []
    lines.append(f"# 第 {les['no']} 次课教案：{les['title']}")
    lines.append("")
    lines.append("| 项 | 内容 |")
    lines.append("|---|---|")
    lines.append(f"| 周次 | 第 {les['week']} 周 |")
    lines.append(f"| 学习领域 | {les['lf']} {lf['name']}（{lf['weeks']} 周） |")
    lines.append(f"| 学时 | {les['hours']} 学时（180 分钟） |")
    lines.append(f"| 场所 | {'【校】学校教室/机房' if les['place']=='校' else '【企】合作企业机房（真实集群）' if les['place']=='企' else '【校】+【企】'} |")
    lines.append(f"| 教学方法 | 双元制六步法 + 费曼时刻 + 布鲁姆分层 |")
    lines.append("")
    lines.append("## 一、教学目标（布鲁姆分层）")
    lines.append("")
    for level, obj in les["objectives"]:
        lines.append(f"- **[{level}]** {obj} —— {BLOOM_DESC[level]}")
    lines.append("")
    lines.append("## 二、重点与难点")
    lines.append("")
    lines.append(f"- **重点**：{'；'.join(les['keypoints'])}")
    lines.append(f"- **难点**：{les['difficulties'][0]}")
    lines.append("")
    lines.append("## 三、教学过程设计（双元制六步法，180 分钟）")
    lines.append("")
    lines.append("| 步骤 | 德语 | 时长 | 活动设计 |")
    lines.append("|---|---|---|---|")
    for step, mins, act in les["six_steps"]:
        lines.append(f"| {step} | {STEP_EN[step]} | {mins}min | {act} |")
    lines.append("")
    lines.append("## 四、费曼学习法环节")
    lines.append("")
    lines.append(f"- **费曼题目**：{les['feynman']}")
    lines.append("- **规则**：抽签 3 人 × 3 分钟；禁用未解释术语（听众举红牌即重讲）；当场补漏成功得满分")
    lines.append("- **评分**：清晰度 2 分 + 类比质量 2 分 + 应对追问 1 分（计入过程考核素质分）")
    lines.append("")
    lines.append("## 五、布鲁姆达成检验（随堂快测）")
    lines.append("")
    for q, a in les["quiz"]:
        lines.append(f"- **Q：{q}**")
        lines.append(f"  - A：{a}")
    lines.append("")
    lines.append("## 六、课后任务与企业衔接")
    lines.append("")
    lines.append(f"- **课后作业**：{les['homework']}")
    lines.append(f"- **企业衔接**：{les['enterprise']}")
    lines.append("")
    lines.append("## 七、教学资源")
    lines.append("")
    lines.append(f"- 课件：[ppt/L{les['no']:02d}.pptx](../ppt/L{les['no']:02d}.pptx)")
    lines.append("- 实训入口：http://10.167.2.175:30181（GraphiQL: /graphql/）")
    lines.append("- 主项目仓库：enterprise-travel-agent（真实现状以 09-项目同步资料 为准）")
    lines.append("")
    lines.append("## 八、教学反思（课后填写）")
    lines.append("")
    lines.append("- 目标达成情况：")
    lines.append("- 六步法时间分配是否需要调整：")
    lines.append("- 费曼时刻亮点/卡壳点：")
    lines.append("- 下一课需要补救的内容：")
    return "\n".join(lines)


def auftrag_md(lf_key: str) -> str:
    lf = LFS[lf_key]
    lessons = [l for l in LESSONS if l["lf"] == lf_key]
    no_range = f"L{lessons[0]['no']:02d}-L{lessons[-1]['no']:02d}"
    tasks = {
        "LF1": [("环境就绪检查表", "个人", "三探针 200 + GraphiQL 首查成功 + metrics 打开"),
                 ("系统架构手绘图", "小组", "6 服务 + 流量数字标注，数字须有出处")],
        "LF2": [("接口用例表", "个人", "≥8 用例含 422 校验与边界值"),
                 ("GraphiQL 测试截图+说明", "小组", "变量化查询/守卫拒绝/双面一致三项"),
                 ("契约一致性核对表", "小组", "三份 proto 逐字段对照 + 改进建议 ≥3 条")],
        "LF3": [("TripPlan 聚合关系图", "小组", "聚合根/实体/端口/事件标注齐全"),
                 ("路由验证报告", "个人", "写落主库/读落副本/副本无写三断言"),
                 ("缓存实验记录", "小组", "命中实验+失效广播+指标对账")],
        "LF4": [("漏洞复现报告", "小组", "固定窗口 2× 突破复现 + 令牌桶修复验证"),
                 ("tokens 时间曲线", "个人", "Python 绘制并标注参数"),
                 ("队列实验记录", "小组", "四态流转 + 失败路径 + KEDA 草案")],
        "LF5": [("新增测试用例（PR 格式）", "个人", "先红后绿截图 + 全量回归绿"),
                 ("feature 文件", "小组", "≥2 个中文业务场景跑通"),
                 ("小组压测报告", "小组", "数据+瓶颈分析+建议，与基线 ±15%")],
        "LF6": [("部署观察记录+HPA 决策链图", "个人", "扩容时间线完整"),
                 ("小组扩容清单", "小组", "四层齐+假设标注+与官方对照 <20%"),
                 ("答辩 PPT+答辩录像", "小组", "15 分钟结构化答辩")],
    }
    lines = []
    lines.append(f"# 学生任务书（Arbeitsauftrag）：{lf['name']}")
    lines.append("")
    lines.append(f"- **学习领域**：{lf_key}（{lf['weeks']} 周，课次 {no_range}）")
    lines.append("- **双元场所**：学校教室/机房 + 合作企业机房（真实集群）")
    lines.append("- **完成要求**：全部成果物上传课程仓库 Issue（附截图/文件），企业课次成果物需企业师傅签字")
    lines.append("")
    lines.append("## 任务清单")
    lines.append("")
    lines.append("| # | 成果物 | 形式 | 合格标准 | 责任 |")
    lines.append("|---|---|---|---|---|")
    for i, (name, who, std) in enumerate(tasks[lf_key], 1):
        lines.append(f"| {i} | {name} | {who} | {std} | {who} |")
    lines.append("")
    lines.append("## 六步法执行要求")
    lines.append("")
    lines.append("1. **资讯**：课前阅读对应教案与局域网指南，带 1 个问题来上课")
    lines.append("2. **计划**：组长组织分工，记录员填写《计划表》（谁/做什么/多久）")
    lines.append("3. **决策**：方案需回答教师两个质询（为什么这样做/失败了怎么办）")
    lines.append("4. **实施**：企业课次遵守生产纪律——最小权限、禁破坏性命令、压测先报备")
    lines.append("5. **检查**：用检查单互查，不允许自检通过即提交")
    lines.append("6. **评价**：费曼时刻人人准备，抽到即讲")
    lines.append("")
    lines.append("## 职业素养要求（企业师傅观察点）")
    lines.append("")
    lines.append("- 守时与出勤；操作留痕（命令+截图）；不确定先问不乱试；团队补位意识")
    lines.append("")
    lines.append("## 评分关联")
    lines.append("")
    lines.append("- 本任务书成果物 = 过程考核 40% 的直接依据（见 07-考核评价/过程考核表）")
    lines.append("- 企业课次表现 = 企业实践考核 30%（见 07-考核评价/企业师傅评价表）")
    return "\n".join(lines)


def gen_pptx(les: dict) -> str:
    from pptx import Presentation
    from pptx.util import Inches, Pt, Emu
    from pptx.dml.color import RGBColor
    from pptx.enum.text import PP_ALIGN

    # 主题：海洋蓝绿（文旅+科技）
    PRIMARY = RGBColor(0x06, 0x5A, 0x82)   # deep blue
    TEAL = RGBColor(0x1C, 0x72, 0x93)
    MIDNIGHT = RGBColor(0x21, 0x2A, 0x5C)
    CREAM = RGBColor(0xF5, 0xF7, 0xFA)
    WHITE = RGBColor(0xFF, 0xFF, 0xFF)
    ACCENT = RGBColor(0xF9, 0x61, 0x67)    # coral accent
    DARK = RGBColor(0x21, 0x2A, 0x33)

    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    SW, SH = prs.slide_width, prs.slide_height

    def add_bg(slide, color):
        fill = slide.background.fill
        fill.solid()
        fill.fore_color.rgb = color

    def add_rect(slide, x, y, w, h, color):
        from pptx.enum.shapes import MSO_SHAPE
        shp = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, w, h)
        shp.fill.solid()
        shp.fill.fore_color.rgb = color
        shp.line.fill.background()
        shp.shadow.inherit = False
        return shp

    def add_text(slide, x, y, w, h, text, size=18, bold=False, color=DARK, align=PP_ALIGN.LEFT, font="微软雅黑"):
        tb = slide.shapes.add_textbox(x, y, w, h)
        tf = tb.text_frame
        tf.word_wrap = True
        first = True
        for line in text.split("\n"):
            p = tf.paragraphs[0] if first else tf.add_paragraph()
            first = False
            p.alignment = align
            run = p.add_run()
            run.text = line
            run.font.size = Pt(size)
            run.font.bold = bold
            run.font.color.rgb = color
            run.font.name = font
            from pptx.oxml.ns import qn
            run.font._rPr.set(qn("a:ea"), "")  # noop guard
            rPr = run._r.get_or_add_rPr()
            ea = rPr.makeelement(qn("a:ea"), {"typeface": font})
            rPr.append(ea)
        return tb

    def title_slide(les):
        s = prs.slides.add_slide(prs.slide_layouts[6])
        add_bg(s, MIDNIGHT)
        add_rect(s, 0, Inches(6.6), SW, Inches(0.9), TEAL)
        add_text(s, Inches(0.9), Inches(1.6), Inches(11.5), Inches(1.2),
                 f"L{les['no']:02d} · {les['title']}", 40, True, WHITE)
        add_text(s, Inches(0.9), Inches(3.0), Inches(11.5), Inches(0.7),
                 f"企业级旅游智能体项目实战 · 第 {les['week']} 周 · {les['lf']} {LFS[les['lf']]['name']}",
                 20, False, RGBColor(0xBE, 0xD8, 0xE8))
        add_text(s, Inches(0.9), Inches(3.8), Inches(11.5), Inches(0.6),
                 "双元制六步法 · 费曼学习法 · 布鲁姆认知分层", 16, False, RGBColor(0x8F, 0xB6, 0xCE))
        add_text(s, Inches(0.9), Inches(6.75), Inches(11.5), Inches(0.6),
                 f"场所：{'学校' if les['place']=='校' else '企业集群' if les['place']=='企' else '学校+企业'}　|　{les['hours']} 学时　|　enterprise-travel-agent 真实项目",
                 14, False, WHITE)
        return s

    def content_slide(title, bullets, note=None, number=None):
        s = prs.slides.add_slide(prs.slide_layouts[6])
        add_bg(s, CREAM)
        add_rect(s, 0, 0, SW, Inches(1.15), PRIMARY)
        add_text(s, Inches(0.55), Inches(0.18), Inches(11.6), Inches(0.8), title, 28, True, WHITE)
        body = "\n".join("• " + b if not b.startswith(("→", "□", "—")) else b for b in bullets)
        add_text(s, Inches(0.7), Inches(1.55), Inches(12.0), Inches(4.9), body, 18, False, DARK)
        if note:
            add_rect(s, Inches(0.7), Inches(6.35), Inches(12.0), Inches(0.75), TEAL)
            add_text(s, Inches(0.95), Inches(6.47), Inches(11.5), Inches(0.55), "★ " + note, 15, True, WHITE)
        if number is not None:
            add_text(s, Inches(12.4), Inches(6.9), Inches(0.8), Inches(0.4), f"{number+1:02d}", 12, False, RGBColor(0x8A, 0x9B, 0xA8))
        return s

    # 封面
    title_slide(les)
    # 内容页
    for idx, (t, bullets) in enumerate(les["slides"]):
        note = None
        if idx == 0 and les["objectives"]:
            note = "本课布鲁姆目标：" + "；".join(f"[{lv}]{obj[:18]}…" for lv, obj in les["objectives"][:2])
        content_slide(t, bullets, note=note, number=idx)
    # 六步法页
    s = prs.slides.add_slide(prs.slide_layouts[6])
    add_bg(s, CREAM)
    add_rect(s, 0, 0, SW, Inches(1.15), PRIMARY)
    add_text(s, Inches(0.55), Inches(0.18), Inches(11.6), Inches(0.8), "六步法教学过程（180 分钟）", 28, True, WHITE)
    rows = ["步骤" + "　|　时长　|　活动"]
    for step, mins, act in les["six_steps"]:
        rows.append(f"{step}（{STEP_EN[step]}）　|　{mins}min　|　{act}")
    add_text(s, Inches(0.7), Inches(1.5), Inches(12.0), Inches(5.2), "\n".join(rows), 15, False, DARK)
    add_text(s, Inches(12.4), Inches(6.9), Inches(0.8), Inches(0.4), f"{len(les['slides'])+2:02d}", 12, False, RGBColor(0x8A, 0x9B, 0xA8))
    # 费曼 + 快测 + 收尾
    content_slide("费曼时刻 + 随堂快测", [
        f"费曼题目：{les['feynman']}",
        "规则：3 人 × 3 分钟；禁用未解释术语；卡壳当场补漏重讲",
        "评分：清晰度2 + 类比质量2 + 应对追问1（过程考核素质分）",
        "— 随堂快测 —",
    ] + [f"Q：{q}" for q, a in les["quiz"]],
        note="答案在教案：04-教案/（教师用）", number=len(les["slides"]))
    content_slide("课后任务与预告", [
        f"课后作业：{les['homework']}",
        f"企业衔接：{les['enterprise']}",
        "成果物提交：课程仓库 Issue（截图/文件）",
        "下节课：见授课计划 02-授课计划.md",
    ], note="证据文化：所有结论必须有实测数据支撑", number=len(les["slides"]) + 1)

    out = os.path.join(ROOT, "ppt", f"L{les['no']:02d}.pptx")
    prs.save(out)
    return out


def main():
    os.makedirs(os.path.join(ROOT, "04-教案"), exist_ok=True)
    os.makedirs(os.path.join(ROOT, "ppt"), exist_ok=True)
    os.makedirs(os.path.join(ROOT, "05-学生任务书"), exist_ok=True)

    for les in LESSONS:
        jx = lesson_jiaaoan_md(les)
        path = os.path.join(ROOT, "04-教案", f"L{les['no']:02d}-教案.md")
        with open(path, "w", encoding="utf-8") as f:
            f.write(jx)
        print("教案:", path)
        ppt = gen_pptx(les)
        print("PPT :", ppt)

    for lf_key in LFS:
        path = os.path.join(ROOT, "05-学生任务书", f"任务书-{lf_key}.md")
        with open(path, "w", encoding="utf-8") as f:
            f.write(auftrag_md(lf_key))
        print("任务书:", path)


if __name__ == "__main__":
    main()
