# Flagship Handoffs

Each directory is a self-contained, immutable review snapshot submitted by the main model.

Naming convention:

    <sequence>_<topic>/

A handoff must contain the exact claim, all assumptions and limitations, and any script or compact data needed for flagship review. It must not depend on files outside `flagship/`.

The flagship model records findings in `reviews/` and decisions in `decisions/`. It never edits a submitted handoff. Corrections require a new handoff sequence.