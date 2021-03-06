The Product is Docs
===================

My general impression of the book so far is that it offers a lot of specific information on a variety of useful topics. However, like the docs it talks about, it is not linear. 


*comprehensive* vs. *relevant*  seems like an enlightening guiding principal for writing to different audiences. -> Where to put the needle for which audience?

regular customer feedback loop. How to generate this? What about 'is this page useful? comment here.'

waterfall - linear approach to project management. (linear is a much better name)
SME - subject matter experts 

How to avoid always trailing? Ask people to write some documentation before they start work on a new feature? 

Ideas: 

* What are the software's core principals? What is the sell to users for why should they use the software and what principles they are adopting when they do. 
* What is considered successful documentation? 


Documentation value, create and track consistent naming conventions. 

.. image:: doc_process.jpg
   :height: 100px
   

**Audience**

Identify Users':

#. goals
#. problems they want to solve
#. decisions they need to make
#. things they want to build 

*Audience Types versus Personas*

A persona is a specific instance of an audience type.  

**Customer Feedback**

*Community*

GitHub already allows users to have discussions and aid each other. 

**Documentation Decisions**

What is your documentation ethos? 
In this case, I would say that contributors should write the documentation in a way that would be clear to their group leader. Technical and in-house jargon is OK. I think of it as my place to figure out how to relate this to the more general audience. Also a main consideration, is how much time and effort it would take to write for a different audience. 

**Learning Objectives**


--------

Measuring Success
-----------------

According to Douglas Hubbard:

    The purpose of measurement is to reduce uncertainty so that you can
    make a decision based on the results. Measurement is not about precise 
    counting, instead it is about supporting a business decision.

    The "Rule of Five" states that there is a 93.75% chance that the 
    median of a population is between the smallest and largest values 
    in any random sample of five from that population. 

For the record, I'm skeptical about that statement since it would
be so easy to pick a skewed subset. It seems in practice the key is 
how the five are selected.

Looking at something quickly online, I update my skepticism. Based on,  
https://www.r-bloggers.com/2014/11/simulating-the-rule-of-five/,
their mathematical argument shows that the median is within
the range of the 5 values samples. Consider the chance of picking
above or below the median. What is the chance that you would
pick above the median 5 times in a row?

The assumption is that the underlying distribution is normal. This
would correspond with situations where there is one right answer,
say a single consensus solution. 
It would not make much sense for a situation in which respondents 
clearly separate into groups, i.e. a bimodal or multimodal distribution.

What Does Success Mean?
-----------------------

According to Mark Baker, author of *Every Page is Page One*: 

    Mean time to productivity is the only true measurement of whether 
    documentation is successful.

The true purpose of your documentation is to educate your customer
about how to use the product. The faster your documentation makes 
yours customers productive, the more successful it is.

The classical metric for the success of documentation is support
case deflection. Unfortunately, support case deflection is a 
difficult metric to capture because it involves measuring the
absence of action. 
