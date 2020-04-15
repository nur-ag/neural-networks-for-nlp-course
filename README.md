# Neural Networks for Natural Language Processing: A Primer

This is a free, interactive, Jupyter notebook-based course for the Software Engineers of the world
that want to get their feet wet with the fancy world of Neural Networks. The focus is simple: learn
the basics of how to build your own neural networks, starting from the algebra that defines the
forward pass in a simple perceptron to advanced architectures line Recurrent and Convolutional
Neural nets. Everything is explained in plain, simple, corny English, with the objective of getting
you to be able to understand how to roll your own.

The aim of the course is not to teach theory: I will not delve into the details about optimization,
gradient descent, or esoteric beliefs about why Neural Networks work. There is no need for that —
Neural Networks are very fun on their own! The course is meant to be a first stepping stone for
seeing how to build code that implements, trains and evaluates Neural Networks. 

This is all done with the frame of reference of Natural Language Processing. Whether you work in
banking, ecommerce or study social trends, text is everywhere. This course focuses on the direct
ways you can perform text classification with Neural Networks, so that you can identify sentiment
of user reviews of your products or identify types of documents.

# Installation

All of the course will be presented using Python as our programming language. We will be using the
following libraries:

* NumPy
* SciPy
* Scikit-Learn
* Matplotlib
* Keras (on any backend, though we will assume Tensorflow)
* Jupyter (for the interactive notebooks)

A bash script is provided alongside with the course material to perform the installation on Linux
or Mac OS. Running:

>  `./install.sh`

Should install all the necessary packages and contents. It might be a good idea to first create a
virtual environment. If you want to install all necessary libraries on Windows, provided you have
python installed and in your path, simply run the following command on the command prompt:

>  `python -m pip install -r requirements.txt`

You will need to extract the embedding files in the `Embeddings/` folder. Additionally, to work 
with the Jupyter notebooks provided for the course, you will need to get familiar with the 
following commands:

>  `jupyter notebook` — which starts the jupyter interface.

>  `jupyter nbextension enable --py --sys-prefix widgetsnbextension` — which enables interactive widgets and only needs to be ran once.

# Course Structure

The course is divided in 4 lessons, which as good programmers start from 0. Those are:

0. Introduction
1. Neural Networks 101
2. Natural Language on Neural Networks
3. Convolutional and Recurrent Neural Networks

Each lesson is complimented with a slide deck giving an overview of what the lesson will entail. 
In any case, the lessons can be followed at your own pace: they are Jupyter notebooks that mingle
an introduction to the algebra needed to build Neural Networks or a description of a specific
network architecture with code examples. 

Peppered through the lessons, you will also find inline widgets that let you experiment with
geometric primitives to intuitively grasp the algebra, or toy around with Network hyper-parameters.
Additionally, lessons include little brain teasers for you to figure out, so that you can test
yourself as you go.

Finally, if you feel ready when you are done with the course, you might want to take on a
challenge! In the `Projects/` folder you will find a small project for multi-label classification
using data from the Cooking StackExchange. How good can your model get? 

# Contributions

I will be more than happy to accomodate improvements to the explanations, additional projects,
fixes, updates, help and any kinds of comments. That is, unless I have no time to do it.

# License

MIT — Please read LICENSE.md for details.

# Who?

I am Nur. If you enjoyed the course or totally hated it, perhaps you will want to direct some
messages my way. I can be reached through the contact form at [nur.wtf](https://nur.wtf/).
