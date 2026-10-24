# Red Team Review — CTL-RB-BIZ-000001

**CULTURETECHLENS — Culture, Clearly Seen. | Black Cultural Intelligence**

Adversarial review of the brief's sourcing, logic, and blind spots. Each check ends with a verdict: **holds**, **flagged** (caveat recorded in brief), or **cut** (excluded).

---

## 1. Sourcing audit

- **Check:** Is every significant claim backed by a source at or above its grade?
  **Verdict: holds.** 28 claims in `claim-ledger.json`; municipal/government sources anchor the VERIFIED tier; peer-reviewed scholarship anchors SUPPORTED; single-source and inference claims are graded PROVISIONAL or UNRESOLVED.

- **Check:** Did any search-result snippet or aggregator slip in as evidence?
  **Verdict: holds.** Snippets and aggregators were used only as finding aids (see sources.md §7). The Till 50,000 figure appears on mortuary-school marketing pages — not cited; carried instead by the Till Memory Project and Duckworth's office with variance preserved.

- **Check:** Are institutional self-histories (Rayner, Leak company pages) over-weighted?
  **Verdict: flagged.** Rayner's founding details and the insurance-funeral nexus rest on the firm's own "About Us" page (C-26, SUPPORTED). The brief marks this and calls for corroboration. Do not let company marketing become the archive.

## 2. Myth and romanticization

- **Check:** Does the "funeral home as movement sanctuary" narrative romanticize?
  **Verdict: flagged.** The national evidence is strong (Sanders/Harvey is archivally grounded), but the brief explicitly states these functions were contingent, uneven, economically reciprocal, and sometimes self-interested. §6 (Counter-Evidence) exists for this reason. The Till case must not be read as typical.

- **Check:** Does the brief imply all Black funeral homes were movement sites?
  **Verdict: holds.** §6 states the documented political functions cluster around specific directors; treating the sector as uniformly political would be selection bias.

## 3. Date, name, and geography conflicts

- **Free African Society: 1787 vs. 1778.** Cann's article gives 1787 in the historical passage and "1778" in a later synthesis line — an internal inconsistency. **Verdict: flagged.** Brief uses 1787 per scholarly consensus; red-team note in C-10.

- **Ernest vs. Earnest Griffin.** Congressional Record: "Earnest Griffin"; obituary and Newberry: "Ernest A. Griffin." **Verdict: flagged.** Working form "Ernest A. Griffin" with note in entities.json and C-24.

- **50,000 vs. 100,000 (Till viewing).** **Verdict: flagged.** Preserved as DISPUTED variance (C-02); brief never cites a single number.

- **Funeral-directors' association lineage.** LOC blog: "National Association of Negro Funeral Directors" affiliated with the 1900 National Negro Business League. Cann: Independent National Funeral Directors Association (1924) → NFDMA (1957). These may be distinct organizations or a conflated lineage. **Verdict: flagged as UNRESOLVED** (entities.json e014). Do not merge them in the knowledge graph.

- **Geography:** All Chicago addresses verified against at least one institutional or press source except 1820 S. Michigan (PROVISIONAL, single secondary). **Verdict: flagged** (C-23).

## 4. Anachronism

- **Check:** "Celebration of life" / modern homegoing framing projected onto 1933–1955?
  **Verdict: holds.** Brief uses period-appropriate terms (visitation, final rites, burial societies) and notes the home-going tradition as documented by LOC without modernizing it.

- **Check:** Worsham College treated as a Black institution?
  **Verdict: cut.** Research confirmed Worsham was white-founded (Albert Worsham, 1911; IBHE records). The brief explicitly corrects this (C-14 note).

- **Check:** "Redlining/credit exclusion" applied where the evidence only supports "without access to traditional credit markets" (LOC)?
  **Verdict: holds.** Brief quotes the LOC formulation rather than importing a stronger causal term.

## 5. Causal overreach

