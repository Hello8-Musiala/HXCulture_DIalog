import os

import gradio as gr

from config.config import Config
from env import get_app_root
from qa.bot import ChatBot

__AVATAR = (os.path.join(get_app_root(), "resource/avatar/musiala.png"),
            os.path.join(get_app_root(), "resource/avatar/roben.png"))


def run_webui():
    chat_app = gr.ChatInterface(
        ChatBot().chat,
        chatbot=gr.Chatbot(height=400, avatar_images=__AVATAR),
        textbox=gr.Textbox(placeholder="请输入你的问题", container=False, scale=7),
        title="「遇见湖南」📒",
        description="你可以问关于湖南文化的一切",
        theme="default",
        examples=["您好", "C罗是球王吗", "雷锋是谁", "刘少奇会写代码吗", "请生成雷锋的图片",
                   "用语音介绍雷锋", "请用广东话给我发语音"],
        cache_examples=False,
        retry_btn=None,
        submit_btn="发送",
        stop_btn="停止",
        undo_btn="删除当前",
        clear_btn="清除所有",
        concurrency_limit=4,
    )

    chat_app.launch(server_name="0.0.0.0"
                    , server_port=int(Config.get_instance().get_with_nested_params("server", "ui_port"))
                    , share=Config.get_instance().get_with_nested_params("server", "ui_share")
                    , max_threads=10)


if __name__ == "__main__":
    run_webui()
