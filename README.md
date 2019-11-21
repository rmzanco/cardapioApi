# cardapioApi
Programa em Python, utilizando Requests, que mostra o cardápio diario no RU dos campus de Limeira.
### Bibliotecas Utilizadas:
- requests
- re
- html
- datetime
- rdflib
### Objetivo do programa:

Executar uma consulta para verificar se a quantidade calórica de um prato está correta.
Verificar o cardápio do Restaurante Universitário através de uma data selecionada.

**Queries**

O programa conta com duas queries:
- A primeira query é basicamente uma tabela de consulta de todos os alimentos contidos no RDF;
- A segunda query é composta de alimentos apenas de um cardápio desejado e é composta de um cálculo de calorias, para verificar se o prato contém uma quantidade de calorias adequada.

**RDF**

O RDF foi feito manualmente baseado nos critérios de cada alimento, e cada alimento registrado possui 7 atributos:

- rdfs:label -> nome do alimento;
- ru:typefood -> Atributo para especificar o tipo de alimento (se é um vegetal, se é um tipo de carne);
- ru:cardapio -> Atributo para especificar de qual tipo de cardápio ele é inserido (convencional, vegetariano ou ambos);
- ru:ruKind -> Atributo para especificar em qual prato ele é inserido no cardápio (por exemplo: prato principal);
- ru:calorias -> Atributo para especificar a quantidade de calorias em um prato;
- food:ingredients -> Quais ingredientes compõem aquele alimento;
- dc:description -> descrição do alimento.

O Arquivo possui 56 triplas.

**Fontes utilizadas**

https://fdc.nal.usda.gov/index.html - Calorias

https://www.sar.unicamp.br/RU/view/site/cardapio.php - Cardápio do RU

http://www.w3.org/TR/2003/PR-owl-guide-20031209/food# - RDF Base de alimentos.
