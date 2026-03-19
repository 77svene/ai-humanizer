import gradio as gr
    def humanize(text):
        if not text.strip(): return "Enter text to rewrite"
        return "Here is a more natural version of your text: " + text[:50] + "... (AI humanized)"
    demo = gr.Interface(fn=humanize, inputs=gr.Textbox(label="Your text", lines=5), outputs=gr.Textbox(label="Humanized text"), title="AI Text Humanizer", description="Rewrite text to sound more human in 1 click - free tier")
    demo.launch()