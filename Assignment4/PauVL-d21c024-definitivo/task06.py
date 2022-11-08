# -*- coding: utf-8 -*-
"""Copia de Task06.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1K91oe9w4PtXsZGFGoTpj1FWoq9AC3Eh6

**Task 06: Modifying RDF(s)**
"""

#!pip install rdflib
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2021-2022/master/Assignment4/course_materials"

"""Leemos el fichero RDF de la forma que lo hemos venido haciendo"""

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example5.rdf", format="xml")

"""Create a new class named Researcher"""

ns = Namespace("http://somewhere#")
g.add((ns.Researcher, RDF.type, RDFS.Class))
for s, p, o in g:
  print(s,p,o)

"""**TASK 6.1: Create a new class named "University"**

"""

print("Creamos una nueva clase llamada \"University\"")
g.add((ns.University, RDF.type, RDFS.Class))
for s, p, o in g:
  print(s,p,o)

"""**TASK 6.2: Add "Researcher" as a subclass of "Person"**"""

print("Añadimos Researcher como subclase de Person")
g.add((ns.Researcher, RDFS.subClassOf, ns.Person))
for s, p, o in g:
  print(s,p,o)

"""**TASK 6.3: Create a new individual of Researcher named "Jane Smith"**"""

print("Create a new individual of Researcher named \"Jane Smith\" ")
vcard_rdf = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")
from rdflib import XSD
resource = (ns.JaneSmith,RDF.type,ns.Researcher)
g.add(resource)
for s, p, o in g:
  print(s,p,o)

"""**TASK 6.4: Add to the individual JaneSmith the fullName, given and family names**"""

print("Add to the individual JaneSmith the fullName, given and family names")
resource = (ns.JaneSmith,vcard_rdf.FN,Literal('Jane Smith', datatype=XSD.string))
g.add(resource)
resource = (ns.JaneSmith,vcard_rdf.Family,Literal('Smith', datatype=XSD.string))
g.add(resource)
resource = (ns.JaneSmith,vcard_rdf.Given,Literal('Jane', datatype=XSD.string))
g.add(resource)
for s, p, o in g:
  print(s,p,o)

"""**TASK 6.5: Add UPM as the university where John Smith works**"""

print("Add UPM as the university where John Smith works")
# Creamos una nueva propiedad en un dominio mío, por ejemplo:
pl = Namespace("http://paulaVelasco#")
g.namespace_manager.bind('pl', pl, override=False)
# y la usamos para asociar la persona a la universidad
#pl:Works a rdfs:Property
resource = (pl.Works,RDF.type,RDF.Property)
g.add(resource)

#pl:Works rdfs:range ns:University
resource = (pl.Works,RDFS.range,ns.University)
g.add(resource)

#pl:Works rdfs:domain ns:Person
resource = (pl.Works,RDFS.domain,ns.Person)
g.add(resource)

#ns.UPM RDF.type ns.University
resource = (ns.UPM, RDF.type, ns.University)
g.add(resource)

#ns:JohnSmith vcard_rdf:Works ns:UPM
resource = (ns.JohnSmith,pl.Works,ns.UPM)
g.add(resource)

for s, p, o in g:
  print(s,p,o)