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
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.colors import HexColor

# Color scheme
PRIMARY_COLOR = HexColor("#1a5490")      # Dark blue
SECONDARY_COLOR = HexColor("#2c5282")    # Medium blue
TEXT_COLOR = HexColor("#333333")         # Dark gray


def format_inline(text: str) -> str:
    """Lightweight markdown inline formatting for bold/italic/links."""
    # Links [text](url)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)
    # Bold **text**
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    # Italic *text*
    text = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<i>\1</i>", text)
    return text

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


def translate_content(content: str) -> str:
    """Lightweight phrase-level translation ES -> EN for the CV body."""
    replacements = [
        ("Profesional con más de **12 años de experiencia**", "Professional with **12+ years of experience**"),
        ("administración de sistemas", "systems administration"),
        ("infraestructura", "infrastructure"),
        ("virtualización", "virtualization"),
        ("automatización", "automation"),
        ("observabilidad", "observability"),
        ("Especialista en **Kubernetes**", "**Kubernetes** specialist"),
        ("clústeres", "clusters"),
        ("on-premise", "on-prem"),
        ("operación de servicios críticos", "operation of critical services"),
        ("confiabilidad", "reliability"),
        ("seguridad", "security"),
        ("estandarización", "standardization"),
        ("disaster recovery", "disaster recovery"),
        ("buenas prácticas", "best practices"),
        ("Bases de datos PostgreSQL cloud-native con CNPG (CloudNativePG)", "Cloud-native PostgreSQL with CNPG (CloudNativePG)"),
        ("respaldos", "backups"),
        ("Diseño, creación y administración", "Design, build, and operate"),
        ("Implementación del ecosistema completo", "Implemented the full ecosystem"),
        ("Despliegue y mantenimiento", "Deployment and maintenance"),
        ("políticas de seguridad", "security policies"),
        ("Implementación de GitOps", "GitOps implementation"),
        ("Automatización con", "Automation with"),
        ("Administración de infraestructura virtualizada", "Virtualized infrastructure administration"),
        ("Optimización de pipelines CI/CD", "CI/CD pipeline optimization"),
        ("Disertante", "Speaker"),
        ("Co-diseño del curso", "Co-designed the course"),
        ("Docente", "Instructor"),
        ("Soporte técnico", "Technical support"),
        ("continuidad operacional", "operational continuity"),
        ("migración progresiva", "progressive migration"),
        ("Testing manual y automático", "Manual and automated testing"),
        ("casos de prueba", "test cases"),
        ("reporte de defectos", "defect reporting"),
        ("Rediseño y optimización", "Redesign and optimization"),
        ("Infraestructura Web", "Web Infrastructure"),
        ("Rol", "Role"),
        ("Duración", "Duration"),
        ("Ediciones", "Editions"),
        ("Contenido del curso", "Course content"),
        ("Troubleshooting", "Troubleshooting"),
        ("Mejores prácticas", "Best practices"),
        ("Temáticas cubiertos", "Topics covered"),
        ("almacenamiento", "storage"),
        ("seguridad en Kubernetes", "Kubernetes security"),
        ("backup/restore", "backup/restore"),
        ("Monitoreo", "Monitoring"),
        ("Observabilidad", "Observability"),
        ("secretos", "secrets"),
        ("políticas", "policies"),
        ("respaldos", "backups"),
        ("recuperación", "recovery"),
        ("clústeres", "clusters"),
        ("base de datos", "database"),
        ("Bases de datos", "Databases"),
        ("Administración de servidores", "Server administration"),
        ("Servicios institucionales", "Institutional services"),
        ("Alta disponibilidad", "High availability"),
        ("Monitoreo de seguridad", "Security monitoring"),
        ("rotación automática", "automatic rotation"),
        ("seguridad runtime", "runtime security"),
        ("admisión", "admission"),
        ("gobernar despliegues", "govern deployments"),
        ("Infraestructura cloud", "Cloud infrastructure"),
        ("kubeadm", "kubeadm"),
        ("EKS", "EKS"),
        ("Longhorn", "Longhorn"),
        ("MinIO", "MinIO"),
        ("Velero", "Velero"),
        ("Vault", "Vault"),
        ("Falco", "Falco"),
        ("CNPG", "CNPG"),
        ("PostgreSQL", "PostgreSQL"),
        ("Prometheus", "Prometheus"),
        ("Grafana", "Grafana"),
        ("Loki", "Loki"),
        ("Argo CD", "Argo CD"),
        ("Terraform", "Terraform"),
        ("Ansible", "Ansible"),
        ("Salt", "Salt"),
        ("Proxmox", "Proxmox"),
        ("GitLab", "GitLab"),
        ("GitOps", "GitOps"),
        ("Control de Versiones", "Version Control"),
        ("merge requests", "merge requests"),
        ("workflows colaborativos", "collaborative workflows"),
        ("GitLab CI/CD", "GitLab CI/CD"),
        ("pipelines", "pipelines"),
        ("jobs", "jobs"),
        ("stages", "stages"),
        ("artifacts", "artifacts"),
        ("variables", "variables"),
        ("webhooks", "webhooks"),
        ("flujos CI/CD complejos", "complex CI/CD flows"),
    ]

    months = [
        ("Enero", "January"), ("Febrero", "February"), ("Marzo", "March"),
        ("Abril", "April"), ("Mayo", "May"), ("Junio", "June"),
        ("Julio", "July"), ("Agosto", "August"), ("Septiembre", "September"),
        ("Octubre", "October"), ("Noviembre", "November"), ("Diciembre", "December"),
        ("Presente", "Present"),
    ]

    for es, en in replacements:
        content = content.replace(es, en)
    for es, en in months:
        content = content.replace(es, en)
    return content

