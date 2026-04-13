# Brooke's Crossing Static Site

This repo contains the static site for `brookescrossing.com`, including HOA content and downloadable forms.

## Structure

- `index.html`: homepage
- `about/`: ARC, dues, gate, and local links pages
- `documents/`: downloadable HOA documents and forms
- `board/`: board roster
- `contact/`: contact details and map
- `assets/`: stylesheet, images, and downloadable PDF files

## Run tests

```bash
python3 -m unittest discover -s tests
```

## Deploy on GitHub Pages

1. Push this repository to GitHub.
2. In repository `Settings`, open `Pages`.
3. Set the source to `Deploy from a branch`.
4. Select the `main` branch and the `/ (root)` folder.
5. If you want to use `brookescrossing.com` as the custom domain, set that in GitHub Pages and update DNS to point at GitHub Pages.