- **Check:** Does the brief credit Rayner with the Till movement effect?
  **Verdict: holds.** §5.1 states Mamie Till-Mobley's decision caused the political effect; Rayner supplied the machinery. The arrow is explicit and repeated in the verdict.

- **Check:** Does the "function-first lens" smuggle functionalism — i.e., assume every feature of the funeral home existed *for* its function?
  **Verdict: flagged.** The brief's thesis says functions "emerged because no other institution… could perform them" — a structural claim, not a design claim. The economics section (§5.7) grounds functions in the firms' own survival incentives to avoid implying community-service intent where business logic suffices.

## 6. Selection, celebrity, and survivorship bias

- **Check:** Are famous funerals (Till, Cooke, Muhammad, Owens, Jackson) over-represented vs. ordinary families?
  **Verdict: flagged.** Named in §6 and §15 as a limit. The record preserves celebrity funerals; the brief does not claim they represent typical practice.

- **Check:** Survivorship bias — Leak and Rayner survive; what about the firms that closed or were acquired?
  **Verdict: flagged.** Griffin's 2007 closure is included; the 2009 Burr Oak scandal is included as counter-evidence; consolidation acquisitions are an explicit unknown (C-21, deferred to CTL-DR-ECON-001).

- **Check:** Are women missing?
  **Verdict: partially flagged.** Alyce Griffin, Dottie Leak, Clarie Collins Harvey, and the Rayner children appear, but women's ownership/labor is an explicit research gap (§10.6).

## 7. Missing ordinary people and institutions

- **Check:** Do ordinary Black Chicagoans appear, or only directors and celebrities?
  **Verdict: flagged.** The "tens of thousands" of Till mourners and burial-society members (7,448 by 1838) are the ordinary people in this record; their individual voices are absent. Funeral programs — the archive of ordinary lives — are the named path to correcting this (§10.1, §10.3).

- **Check:** Are churches given their due as co-institutions (Roberts Temple) rather than backdrop?
  **Verdict: holds.** Roberts Temple is an entity with its own record, National Monument status, and address; the brief treats the funeral as a funeral-home/church/press joint production.

## 8. Visual rights

- **Check:** Any rights-managed, unknown-provenance, or AI-generated imagery?
  **Verdict: holds.** No Getty/Alamy/Chicago History Museum images used. V-01: LOC "No known restrictions." V-02: CC0-stated but file-page verification blocked — status is "sourced (re-verify)" not "cleared." V-03–V-05 are original builds. V-06 is a link, never a download. No AI-generated historical imagery exists in this brief.

## 9. Duplicate entities

- **Check:** Entity ID uniqueness; name collisions across sibling packages.
  **Verdict: holds.** 27 entities, no duplicate IDs. Name-variant aliases recorded (Earnest/Ernest Griffin; NFDMA variants). Sibling-package entities (Defender, JPC) referenced by name with their own package IDs, not duplicated. Note: a future graph merge must reconcile "Metropolitan Funeral Home" (this brief) with any Defender-package entity for 4445 S. King Dr.

## 10. What would change the brief's conclusions

1. Discovery of Rayner, Leak, or Griffin business papers — could upgrade C-06, C-08, C-09, C-13 from PROVISIONAL or confirm their absence.
2. Defender/Jet/Ebony morgue evidence of specific political meetings in Chicago funeral homes — would resolve the largest Chicago gap.
3. Consolidation acquisition records — would complete the economics section.
4. A verified single crowd count for the Till viewing — would retire C-02's dispute (unlikely; preserve variance).

---

## Final red-team verdict

**The brief's central thesis holds under adversarial review** — the mechanism (segregated asset concentration) is well-evidenced and the national pattern is archivally grounded — **but its Chicago-specific political and financial claims must stay at PROVISIONAL until archives or oral histories anchor them.** The two most likely failure modes are (a) letting the Till case's extraordinariness inflate into a general claim, and (b) letting institutional self-histories substitute for an archive. Both are guarded in the text; both need watching in CTL-DR-ECON-001.
