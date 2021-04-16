# Artifact for Well-Typed Programs Can Go Wrong: A Study of Typing-Related Bugs in JVM Compilers

This is the artifact for the paper titled
"Well-Typed Programs Can Go Wrong:
A Study of Typing-Related Bugs in JVM Compilers".

An archived version of the artifact will also be published on Zenodo,
upon this paper's publication.

# Overview

The artifact contains the dataset and scripts to re-compute the results
described in our paper. The artifact has the following structure:

* `scripts`: This is the directory that contains the scripts needed to
reproduce the results presented in our paper.
* `scripts/fetch`: This is the directory that contains the scripts needed to
download the initial dataset described in our paper (Phase 1 and Phase 2).
* `categorization`: A python DSL language used to categorize the analyzed bugs.
For more information see `categorization/README.md`.
* `data`: This is dataset of 320 typing-related bugs.
* `data/bugs.json`: Contains all 320 bugs of our study. Each bug has the
following fields:
    * `language`: The language of the compiler.
    * `compiler`: The compiler in which the bug occurred.
    * `is_correct`: `True` if the bug-revealing test case is compilable;
       `False` otherwise.
    * `symptom`: The symptom of this bug.
    * `pattern`: The category of this bug.
    * `root_cause`: The cause that introduced this bug.
    * `chars`: The characteristics of the test case that trigger the bug.
* `data/characteristics.json`: The categories and the sub-categories of
the characteristics that trigger the bugs in our dataset.
* `data/{groovy,java,kotlin,scala}.json`: Data about the timestamp,
the reporter, the assignee, and the number of comments for each bug.
* `data/diffs/{groovy,java,kotlin,scala}/bug_id/*.diff`: The revision of the bug fix.
* `data/diffs/{groovy,java,kotlin,scala}/bug_id/stats.csv`: The LoC of the bug fix.
* `data/test_cases/{groovy,java,kotlin,scala}/bug_id/*.{kt,java,scala,groovy}`:
The test case of the fix.
* `data/test_cases/{groovy,java,kotlin,scala}/bug_id/stats.json`:
Statistics on the bug fix (number of declarations, method/function calls, LoCs).
* `data/iterations/1/{groovy,java,kotlin,scala}.txt`: Bugs analyzed in each
iteration. Each line contains two entries (comma separated):
(1) the URL pointing to the bug report,
and (2) the URL pointing to the fix of the bugs.
* `data/collection`: Phase 2 dataset (4.153 bugs).

# Requirements

* A Unix-like operating system (tested on Ubuntu and Debian).

* An installation of Python3

* An installation of Docker

* At least 20GB of available disk space

# Getting Started

## Setup

There are two ways to reproduce the results of the paper.
If you are in an Ubuntu/Debian OS,
we provide the instructions for installing the necessary
apt packages and libraries.
Otherwise if you do not own an Ubuntu/Debian environment,
this artifact also provides a Docker image 
that offers the required setup
for executing the scripts and reproducing the results of our paper.

#### Ubuntu/Debian

**NOTE**: If you do not run an Ubuntu/Debian OS, please jump to the
Section "Installing Docker Image".

You need to install some `apt` packages and some Python packages to run the
experiments of this artifact.
First, download the following packages using `apt`.

```bash
apt install curl jq git mercurial diffstat cloc
```

You also need to install some Python packages.
In a Python virtualenv run the following:

```bash
virtualenv .env
source .env/bin/activate
pip install requests matplotlib pandas seaborn
```

#### Installing Docker Image

To build the Docker image from source,
run the following command (estimated running time: ~3 min)

```bash
docker build . -t bug-study
```

Run the following command to create a new container.

```bash
docker run -it \
    -v $(pwd)/scripts:/home/scripts \
    -v $(pwd)/downloads:/home/downloads \
    -v $(pwd)/data:/home/data \
    -v $(pwd)/figures:/home/figures \
    bug-study /bin/bash
```

