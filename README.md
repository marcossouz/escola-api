<h1 align="center">ESCOLA-API</h1>


<p align="center">
Uma API de uma escola, capaz de criar alunos, visualizar os dados desse aluno, atualizar tanto alunos, como curso, e vincular esses nossos dois recursos, criando, assim, as matrículas dos alunos.
</p>
<br>

<p align="center">
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray"/>
<img src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white"/>
</p>

<p align="center">
 <a href="#pré-requisitos">Pré Requisitos</a> •
 <a href="#instalação">Instalação</a> •
 <a href="#comandos-adicionais">Comandos adicionais</a> •
 <a href="#tecnologias">Tecnologias</a> •
 <a href="#status">status</a> •
 <a href="#funcionalidades">Funcionalidades</a> •
 <a href="#rotas">Rotas</a> •
 <a href="#informações-adicionais">Informações adicionais</a> •
 <a href="#contribuições">Autor</a>
</p>

### Pré Requisitos

- `$ python3 -m venv .venv`
- `$ source .venv/bin/activate`
- `$ pip install -r requirements.txt`

### Instalação

- `$ ./manage.py migrate`
- `$ ./manage.py createsuperuser`
- `$ ./manage.py runserver`

### Comandos adicionais

- Ao instalar novos pacotes: `$ pip freeze > requirements.txt`

### Tecnologias

- Django Rest Framework
- SQLite


### Status

- Projeto de estudos finalizado.

### Funcionalidades

- [x] Manter Aluno
- [x] Manter Curso
- [x] Manter Matrícula
- [x] Listar todos os alunos de um curso
- [x] Listar todos os cursos que um aluno está matriculado

### Rotas

- <URL_API>/alunos/
- <URL_API>/cursos/
- <URL_API>/matriculas/
- <URL_API>/alunos/<id>/matriculas/
- <URL_API>/cursos/<id>/matriculas/

### Informações adicionais

- Projeto realizado em acompanhamento ao curso: <a herf="https://cursos.alura.com.br/course/api-django-3-rest-framework">api-django-3-rest-framework</a> 

### Contribuições

<div align="center">
<img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/18218791?v=4" width="100px;" alt=""/><br /><sub><b>Marcos Souza</b></sub></a><br />
</div>