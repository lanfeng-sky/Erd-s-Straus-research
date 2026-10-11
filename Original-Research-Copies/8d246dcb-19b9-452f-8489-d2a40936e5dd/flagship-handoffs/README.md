# Flagship Handoffs

Each directory is a self-contained, immutable review snapshot submitted by the main model.

Naming convention:

    <sequence>_<topic>/

A handoff must contain the exact claim, all assumptions and limitations, and any script or compact data needed for flagship review. It must not depend on files outside `flagship/`.

H-001 through H-004 are historical compressed packages. Their consolidated mathematical content is in `../historical_compression.md`; raw proof, replay, dataset and hash payloads are retained only for optional user-authorized inspection and are not the default reading path. H-005 and later are not covered by this compression notice.

The flagship model records findings in `reviews/` and decisions in `decisions/`. It never edits a submitted handoff. Corrections require a new handoff sequence.