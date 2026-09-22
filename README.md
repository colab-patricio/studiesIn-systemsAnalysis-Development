# Studies in Systems Analysis & Development

This repository collects the coursework I completed during my undergraduate degree in **Systems Analysis and Development** (*Análise e Desenvolvimento de Sistemas*), along with related self-study from online courses.

Its purpose is to keep a record of my learning path: exercises, assessments and small projects, organized by semester and subject.

> **Note:** The course material is in Brazilian Portuguese, so problem statements, comments and variable names are written in Portuguese.

## Repository structure

```text
.
├── Graduação/                          # Undergraduate coursework, by semester
│   ├── 1st_semester/
│   │   ├── logicaProgramacao_algoritmos/   # Programming Logic & Algorithms
│   │   │   ├── AF/                         # Assessment deliverables
│   │   │   └── AT/
│   │   └── organizacaoArq_computadores/    # Computer Organization & Architecture
│   │       └── AF/
│   ├── 2nd_semester/
│   ├── 3rd_semester/
│   ├── 4th_semester/
│   └── 5th_semester/
├── Cursos/                             # Complementary courses
│   ├── cursoemvideo_por_gustavoGuanabara/  # Curso em Vídeo (Gustavo Guanabara)
│   └── theOdin_project/                    # The Odin Project
├── pyproject.toml                      # Python project config (uv)
└── uv.lock
```

Each subject folder contains its assessment deliverables (for example `AT` and `AF`), with one file per question (e.g. `Q1AT.py`). Empty folders hold a `.gitkeep` placeholder until content is added.

### Complementary courses

- **[Curso em Vídeo](https://www.cursoemvideo.com/)** by Gustavo Guanabara
- **[The Odin Project](https://www.theodinproject.com/)**

## Getting started

Clone the repository and set up the Python environment with uv:

```bash
git clone https://github.com/colab-patricio/studiesIn-systemsAnalysis-Development.git
cd studiesIn-systemsAnalysis-Development
uv sync
```

Run any exercise directly:

```bash
uv run python "Graduação/1st_semester/logicaProgramacao_algoritmos/AT/Q1AT.py"
```

Notebooks can be opened locally with Jupyter or in Google Colab through the badge at the top of each notebook.

## Author

**Alexandre Patricio**, Systems Analysis and Development student.
GitHub: [@colab-patricio](https://github.com/colab-patricio)
