from rdflib import Graph;

tipo = input("Selecione o tipo de cardápio (convencional/vegetariano): ")


g = Graph();
filename = "cardapioRuRdfPrototype.ttl"
g.parse(filename, format='turtle');
g.bind('ru', 'http://www.sar.unicamp.br/RU/view/site/cardapio.php#')
ans = g.query(
    """
        SELECT ?type ?food ?desc ?kcal
        WHERE{ 

        ?a rdfs:label ?food .
        ?a dc:description ?desc .
        ?a ru:calorias ?kcal .
        ?a ru:cardapio ?type
        FILTER regex(?type, "both", "i")
        } 
    """
)

ans2 = g.query(
    """
           SELECT ?type ?food ?desc ?kcal
           WHERE{ 
    
           ?a rdfs:label ?food .
           ?a dc:description ?desc .
           ?a ru:calorias ?kcal .
           ?a ru:cardapio ?type
           FILTER regex(?type, """ + "\"" + tipo + "\"" + """ , "i")
           } 
       """
)

totalkcal = 0
for row in ans:

    print("nome do alimento: ", row.food)
    print("descricao: ", row.desc)
    print("calorias: ", row.kcal + " kcal")
    intKcal = float(row.kcal)
    totalkcal = totalkcal + intKcal

for row in ans2:
    print("nome do alimento: ", row.food)
    print("descricao: ", row.desc)
    print("calorias: ", row.kcal + " kcal")
    intKcal = float(row.kcal)
    totalkcal = totalkcal + intKcal

print("-------------------------------------------------------------")
strTotal = str(totalkcal)
print("total de Calorias nessa refeição: " + strTotal + " kcal")
if (totalkcal > 550) and (totalkcal < 700):
    print("Quantidade calórica ideal para um prato de comida")