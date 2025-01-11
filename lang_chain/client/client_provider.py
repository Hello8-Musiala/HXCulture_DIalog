# -*- coding: utf-8 -*-
# @Time    : 2024/6/17 13:02
# @Author  : hello8
# @FileName: client_provider.py
# @Software: VSCode
# @Affiliation: hunnu.edu.cn
from enum import Enum


class ClientProvider(Enum):
    """
    used to distinguish the client provider
    """

    UNKNOWN = None
    ZHIPU = "zhipu"
    BAICHUAN = "baichuan"
    QWEN = "qwen"
    MOONSHOT = "moonshot"
    LINGYIWANWU = "lingyiwanwu"
    DEEPSEEK = "deepseek"
    DOUBAO = "doubao"
    OLLAMA = "ollama"
    ANYAPI = "anyapi"

