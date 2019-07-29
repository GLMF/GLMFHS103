import sys
from antlr4 import *
from glmfLexer import glmfLexer
from glmfParser import glmfParser
from glmfListener import glmfListener
from PyInquirer import prompt
from typing import Dict, Any
import argparse


OUTPUT_FILENAME = 'output.odt'


def checkChgOutput(answers : Dict[str, Any]) -> bool:
    return answers['chgOutput']


def getParametersCLI() -> Dict[str, Any]:
    widget = [
        {
            'type': 'input',
            'name': 'filename',
            'qmark': '>',
            'message': 'Saisissez le nom du fichier à convertir :'
        },
        {           
            'type': 'confirm',
            'name': 'latex',
            'qmark': '>',
            'message': 'Présence de syntaxe LaTeX ?',
            'default': False
        },
        {           
            'type': 'confirm',
            'name': 'chgOutput',
            'qmark': '>',
            'message': 'Voulez-vous changer le nom du fichier de sortie (défaut {}) ?'.format(OUTPUT_FILENAME),
            'default': False
        },
        {
            'type': 'input',
            'name': 'output',
            'qmark': '>',
            'message': 'Saisissez le nom du fichier de sortie :',
            'when': lambda answers : checkChgOutput(answers)
        }
    ]

    result = prompt(widget)
    if not result['chgOutput']:
        result['output'] = OUTPUT_FILENAME
    return result


def getParameters() -> Dict[str, Any]:
    parser = argparse.ArgumentParser(description='Outil de conversion d\'articles pour GLMF')
    parser.add_argument('filename', help='Nom du fichier à convertir')
    parser.add_argument('-l', '--latex', help='Présence de syntaxe LaTeX', action='store_true')
    parser.add_argument('-o', '--output', help='Nom du fichier de sortie ({} par défaut)'.format(OUTPUT_FILENAME), default=OUTPUT_FILENAME)
    args = parser.parse_args()
    return args.__dict__



if __name__ == '__main__':
    if len(sys.argv) == 1:
        args = getParametersCLI()
    else:
        args = getParameters()
    data = FileStream(args['filename'], encoding='utf-8')
    lexer = glmfLexer(data)
    stream = CommonTokenStream(lexer)
    parser = glmfParser(stream)
    tree = parser.article()

    glmfArticle = glmfListener(args['output'], args['latex'])
    walker = ParseTreeWalker()
    walker.walk(glmfArticle, tree)
