# Plug-ins: Adding Flexibility to Your Apps

Talk given at [PyCon, Cleveland, OH, USA](https://us.pycon.org/2019/) on May 5, 2019

- [ [Abstract] ](https://us.pycon.org/2019/schedule/presentation/227/)
- [ [Slides] ](20190505_plugins.md)
- [ [Video] ](https://www.youtube.com/watch?v=98s9YfoXB68)

The slides were presented using [`mdp`](https://github.com/visit1985/mdp). The content of the slides are available below.

The code is available in two different directories:

- [`code_talk`](code_talk/) contains the code as written during the presentation
- [`code_pyplugs`](code_pyplugs) contains the expanded code based on [`pyplugs`](https://pypi.org/project/pyplugs/) shown at the end of the talk

The [`pyplugs`]() library is [available at PyPI](https://pypi.org/project/pyplugs/).


## Presentation

_This is the content of the presentation slides, adapted to a flat text file:_

**Plug-ins: Adding Flexibility to Your Apps**

Geir Arne Hjelle

---

### Agenda

- Motivation

- Example: Plotter app
    - Different data formats
    - Choosing what to plot
    - More plotting styles

- Plug-ins

---

### Motivation

Modularized code:

- is **less complex**
- is **easier to maintain and test**
- is **easier to extend**

With plug-ins, your app:

- can be **controlled by configuration settings**
- can be **extended and customized for and by users**
- can be **better structured, and developed faster**

---

### Demo time

We'll build a simple **plotter app**:

- Command line application
- Read data from a CSV file
- Plot data in a simple line graph

---

### Decorators

A **decorator** is a function that wraps another function:

```
decorated = decorator(original)
```

- Decorators are typically used to add some common
  functionality across many functions or methods
- In most cases, decorators are applied using @-syntax:

    ```
    @click.command()
    def main(file_path): 
        ...
    ```

[realpython.com/primer-on-python-decorators](https://realpython.com/primer-on-python-decorators/)

---

### Demo time

Let's expand our plotter app:

- Support more file formats, like JSON
- Support more kinds of plots
- Control which data to plot

---

### PyPlugs

**A simple decorator based plug-in architecture for Python**

```
$ pip install pyplugs
```

Three levels:

- **Plug-in packages:** Directories containing files with plug-ins
- **Plug-ins:** Modules containing registered functions or classes
- **Plug-in funcs:** Several registered functions in the same file

---

### PyPlugs

**Example use cases for plug-ins:**

- **Readers** for different file formats
- **Models** for flexible calculations
- **Filters** for filtering your data
- **Writers** for storing your data in different formats
- **Notifiers** for sending you data to different devices
- **Components** for building your GUI

---

### Thank You For Your Attention

- **Me:** @gahjelle
- **Code:** [github.com/gahjelle/talks]()
- **PyPlugs:** [pyplugs.readthedocs.io]()
- **Real Python:** [realpython.com](https://realpython.com/)
