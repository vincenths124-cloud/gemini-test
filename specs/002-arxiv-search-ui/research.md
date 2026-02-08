# Research: GUI Library Selection

**Date**: 2026-02-08

## Decision

We will use **CustomTkinter** for the GUI of the arXiv Search UI application.

## Rationale

- **Modern Look and Feel**: CustomTkinter provides a modern and aesthetically pleasing UI out of the box, which is a significant advantage over the outdated appearance of standard Tkinter.
- **Ease of Use**: It is based on Tkinter and is easy to learn and use, making it suitable for this project's scope.
- **Good Balance**: It offers a good balance between features and complexity. It is not as complex as PyQt, which would be overkill for this application, but it provides more features and a better look than standard Tkinter.
- **Active Development**: It is an actively developed library with good community support.

## Alternatives Considered

- **PyQt**: Rejected due to its complexity and licensing model. It is too powerful for this project's needs.
- **Tkinter**: Rejected due to its outdated look and feel, and limited set of widgets.
