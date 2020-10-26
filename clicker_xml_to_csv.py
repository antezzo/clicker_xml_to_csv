# Clicker data XML to CSV converter
# Matthew Antezzo
# 10/20/20
#
# usage: clicker_xml_to_csv.py -i <input_directory> -o <output_directory>

import os, sys, getopt, csv
from pathlib import Path
import clicker_xml_parser
from attr_parser import parse_attr
# gets arguments from command line and prints usage
def main(argv):
    input_dir = ''
    output_dir = ''
    try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print('usage: clicker_xml_to_csv.py -i <input_directory> -o <output_directory>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('usage: clicker_xml_to_csv.py -i <input_directory> -o <output_directory>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            input_dir = arg
        elif opt in ("-o", "--ofile"):
            output_dir = arg
    if input_dir == '' or output_dir == '':
        print('usage: clicker_xml_to_csv.py -i <input_directory> -o <output_directory>')
        sys.exit(2)
    if input_dir[-1] != '/':
        input_dir += '/'
    if output_dir[-1] != '/':
        output_dir += '/'
    return input_dir, output_dir

# writes a dictionary value set to .csv
def write_vals_to_csv(xml_list, filename):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = list(xml_list[0][0])
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        #write header
        writer.writerow(parse_attr(fieldnames))
        for vals in xml_list: 
            for entry in vals:
                writer.writerow(entry)

if __name__ == "__main__":
    input_dir, output_dir = main(sys.argv[1:])

    p = Path(output_dir)
    p.mkdir(exist_ok=True)

    # scans input directory for .xml files and converts their data to two separate .csv files:
    # filename-responses.csv: all responses to every question (with question ids)
    # filename-questions.csv: all questions in the session
    with os.scandir(input_dir) as entries:
        question_objects = []
        response_objects = []
        for entry in entries:
            if entry.name[-4:] == '.xml':
                response_objects.append(clicker_xml_parser.get_responses(input_dir + entry.name))
                question_objects.append(clicker_xml_parser.get_questions(input_dir + entry.name))            
        
        responses_output_file = output_dir + 'responses.csv'
        questions_output_file = output_dir + 'questions.csv'
        write_vals_to_csv(response_objects, responses_output_file)
        write_vals_to_csv(question_objects, questions_output_file)