from io import BytesIO

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate

styles = getSampleStyleSheet()


def create_pdf(report):
    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)
    story = []

    story.append(
        Paragraph(f"<b>{report.title}</b>", styles["Title"])
    )

    story.append(Paragraph("Abstract", styles["Heading2"]))
    story.append(Paragraph(report.abstract, styles["BodyText"]))

    story.append(Paragraph("Introduction", styles["Heading2"]))
    story.append(Paragraph(report.introduction, styles["BodyText"]))

    story.append(Paragraph("Key Findings", styles["Heading2"]))
    for item in report.key_findings:
        story.append(
            Paragraph(f"• {item}", styles["BodyText"])
        )

    story.append(
        Paragraph("Comparative Analysis", styles["Heading2"])
    )
    story.append(
        Paragraph(report.comparative_analysis, styles["BodyText"])
    )

    story.append(Paragraph("Limitations", styles["Heading2"]))
    story.append(
        Paragraph(report.limitations, styles["BodyText"])
    )

    story.append(Paragraph("Conclusion", styles["Heading2"]))
    story.append(
        Paragraph(report.conclusion, styles["BodyText"])
    )

    story.append(Paragraph("References", styles["Heading2"]))
    for ref in report.references:
        story.append(Paragraph(ref, styles["BodyText"]))

    doc.build(story)

    buffer.seek(0)
    return buffer