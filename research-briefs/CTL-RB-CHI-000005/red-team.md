# Red Team — CTL-RB-CHI-000005: Chicago's Great Migration Geography

**CULTURETECHLENS** — *Culture, Clearly Seen.* — Black Cultural Intelligence
*2026-09-28. Adversarial review of the brief's claims before publication.*

## RT-1 — Population figures lack exact Census table provenance
**Risk:** Every decennial figure (N-02, S-01) is capped at SUPPORTED. A reader
could mistake convergence across secondary sources for verification.
**Mitigation:** Brief §22 states the cap explicitly; claim ledger notes the
1920 variant (109,458 vs. 109,408). **Action:** pull NHGIS/Census tables at
publish; V-GRAPH-1 is blocked until then.

## RT-2 — "75%" vs. "90%" share tension
**Risk:** S-07 (75% in the Black Belt, mid-century) and N-31's relay (>90% in
Bronzeville by the 1930s) look contradictory.
**Mitigation:** Brief §11 and §22 flag the definitional difference (census-tract
Black Belt vs. named-neighborhood Bronzeville). **Action:** do not mix the two
figures in any graphic or summary sentence.

## RT-3 — "80% covenant coverage" is provisional
**Risk:** N-29 rests on Wikipedia alone; repeating it would launder a weak figure.
**Mitigation:** Graded PROVISIONAL; brief §10 calls it out as poorly sourced.
**Action:** exclude from all publish graphics unless a covenant-coverage study is found.

## RT-4 — Boundary descriptions are snapshots, not a dataset
**Risk:** White (1919), Drake & Cayton (1920s), and CULtivate (1940s) boundaries
use different methods and years; stacking them as a single "moving edge" could
imply false precision.
**Mitigation:** Brief §§05/22 label each as a dated snapshot. V-GRAPH-2 must
carry the same caveat on the map itself, not in a footnote.

## RT-5 — HOLC causation overstatement
**Risk:** Popular narratives treat redlining maps as the direct cause of
disinvestment; the Chicago Fed evidence (N-30) says the maps postdated most HOLC
lending.
**Mitigation:** Brief §21 states the precision point directly.
**Action:** any HOLC visual must avoid implying direct HOLC-lending causation.

## RT-6 — Defender causal weight
**Risk:** Treating the Defender as the engine of migration overstates one
institution's role (sibling red-team flag; S-08, N-18).
**Mitigation:** Brief §08 keeps the paper as enabler, not engine.

## RT-7 — South-Side-heavy evidence base
**Risk:** The corpus (and this brief) is stronger on Bronzeville than on the West
Side's churches, block clubs, women, and workers — noted in the sibling's gaps.
**Mitigation:** Brief §15 and the verdicts name the gap; West Side institutional
mapping is the top "research next" item.

## RT-8 — Clyde Ross purchase conflict
**Risk:** 1958/$27,000 (Moyers) vs. 1961/$26,000 (other accounts) — unresolved.
**Mitigation:** Ledger N-record and brief §19 state the conflict.
**Action:** never print one version without the other.

## RT-9 — Oral history as boundary data
**Risk:** Facing History testimony (N-24: 63rd → 75th → 90th) is interpretive,
not a boundary dataset.
**Mitigation:** Brief §14 frames it as described direction, not exact bounds.

## RT-10 — Single-source relays at SUPPORTED
**Risk:** N-14 (rent burden), N-26 (14 neighborhoods), N-35 (packinghouse) each
rest on one relay; SUPPORTED could be read as stronger than it is.
**Mitigation:** Ledger notes single-source status on each; brief presents them as
study-specific findings.
**Action:** seek corroboration before any VERIFIED upgrade.

## RT-11 — Video relevance without viewing
**Risk:** The directive forbids embedding anything "unwatched." Relevance was
assessed from titles, descriptions, uploader authority, and the billmoyers.com
feature page — not from viewing the video streams.
**Mitigation:** visuals.md records exactly what was reviewed; V-VID-2 is
link-only with embed status unverified.
**Action:** view both videos (or confirm transcripts) before publication; re-check
embed status.

## RT-12 — Process issues in the shared source log
**Risk:** (a) Some appended log lines were secondary, not new primary sources as
requested; (b) one WBEZ line was edited post-append with `sed`, violating
append-only.
**Mitigation:** Disclosed in sources.md; no further retroactive edits.
**Action:** treat the shared log as partially compromised for provenance auditing;
the claim ledger in this brief is the authoritative record.

## RT-13 — Image licensing asymmetry
**Risk:** V-IMG-2's clearance rests on PICRYL's "No known restrictions" record,
not a re-verified Commons file page (fetch blocked).
**Mitigation:** visuals.md documents the exact basis and forbids claiming Commons
licensing.
**Action:** re-verify on the Commons file page or LOC item page before publication.
