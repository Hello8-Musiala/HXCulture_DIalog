
from typing import List, Dict

from lang_chain.client.client_factory import ClientFactory

_PROMPT_ = "请从上述对话中帮我提取出文生视频所对应的文本内容"


def __construct_messages(question: str, history: List[List | None]) -> List[Dict[str, str]]:
    messages = [
        {"role": "system", "content": "你现在扮演信息抽取的角色，要求根据用户输入和AI的回答，正确提取出信息，无需包含提示文字"}]

    for user_input, ai_response in history:
        messages.append({"role": "user", "content": user_input})
        messages.append(
            {"role": "assistant", "content": repr(ai_response)})

    messages.append({"role": "user", "content": question})
    messages.append({"role": "user", "content": _PROMPT_})

    return messages


def extract_text(question: str,
                 history: List[List | None] | None = None) -> str:
    messages = __construct_messages(question, history if history else [])
    result = ClientFactory().get_client().chat_using_messages(messages)

    return result
