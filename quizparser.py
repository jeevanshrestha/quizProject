
import xml.sax
from quiz import *
from enum import Enum, unique


@unique
class QuizParserState(Enum):
    IDLE = 0
    PARSE_QUIZ =1
    PARSE_DESCRIPTION = 2
    PARSE_QUESTION = 3
    PARSE_