After executing the command, you will be able to enter the home directory
(i.e., `/home`). This directory contains
(1) the scripts for reproducing the results of the paper (see `scripts/`),
(2) the data of our bug study (see `data/`),
(3) a dedicated directory for storing the generated figures (see `figures/`),
and (4) `downloads/` which is the directory where the data of Phase 1 and
Phase 2 will be saved if you decide to get the initial data from their sources.

Some further explanations:

The option `-v` is used to mount a local volume inside the Docker container.
This option is used to mount data from this repository
inside the Docker container,
to store the figures produced from the scripts in `$(pwd)/figures`.

## Download the bugs and fixes from sources

**NOTE 1:**
To complete this step,
you need to obtain a Github access token
(see [here](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token)) so that
you are able to interact with the Github API.
Once you obtain it,
please assign it to a shell variable named `GH_TOKEN`.

```bash
export GH_TOKEN=<your Github access token>
```

**NOTE 2:** Before executing this step,
please also ensure that you have at least 20GB of available disk space.

The following script applies our bug collection approach.
Specifically,
it searches over the issue trackers of the examined compilers
and retrieves fixed typing-related bugs that meet our search criteria
as described in Section 2.1 of our paper.
Then,
it runs the `Phase 2` of our bug collection approach to filter out bugs
without any explicit fix or a test case.
At this point, we should note that the generated dataset will probably
contain more bugs than the dataset described in the paper (see Table 1),
because new bugs will have been fixed from the time we downloaded
the bugs until now.

* Download the data (~18 hours).

```bash
./scripts/fetch/fetch.sh downloads $GH_TOKEN
```

The command above executes six scripts.
The first five scripts compose the `Phase 1` of our bug collection approach,
while the 6th script stands for the `Phase 2` of our approach.
In the following,
the shell variable `$DOWNLOADS` corresponds to the `downloads/` directory,
which is passed as an argument of the first command
(`scripts/fetch/fetch.sh`).


### 1. Fetch Groovy bugs

```bash
python scripts/fetch/fetch_groovy_bugs.py $DOWNLOADS/bugs/groovy.txt \
        $DOWNLOADS/bugs/fixes/descriptions/groovy $DOWNLOADS/bugs/groovy.json
```

