# DOCUMENTACIÓN DEL PROYECTO

## 📋 Descripción General

Este repositorio contiene tu CV profesional con **automatización completa** para generar PDFs en español e inglés desde una única fuente de verdad (Markdown).

### Objetivos
- ✅ CV siempre actualizado en un único archivo Markdown
- ✅ Generación automática de PDFs (ES + EN) desde el Markdown
- ✅ PDFs almacenados en directorio `/pdfs/` para mantener limpio el repositorio
- ✅ Automatización con GitHub Actions (sin intervención manual)
- ✅ README como presentación profesional del perfil

---

## 🏗️ Estructura del Proyecto

```
/home/gbarud/cv/
├── README.md                           # Tu presentación profesional
├── CV_Gerardo_Barud_ES.md             # ⭐ FUENTE DE VERDAD - CV en Español
├── generate_cv_pdf.py                 # Script Python que genera los PDFs
├── pdfs/                              # Directorio de PDFs generados
│   ├── CV_Gerardo_Barud_ES.pdf       # PDF generado automáticamente
│   └── CV_Gerardo_Barud_EN.pdf       # PDF generado automáticamente
├── .github/workflows/
│   └── generate-cv.yml                # GitHub Actions workflow
└── .git/                              # Control de versiones
```

---

## 🔄 Flujo de Trabajo

### Ciclo de Vida del CV

```
┌─────────────────────────────────────────────────────────┐
│ 1. TÚ EDITAS: CV_Gerardo_Barud_ES.md                    │
│    (Única fuente de verdad - aquí va TODO)              │
└────────────────┬────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────┐
│ 2. HACES: git add . && git commit && git push           │
│    (Envías cambios a GitHub)                            │
└────────────────┬────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────┐
│ 3. GITHUB ACTIONS SE EJECUTA AUTOMÁTICAMENTE            │
│    (No necesitas hacer nada más)                        │
└────────────────┬────────────────────────────────────────┘
                 │
        ┌────────┴───────────┐
        ▼                    ▼
   ┌──────────┐         ┌──────────┐
   │ Genera   │         │ Genera   │
   │ PDF_ES   │         │ PDF_EN   │
   └────┬─────┘         └────┬─────┘
        │                    │
        └────────┬───────────┘
                 ▼
┌─────────────────────────────────────────────────────────┐
│ 4. ARCHIVOS GUARDADOS: pdfs/                            │
│    ✅ CV_Gerardo_Barud_ES.pdf                          │
│    ✅ CV_Gerardo_Barud_EN.pdf                          │
│    ✅ Auto-committed a GitHub                           │
└─────────────────────────────────────────────────────────┘
```

---

## 🚀 Cómo Usar

### OPCIÓN 1: Con GitHub (Recomendado)

1. **Edita tu CV localmente**
   ```bash
   nano CV_Gerardo_Barud_ES.md
   # O usa tu editor favorito (VS Code, vim, etc)
   ```

2. **Haz commit y push**
   ```bash
   cd /home/gbarud/cv
   git add CV_Gerardo_Barud_ES.md
   git commit -m "Actualizo CV con nueva experiencia"
   git push origin main
   ```

3. **¡Listo!** GitHub Actions genera automáticamente los PDFs en ~2 minutos
   - Los PDFs se guardan en `/pdfs/`
   - Se auto-commitean los cambios
   - Todo disponible en tu repositorio de GitHub

### OPCIÓN 2: Sin GitHub (Solo Local)

```bash
# Instala dependencia (una sola vez)
pip install reportlab

# Genera los PDFs localmente
cd /home/gbarud/cv
python3 generate_cv_pdf.py BOTH      # Genera ambas versiones
# o
python3 generate_cv_pdf.py ES        # Solo español
python3 generate_cv_pdf.py EN        # Solo inglés

# Los archivos se crean en: /home/gbarud/cv/pdfs/
```

---

## 📝 Archivos Principales

### `CV_Gerardo_Barud_ES.md` ⭐ IMPORTANTE

**Este es tu único CV a mantener.** Aquí va toda la información:
- Perfil profesional
- Experiencia laboral
- Formación y cursos
- Charlas y disertaciones
- Habilidades técnicas
- Idiomas
- Otras actividades

**Formato Markdown:**
```markdown
# Tu Nombre

## SECCIÓN

### Subsección

- Punto 1
- Punto 2
```

El script automáticamente:
- Lee este archivo
- Genera PDF en español idéntico al Markdown
- Traduce títulos y crea PDF en inglés
- Guarda ambos en `/pdfs/`

### `generate_cv_pdf.py`

Script Python que hace la magia:
- Lee `CV_Gerardo_Barud_ES.md`
- Parsea la estructura Markdown
- Genera PDFs profesionales con estilo
- Crea versión en inglés automáticamente
- Guarda en `/pdfs/CV_Gerardo_Barud_{ES|EN}.pdf`

**No necesitas editarlo**, pero si quieres cambiar colores o estilos:
- Línea 14: `PRIMARY_COLOR` - Color de títulos
- Línea 15: `SECONDARY_COLOR` - Color de subtítulos
- Línea 16: `TEXT_COLOR` - Color de texto normal

### `README.md`

