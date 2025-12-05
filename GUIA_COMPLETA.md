# 📖 Guía Completa: CV Automatizado con GitHub

## 🎯 Objetivo

Tu CV siempre estará actualizado en estos formatos:
- 📝 **Markdown** (Español e Inglés) - Fuente de verdad
- 📄 **ODT (LibreOffice)** - Generado automáticamente
- 🌐 **GitHub** - Tu portada profesional

---

## 🏗️ Estructura del Proyecto

```
/home/gbarud/cv/
├── README.md                          # Portada de GitHub
├── CV_Gerardo_Barud_ES.md            # CV fuente (Español)
├── CV_Gerardo_Barud_EN.md            # CV fuente (Inglés)
├── CV_Gerardo_Barud_ES.odt           # Generado automáticamente
├── CV_Gerardo_Barud_EN.odt           # Generado automáticamente
├── generate_cv_odt.py                # Script Python (reutilizable)
├── .github/
│   └── workflows/
│       └── generate-cv.yml           # GitHub Actions CI/CD
└── .git/                             # Repositorio Git
```

---

## 🔄 Flujo de Trabajo

### Opción 1: Actualizar Localmente (SIN GitHub Actions)

**Paso 1: Edita el markdown**
```bash
cd /home/gbarud/cv
# Abre y edita:
# - CV_Gerardo_Barud_ES.md  (Español)
# - CV_Gerardo_Barud_EN.md  (Inglés)
```

**Paso 2: Genera los ODT localmente**
```bash
# Asegúrate de estar en la carpeta cv
cd /home/gbarud/cv

# Opción A: Generar ambos (recomendado)
python3 generate_cv_odt.py BOTH

# Opción B: Solo español
python3 generate_cv_odt.py ES

# Opción C: Solo inglés
python3 generate_cv_odt.py EN
```

**Paso 3: Verifica los archivos generados**
```bash
ls -lh CV_Gerardo_Barud*.odt
# Deberías ver:
# CV_Gerardo_Barud_ES.odt
# CV_Gerardo_Barud_EN.odt
```

**Paso 4: Confirma los cambios**
```bash
cd /home/gbarud/cv
git add CV_Gerardo_Barud_*.md CV_Gerardo_Barud_*.odt
git commit -m "Actualización de CV: [descripción de cambios]"
```

---

### Opción 2: Automatizado en GitHub (RECOMENDADO)

Con GitHub Actions, TODO se automatiza:

**Paso 1: Sube tu repositorio a GitHub**
```bash
cd /home/gbarud/cv

# Agregamos el remote (reemplaza USER por tu usuario GitHub)
git remote add origin https://github.com/USER/cv.git
git branch -M main
git push -u origin main
```

**Paso 2: Ahora cada vez que hagas cambios**

Solo necesitas:
```bash
# Editar los MD
nano CV_Gerardo_Barud_ES.md
nano CV_Gerardo_Barud_EN.md

# Commit y push
git add CV_Gerardo_Barud_*.md
git commit -m "Actualización: Agregué nueva experiencia"
git push
```

**Paso 3: GitHub Actions hace el resto**
- 🤖 Detecta cambios en `.md`
- 🤖 Ejecuta el script `generate_cv_odt.py`
- 🤖 Genera los ODT automáticamente
- 🤖 Hace commit de los archivos
- 🤖 Crea un Release con ambas versiones
- ✅ ¡Listo!

---

## 📝 Ejemplo Práctico

### Escenario: Agregué una nueva experiencia laboral

**1. Editar el MD:**
```bash
vim CV_Gerardo_Barud_ES.md

# Agregué sección nueva en EXPERIENCIA PROFESIONAL
```

**2. Opción A - Con CI/CD (GitHub)**
```bash
git add CV_Gerardo_Barud_ES.md
git commit -m "Agregué experiencia en Nueva Empresa"
git push origin main

# ⏳ GitHub Actions ejecuta automáticamente
# 🤖 Se generan los ODT
# 📦 Se crea un Release
# ✅ Listo en ~2 minutos
```

**2. Opción B - Localmente**
```bash
python3 generate_cv_odt.py BOTH
git add CV_Gerardo_Barud_*.odt
git commit -m "Agregué experiencia en Nueva Empresa"
git push origin main
```

---

## 🔧 Uso del Script `generate_cv_odt.py`

### Desde terminal
```bash
# Generar ambos
/home/gbarud/cv/.venv/bin/python /home/gbarud/cv/generate_cv_odt.py BOTH

# Solo español
/home/gbarud/cv/.venv/bin/python /home/gbarud/cv/generate_cv_odt.py ES

# Solo inglés
/home/gbarud/cv/.venv/bin/python /home/gbarud/cv/generate_cv_odt.py EN
```

