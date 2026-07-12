# ChinaXiv-Style Submission Checklist

Prepared files:

- `paper_chinaxiv.md`: source manuscript with numbered citations and numbered references
- `paper_chinaxiv.docx`: Word submission document
- `paper_chinaxiv_professional_revision_v3.pdf`: final professionally revised PDF submission document
- `references.bib`: source bibliography
- `figures/architecture_diagram.png`: MLLM architecture diagram
- `figures/connector_tradeoff_diagram.png`: connector trade-off diagram
- `figures/benchmark_taxonomy_diagram.png`: benchmark taxonomy diagram
- `figures/grounding_workflow_diagram.png`: grounding workflow diagram
- `figures/hallucination_illustration.png`: hallucination illustration
- `figures/model_timeline.png`: model timeline chart
- `figures/benchmark_timeline.png`: benchmark timeline chart
- `docs/chinaxiv_sample_comparison.md`: layout comparison with the provided ChinaXiv sample

Formatting applied:

- Letter page size matching the provided ChinaXiv sample PDF
- Narrow centered margins closely matching the provided ChinaXiv sample
- Bottom footer rule on every page, matching the provided ChinaXiv sample style
- Centered title, author, affiliation, and corresponding-author information
- English abstract with 222 words
- Keywords
- Numbered section headings
- Main text in academic manuscript layout
- Three inserted comparison/taxonomy tables
- Comprehensive model comparison table
- Seven inserted academic diagrams/charts
- Fourteen Author's Analysis subsections
- Two practical case studies
- Numbered in-text citations, e.g. `[1]`
- 67 numbered references formatted in GB/T 7714-like style
- Code Availability section with the populated GitHub repository URL
- Final verification checklist

Integrity checks:

- No fabricated benchmark numbers
- No claimed original model-training experiments
- References are generated from `references.bib`
- Citation keys from the draft are converted to numbered citations
- The Word document contains the two taxonomy tables
- The Word document contains reproducible generated charts
- Source code is available in `scripts/` and `src/`, with environment files in `requirements.txt` and `environment.yml`
