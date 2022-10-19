# -*- coding: utf-8 -*-
"""Task06.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hDWrt7r8eQEVrpHqFk1W7kyCmnwl2JDf

**Task 06: Modifying RDF(s)**
"""

!pip install rdflib 
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2021-2022/master/Assignment4/course_materials"

"""Leemos el fichero RDF de la forma que lo hemos venido haciendo"""

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
# Create a Graph
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

g.add((ns.University, RDF.type, RDFS.Class))

# Visualize the results
for s, p, o in g:
  print(s,p,o)

"""**TASK 6.2: Add "Researcher" as a subclass of "Person"**"""

# A researcher is a person
g.add((ns.Researcher, RDFS.subClassOf, ns.Person))

# Visualize the results
for s, p, o in g:
  print(s,p,o)

"""**TASK 6.3: Create a new individual of Researcher named "Jane Smith"**"""

# Jane Smith is a researcher
g.add((ns.JaneSmith, RDF.type, ns.Researcher))

# Visualize the results
for s, p, o in g:
  print(s,p,o)

"""**TASK 6.4: Add to the individual JaneSmith the fullName, given and family names**"""

# TO DO
vcard = Namespace("http://www.w3.org/2001/vcard-rdf/3.0/")
# Jane's fullname is Jane Smith
g.add((ns.JaneSmith, vcard.FN, Literal("Jane Smith")))
# Jane Smith's given name is Jane
g.add((ns.JaneSmith, vcard.Given, Literal("Jane")))
# Jane's family name is Smith
g.add((ns.JaneSmith, vcard.Family, Literal("Smith")))

# Visualize the results
for s, p, o in g:
  print(s,p,o)

"""**TASK 6.5: Add UPM as the university where John Smith works**"""

# UPM is a university
g.add((ns.UPM, RDF.type, ns.University))

# John Smith works for UPM
g.add((ns.JohnSmith, vcard.works_for, ns.UPM))

# Visualize the results
for s, p, o in g:
  print(s,p,o)
