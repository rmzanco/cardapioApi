from rdflib import Graph ;
g = Graph();
filename = "cardapioRuRdfPrototype.ttl"
g.parse(filename, format='turtle');
g.bind('ru', 'http://www.sar.unicamp.br/RU/view/site/cardapio.php#')
ans = g.query(
    """
        SELECT ?food ?desc ?kcal
        WHERE{ 
        
        ?a rdfs:label ?food .
        ?a dc:description ?desc .
        ?a ru:calorias ?kcal .
               
        } """
)

totalkcal = 0
for row in ans:
    print("nome do alimento: ", row.food)
    print("descricao: ",        row.desc)
    print("calorias: ",         row.kcal + " kcal")