### Alias útil (opcional)
Agrega esto a tu `~/.zshrc`:
```bash
alias gencv='cd /home/gbarud/cv && /home/gbarud/cv/.venv/bin/python generate_cv_odt.py'
```

Después puedes usar:
```bash
gencv BOTH  # Genera ambos
gencv ES    # Solo español
```

---

## 🌐 Configurar GitHub

### Paso 1: Crear repositorio en GitHub
1. Ve a [github.com/new](https://github.com/new)
2. Nombre: `cv` (o como prefieras)
3. Descripción: "My professional CV with automated generation"
4. Elige público (así puedes compartir) o privado
5. NO inicialices con README (ya tienes uno)

### Paso 2: Conectar tu repositorio local
```bash
cd /home/gbarud/cv

# Agregar remoto
git remote add origin https://github.com/TU_USUARIO/cv.git

# Cambiar rama a main si es necesario
git branch -M main

# Hacer push
git push -u origin main
```

### Paso 3: Verificar que GitHub Actions funciona
1. Ve a tu repositorio en GitHub
2. Click en "Actions"
3. Deberías ver workflows disponibles
4. Ahora cada vez que hagas `git push`, se ejecutará automáticamente

---

## 📊 Ventajas del Sistema

| Feature | Sin Automatización | Con GitHub Actions |
|---------|-------------------|-------------------|
| Editar CV | ✅ Fácil | ✅ Fácil |
| Generar ODT | ⚠️ Manual cada vez | ✅ Automático |
| Sincronizar versiones | ⚠️ Fácil olvidar | ✅ Siempre sincronizado |
| Disponibilidad | 💾 Solo local | 🌐 En GitHub (URL compartible) |
| Historial de versiones | ❌ No | ✅ Git history |
| Releases | ❌ No | ✅ Automáticos |
| Control de cambios | ⚠️ Manual | ✅ Git + GitHub |

---

## 🐛 Troubleshooting

### Problema: "El script no genera ODT"
```bash
# Verifica que odfpy está instalado
pip install odfpy

# Verifica el entorno virtual
source /home/gbarud/cv/.venv/bin/activate
python generate_cv_odt.py BOTH
```

### Problema: "GitHub Actions no ejecuta"
1. Verifica que el archivo está en: `.github/workflows/generate-cv.yml`
2. Va a Settings → Actions → General
3. Asegúrate que "Actions" está habilitado
4. Comprueba que el workflow tiene los permisos correctos

### Problema: "Los cambios no se aplican"
```bash
# Asegúrate de hacer commit del MD correcto
git status  # Ver qué cambios hay
git add CV_Gerardo_Barud_*.md
git commit -m "Cambios en CV"
git push origin main
```

---

## 📋 Checklist: Configuración Inicial

- [ ] MD en español (`CV_Gerardo_Barud_ES.md`) listo
- [ ] MD en inglés (`CV_Gerardo_Barud_EN.md`) listo
- [ ] Script `generate_cv_odt.py` funciona localmente
- [ ] Repositorio Git inicializado
- [ ] README.md creado
- [ ] `.github/workflows/generate-cv.yml` en lugar
- [ ] Repositorio subido a GitHub
- [ ] GitHub Actions visible en Actions tab
- [ ] Primer push disparó la automatización
- [ ] ODT generados correctamente

---

## 🚀 Próximos Pasos

1. **Crear el repositorio en GitHub** (si aún no lo hiciste)
2. **Hacer push a main**:
   ```bash
   cd /home/gbarud/cv
   git push -u origin main
   ```
3. **Compartir tu CV profesional**:
   - URL de tu MD: `https://github.com/TU_USUARIO/cv`
   - Descargar ODT desde Releases
   - Compartir el repo en LinkedIn/redes

---

## 📚 Recursos Útiles

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [ODF Library (odfpy)](https://odfpy.readthedocs.io/)
- [Markdown Guide](https://www.markdownguide.org/)
- [Git Workflow](https://git-scm.com/book/en/v2)

---

## ❓ Preguntas Frecuentes

**P: ¿Necesito los ODT en la repo?**  
R: No, pero es bueno tenerlos para descargas directas. GitHub Actions los genera automáticamente.

**P: ¿Puedo editar el script Python?**  
R: Sí, es tuyo. Puedes modificar estilos, colores, etc. en `generate_cv_odt.py`

**P: ¿Qué pasa si GitHub Actions falla?**  
R: Recibirás un email. Revisa los logs en Actions → último workflow → click en el paso que falló.

**P: ¿Puedo generar PDF en lugar de ODT?**  
R: Sí, necesitarías modificar el script para usar `python-pptx` o instalar LibreOffice CLI.

**P: ¿Cómo comparto mi CV?**  
R: 
- Comparte el MD: Link directo en GitHub
- Comparte el ODT: Descárgalo desde Releases
- Comparte la URL: Tu perfil es tu portada

---

**Última actualización**: 2025-12-05  
**Versión**: 1.0
