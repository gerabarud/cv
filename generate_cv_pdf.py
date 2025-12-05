#!/usr/bin/env python3
"""
CV Generator: Converts Markdown CV to professionally styled PDF documents
Generates both Spanish and English versions from single Markdown source
Usage: python3 generate_cv_pdf.py [ES|EN|BOTH]
"""

import sys
import os
import re

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm, inch
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.colors import HexColor

# Color scheme
PRIMARY_COLOR = HexColor("#1a5490")      # Dark blue
SECONDARY_COLOR = HexColor("#2c5282")    # Medium blue
TEXT_COLOR = HexColor("#333333")         # Dark gray

def translate_section_titles(content, language="EN"):
    """Translate main section titles"""
    if language == "ES":
        return content
    
    translations = {
        "PERFIL PROFESIONAL": "PROFESSIONAL PROFILE",
        "EXPERIENCIA PROFESIONAL": "PROFESSIONAL EXPERIENCE",
        "FORMACIÓN Y CURSOS": "TRAINING & COURSES",
        "CHARLAS Y DISERTACIONES": "TALKS & LECTURES",
        "HABILIDADES TÉCNICAS": "TECHNICAL SKILLS",
        "IDIOMAS": "LANGUAGES",
        "OTRAS ACTIVIDADES": "OTHER ACTIVITIES",
        "Agosto": "August",
        "Presente": "Present",
    }
    
    result = content
    for es, en in translations.items():
        result = result.replace(es, en)
    return result

def parse_markdown(md_content):
    """Parse markdown and extract elements"""
    elements = []
    lines = md_content.strip().split('\n')
    
    for line in lines:
        line = line.strip()
        
        if not line:
            continue
        
        # Main title (# Text)
        if line.startswith('# ') and not line.startswith('## '):
            title = line.replace('# ', '').strip()
            elements.append(('title', title))
        
        # Section (## Text)
        elif line.startswith('## '):
            section = line.replace('## ', '').strip()
            elements.append(('section', section))
        
        # Subsection (### Text)
        elif line.startswith('### '):
            subsection = line.replace('### ', '').strip()
            elements.append(('subsection', subsection))
        
        # Bullet
        elif line.startswith('- '):
            bullet = line.replace('- ', '').strip()
            elements.append(('bullet', bullet))
        
        # Separator
        elif line.startswith('---'):
            elements.append(('spacer', ''))
        
        # Normal text
        elif not line.startswith('---'):
            elements.append(('text', line))
    
    return elements

def create_pdf(md_file, language="ES"):
    """Create PDF from Markdown"""
    
    # Read markdown
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Translate if needed
    if language == "EN":
        content = translate_section_titles(content, language)
    
    # Parse
    elements = parse_markdown(content)
    
    # Create PDF
    pdf_file = f"/home/gbarud/cv/pdfs/CV_Gerardo_Barud_{language}.pdf"
    doc = SimpleDocTemplate(
        pdf_file,
        pagesize=A4,
        rightMargin=1.5*cm,
        leftMargin=1.5*cm,
        topMargin=1.5*cm,
        bottomMargin=1.5*cm,
        title=f"CV Gerardo Barud - {language}"
    )
    
    # Styles
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Normal'],
        fontSize=24,
        textColor=PRIMARY_COLOR,
        spaceAfter=3,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    subtitle_style = ParagraphStyle(
        'Subtitle',
        parent=styles['Normal'],
        fontSize=11,
        textColor=SECONDARY_COLOR,
        spaceAfter=3,
        alignment=TA_CENTER,
        fontName='Helvetica'
    )
    
    contact_style = ParagraphStyle(
        'Contact',
        parent=styles['Normal'],
        fontSize=9,
        textColor=TEXT_COLOR,
        spaceAfter=12,
        alignment=TA_CENTER,
        fontName='Helvetica'
    )
    
    section_style = ParagraphStyle(
        'SectionHeader',
        parent=styles['Normal'],
        fontSize=12,
        textColor=PRIMARY_COLOR,
        spaceAfter=8,
        spaceBefore=10,
        fontName='Helvetica-Bold'
    )
    
    subsection_style = ParagraphStyle(
        'Subsection',
        parent=styles['Normal'],
        fontSize=11,
        textColor=SECONDARY_COLOR,
        spaceAfter=2,
        fontName='Helvetica-Bold'
    )
    
    bullet_style = ParagraphStyle(
        'Bullet',
        parent=styles['Normal'],
        fontSize=10,
        textColor=TEXT_COLOR,
        spaceAfter=4,
        leftIndent=20,
        fontName='Helvetica'
    )
    
    normal_style = ParagraphStyle(
        'Normal',
        parent=styles['Normal'],
        fontSize=10,
        textColor=TEXT_COLOR,
        spaceAfter=6,
        alignment=TA_JUSTIFY,
        fontName='Helvetica'
    )
    
    # Build content
    content_elements = []
    
    for elem_type, elem_text in elements:
        if elem_type == 'title':
            content_elements.append(Paragraph(elem_text, title_style))
        
        elif elem_type == 'text':
            # Check if it's contact info
            if any(x in elem_text for x in ['📍', '📧', '🔗', '@']):
                clean = elem_text.replace('📍', '').replace('📧', '').replace('🔗', '').strip()
                content_elements.append(Paragraph(clean, contact_style))
            else:
                content_elements.append(Paragraph(elem_text, subtitle_style))
        
        elif elem_type == 'section':
            content_elements.append(Spacer(1, 6))
            content_elements.append(Paragraph(elem_text, section_style))
        
        elif elem_type == 'subsection':
            content_elements.append(Paragraph(elem_text, subsection_style))
        
        elif elem_type == 'bullet':
            content_elements.append(Paragraph(f"• {elem_text}", bullet_style))
        
        elif elem_type == 'spacer':
            content_elements.append(Spacer(1, 2))
    
    # Generate PDF
    try:
        doc.build(content_elements)
        print(f"✅ PDF creado: {pdf_file}")
    except Exception as e:
        print(f"❌ Error generando PDF: {e}")

def main():
    if len(sys.argv) < 2:
        print("Uso: python3 generate_cv_pdf.py [ES|EN|BOTH]")
        sys.exit(1)
    
    option = sys.argv[1].upper()
    md_file = "/home/gbarud/cv/CV_Gerardo_Barud_ES.md"
    
    if not os.path.exists(md_file):
        print(f"Error: {md_file} no encontrado")
        sys.exit(1)
    
    if option == "ES":
        create_pdf(md_file, "ES")
    elif option == "EN":
        create_pdf(md_file, "EN")
    elif option == "BOTH":
        create_pdf(md_file, "ES")
        create_pdf(md_file, "EN")
    else:
        print("Opción inválida. Usa: ES, EN o BOTH")
        sys.exit(1)

if __name__ == "__main__":
    main()
