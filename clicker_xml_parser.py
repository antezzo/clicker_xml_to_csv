# Clicker data XML Parser

import xml.etree.ElementTree as ET
import csv

def get_root(filename):
    tree = ET.parse(filename) # parses xml file
    root = tree.getroot() # gets root
    return root

def get_questions(filename):
    tree_root = get_root(filename)
    questions = []
    for p in tree_root.findall('p'):
        questions.append(p.attrib)
    return questions

def get_responses(filename):
    tree_root = get_root(filename)
    answers = []
    for child in tree_root:
        for v in child.findall('v'):
            v_attribs = v.attrib
            v_attribs.update({'quuid' : child.attrib['quuid']})
            answers.append(v.attrib)
    return answers
