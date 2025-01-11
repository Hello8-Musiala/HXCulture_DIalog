import gradio as gr

with gr.Blocks() as demo:
   gr.Image(interactive=True)
   gr.Image(interactive=False)

demo.launch(share=True)