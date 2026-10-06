# True Size of Africa — manifest

Graphic: `true-size-of-africa.png` (1920×1080, PNG)
Built: 2026-10-05 · Method: programmatic only (Pillow). No AI-generated imagery.
Generator: `/tmp/build_true_size.py` (re-runnable)

## Caption

For more than 450 years, the Mercator projection — built for 16th-century navigation, not truth — has shrunk Africa on the world's classroom walls, making a continent of 30.37 million km² look no larger than Greenland. This is not a cartographic footnote; it is a cultural-intelligence story about who gets seen at full scale and who does not. On 4 September 2026, the UN General Assembly voted 164–1 to promote map projections that show continents' true relative size. CultureTechLens applies a global lens because the diaspora is global — and you cannot think clearly about a place you cannot see clearly. Culture, clearly seen.

## Area figures (all LAND area, km²)

| # | Entity | km² | Source |
|---|--------|-----|--------|
| — | Africa (continent) | 30,370,000 | ISS Africa / UN General Assembly "Correct the Map" resolution context (Sept 2026): "30.37 million square kilometer land area" |
| 1 | United States | 9,147,593 | UN Statistics Division / FAO, via Wikipedia "List of countries and dependencies by area" (land column) |
| 2 | China | 9,326,410 | same |
| 3 | India | 2,973,190 | same |
| 4 | Mexico | 1,943,950 | same |
| 5 | Peru | 1,279,996 | same |
| 6 | France | 543,941 | UN figures, via Wikipedia "List of European countries by area" (metropolitan France) |
| 7 | Spain | 498,485 | same (UN figure) |
| 8 | Sweden | 407,284 | UN Statistics Division / FAO, via Wikipedia "List of countries and dependencies by area" (land column) |
| 9 | Norway | 366,704 | same (includes Svalbard and Jan Mayen; mainland 304,282) |
| 10 | Japan | 364,485 | same |
| 11 | Germany | 349,390 | same |

Sum of the 11 comparison areas: 27,203,428 km² — fits inside Africa's 30,370,000 km² with ~3.17M km² to spare, which is why the graphic's claim ("all fit inside it") holds.

Greenland reference on the graphic (~2.17M km²): standard figure, used only for the Mercator comparison note.
UNGA vote (164–1, 4 Sept 2026): reported by ATC News / Diplomatic Watch, Sept 2026.

## Design notes

- Africa silhouette: simplified hand-built polygon (equirectangular projection of ~80 coastal waypoints) + Madagascar. Simplified but recognizable; not a survey-grade coastline.
- Comparison countries: schematic rectangles with TRUE relative areas — each rectangle's pixel area ÷ Africa's pixel area equals that country's km² ÷ 30,370,000 exactly. Rectangles are clipped to the Africa silhouette, so the visual claim is enforced geometrically.
- Eastern Europe was deliberately omitted: no single agreed definition, and the graphic's claim holds without it.
- CTL branding: wordmark, "Culture, Clearly Seen.", culturetechlens.com, "Source: CultureTechLens", data-source credit line. Palette: Ink / Sesame Gold / Deep Bronze / Deep Red on paper.

## Suggested alt text

"Infographic titled 'The True Size of Africa': a black silhouette of Africa containing true-to-scale rectangles for the United States, China, India, Mexico, Peru, France, Spain, Sweden, Norway, Japan, and Germany, with a numbered legend giving each country's land area. Caption notes the 1569 Mercator projection shrinks Africa and the UN's 2026 vote for true-size maps. Branded CultureTechLens."
