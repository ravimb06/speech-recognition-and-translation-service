from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Paragraph, SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet

def save_to_pdf(text, filename):
    pdfmetrics.registerFont(TTFont('Arial', 'arial.ttf', 'UTF-8'))
    style = getSampleStyleSheet()["Normal"]
    style.fontName = "Arial" 
    doc = SimpleDocTemplate(filename, pagesize=letter)
    story = [Paragraph(text, style)]
    doc.build(story)