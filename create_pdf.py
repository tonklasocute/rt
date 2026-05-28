#!/usr/bin/env python3
"""Generate comprehensive RT exam guide PDF with Thai font support."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, HRFlowable
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
import re
import os

# Register Arial Unicode for Thai support
FONT_PATH = "/Library/Fonts/Arial Unicode.ttf"
pdfmetrics.registerFont(TTFont("ArialUnicode", FONT_PATH))
pdfmetrics.registerFont(TTFont("ArialUnicodeBold", FONT_PATH))

BASE_FONT = "ArialUnicode"
BOLD_FONT = "ArialUnicode"

# Colors
DARK_BLUE = colors.HexColor("#1a3a5c")
MED_BLUE = colors.HexColor("#2563EB")
LIGHT_BLUE = colors.HexColor("#EFF6FF")
ACCENT = colors.HexColor("#059669")
ORANGE = colors.HexColor("#D97706")
RED = colors.HexColor("#DC2626")
GRAY = colors.HexColor("#6B7280")
LIGHT_GRAY = colors.HexColor("#F3F4F6")
DARK_GRAY = colors.HexColor("#374151")

def make_styles():
    styles = {}

    styles["cover_title"] = ParagraphStyle(
        "cover_title", fontName=BASE_FONT, fontSize=26,
        textColor=DARK_BLUE, spaceAfter=12, alignment=TA_CENTER, leading=34
    )
    styles["cover_sub"] = ParagraphStyle(
        "cover_sub", fontName=BASE_FONT, fontSize=16,
        textColor=MED_BLUE, spaceAfter=8, alignment=TA_CENTER, leading=22
    )
    styles["cover_detail"] = ParagraphStyle(
        "cover_detail", fontName=BASE_FONT, fontSize=11,
        textColor=GRAY, spaceAfter=6, alignment=TA_CENTER, leading=16
    )
    styles["h1"] = ParagraphStyle(
        "h1", fontName=BASE_FONT, fontSize=18,
        textColor=colors.white, spaceAfter=10, spaceBefore=16, leading=24,
        backColor=DARK_BLUE, borderPadding=(6, 10, 6, 10)
    )
    styles["h2"] = ParagraphStyle(
        "h2", fontName=BASE_FONT, fontSize=14,
        textColor=DARK_BLUE, spaceAfter=8, spaceBefore=12, leading=20,
        borderPadding=(4, 0, 4, 8), leftIndent=0,
        borderLeftColor=MED_BLUE, borderLeftWidth=4
    )
    styles["h3"] = ParagraphStyle(
        "h3", fontName=BASE_FONT, fontSize=12,
        textColor=MED_BLUE, spaceAfter=6, spaceBefore=8, leading=18
    )
    styles["body"] = ParagraphStyle(
        "body", fontName=BASE_FONT, fontSize=9.5,
        textColor=DARK_GRAY, spaceAfter=4, leading=15, alignment=TA_JUSTIFY
    )
    styles["bullet"] = ParagraphStyle(
        "bullet", fontName=BASE_FONT, fontSize=9.5,
        textColor=DARK_GRAY, spaceAfter=3, leading=15,
        leftIndent=15, firstLineIndent=-10
    )
    styles["sub_bullet"] = ParagraphStyle(
        "sub_bullet", fontName=BASE_FONT, fontSize=9,
        textColor=DARK_GRAY, spaceAfter=2, leading=14,
        leftIndent=28, firstLineIndent=-10
    )
    styles["formula"] = ParagraphStyle(
        "formula", fontName=BASE_FONT, fontSize=10,
        textColor=colors.white, spaceAfter=6, leading=16,
        backColor=MED_BLUE, borderPadding=(6, 10, 6, 10), alignment=TA_CENTER
    )
    styles["highlight"] = ParagraphStyle(
        "highlight", fontName=BASE_FONT, fontSize=9.5,
        textColor=DARK_GRAY, spaceAfter=5, leading=15,
        backColor=LIGHT_BLUE, borderPadding=(5, 8, 5, 8),
        borderColor=MED_BLUE, borderWidth=1
    )
    styles["warning"] = ParagraphStyle(
        "warning", fontName=BASE_FONT, fontSize=9.5,
        textColor=DARK_GRAY, spaceAfter=5, leading=15,
        backColor=colors.HexColor("#FEF3C7"), borderPadding=(5, 8, 5, 8),
        borderColor=ORANGE, borderWidth=1
    )
    styles["exam_q"] = ParagraphStyle(
        "exam_q", fontName=BASE_FONT, fontSize=9.5,
        textColor=DARK_GRAY, spaceAfter=4, leading=15,
        backColor=LIGHT_GRAY, borderPadding=(5, 8, 5, 8)
    )
    styles["answer"] = ParagraphStyle(
        "answer", fontName=BASE_FONT, fontSize=9.5,
        textColor=colors.white, spaceAfter=6, leading=15,
        backColor=ACCENT, borderPadding=(5, 8, 5, 8)
    )
    styles["normal_small"] = ParagraphStyle(
        "normal_small", fontName=BASE_FONT, fontSize=8.5,
        textColor=DARK_GRAY, spaceAfter=3, leading=13
    )
    styles["footer"] = ParagraphStyle(
        "footer", fontName=BASE_FONT, fontSize=8,
        textColor=GRAY, alignment=TA_CENTER, leading=12
    )
    return styles

def make_table(data, col_widths=None, header_bg=DARK_BLUE, header_text=colors.white,
               stripe=True):
    if col_widths is None:
        page_w = A4[0] - 4*cm
        col_widths = [page_w / len(data[0])] * len(data)

    style = [
        ("FONTNAME", (0, 0), (-1, -1), BASE_FONT),
        ("FONTSIZE", (0, 0), (-1, -1), 8.5),
        ("TEXTCOLOR", (0, 0), (-1, -1), DARK_GRAY),
        ("BACKGROUND", (0, 0), (-1, 0), header_bg),
        ("TEXTCOLOR", (0, 0), (-1, 0), header_text),
        ("FONTSIZE", (0, 0), (-1, 0), 9),
        ("ALIGN", (0, 0), (-1, -1), "LEFT"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("ROWBACKGROUND", (0, 0), (-1, -1), [colors.white, LIGHT_GRAY] if stripe else [colors.white]),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#D1D5DB")),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("ROWBACKGROUND", (0, 0), (-1, 0), header_bg),
    ]
    t = Table(data, colWidths=col_widths, repeatRows=1)
    t.setStyle(TableStyle(style))
    return t

def add_page_number(canvas, doc):
    canvas.saveState()
    canvas.setFont(BASE_FONT, 8)
    canvas.setFillColor(GRAY)
    page_num = canvas.getPageNumber()
    canvas.drawCentredString(A4[0]/2, 1.5*cm, f"หน้า {page_num}")
    canvas.drawString(2*cm, 1.5*cm, "คู่มือสอบใบอนุญาตประกอบวิชาชีพรังสีเทคนิค")
    canvas.restoreState()

def build_content(S):
    """Build all content elements."""
    story = []

    # ===== COVER PAGE =====
    story.append(Spacer(1, 3*cm))
    story.append(Paragraph("คู่มือสอบใบอนุญาตประกอบวิชาชีพรังสีเทคนิค", S["cover_title"]))
    story.append(Paragraph("Radiologic Technology Licensing Exam", S["cover_title"]))
    story.append(Spacer(1, 0.5*cm))
    story.append(Paragraph("ฉบับสมบูรณ์ — Comprehensive Board Review", S["cover_sub"]))
    story.append(Spacer(1, 1*cm))
    story.append(HRFlowable(width="80%", thickness=2, color=MED_BLUE, hAlign="CENTER"))
    story.append(Spacer(1, 0.5*cm))
    story.append(Paragraph("ครอบคลุมทุกหัวข้อที่ออกสอบ", S["cover_detail"]))
    story.append(Paragraph("18 Sections | 150+ Mock Questions | Mnemonics & Tables", S["cover_detail"]))
    story.append(Spacer(1, 0.5*cm))
    story.append(Paragraph("Physics | Positioning | CT | MRI | Nuclear Medicine | Contrast Media", S["cover_detail"]))
    story.append(Paragraph("Mammography | Fluoroscopy | Radiation Therapy | QC | Law & Ethics", S["cover_detail"]))
    story.append(Spacer(1, 2*cm))
    story.append(Paragraph("Intensive Crash Course Edition", S["cover_sub"]))
    story.append(PageBreak())

    # ===== TABLE OF CONTENTS =====
    story.append(Paragraph("📋 สารบัญ (Table of Contents)", S["h1"]))
    story.append(Spacer(1, 0.3*cm))
    toc_data = [
        ["Section", "หัวข้อ"],
        ["Section 1", "Overview วิชาชีพรังสีเทคนิค"],
        ["Section 2", "Radiologic Physics (ฟิสิกส์รังสี)"],
        ["Section 3", "Image Quality (คุณภาพภาพ)"],
        ["Section 4", "Digital Radiography (CR/DR/PACS)"],
        ["Section 5", "Radiographic Positioning (การจัดท่าถ่ายภาพ)"],
        ["Section 6", "Cross-Sectional Anatomy"],
        ["Section 7", "CT Scan"],
        ["Section 8", "MRI"],
        ["Section 9", "Mammography"],
        ["Section 10", "Fluoroscopy & Interventional"],
        ["Section 11", "Nuclear Medicine"],
        ["Section 12", "Radiation Therapy"],
        ["Section 13", "Contrast Media"],
        ["Section 14", "Quality Control (QC/QA)"],
        ["Section 15", "Law, Ethics & Professional"],
        ["Section 16", "High-Yield Exam Summary"],
        ["Section 17", "Mock Exam 150 ข้อ + เฉลยละเอียด"],
        ["Section 18", "Crash Course Before Exam"],
    ]
    story.append(make_table(toc_data, col_widths=[4*cm, 13*cm]))
    story.append(PageBreak())

    # Read and process markdown files
    parts = [
        "/Users/cms-rd-1/Documents/GitHub/rt/rt_exam_guide_part1.md",
        "/Users/cms-rd-1/Documents/GitHub/rt/rt_exam_guide_part2.md",
        "/Users/cms-rd-1/Documents/GitHub/rt/rt_exam_guide_part3.md",
        "/Users/cms-rd-1/Documents/GitHub/rt/rt_exam_guide_part4.md",
    ]

    for part_path in parts:
        with open(part_path, "r", encoding="utf-8") as f:
            content = f.read()
        process_markdown(content, story, S)

    return story


def process_markdown(content, story, S):
    """Process markdown content into PDF elements."""
    lines = content.split("\n")
    i = 0
    table_lines = []
    in_table = False
    in_code = False
    code_lines = []

    while i < len(lines):
        line = lines[i]

        # Code block
        if line.startswith("```"):
            if not in_code:
                in_code = True
                code_lines = []
            else:
                in_code = False
                if code_lines:
                    code_text = "\n".join(code_lines)
                    # Render as styled paragraph
                    for cl in code_lines:
                        if cl.strip():
                            story.append(Paragraph(
                                escape_html(cl),
                                ParagraphStyle("code", fontName=BASE_FONT, fontSize=8.5,
                                               textColor=colors.white, backColor=DARK_GRAY,
                                               leading=14, leftIndent=10, spaceAfter=1,
                                               borderPadding=(2, 8, 2, 8))
                            ))
                    story.append(Spacer(1, 0.2*cm))
                code_lines = []
            i += 1
            continue

        if in_code:
            code_lines.append(line)
            i += 1
            continue

        # Table detection
        if "|" in line and line.strip().startswith("|"):
            if not in_table:
                in_table = True
                table_lines = []
            table_lines.append(line)
            i += 1
            continue
        elif in_table:
            in_table = False
            render_md_table(table_lines, story, S)
            table_lines = []
            continue

        # Headings
        if line.startswith("# "):
            text = line[2:].strip()
            if "SECTION" in text or text.startswith("คู่มือ"):
                story.append(PageBreak())
            story.append(Spacer(1, 0.3*cm))
            story.append(Paragraph(escape_html(text), S["h1"]))
            story.append(Spacer(1, 0.2*cm))
        elif line.startswith("## "):
            text = line[3:].strip()
            story.append(Spacer(1, 0.2*cm))
            # Add colored left border effect via background
            p = Paragraph(f"<font color='#{MED_BLUE.hexval()[2:]}'>■</font>  {escape_html(text)}", S["h2"])
            story.append(p)
        elif line.startswith("### "):
            text = line[4:].strip()
            story.append(Paragraph(escape_html(text), S["h3"]))
        elif line.startswith("#### "):
            text = line[5:].strip()
            story.append(Paragraph(f"<b>{escape_html(text)}</b>", S["body"]))

        # Horizontal rule
        elif line.strip().startswith("---"):
            story.append(HRFlowable(width="100%", thickness=1, color=GRAY, spaceAfter=5, spaceBefore=5))

        # Bullet points
        elif line.strip().startswith("- "):
            text = line.strip()[2:]
            # Check for bold
            text = process_inline(text)
            if line.startswith("  - ") or line.startswith("    - "):
                story.append(Paragraph(f"  ◦  {text}", S["sub_bullet"]))
            else:
                story.append(Paragraph(f"• {text}", S["bullet"]))

        # Numbered lists
        elif re.match(r"^\d+\.", line.strip()):
            text = re.sub(r"^\d+\.\s*", "", line.strip())
            text = process_inline(text)
            story.append(Paragraph(f"  {text}", S["bullet"]))

        # Special markers
        elif line.strip().startswith("⭐") or line.strip().startswith("⚠️"):
            text = process_inline(line.strip())
            story.append(Paragraph(text, S["highlight"]))

        # Formulas (lines with $$)
        elif "$$" in line:
            formula = line.replace("$$", "").strip()
            if formula:
                story.append(Paragraph(formula, S["formula"]))

        # Exam questions (lines with **ข้อ)
        elif line.strip().startswith("**ข้อ") and ":**" in line:
            text = process_inline(line.strip())
            story.append(Spacer(1, 0.15*cm))
            story.append(Paragraph(text, S["exam_q"]))

        # Answer lines
        elif line.strip().startswith("**เฉลย:"):
            text = process_inline(line.strip())
            story.append(Paragraph(text, S["answer"]))
            story.append(Spacer(1, 0.1*cm))

        # Answer choices (- A., - B., etc.)
        elif re.match(r"^- [A-D]\.", line.strip()):
            text = process_inline(line.strip()[2:])
            story.append(Paragraph(f"    {text}", S["normal_small"]))

        # Empty line
        elif line.strip() == "":
            story.append(Spacer(1, 0.1*cm))

        # Regular text
        elif line.strip():
            text = process_inline(line.strip())
            story.append(Paragraph(text, S["body"]))

        i += 1

    # Flush any remaining table
    if table_lines:
        render_md_table(table_lines, story, S)


def escape_html(text):
    """Escape HTML special characters."""
    text = text.replace("&", "&amp;")
    text = text.replace("<", "&lt;")
    text = text.replace(">", "&gt;")
    return text


def process_inline(text):
    """Process inline markdown: bold, italic, etc."""
    # Escape HTML first (but preserve existing)
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    # Bold: **text**
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    # Italic: *text*
    text = re.sub(r"\*([^*]+?)\*", r"<i>\1</i>", text)
    # Code: `text`
    text = re.sub(r"`(.+?)`", r"<font face='Courier' size='8'>\1</font>", text)
    return text


def render_md_table(table_lines, story, S):
    """Render markdown table to PDF table."""
    rows = []
    for line in table_lines:
        if re.match(r"^\|[-\s|:]+\|$", line.strip()):
            continue  # Skip separator lines
        cells = [c.strip() for c in line.split("|") if c.strip() != ""]
        if cells:
            rows.append(cells)

    if not rows:
        return

    # Normalize column count
    max_cols = max(len(r) for r in rows)
    normalized = []
    for r in rows:
        while len(r) < max_cols:
            r.append("")
        normalized.append(r[:max_cols])

    # Convert to Paragraph objects
    page_w = A4[0] - 4*cm
    col_w = page_w / max_cols
    col_widths = [col_w] * max_cols

    pdf_rows = []
    for ri, row in enumerate(normalized):
        pdf_row = []
        for ci, cell in enumerate(row):
            cell_text = process_inline(cell)
            if ri == 0:
                p = Paragraph(f"<b>{cell_text}</b>",
                               ParagraphStyle("th", fontName=BASE_FONT, fontSize=8.5,
                                              textColor=colors.white, leading=13))
            else:
                p = Paragraph(cell_text,
                               ParagraphStyle("td", fontName=BASE_FONT, fontSize=8.5,
                                              textColor=DARK_GRAY, leading=13))
            pdf_row.append(p)
        pdf_rows.append(pdf_row)

    if len(pdf_rows) < 1:
        return

    style = [
        ("BACKGROUND", (0, 0), (-1, 0), DARK_BLUE),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, -1), BASE_FONT),
        ("FONTSIZE", (0, 0), (-1, -1), 8.5),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#D1D5DB")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
    ]
    # Alternating rows
    for ri in range(1, len(pdf_rows), 2):
        style.append(("BACKGROUND", (0, ri), (-1, ri), LIGHT_GRAY))

    t = Table(pdf_rows, colWidths=col_widths, repeatRows=1)
    t.setStyle(TableStyle(style))
    story.append(t)
    story.append(Spacer(1, 0.3*cm))


def main():
    output_path = "/Users/cms-rd-1/Documents/GitHub/rt/RT_Exam_Guide_Complete.pdf"

    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        leftMargin=2*cm,
        rightMargin=2*cm,
        topMargin=2.5*cm,
        bottomMargin=2.5*cm,
        title="คู่มือสอบใบอนุญาตประกอบวิชาชีพรังสีเทคนิค",
        author="RT Board Review",
        subject="Radiologic Technology Licensing Exam Comprehensive Review",
    )

    S = make_styles()
    print("Building content...")
    story = build_content(S)

    print(f"Building PDF with {len(story)} elements...")
    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)

    size_mb = os.path.getsize(output_path) / (1024 * 1024)
    print(f"\n✅ PDF created: {output_path}")
    print(f"   File size: {size_mb:.1f} MB")


if __name__ == "__main__":
    main()
