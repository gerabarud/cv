# 👋 Welcome! | ¡Bienvenido!

This repository contains my professional CV (Curriculum Vitae) with automated generation of multiple formats.

---

## 📄 My CV

### Spanish Version | Versión en Español
- **Markdown**: [CV_Gerardo_Barud_ES.md](./CV_Gerardo_Barud_ES.md)
- **LibreOffice**: [CV_Gerardo_Barud_ES.odt](./CV_Gerardo_Barud_ES.odt)

### English Version | Versión en Inglés
- **Markdown**: [CV_Gerardo_Barud_EN.md](./CV_Gerardo_Barud_EN.md)
- **LibreOffice**: [CV_Gerardo_Barud_EN.odt](./CV_Gerardo_Barud_EN.odt)

---

## 🚀 About Me | Acerca de mí

I am a **SysAdmin/SRE specialist** with **12+ years of experience** in:
- 🐧 Linux Systems Administration
- ☸️ Kubernetes & Container Orchestration
- ☁️ Cloud Infrastructure (AWS, On-Premise)
- 📊 Observability & Monitoring
- 🔐 Security & Disaster Recovery

**Soy un especialista SysAdmin/SRE con 12+ años de experiencia en:**
- Administración de Sistemas Linux
- Orquestación de Contenedores & Kubernetes
- Infraestructura Cloud (AWS, On-Premise)
- Observabilidad y Monitoreo
- Seguridad y Disaster Recovery

---

## 🔧 Key Technologies | Tecnologías Clave

### Kubernetes Ecosystem
- **Orchestration**: kubeadm, CAPI, EKS
- **Networking**: Calico, Ingress Nginx, MetalLB
- **Storage**: Longhorn, MinIO, Velero
- **Secrets**: Vault, Sealed Secrets
- **Security**: RBAC, ValidationAdmissionPolicy, Falco
- **Observability**: Prometheus, Grafana, Loki
- **Databases**: CNPG (PostgreSQL), etcd

### Infrastructure & Automation
- **IaC**: Terraform, Ansible, Salt
- **Virtualization**: Proxmox VE
- **CI/CD**: GitLab (runners, pipelines)
- **GitOps**: Argo CD

---

## 🎓 Teaching & Community

I actively contribute to the technical community through:
- 📚 Teaching production Kubernetes courses for national universities (RIU)
- 🎤 Speaking at professional workshops and conferences
- 📖 Authoring infrastructure documentation
- 👥 Mentoring and technical training

Contribuyo activamente a la comunidad técnica mediante:
- Impartiendo cursos de Kubernetes para universidades nacionales
- Disertaciones en workshops y conferencias profesionales
- Autoría de documentación de infraestructura
- Mentoría y capacitación técnica

---

## 📝 How to Use This Repository | Cómo usar este repositorio

### Editing the CV | Editar el CV

1. **Edit the Markdown files** | Editar los archivos Markdown:
   - Spanish: `CV_Gerardo_Barud_ES.md`
   - English: `CV_Gerardo_Barud_EN.md`

2. **Commit and push** to the `main` branch

3. **GitHub Actions will automatically**:
   - Generate ODT files from the Markdown
   - Commit the generated files
   - Create a release with both formats

### Running Locally | Ejecutar localmente

Generate CV files locally:

```bash
# Install dependencies (one time)
pip install odfpy

# Generate both Spanish and English versions
python3 generate_cv_odt.py BOTH

# Or individual versions
python3 generate_cv_odt.py ES   # Spanish only
python3 generate_cv_odt.py EN   # English only
```

---

## 🤖 Automation | Automatización

This repository uses **GitHub Actions** to automatically:

1. ✅ Detect changes to MD files
2. ✅ Generate ODT files using the Python script
3. ✅ Commit generated files back to the repo
4. ✅ Create releases with both format versions

### Workflow File
See [.github/workflows/generate-cv.yml](./.github/workflows/generate-cv.yml)

**Step by step for CI/CD:**

```
You modify MD files
        ↓
Push to main branch
        ↓
GitHub Actions triggered
        ↓
Python script runs (generate_cv_odt.py)
        ↓
ODT files generated
        ↓
Files auto-committed & pushed
        ↓
Release created with both versions
        ↓
Ready to download from GitHub!
```

---

## 📥 Downloading Your CV | Descargar tu CV

### Option 1: Direct from Repository | Opción 1: Directamente del repositorio
- [CV_Gerardo_Barud_ES.odt](./CV_Gerardo_Barud_ES.odt) - Spanish version
- [CV_Gerardo_Barud_EN.odt](./CV_Gerardo_Barud_EN.odt) - English version

### Option 2: From Releases | Opción 2: Desde Releases
Go to [Releases](../../releases) section to download all versions

### Option 3: View as Markdown | Opción 3: Ver como Markdown
- [Spanish MD](./CV_Gerardo_Barud_ES.md)
- [English MD](./CV_Gerardo_Barud_EN.md)

---

## 📧 Contact | Contacto

- **Email**: gabarud@gmail.com
- **GitHub**: [@gerabarud](https://github.com/gerabarud)
- **LinkedIn**: [Gerardo Barud](https://linkedin.com/in/gbarud)

---

## 📋 Structure | Estructura

```
cv/
├── README.md                          # This file | Este archivo
├── CV_Gerardo_Barud_ES.md            # Spanish markdown
├── CV_Gerardo_Barud_EN.md            # English markdown
├── CV_Gerardo_Barud_ES.odt           # Spanish LibreOffice (auto-generated)
├── CV_Gerardo_Barud_EN.odt           # English LibreOffice (auto-generated)
├── generate_cv_odt.py                # Python script to generate ODTs
└── .github/
    └── workflows/
        └── generate-cv.yml           # GitHub Actions workflow
```

---

## 🔄 Workflow Summary | Resumen del Workflow

| Step | Action | Automatic? |
|------|--------|-----------|
| 1 | Edit `.md` files | Manual ✍️ |
| 2 | Commit & push | Manual ✍️ |
| 3 | GitHub Actions runs | Automatic 🤖 |
| 4 | Generate ODT files | Automatic 🤖 |
| 5 | Commit generated files | Automatic 🤖 |
| 6 | Create release | Automatic 🤖 |

---

## 💡 Tips | Consejos

1. **Always edit the MD files** - They are the source of truth
   - *Siempre edita los MD* - Son la fuente de verdad

2. **Commit messages are auto-generated** - No need to worry about them
   - *Los mensajes de commit son auto-generados* - No necesitas preocuparte

3. **ODT files are generated automatically** - Don't edit them manually
   - *Los ODT se generan automáticamente* - No los edites manualmente

4. **Both Spanish and English are always in sync**
   - *Español e Inglés siempre están sincronizados*

---

## 📜 License | Licencia

This CV is provided as-is for personal use.

---

**Last updated** | **Última actualización**: 2025-12-05

Made with ❤️ | Hecho con ❤️
