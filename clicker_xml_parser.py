# Clicker data XML Parser
# Matthew Antezzo
# 10/20/20

import xml.etree.ElementTree as ET
import csv

# gets the root element for an .xml file
def get_root(filename):
    tree = ET.parse(filename) # parses xml file
    root = tree.getroot() # gets root
    return root

# gets all questions (p) and returns an array of question dictionaries
def get_questions(filename):
    tree_root = get_root(filename)
    questions = []
    for p in tree_root.findall('p'):
        questions.append(p.attrib)
    return questions

# gets all student responses and question id and returns an array of
# response dictionaries
def get_responses(filename):
    tree_root = get_root(filename)
    answers = []
    for child in tree_root:
        for v in child.findall('v'):
            v_attribs = v.attrib
            v_attribs.update({'quuid' : child.attrib['quuid']})
            answers.append(v.attrib)
    return answers