This script fetches `groovyc` bugs
using the Jira REST API
(see <https://issues.apache.org/jira/rest/api>).
It saves (1) the URLs of the retrieved bugs
in `$DOWNLOADS/bugs/groovy.txt`,
(2) the description and the summary of each
bug in
`$DOWNLOADS/bugs/fixes/descriptions/groovy/GROOVY-XXXX`
(where `XXXX` stands for the id of the bug), 
and (3) some general statistics,
(such as `created` timestamp, `resolution` timestamp, and `reporter`)
in `$DOWNLOADS/bugs/groovy.json`.

### 2. Fetch Kotlin bugs

```bash
python scripts/fetch/fetch_kotlin_bugs.py $DOWNLOADS/bugs/kotlin.txt \
        $DOWNLOADS/bugs/fixes/descriptions/kotlin $DOWNLOADS/bugs/kotlin.json
```

This script fetches `kotlinc` bugs
using the YouTrack REST API
(see <https://youtrack.jetbrains.com/api/issues>).
The script stores
(1) the URLs of the retrieved `kotlinc` bugs
in `$DOWNLOADS/bugs/kotlin.txt`,
(2) the description and the summary for each
bug in
`$DOWNLOADS/bugs/fixes/descriptions/kotlin/KT-XXXX`,
and (3) some general statistics
(such as `created` timestamp, `resolution` timestamp, and `reporter`)
in `$DOWNLOADS/bugs/kotlin.json`.

### 3. Fetch Java bugs

```bash
python scripts/fetch/fetch_java_bugs.py $DOWNLOADS/bugs/java.txt \
        $DOWNLOADS/bugs/fixes/descriptions/java $DOWNLOADS/bugs/java.json
```

This script fetches `javac` bugs
using the Jira REST API
(see <https://bugs.openjdk.java.net/rest/api>),
The script saves
(1) the URLs of the retrieved bugs
in `$DOWNLOADS/bugs/java.txt`,
(2) the description and the summary for each bug in
`$DOWNLOADS/bugs/fixes/descriptions/java/JDK-XXXX`,
(3) some general statistics
(such as `created` timestamp, `resolution` timestamp, and `reporter`)
in `$DOWNLOADS/bugs/java.json`.

### 4. Fetch Scala bugs

```bash
python scripts/fetch/fetch_scala_bugs.py $DOWNLOADS/bugs/scala.txt \
        $DOWNLOADS/bugs/fixes/descriptions/scala $DOWNLOADS/bugs/scala.json $GH_TOKEN
```

This script fetches bugs related to `scalac` and `dotty`
using the Github REST API
(see <https://api.github.com>).
The script saves
(1) the URLs of the scripts
in `$DOWNLOADS/bugs/scala.txt`,
(2) the description and the summary for each bug in
`$DOWNLOADS/bugs/fixes/descriptions/scala/scala-XXXX`,
and (3) some general
statistics
(such as `created` timestamp, `resolution` timestamp, and `reporter`)
in `$DOWNLOADS/bugs/scala.json`.

### 5. Clone compilers' repositories

```bash
./scripts/fetch/clone.sh $DOWNLOADS/repos
```

This script clones a number of repositories.
We use the history of these repositories to search for fixes
corresponding to the collected bugs.
In particular,
the script downloads the following repositories.

```
https://github.com/JetBrains/kotlin
https://github.com/apache/groovy
https://github.com/lampepfl/dotty
https://github.com/scala/scala
https://github.com/openjdk/valhalla
http://hg.openjdk.java.net/type-annotations/type-annotations/
http://hg.openjdk.java.net/jdk/jdk/
http://hg.openjdk.java.net/jdk7/jdk7/
http://hg.openjdk.java.net/jdk7u/jdk7u/
http://hg.openjdk.java.net/jdk8/jdk8/
http://hg.openjdk.java.net/jdk8u/jdk8u/
http://hg.openjdk.java.net/jdk9/jdk9/
http://hg.openjdk.java.net/jdk10/master/
http://hg.openjdk.java.net/jdk/jdk13/
http://hg.openjdk.java.net/jdk/jdk14/
```

### 6. Detect fixes for the collected bugs

```
./scripts/fetch/find_fixes.sh $DOWNLOADS/bugs \
        $DOWNLOADS/bugs/fixes/descriptions $DOWNLOADS/repos \
        $DOWNLOADS/bugs/fixes $GH_TOKEN 2>&1 | tee $DOWNLOADS/logs
```

This script is responsible for detecting fixes
associated with the bugs fetched by
the previous scripts.
To do so,
for each bug,
it first searches over
the corresponding repository for commits containing
the ID of the bug in the commit message.
If that fails and the repository is hosted in GitHub,
then the script searches for
pull requests that have tagged the given bug ID.
Finally,
the script saves the URLs of bug reports,
and the URLs of their fixes in
`$DOWNLOADS/bugs/fixes/{groovy,kotlin,java,scala}.txt`.


To print some general statistics regarding
our bug collection approach run

```bash
./scripts/data_collection_stats.sh downloads/bugs
```

The above script prints the total number of bugs collected
in the previous step.
It produces an output similar to the following.

```
Language         Phase 1         Phase 2
----------------------------------------
    Java            1252             873
 Scala 2            1180            1067
 Scala 3             429             366
  Kotlin            2189            1601
  Groovy             300             246
----------------------------------------
   Total            5350            4153
```

## Download the 320 typing-related bugs

To download the data associated with
the 320 typing-related that
were manually examined in our paper,
run the following script (estimated running time: 4--5 min)

```bash
./scripts/fetch/get_data_for_selected_bugs.sh downloads data
```

Finally, we need to get the fixes and the statistics for the selected bugs
of our dataset. This script takes as input the `download` directory, which
includes the initial dataset, and the `data` directory, which must contain
an `iterations` directory with the selected bugs. Specifically, in this
directory, files contain bugs associated with their fixes.
For example, you can look at `data/iterations/1/java.txt`. The script
downloads fixes' diffs, and computes statistics for these fixes in
`data/diffs/{groovy,java,kotlin,scala}/bug_id`. Each generated directory
contains a `.diff` and a `stats.csv` file. More specifically, the following
scripts will be executed.

1. Get fixes of the bugs.

```bash
./scripts/fetch/get_fixes.sh $DATA/iterations $DOWNLOADS/repos $DATA/diffs
```

This script finds the bugs' fixes in `$DATA/iterations` from the corresponding
compiler's repository or its pull request from GitHub.
Finally, it saves the diffs in `$DATA/diffs`.

2. Compute statistics of diffs.

```bash
./scripts/fetch/get_diff_stats.sh $DATA/diffs
```

Using `diffstat` this script computes the stats of the diffs.

3. Copy general statistics.

```bash
python scripts/fetch/copy_stats.py $DATA/iterations/ $DOWNLOADS/bugs/ $DATA/
```

For the bugs in `$DATA/iterations/` this script copies their statistics from
the files `$DOWNLOADS/bugs/{groovy,kotlin,java,scala}.json`
into `$DATA/{groovy,kotlin,java,scala}.json`.

4. Compute LoCs of test cases.

```bash
./scripts/fetch/add_locs.sh $DATA/test_cases
```

Using `cloc`, this script computes the stats of the test cases.

# Step by Step Instructions

In the following section, we provide scripts that reproduce the results
presented in the paper using the dataset from `data` directory.

## Collecting Bugs & Fixes (Section 2.1)

Run the following script to print the results of the bug collection phases.
Specifically, it will print the data of Table 1.

```bash
./scripts/data_collection_stats.sh data/collection
```

In `data/collection` directory is the data of the bugs that compose our
initial dataset. The above script prints the following.

```
Language         Phase 1         Phase 2
----------------------------------------
    Java            1252             873
 Scala 2            1180            1067
 Scala 3             429             366
  Kotlin            2189            1601
  Groovy             300             246
----------------------------------------
   Total            5350            4153
```


## RQ1: Symptoms (Section 3.1)

For the first research question, we will use a script reproduce Fig 1 that
shows the distribution of symptom categories. To do so, run:

```bash
python scripts/rq1.py data/bugs.json --output figures/symptoms.pdf
```

This produces `symptoms.pdf` in the `figures` directory.
It also prints a table in standard output that presents the total values
and the percentages of symptoms per compiler. Specifically, it will print
the following.

```
Symptom                               groovyc          javac        kotlinc scalac & Dotty          Total
---------------------------------------------------------------------------------------------------------
Unexpected Compile-Time Error      59 (73.8%)     38 (47.5%)     30 (37.5%)     36 (45.0%)    163 (50.9%)
Internal Compiler Error            10 (12.5%)     25 (31.2%)     18 (22.5%)     26 (32.5%)     79 (24.7%)
Unexpected Runtime Behavior         9 (11.2%)     11 (13.8%)     22 (27.5%)     11 (13.8%)     53 (16.6%)
Misleading Report                    2 (2.5%)       4 (5.0%)       7 (8.8%)       5 (6.2%)      18 (5.6%)
Compilation Performance Issue        0 (0.0%)       2 (2.5%)       3 (3.8%)       2 (2.5%)       7 (2.2%)
```

## RQ2: Bug Patterns (Section 3.2)

For the second research question, first we will reproduce Figures 7a and 7b.
These figures demonstrates the distribution of bug patterns with regards to
the compiler and the symptoms. Second, we will produce two tables, one for
each figure that display the total values and the percentages of the patterns.

```bash
python scripts/rq2.py data/bugs.json --patterns figures/patterns.pdf \
    --patterns-symptoms figures/patterns_symptoms.pdf
```

The above command produce the figures `figures/patterns.pdf` and
`figures/patterns_symptoms.pdf`, and it prints the following in the
standard output.

```
Pattern                                      groovyc              javac            kotlinc     scalac & Dotty              Total
--------------------------------------------------------------------------------------------------------------------------------
Type-related Bugs                         37 (46.2%)         34 (42.5%)         31 (38.8%)         27 (33.8%)        129 (40.3%)
Semantic Analysis Bugs                    17 (21.2%)         16 (20.0%)         20 (25.0%)         24 (30.0%)         77 (24.1%)
Resolution & Environment Bugs             24 (30.0%)         17 (21.2%)         22 (27.5%)         14 (17.5%)         77 (24.1%)
Error Handling & Reporting Bugs             1 (1.2%)         10 (12.5%)           5 (6.2%)           6 (7.5%)          22 (6.9%)
AST Transformation Bugs                     1 (1.2%)           3 (3.8%)           2 (2.5%)          9 (11.2%)          15 (4.7%)

Pattern                                Unexpected        Internal      Unexpected      Misleading     Compilation           Total
---------------------------------------------------------------------------------------------------------------------------------
Type-related Bugs                      90 (28.1%)       23 (7.2%)       10 (3.1%)        3 (0.9%)        3 (0.9%)     129 (40.3%)
Semantic Analysis Bugs                  24 (7.5%)       21 (6.6%)       27 (8.4%)        3 (0.9%)        2 (0.6%)      77 (24.1%)
Resolution & Environment Bugs          44 (13.8%)       11 (3.4%)       16 (5.0%)        5 (1.6%)        1 (0.3%)      77 (24.1%)
Error Handling & Reporting Bugs          0 (0.0%)       15 (4.7%)        0 (0.0%)        7 (2.2%)        0 (0.0%)       22 (6.9%)
AST Transformation Bugs                  5 (1.6%)        9 (2.8%)        0 (0.0%)        0 (0.0%)        1 (0.3%)       15 (4.7%)
```


## RQ3: Bug Fixes (Section 3.3)

In the third research question, we study the duration and the fixes of the bugs.
Hence, we will produce Fig 13a, Fig 13b, and Fig 14. We will also print in
the standard output the mean, median, standard deviation, max, and min per
language for files number, lines number, and duration of the fixes.


```bash
python scripts/rq3.py data/diffs/ data/ --directory figures
```

The previous command saves Fig 13a in `figures/lines.pdf`, Fig 13b in
`figures/files.pdf`, and Fig 14 in `figures/duration.pdf`.
Note that you can use `--all` option to plot lines for all languages in
the figures `lines.pdf` and `files.pdf`.
The script also prints the following tables.

```
                         Lines
============================================================
          Mean      Median    SD        Min       Max
------------------------------------------------------------
Java      30        16        40        1         190
Kotlin    56        21        144       1         1177
Groovy    49        23        89        1         706
Scala     73        9         379       1         3381
------------------------------------------------------------
Total     52        16        208       1         3381

                         Files
============================================================
          Mean      Median    SD        Min       Max
------------------------------------------------------------
Java      1         1         1         1         5
Kotlin    2         2         2         1         15
Groovy    1         1         0         1         5
Scala     2         1         5         1         45
------------------------------------------------------------
Total     2         1         3         1         45

                      Duration
============================================================
          Mean      Median    SD        Min       Max
------------------------------------------------------------
Java      131       21        284       0         1621
Kotlin    164       34        296       0         1337
Groovy    122       8         278       0         1472
Scala     328       55        628       0         3209
------------------------------------------------------------
Total     186       24        407       0         3209
```

## RQ4: Test Case Characteristics (Section 3.4)


For this research question, we will use two scripts.
The first script, will generate Figure 15 and it will print Tables 2, 3, and 4
in the standard output. Whereas the second script will print the lift scores
reported in Section 3.4.2.

```bash
python scripts/rq4.py data/characteristics.json data/bugs.json data/test_cases/ \
    --output figures/characteristics.pdf
```

This script generates `figures/characteristics.pdf` and produces:

```
General statistics on test case characteristics
===============================================================
Compilable test cases                         216 / 320 (67.5%)
Non-compilable test cases                     104 / 320 (32.5%)
---------------------------------------------------------------
LoC (mean)                                                 10.2
LoC (median)                                                  8
---------------------------------------------------------------
Number of class decls (mean)                                2.0
Number of class decls (median)                                2
---------------------------------------------------------------
Number of method decls (mean)                               2.9
Number of method decls (median)                               2
Number of method calls (mean)                               2.5
Number of method calls (median)                               1
---------------------------------------------------------------

Most frequent features
===============================================================
Parameterized type                                       46.56%
Type argument type inference                             31.87%
Parameterized class                                      30.00%
Parameterized function                                   26.25%
Inheritance                                              24.06%

Least frequent features
===============================================================
Multiple implements                                       2.19%
this                                                      2.19%
Arithmetic Expressions                                    1.88%
Loops                                                     1.25%
Sealed Classes                                            0.94%

Most bug-triggering features per language
===========================================================================================================================================================
                 Java                                 Groovy                                Kotlin                                Scala
-----------------------------------------------------------------------------------------------------------------------------------------------------------
Parameterized type            51.25% | Parameterized type            41.25% | Parameterized type            36.25% | Parameterized type            57.50% |
Type argument type inference  42.50% | Collection API                35.00% | Parameterized class           33.75% | Parameterized class           42.50% |
Single Abstract Method        37.50% | Type argument type inference  35.00% | Type argument type inference  32.50% | Inheritance                   32.50% |
Parameterized function        35.00% | Lambda                        25.00% | Parameterized function        26.25% | Implicits                     23.75% |
Parameterized class           30.00% | Parameterized function        21.25% | Inheritance                   25.00% | Parameterized function        22.50% |

Most frequent characteristic categories
========================================
Parametric polymorphism           57.19%
OOP features                      53.75%
Type inference                    43.44%
Type system features              36.25%
Functional programming            31.56%
Standard library                  30.63%
Standard features                 28.75%
Other                             28.75%
```

As already mentioned, the following script reports the lift scores that we
refer in the paper.

```bash
python scripts/lift.py data/bugs.json data/ data/diffs/
```

It produces:

```
Char Categories -> Char Categories
Lift        Standard library -> Functional programming : 5.3639 (Confidence A->B: 0.5306, Support B: 0.0989) -- Totals A: 98, B: 101, A-B: 52
Lift        Standard library -> Type inference         : 5.1717 (Confidence A->B: 0.7041, Support B: 0.1361) -- Totals A: 98, B: 139, A-B: 69
Characteristics -> Characteristics
Lift            Variable arguments -> Overloading                  : 24.0125 (Confidence A->B: 0.4545, Support B: 0.0189) -- Totals A: 11, B: 29, A-B: 5
Lift             Use-site variance -> Parameterized function       : 17.1653 (Confidence A->B: 0.9412, Support B: 0.0548) -- Totals A: 17, B: 84, A-B: 16
Lift  Type argument type inference -> Parameterized function       : 12.6951 (Confidence A->B: 0.6961, Support B: 0.0548) -- Totals A: 102, B: 84, A-B: 71
Lift                     Implicits -> Parameterized class          : 10.9189 (Confidence A->B: 0.6842, Support B: 0.0627) -- Totals A: 19, B: 96, A-B: 13
Lift  Type argument type inference -> Collection API               : 8.5826 (Confidence A->B: 0.3922, Support B: 0.0457) -- Totals A: 102, B: 70, A-B: 40
Lift  Type argument type inference -> Parameterized type           : 6.9554 (Confidence A->B: 0.6765, Support B: 0.0973) -- Totals A: 102, B: 149, A-B: 69
```

Note that this script can be used to compute various lift scores.
To print all available lift scores use the option `--all`.
Furthermore, you can set the number of pairs to print with `--limit` option,
a threshold with `--threshold` option, and a population threshold with
`--ithreshold`.

```
usage: lift.py [-h] [--threshold THRESHOLD] [--ithreshold ITHRESHOLD]
               [--limit LIMIT] [--all] bugs stats diffs

Lift correlations

positional arguments:
  bugs                  File with the bugs
  stats                 Directory that contains the stats for the bugs.
  diffs                 Directory that contains the diffs of the bug fixes.

optional arguments:
  -h, --help            show this help message and exit
  --threshold THRESHOLD
                        Threshold for lift.
  --ithreshold ITHRESHOLD
                        Intersections threshold for lift.
  --limit LIMIT         Max entries to show per pair.
  --all                 Print lift score for all categories
```
