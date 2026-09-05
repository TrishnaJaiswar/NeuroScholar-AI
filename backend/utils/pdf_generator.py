from io import BytesIO
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
)

styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    "CustomTitle",
    parent=styles["Title"],
    fontSize=20,
    leading=24,
    alignment=TA_CENTER,
    spaceAfter=20,
)

heading_style = ParagraphStyle(
    "CustomHeading",
    parent=styles["Heading2"],
    fontSize=14,
    leading=18,
    spaceBefore=12,
    spaceAfter=8,
    textColor=colors.HexColor("#1D4ED8"),
)

body_style = ParagraphStyle(
    "CustomBody",
    parent=styles["BodyText"],
    fontSize=10,
    leading=15,
    spaceAfter=8,
)


def safe_text(value):
    if value is None:
        return ""
    return escape(str(value)).replace("\n", "<br/>")


def create_pdf(report):
    buffer = BytesIO()

    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=0.7 * inch,
        leftMargin=0.7 * inch,
        topMargin=0.7 * inch,
        bottomMargin=0.7 * inch,
        title=report.title,
        author="NeuroScholar AI",
    )

    story = []

    # Title
    story.append(
        Paragraph(
            safe_text(report.title),
            title_style,
        )
    )

    story.append(Spacer(1, 10))

    # Abstract
    story.append(
        Paragraph("Abstract", heading_style)
    )

    story.append(
        Paragraph(
            safe_text(report.abstract),
            body_style,
        )
    )

    # Introduction
    story.append(
        Paragraph("Introduction", heading_style)
    )

    story.append(
        Paragraph(
            safe_text(report.introduction),
            body_style,
        )
    )

    # Key Findings
    story.append(
        Paragraph("Key Findings", heading_style)
    )

    for finding in report.key_findings:
        story.append(
            Paragraph(
                f"• {safe_text(finding)}",
                body_style,
            )
        )

    # Comparative Analysis
    story.append(
        Paragraph(
            "Comparative Analysis",
            heading_style,
        )
    )

    story.append(
        Paragraph(
            safe_text(report.comparative_analysis),
            body_style,
        )
    )

    # Limitations
    story.append(
        Paragraph("Limitations", heading_style)
    )

    story.append(
        Paragraph(
            safe_text(report.limitations),
            body_style,
        )
    )

    # Conclusion
    story.append(
        Paragraph("Conclusion", heading_style)
    )

    story.append(
        Paragraph(
            safe_text(report.conclusion),
            body_style,
        )
    )

    # References
    story.append(
        Paragraph("References", heading_style)
    )

    for reference in report.references:
        story.append(
            Paragraph(
                f"• {safe_text(reference)}",
                body_style,
            )
        )

    doc.build(story)

    buffer.seek(0)

    return buffer.getvalue()