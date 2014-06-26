# CRUD básico usando Django 1.4 e Twitter Bootstrap.

1) Use o virtualenvwrapper para gerenciar os seus ambientes:
http://www.doughellmann.com/projects/virtualenvwrapper/

Para entender um pouco mais sobre virtualenv, pip e pacotes Python:
http://hltbra.blogspot.com.br/2010/05/gerenciando-ambientes-virtuais-e.html

2) Para o projeto funcionar, após as configuração do virtualenv, instalação do pip e criação de um ambiente,
instale o Django e o South:

	pip install django==1.4.1

	pip install south

3) E para os forms ficarem com as caracteristicas de validação do bootstrap instale o django-bootstrap-toolkit

	pip install django-bootstrap-toolkit

github do projeto: https://github.com/dyve/django-bootstrap-toolkit

Após as instalações, realize a criação da base de dados:
  
	python manage.py syncdb

Para visualizar o projeto no browser execute o comando para iniciar o servidor do django e então acesse localhost:8000:

	python manage.py runserver

Para conseguir fazer um cadastro será necessária a existência de uma profissão. Acesse a área administrativa em
localhost:8000/admin e então cadastre uma profissão.

