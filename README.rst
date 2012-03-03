SublimeAutoSemiColon
================

This plugin automatically moves a semi-colon to outside of the last bracket when pressed inside one of more pairs of brackets.

Installing
----------
**Without Git:** Download the latest source from `GitHub <http://github.com/LewisW/SublimeAutoSemiColon>`_ and copy the whole directory into the Packages directory.

**With Git:** Clone the repository in your Sublime Text 2 Packages directory, located somewhere in user's "Home" directory::

    git clone git://github.com/LewisW/SublimeAutoSemiColon.git


The "Packages" packages directory is located at:

* OS X::

    ~/Library/Application Support/Sublime Text 2/Packages/

* Linux::

    ~/.Sublime Text 2/Packages/

* Windows::

    %APPDATA%/Sublime Text 2/Packages/


Using
-----

Pressing the semi-colon in the following scenario:

function(|)

Would result in:

function();|

It does it in 2 steps, meaning that pressing ctrl + z will move the semi-colon back it its original location:

function(;|)