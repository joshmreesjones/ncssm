FreeStream
==========

Overview
--------
A music streaming application written in Java that plays from SoundCloud, Jamendo, FreeMusicArchive, LastFM, and BandCamp. This project is unfinished.

How to run FreeStream
---------------------
There are three ways to run FreeStream.

1. Use `ant`: if you don't have ant, [install it](http://ant.apache.org/manual/install.html), then simply navigate to the root directory (containing build.xml) and run `ant`. Ant will read from `build.xml` and compile, jar, and run FreeStream.
2. Run the precompiled jar: instead of recompiling, you can navigate to the root directory and run the precompiled JAR with `java -jar dist/FreeStream.jar`.
3. Manually compile everything: don't do this. Seriously. But if you really want to, all the source files are in `src/edu/ncssm/cs/freestream` and should be compiled to `/bin/edu/ncssm/cs/freestream`. Note that FreeStream depends on a number of libraries, all JARs located in `lib`.

Notes
-----
- This project was a final project for Data Structures 1 at NCSSM.
- `count` counts the number of lines in the project.
