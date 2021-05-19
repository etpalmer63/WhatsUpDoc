Docs Like Code
==============


**Summary Impression**

*Docs Like Code*, is aimed at moving people from the single PDF publication
to a GitHub-webpage continuous integration/development system with 
incremental improvements and tracking. There is less focus on content and
specifics about what should be present in the docs or webpages themselves. 
In a scenario where one is coming from a coding background with an 
already established dev-style workflow for managing documentation, the
book is trying to convince the already initiated.  I would like to see 
more information on defining the audience, a style
guide or analysis of essential aspects of the webpage presentation. 





Note: I started by skipping directly to the tutorial section. 

Goals of treating docs like code:

1. `Promote collaboration`_ 
    Keep docs and code together to encourage similar treatment and importance,
2. `Get long-tail contributions`_, important contributions on esoteric topics --The small but mighty contribution. 
    Split docs into smaller parts to encourage contributions.
3. `Track issues with documentation`_
    Using bug-fix tracking, allows users to judge whether the fix is an improvement.
4. `Get better reviews`_
    Not sure about this one yet.   
5. `Make beautiful docs`_
    Create modern looking docs. (Sphinx is already up!)
6. `Use developer tools and workflows`_
    Apply dev tools and techniques, such as automated builds, to let you and
    your team focus on content. 
7. `Get value from cost-effective tools`_
    Most tools are free. 

-------------

.. _`Promote collaboration`: 
   
**Promote Collaboration**

Writing with and for your audience, you will get to know them better. 


------------

.. _`Get long-tail contributions`:

**Get Long-Tail Contribtions**

By splitting up documentation into many small tasks and plain text, 
the barrier to contribution is lowered. This encourages those who 
may have put a lot of effort into figuring out a specific topic
to contribute to the documentation, such as specialist with 
technical details. These contributions likely 
have higher value because main/general topics and usually already covered
well. 


------------

.. _`Track issues with documentation`:

**Track Issues with Documenation**

By using a bug--fix approach to improving documentation, errors or
less useful documentation is identified for improvements that can be
directly compared. This also allows you to show incremental improvements 
over time. Improvements could be fixing errors and typos, or even 
feature requests for the docs themselves. 


--------------

.. _`Get better reviews`:

**Get Better Reviews**

In comparison to the single pdf sign-off, treating docs like code
allows reviewers to see and easily compare changes. The incremental
improvements approach also means more smaller reviews. 

It turns out GitHub is great for incremental improvement to lots of
things!

---------------

.. _`Make beautiful docs`:

**Make Beautiful Docs**

Great doc themes are clean, useful and helpful in organizing the 
docs. The Read the Docs theme is often referred to as a 
"gold standard." 


--------------

.. _`Use developer tools and workflows`:

**Use Developer Tools and Workflows**

Automate builds, run simple tests to ensure quality. Continuous 
building with tests can ensure docs are published correctly
so that contributors can focus on content. 

Speed matters and docs must keep up.



--------------

.. _`Get value from cost-effective tools`:

**Get Value From Cost-Effective Tools**

GitHub, vim, python, Sphinx, these things are all free. Html
hosting can be done cost effectively.

-------------


Workflows
---------

Docs are in the code repo and are published together with code updates.
|:arrow_right:| use dev workflow.

How will you publish? i.e. When to :code:`make html`?

Local previews seem the most convenient. 

Content
-------

How will you make it easy and efficient for contributors to author content. 
In my case, I believe nothing beats a good text editor. Also considering the
audience, the closer to the development environment the better. 

Automate Builds
---------------

For docs, continuous integration and development means docs are tested, merged 
and deployed with each patch. 


