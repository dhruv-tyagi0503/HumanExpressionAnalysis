# AUTOGENERATED! DO NOT EDIT! File to edit: ../app.ipynb.

# %% auto 0
__all__ = ['temp', 'lear', 'categories', 'image', 'label', 'examples', 'intf', 'classify_image']

# %% ../app.ipynb 2
%pip install -q gradio

# %% ../app.ipynb 4
%pip install -Uqq fastai fastbook

# %% ../app.ipynb 5
from fastai.vision.all import *
import gradio as gr

# %% ../app.ipynb 7
import pathlib
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

# %% ../app.ipynb 8
lear=load_learner('humansenti.pkl')

# %% ../app.ipynb 10
categories=('angry','happy','sad','stressed')
def classify_image(img):
    pred,idx,probs=lear.predict(img)
    return dict(zip(categories,map(float,probs)))


# %% ../app.ipynb 15
image=gr.Image()
label=gr.Label()
examples=['happy.jpg','sad.jpg']
intf=gr.Interface(fn=classify_image,inputs=[image],outputs=label, examples=examples)
intf.launch(inline=False)
