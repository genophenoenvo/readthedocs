# ReadTheDocs (RTD)

The repo is the [Read the Docs documentation](https://readthedocs.org/) in use by the GenoPhenoEnvo project. 

## Goals of these docs

The goal of the documentation should beto provide basic learning materials to help researchers, educators, and students effectively (re)use our research material in the CyVerse cyberinfrastructure. 

All documentation is considered a work-in-progress; even the best efforts will be incomplete, contain ambiguities, inaccuracies, and at some point, will become out of date. 

## Maintained Sections

We maintain the following templates. All documentation in the should be derived from these. They can be adapted slightly, but documentation should strive to be consistently formatted. 

    - URL: https://github.com/genophenoenvo/readthedocs
    
- **Research**: Specific explanations of the research and how to reproduce it

- **Data Sources**: Information about the data sets we're using in the project

- **Documentation**: Explanation of where data sets are located and how to (re)create our workflows.

- **Tutorials**: Tutorials to teach how to use our platforms. 

## Making Changes to the RTD on our website

This repository contains all of the necessary build material to generate a ReadTheDocs website

Because we're using a separate Bootstrap.js website for our main page, this repository is necessary for rendering the `html` components of the documentation.

To build the ReadTheDocs pages, you must install [Sphinx](https://docs.readthedocs.io/en/stable/intro/getting-started-with-sphinx.html) on your local computer

After you've installed Sphinx, you should be ready to edit the documentation pages:

```
git clone https://github.com/genophenoenvo/readthedocs
cd readthedocs
sphinx-autobuild -b html --host 0.0.0.0 --port 8000 --poll . readthedocs
```

After you've made any changes to the ReStructuredText pages and rendered the new HTML (located in the `/readthedocs/readthedocs` folder) with Sphinx locally
you will need to copy these changes to the main webpage [GitHub Repository](https://github.com/genophenoenvo/genophenoenvo.github.io) by copying over the `/readthedocs` sub-folder. Do not copy over the entire `git` repository as it will give you a Git error. 
