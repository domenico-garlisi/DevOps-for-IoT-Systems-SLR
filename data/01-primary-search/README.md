# Primary search results

```
01-primary-search/
├── raw/                                   # verbatim per-database exports, native schema/delimiter
│   ├── wos-primary-29042026.csv
│   ├── ieee-primary-29042026.csv
│   ├── acm-primary-29042026.csv
│   └── scopus-primary-29042026.csv
└── uniformed/                             # same records, remapped to a common `;`-delimited schema
    ├── wos-29042026-uniformed.csv
    ├── ieee-29042026-uniformed.csv
    ├── acm-29042026-uniformed.csv
    └── scopus-29042026-uniformed.csv
```

`uniformed/` normalizes every database's export to the same field set —
`source;entry_type;document_type;title;authors;year;doi;url;abstract;keywords;journal;booktitle;publisher;pages`

## Export log
| Database | Search | Date run | Raw file | Uniformed file | Result count | Notes |
|---|---|---|---|---|---:|---|
| WoS | Primary | 2026-04-29 | `raw/wos-primary-29042026.csv` | `uniformed/wos-29042026-uniformed.csv` | 149 | |
| IEEE Xplore | Primary | 2026-04-29 | `raw/ieee-primary-29042026.csv` | `uniformed/ieee-29042026-uniformed.csv` | 274 | |
| ACM DL | Primary | 2026-04-29 | `raw/acm-primary-29042026.csv` | `uniformed/acm-29042026-uniformed.csv` | 359 | |
| Scopus | Primary | 2026-04-29 | `raw/scopus-primary-29042026.csv` | `uniformed/scopus-29042026-uniformed.csv` | 327 | |
