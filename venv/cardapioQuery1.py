from rdflib import Graph ;
g = Graph();
filename = "cardapioRuRdfPrototype.ttl"
g.parse(filename, format='turtle');
g.bind('ru', 'http://www.sar.unicamp.br/RU/view/site/cardapio.php#')
ans = g.query(
    """
        SELECT ?food ?desc
        WHERE{ 
        
        ?a rdfs:label ?food .
        ?a dc:description ?desc .
               
        }"""
)
for row in ans:
    print("nome do alimento: ", row.food)
    print("descricao: ",        row.desc)