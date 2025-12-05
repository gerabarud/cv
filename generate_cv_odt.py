#!/usr/bin/env python3
"""
CV Generator Script
Generates ODT (LibreOffice) files from Markdown CV files.
Usage: python3 generate_cv_odt.py [ES|EN|BOTH]
"""

import sys
import re
from odf.opendocument import OpenDocumentText
from odf.style import Style, TextProperties, ParagraphProperties
from odf.text import P

def parse_markdown(md_content):
    """Parse markdown content and extract sections."""
    sections = {}
    current_section = None
    current_content = []
    
    lines = md_content.split('\n')
    
    for line in lines:
        if line.startswith('# ') and not line.startswith('## '):
            # Main title
            sections['title'] = line.replace('# ', '').strip()
        elif line.startswith('## '):
            # Section header
            if current_section:
                sections[current_section] = '\n'.join(current_content).strip()
            current_section = line.replace('## ', '').strip()
            current_content = []
        elif current_section:
            current_content.append(line)
    
    if current_section:
        sections[current_section] = '\n'.join(current_content).strip()
    
    return sections

def create_odt_from_md(md_filepath, output_filepath):
    """Create ODT document from markdown file."""
    
    # Read markdown
    with open(md_filepath, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # Create document
    doc = OpenDocumentText()
    
    # ===== STYLES =====
    # Main name
    style_name = Style(name="Name", family="paragraph")
    style_name.addElement(ParagraphProperties(textalign="center", marginbottom="0.2cm"))
    name_props = TextProperties(fontsize="24pt", fontweight="bold", color="#1a5490")
    style_name.addElement(name_props)
    doc.styles.addElement(style_name)
    
    # Subtitle
    style_subtitle = Style(name="Subtitle", family="paragraph")
    style_subtitle.addElement(ParagraphProperties(textalign="center", marginbottom="0.3cm"))
    subtitle_props = TextProperties(fontsize="14pt", color="#4a4a4a", fontstyle="italic")
    style_subtitle.addElement(subtitle_props)
    doc.styles.addElement(style_subtitle)
    
    # Contact info
    style_contact = Style(name="Contact", family="paragraph")
    style_contact.addElement(ParagraphProperties(textalign="center", marginbottom="0.5cm"))
    contact_props = TextProperties(fontsize="10pt", color="#333333")
    style_contact.addElement(contact_props)
    doc.styles.addElement(style_contact)
    
    # Sections
    style_section = Style(name="Section", family="paragraph")
    style_section.addElement(ParagraphProperties(margintop="0.4cm", marginbottom="0.2cm",
                                                 borderlinewidthbottom="0.05cm",
                                                 borderleft="none", borderright="none", bordertop="none",
                                                 borderbottom="0.05cm solid #1a5490",
                                                 paddingbottom="0.1cm"))
    section_props = TextProperties(fontsize="14pt", fontweight="bold", color="#1a5490")
    style_section.addElement(section_props)
    doc.styles.addElement(style_section)
    
    # Job titles
    style_jobtitle = Style(name="JobTitle", family="paragraph")
    style_jobtitle.addElement(ParagraphProperties(marginbottom="0.05cm", margintop="0.2cm"))
    job_props = TextProperties(fontsize="11pt", fontweight="bold", color="#2c5282")
    style_jobtitle.addElement(job_props)
    doc.styles.addElement(style_jobtitle)
    
    # Company/Institution
    style_company = Style(name="Company", family="paragraph")
    style_company.addElement(ParagraphProperties(marginbottom="0.05cm"))
    company_props = TextProperties(fontsize="10pt", fontstyle="italic", color="#4a4a4a")
    style_company.addElement(company_props)
    doc.styles.addElement(style_company)
    
    # Dates
    style_date = Style(name="DateStyle", family="paragraph")
    style_date.addElement(ParagraphProperties(marginbottom="0.2cm"))
    date_props = TextProperties(fontsize="9pt", color="#666666")
    style_date.addElement(date_props)
    doc.styles.addElement(style_date)
    
    # Normal text
    style_normal = Style(name="Normal", family="paragraph")
    style_normal.addElement(ParagraphProperties(marginbottom="0.15cm", textalign="justify"))
    normal_props = TextProperties(fontsize="10pt", color="#333333")
    style_normal.addElement(normal_props)
    doc.styles.addElement(style_normal)
    
    # Bullets
    style_bullet = Style(name="Bullet", family="paragraph")
    style_bullet.addElement(ParagraphProperties(marginleft="0.5cm", marginbottom="0.1cm"))
    bullet_props = TextProperties(fontsize="10pt", color="#333333")
    style_bullet.addElement(bullet_props)
    doc.styles.addElement(style_bullet)
    
    # Skills
    style_skill = Style(name="Skill", family="paragraph")
    style_skill.addElement(ParagraphProperties(marginleft="0.3cm", marginbottom="0.1cm"))
    skill_props = TextProperties(fontsize="10pt", color="#333333")
    style_skill.addElement(skill_props)
    doc.styles.addElement(style_skill)
    
    # ===== CONTENT PARSING AND BUILDING =====
    
    # Extract title and contact from first lines
    lines = md_content.split('\n')
    title = ""
    subtitle = ""
    contact_lines = []
    
    for i, line in enumerate(lines):
        if line.startswith('# ') and not line.startswith('## '):
            title = line.replace('# ', '').strip()
        elif line.startswith('**') and i < 10:
            if subtitle == "":
                subtitle = line.replace('**', '').strip()
            else:
                contact_lines.append(line.replace('**', '').strip())
        elif '📍' in line or '📧' in line or '🔗' in line:
            contact_lines.append(line.strip())
    
    # Title
    p = P(stylename=style_name)
    p.addText(title)
    doc.text.addElement(p)
    
    # Subtitle
    if subtitle:
        p = P(stylename=style_subtitle)
        p.addText(subtitle)
        doc.text.addElement(p)
    
    # Contact info
    for contact in contact_lines:
        p = P(stylename=style_contact)
        p.addText(contact)
        doc.text.addElement(p)
    
    doc.text.addElement(P())
    
    # Parse sections
    sections = parse_markdown(md_content)
    
    # Process content
    for section_name, section_content in sections.items():
        if section_name in ['title']:
            continue
        
        # Add section header
        p = P(stylename=style_section)
        p.addText(section_name)
        doc.text.addElement(p)
        
        # Process section content
        content_lines = section_content.split('\n')
        for line in content_lines:
            line = line.strip()
            if not line:
                doc.text.addElement(P())
            elif line.startswith('###'):
                # Subsection (job title, company, etc.)
                text = line.replace('###', '').replace('**', '').strip()
                p = P(stylename=style_jobtitle)
                p.addText(text)
                doc.text.addElement(p)
            elif line.startswith('*') and not line.startswith('**'):
                # Bullet point
                text = line.lstrip('- *').rstrip('*').strip()
                p = P(stylename=style_bullet)
                p.addText("• " + text)
                doc.text.addElement(p)
            elif line.startswith('-'):
                # Bullet point (markdown style)
                text = line.lstrip('- ').strip()
                p = P(stylename=style_bullet)
                p.addText("• " + text)
                doc.text.addElement(p)
            elif line.startswith('*') and line.endswith('*'):
                # Emphasis (italics) - usually dates or company
                text = line.replace('*', '').strip()
                p = P(stylename=style_date)
                p.addText(text)
                doc.text.addElement(p)
            elif line.startswith('**') and line.endswith('**'):
                # Bold - company or role
                text = line.replace('**', '').strip()
                if '–' in text or 'vs' in text:
                    p = P(stylename=style_date)
                else:
                    p = P(stylename=style_company)
                p.addText(text)
                doc.text.addElement(p)
            elif len(line) > 20:
                # Regular paragraph
                p = P(stylename=style_normal)
                p.addText(line)
                doc.text.addElement(p)
            else:
                # Short text - could be various things
                p = P(stylename=style_bullet)
                p.addText(line)
                doc.text.addElement(p)
    
    # Save document
    doc.save(output_filepath)
    print(f"✅ Successfully created: {output_filepath}")

def main():
    language = "BOTH"
    if len(sys.argv) > 1:
        language = sys.argv[1].upper()
    
    if language not in ["ES", "EN", "BOTH"]:
        print("Usage: python3 generate_cv_odt.py [ES|EN|BOTH]")
        sys.exit(1)
    
    base_path = "/home/gbarud/cv"
    
    if language in ["ES", "BOTH"]:
        md_es = f"{base_path}/CV_Gerardo_Barud_ES.md"
        odt_es = f"{base_path}/CV_Gerardo_Barud_ES.odt"
        try:
            create_odt_from_md(md_es, odt_es)
        except Exception as e:
            print(f"❌ Error generating Spanish CV: {e}")
    
    if language in ["EN", "BOTH"]:
        md_en = f"{base_path}/CV_Gerardo_Barud_EN.md"
        odt_en = f"{base_path}/CV_Gerardo_Barud_EN.odt"
        try:
            create_odt_from_md(md_en, odt_en)
        except Exception as e:
            print(f"❌ Error generating English CV: {e}")

if __name__ == "__main__":
    main()
