# -*- coding: utf-8 -*-
# @Time    : 2024/6/17 10:06
# @Author  : hello8
# @FileName: client.py
# @Software: VSCode
# @Affiliation: hunnu.edu.cn
from lang_chain.client.llm_client_generic import LLMClientGeneric


class AnyAPIClient(LLMClientGeneric):
    """
    ANYAPI AI Client
    """
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)

