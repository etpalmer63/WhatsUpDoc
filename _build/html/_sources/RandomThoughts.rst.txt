.. include:: <isonum.txt>

Random Thoughts
===============

What goes here?


Spellcheck
----------

For spellchecking documents, the command line tool Aspell works well. Use:

.. code-block:: 

   aspell -c <filename>

Only one file name can be specified at a time. Therefore, a bash script
will be needed to loop through the files. 

It's also possible to add your own dictionary, see man aspell. 


Robot Proofreader
-----------------
   
For proofreading ChromeVox. However, it can get tedious quickly. I wish
it had a more accessible on/off button. 



Content and Feedback
--------------------

Addressing questions:

1. How to learn the information I need without taking the time of 
   engineers who write the code?
2. How to generate feedback from users without taking their time
   and effort? 


Collect information from online discussion forum and chats. Develop
a system of categorizing this information (sounds like an ML problem!).
Use these categories to identify areas of the documentation that need
additional attention. 

What's the best way to do this? 

Would need to save a collection of cut and pasted text files. Some will
be a chat between two people, some may be chats between multiple people. 
Also, forwarded and direct emails would need to be included. 


Feedback:

Encourage people to use GitHub's bug tracker for question, 
feedback and improvements. This way questions can be tracked and
documentation can be tailored.






Code Testing For Docs
---------------------

To learn more about Github's automated testing, new features are coming:

* auto spellcheck using custom dictionary
* code compile test 
* auto html build

|:+1:| Recently added GitHub workflows to test build upon push to main. 


Things Each Page Should Include
-------------------------------

A list of the most relevant files which are covered by the documentation.
A date when that documentation was last updated.
Feedback: A Thumbs Up/Down, Comment thing. -- What's the easiest way to 
do this?


*Feedback* |rarr|  Methods for automatically tracking? Are page views enough. Would it 
be helpful to know where people start. Or is number of views enough. 



Feedback_

.. _Feedback: https://github.com/etpalmer63/WhatsUpDoc/issues/new