Tu presentación profesional en GitHub. No es documentación del proyecto, sino tu **portada**:
- Quién eres (resumen impactante)
- Qué haces (servicios)
- Experiencia destacada
- Stack tecnológico
- Cómo contactarte
- Links a tus CVs

### `.github/workflows/generate-cv.yml`

El cerebro de la automatización:
- Se ejecuta cada vez que haces push
- Detecta cambios en `CV_Gerardo_Barud_ES.md`
- Corre `generate_cv_pdf.py BOTH`
- Auto-commitea los PDFs generados
- Todo sin que hagas nada

---

## 🔧 Configuración Inicial

**Primera vez que usas GitHub Actions:**

1. Crea un repositorio en GitHub
2. Haz push con: `git push -u origin main`
3. Ve a GitHub → Settings → Actions
4. Asegúrate que Actions esté habilitado
5. Haz push de un cambio prueba y verás que se ejecuta

---

## 📊 Estado Actual

✅ **Setup Completo:**
- CV en Markdown: `CV_Gerardo_Barud_ES.md` (7.3K)
- Script de generación: `generate_cv_pdf.py` (funcional)
- GitHub Actions workflow: `.github/workflows/generate-cv.yml`
- README profesional: `README.md` (tu portada)
- Directorio PDFs: `/pdfs/` (listos para generación)

✅ **Necesita Hacer Una Vez:**
- Crear repositorio en GitHub
- Hacer `git push -u origin main` para activar Actions

---

## 🎨 Personalización

### Cambiar colores del PDF

Edita `generate_cv_pdf.py` líneas 14-16:
```python
PRIMARY_COLOR = HexColor("#1a5490")      # Azul oscuro para títulos
SECONDARY_COLOR = HexColor("#2c5282")    # Azul medio para subtítulos
TEXT_COLOR = HexColor("#333333")         # Gris oscuro para texto
```

Usa cualquier color en formato hexadecimal (ej: `#FF5733`).

### Cambiar fuente del PDF

En `generate_cv_pdf.py`, busca `fontName` en las definiciones de estilo:
```python
fontName='Helvetica-Bold'  # Cambia a 'Times-Bold', 'Courier', etc
```

### Traducción automática

El script traduce automáticamente estos términos al inglés:
- Títulos de secciones
- Meses
- Palabras comunes

Para agregar más traducciones, edita la función `translate_content()` en `generate_cv_pdf.py`.

---

## 🐛 Troubleshooting

### "Los PDFs no se generan"
```bash
# Verifica que reportlab está instalado
pip list | grep reportlab

# Si no está:
pip install reportlab
```

### "GitHub Actions no se ejecuta"
1. Verifica que el repositorio sea público
2. Abre GitHub → Actions y mira los logs
3. Asegúrate que el archivo está en `main` branch
4. Espera ~2 minutos (a veces tarda)

### "Los PDFs tienen errores de encoding"
Asegúrate que el CV está guardado en UTF-8:
```bash
file -i CV_Gerardo_Barud_ES.md
# Debe mostrar: UTF-8
```

---

## 💡 Tips Útiles

### Alias rápido
```bash
echo "alias gencv='cd /home/gbarud/cv && python3 generate_cv_pdf.py'" >> ~/.zshrc
source ~/.zshrc

# Después:
gencv BOTH    # Genera ambos
```

### Ver qué cambió
```bash
cd /home/gbarud/cv
git diff CV_Gerardo_Barud_ES.md    # Ver cambios sin commitear
git log --oneline                  # Ver historial de commits
```

### Revertir cambios
```bash
git checkout -- CV_Gerardo_Barud_ES.md    # Deshace cambios
git reset HEAD~1                           # Deshace último commit
```

---

## 📈 Flujo de Actualización Normal

**Cada vez que quieras actualizar tu CV:**

```bash
# 1. Editar
nano CV_Gerardo_Barud_ES.md

# 2. Previsualizar (opcional)
python3 generate_cv_pdf.py BOTH

# 3. Commit y push
git add CV_Gerardo_Barud_ES.md
git commit -m "Actualizo experiencia en [tema]"
git push origin main

# 4. Espera ~2 minutos y listo
# Los PDFs se actualizan automáticamente
```

---

## 🔐 Seguridad

- Tu CV está en tu repositorio personal (privado si quieres)
- Los PDFs se generan localmente (en tu máquina)
- GitHub Actions solo corre scripts que tú autorizas
- No se almacenan datos sensibles en GitHub

---

## 📞 Soporte Rápido

| Problema | Solución |
|----------|----------|
| PDF no se genera | `pip install reportlab` |
| Actions no corre | Verifica que hiciste `git push` |
| PDF tiene error | Verifica encoding UTF-8 |
| Cambios no aparecen | Espera 2 minutos y refresca GitHub |
| Quiero volver atrás | `git checkout -- archivo` |

---

## 📚 Recursos

- ReportLab Docs: https://www.reportlab.com/docs/reportlab-userguide.pdf
- GitHub Actions: https://docs.github.com/actions
- Markdown Guide: https://www.markdownguide.org/

---

**Última actualización**: 5 de diciembre de 2025

*Preguntas? Abre un issue o contacta a gabarud@gmail.com*
