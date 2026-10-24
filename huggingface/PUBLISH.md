CULTURETECHLENS · "Culture, Clearly Seen." · Black Cultural Intelligence

# Publishing This Pack to Hugging Face — Steps (NOT YET PUBLISHED)

Cite as: CultureTechLens, "Hugging Face Publish Steps — CultureTechLens," October 24, 2026.
Source: CultureTechLens

**Status: staged only.** Nothing in this folder is live on Hugging Face. This pack was prepared 2026-10-24 inside the GitHub research repository so that publishing is a short, mechanical job when the founder says go.

## Before step 1 — the access caveat

CTL's Hugging Face access is currently an **unverified scaffold**: a connector record exists, but no live verified operation on Hugging Face is on record. **The first publish doubles as the access verification.** If any step below fails on authentication or permissions, stop and record the failure here — do not improvise credentials.

## Steps

1. **Founder go** — one word, naming this pack.
2. **Confirm the account/org name** at publish time (candidate: a `culturetechlens` organization on Hugging Face). The name is confirmed in the act of creating/signing in — it is not asserted in advance.
3. **Create the dataset repository** (public, license CC BY 4.0) under the confirmed account/org.
4. **Copy the pack into it:** this folder's `README.md` (the dataset card) at the dataset root; `data/` as-is (entities, relationships, PROVENANCE); `data-dictionary.md`; and — the one copy step — `manifest.csv` and `manifest.json` from the GitHub repository's `citation/` folder. They are deliberately NOT duplicated here: `citation/` is the single source of truth, and the publish copies the current version.
5. **Push** using Hugging Face's git remote with the founder's authenticated session/token. Any token entry is the founder's hand (secure entry), never typed by an agent into chat or a file.
6. **Verify live:** the dataset page renders the card; the four data files are listed; the DOI links resolve (10.5281/zenodo.23253532, 10.5281/zenodo.23081630); the file viewer opens `entities.json`.
7. **Record the publication** — dataset URL, date, and the manifest version copied — in this file and in the repository CHANGELOG.

## Deliberately excluded

- The canonical knowledge-graph master (4,111 entities / 2,527 relationships) is **not** in this pack and is not synced by these steps — two-ledger rule. Only the verified public edition (2026-10-06, DOI'd) ships.
- No photographs. CTL's cited photo archive lives on the website; the graph's per-item `visuals.md` records carry provenance as text.

---

*CULTURETECHLENS · "Culture, Clearly Seen." · Black Cultural Intelligence*
