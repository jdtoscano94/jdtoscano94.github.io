# jdtoscano94.github.io

Personal academic site. Static HTML generated from `data.json`.

Update workflow:
1. Edit `data.json` (add a paper under the right pillar, a talk, a repo).
2. Drop a thumbnail as `docs/assets/thumbs/<key>.jpg` (about 720 px wide).
3. Run `python3 build.py` and commit `data.json` + `docs/`.

GitHub Pages serves the `docs/` folder from `main`.
