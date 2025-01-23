---
permalink: /
title: "Minseog Oh"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

Hi!
I am a Ph.D. candidate in Finance at KAIST.
My research interests are
- Financial econometrics
- Risk management
- High-dimensional analysis

Education
======
- Ph.D. in Management Engineering, KAIST, 2020--2025
- B.S. in Mathematical Sciences, KAIST, 2016--2020
  - Double major in Computer Science
  - Minor in Economics
  - Summa Cum Laude


Published/Accepted Papers
======
- __Oh, M.__, Kim, D., and Wang, Y. (2024+) Robust Realized Integrated Beta Estimator with Application to Dynamic Analysis of Integrated Beta. To appear in ___Journal of Econometrics___.

- Kim, D. and __Oh, M.__  (2024) Dynamic Realized Minimum Variance Portfolio Models. ___Journal of Business & Economic Statistics___, 42, 1238-1249.

- Kim, D., __Oh, M.__, Song, X., and Wang, Y. (2024)  Factor Overnight GARCH-Ito Models. ___Journal of Financial Econometrics___, 22, 1209-1235.

- __Oh, M.__ and Kim, D. (2024).  Effect of the U.S.--China Trade War on Stock Markets: A Financial Contagion Perspective.   ___Journal of Financial Econometrics___, 22, 954-1005.

-  Kim, D., __Oh, M.__, and Wang, Y. (2022). Conditional Quantile Analysis for Realized GARCH Models. ___Journal of Time Series Analysis___, 43, 640-665. 

Working Papers
=====
- __Oh, M.__ and Kim, D.  Property of Inverse Covariance Matrix-based Financial Adjacency Matrix for Detecting Local Groups.

- Kim, D., __Oh, M.__, and Shin, M. High-Dimensional Time-Varying Coefficient Estimation.


Site-wide configuration
------
The main configuration file for the site is in the base directory in [_config.yml](https://github.com/academicpages/academicpages.github.io/blob/master/_config.yml), which defines the content in the sidebars and other site-wide features. You will need to replace the default variables with ones about yourself and your site's github repository. The configuration file for the top menu is in [_data/navigation.yml](https://github.com/academicpages/academicpages.github.io/blob/master/_data/navigation.yml). For example, if you don't have a portfolio or blog posts, you can remove those items from that navigation.yml file to remove them from the header. 

Create content & metadata
------
For site content, there is one markdown file for each type of content, which are stored in directories like _publications, _talks, _posts, _teaching, or _pages. For example, each talk is a markdown file in the [_talks directory](https://github.com/academicpages/academicpages.github.io/tree/master/_talks). At the top of each markdown file is structured data in YAML about the talk, which the theme will parse to do lots of cool stuff. The same structured data about a talk is used to generate the list of talks on the [Talks page](https://academicpages.github.io/talks), each [individual page](https://academicpages.github.io/talks/2012-03-01-talk-1) for specific talks, the talks section for the [CV page](https://academicpages.github.io/cv), and the [map of places you've given a talk](https://academicpages.github.io/talkmap.html) (if you run this [python file](https://github.com/academicpages/academicpages.github.io/blob/master/talkmap.py) or [Jupyter notebook](https://github.com/academicpages/academicpages.github.io/blob/master/talkmap.ipynb), which creates the HTML for the map based on the contents of the _talks directory).

**Markdown generator**

The repository includes [a set of Jupyter notebooks](https://github.com/academicpages/academicpages.github.io/tree/master/markdown_generator
) that converts a CSV containing structured data about talks or presentations into individual markdown files that will be properly formatted for the Academic Pages template. The sample CSVs in that directory are the ones I used to create my own personal website at stuartgeiger.com. My usual workflow is that I keep a spreadsheet of my publications and talks, then run the code in these notebooks to generate the markdown files, then commit and push them to the GitHub repository.

How to edit your site's GitHub repository
------
Many people use a git client to create files on their local computer and then push them to GitHub's servers. If you are not familiar with git, you can directly edit these configuration and markdown files directly in the github.com interface. Navigate to a file (like [this one](https://github.com/academicpages/academicpages.github.io/blob/master/_talks/2012-03-01-talk-1.md) and click the pencil icon in the top right of the content preview (to the right of the "Raw | Blame | History" buttons). You can delete a file by clicking the trashcan icon to the right of the pencil icon. You can also create new files or upload files by navigating to a directory and clicking the "Create new file" or "Upload files" buttons. 

Example: editing a markdown file for a talk
![Editing a markdown file for a talk](/images/editing-talk.png)

For more info
------
More info about configuring Academic Pages can be found in [the guide](https://academicpages.github.io/markdown/), the [growing wiki](https://github.com/academicpages/academicpages.github.io/wiki), and you can always [ask a question on GitHub](https://github.com/academicpages/academicpages.github.io/discussions). The [guides for the Minimal Mistakes theme](https://mmistakes.github.io/minimal-mistakes/docs/configuration/) (which this theme was forked from) might also be helpful.
