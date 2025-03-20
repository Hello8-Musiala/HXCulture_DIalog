import os

import gradio as gr

from config.config import Config
from env import get_app_root
from qa.bot import ChatBot

__AVATAR = (os.path.join(get_app_root(), "resource/avatar/user.png"),
            os.path.join(get_app_root(), "resource/avatar/bot.png"))


def run_webui():
    chat_app = gr.ChatInterface(
        ChatBot().chat,
        chatbot=gr.Chatbot(height=400, avatar_images=__AVATAR),
        textbox=gr.Textbox(placeholder="请输入你的问题", container=False, scale=7),
        title="「遇见湖南」📒",
        description="你可以咨询关于湖湘文化的一切",
        theme="default",
        examples=["您好", "彭德怀出生于哪一天", "雷锋是谁", "刘少奇和毛泽东的关系",
"用语音介绍雷锋", "请用广东话给我发语音"],
        cache_examples=False,
        retry_btn=None,
        submit_btn="发送 🚀",
        stop_btn="停止 ✋",
        undo_btn="撤回 🔄",
        clear_btn="清除所有",
        concurrency_limit=4,
    )

    try:
        server_port = int(Config.get_instance().get_with_nested_params("server", "ui_port"))
        share = Config.get_instance().get_with_nested_params("server", "ui_share")
    except Exception as e:
        print(f"Error loading server configuration: {e}")
        return

    chat_app.launch(server_name="0.0.0.0", server_port=server_port, share=share, max_threads=10)


if __name__ == "__main__":
    run_webui()
