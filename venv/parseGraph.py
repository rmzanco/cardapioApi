from rdflib import Graph ;
g = Graph();
filename = "cardapioRuRdfPrototype.ttl"
g.parse(filename, format='turtle');
print(filename, 'tem', len(g), 'triplas')

for s,p,o in g:
    print(s, ":", p, ":", o)