def parse_markdown(md_content):
    """Parse markdown and extract elements"""
    elements = []
    lines = md_content.split('\n')
    
    for line in lines:
        # Don't strip to preserve indentation detection
        stripped = line.strip()
        
        if not stripped:
            continue
        
        # Main title (# Text)
        if stripped.startswith('# ') and not stripped.startswith('## '):
            title = stripped.replace('# ', '').strip()
            elements.append(('title', title))
        
        # Section (## Text)
        elif stripped.startswith('## '):
            section = stripped.replace('## ', '').strip()
            elements.append(('section', section))
        
        # Subsection (### Text)
        elif stripped.startswith('### '):
            subsection = stripped.replace('### ', '').strip()
            elements.append(('subsection', subsection))
        
        # Nested bullet (starts with spaces then -)
        elif line.startswith('  - '):
            bullet = line.replace('  - ', '').strip()
            elements.append(('nested_bullet', bullet))
        
        # Regular bullet
        elif stripped.startswith('- '):
            bullet = stripped.replace('- ', '').strip()
            elements.append(('bullet', bullet))
        
        # Separator
        elif stripped.startswith('---'):
            elements.append(('spacer', ''))
        
        # Normal text
        elif not stripped.startswith('---'):
            elements.append(('text', stripped))
    
    return elements

def create_pdf(md_file, language="ES"):
    """Create PDF from Markdown"""
    
    # Read markdown
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Translate if needed
    if language == "EN":
        content = translate_section_titles(content, language)
        content = translate_content(content)
    
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
        fontSize=21,
        textColor=PRIMARY_COLOR,
        spaceAfter=12,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )

    contact_style = ParagraphStyle(
        'Contact',
        parent=styles['Normal'],
        fontSize=9,
        textColor=TEXT_COLOR,
        spaceAfter=12,
        alignment=TA_LEFT,
        fontName='Helvetica'
    )

    section_style = ParagraphStyle(
        'SectionHeader',
        parent=styles['Normal'],
        fontSize=12.5,
        textColor=PRIMARY_COLOR,
        spaceAfter=10,
        spaceBefore=12,
        alignment=TA_LEFT,
        fontName='Helvetica-Bold'
    )

    subsection_style = ParagraphStyle(
        'Subsection',
        parent=styles['Normal'],
        fontSize=11,
        textColor=SECONDARY_COLOR,
        spaceAfter=4,
        spaceBefore=6,
        alignment=TA_LEFT,
        fontName='Helvetica-Bold'
    )

    bullet_style = ParagraphStyle(
        'Bullet',
        parent=styles['Normal'],
        fontSize=10.2,
        textColor=TEXT_COLOR,
        spaceAfter=6,
        leftIndent=16,
        bulletIndent=12,
        alignment=TA_LEFT,
        fontName='Helvetica'
    )

    nested_bullet_style = ParagraphStyle(
        'NestedBullet',
        parent=styles['Normal'],
        fontSize=10.2,
        textColor=TEXT_COLOR,
        spaceAfter=4,
        leftIndent=40,
        bulletIndent=30,
        alignment=TA_LEFT,
        fontName='Helvetica'
    )

    normal_style = ParagraphStyle(
        'NormalCustom',
        parent=styles['Normal'],
        fontSize=10.2,
        textColor=TEXT_COLOR,
        spaceAfter=8,
        alignment=TA_LEFT,
        fontName='Helvetica'
    )
    
    # Build content
    content_elements = []
    
    first_block_done = False
    for elem_type, raw_text in elements:
        elem_text = format_inline(raw_text)

        if elem_type == 'title':
            content_elements.append(Paragraph(elem_text, title_style))
            content_elements.append(Spacer(1, 8))
            first_block_done = True

        elif elem_type == 'text':
            if any(x in raw_text for x in ['📍', '📧', '🔗', '@']):
                clean = raw_text.replace('📍', '').replace('📧', '').replace('🔗', '').strip()
                content_elements.append(Paragraph(format_inline(clean), contact_style))
            else:
                # For the first descriptive block, keep a small spacer
                if not first_block_done:
                    content_elements.append(Spacer(1, 4))
                    first_block_done = True
                content_elements.append(Paragraph(elem_text, normal_style))

        elif elem_type == 'section':
            content_elements.append(Spacer(1, 8))
            content_elements.append(Paragraph(elem_text, section_style))

        elif elem_type == 'subsection':
            content_elements.append(Spacer(1, 4))
            content_elements.append(Paragraph(elem_text, subsection_style))

        elif elem_type == 'bullet':
            content_elements.append(Paragraph(f"• {elem_text}", bullet_style))

        elif elem_type == 'nested_bullet':
            content_elements.append(Paragraph(f"◦ {elem_text}", nested_bullet_style))

        elif elem_type == 'spacer':
            content_elements.append(Spacer(1, 8))
    
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
