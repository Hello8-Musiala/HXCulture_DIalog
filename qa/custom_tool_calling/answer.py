
from typing import Tuple, List, Any

from qa.custom_tool_calling.function_tool import map_question_to_function, map_question_to_function_args

from qa.custom_tool_calling.question_parser import parse_question, check_entity, QuestionType


def get_answer(question: str,
               history: List[List | None] = None) -> (
        Tuple[Any, QuestionType]):
    """
    根据问题获取答案或者完成任务
    :param history:
    :param question:
    :return:
    """
    question_type = parse_question(question)
    entities = check_entity(question)

    function = map_question_to_function(question_type)
    args_getter = map_question_to_function_args(question_type)
    args = args_getter([question_type, question, history, entities])

    result = function(*args)
    if not result:
        function = map_question_to_function(QuestionType.UNKNOWN)
        args_getter = map_question_to_function_args(QuestionType.UNKNOWN)
        args = args_getter([question_type, question, history, entities])
        result = function(*args)

    return result
