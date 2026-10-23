# Intro Linked

**Your profile picture is your introduction.** Intro Linked is a proof-of-concept professional profile where a short video plays inside the round profile-picture slot. When the clip ends, its final frame remains as your profile photo.

**[View the source on GitHub](https://github.com/LSyria/intro-linked)**

## What the demo does

- Professional profile for Leonard Syriaque, including About, Experience, and Skills.
- Video embedded directly in the round profile-picture area.
- Muted autoplay when browser policy permits, with tap to hear/replay.
- Video freezes on its final frame instead of disappearing.
- Record or upload a real introduction (up to 30 seconds) from a supported device.
- Responsive desktop and mobile layout.
- Example synthetic placeholder clip and original demo portrait embedded in the page.

## Run it

The entire demo lives in **`index.html`** (HTML, CSS, JavaScript, and demonstration media are embedded).

Open `index.html` in a modern browser, or run:

```bash
python3 -m http.server 8000
```

Visit http://localhost:8000.

## GitHub Pages

A GitHub Actions workflow is included at `.github/workflows/pages.yml`.

1. Go to **Settings → Pages** in the repository.
2. Choose **GitHub Actions** under *Build and deployment*.
3. In **Actions**, run **Deploy Intro Linked to GitHub Pages**, or push a new commit to `main`.
4. Once deployment succeeds, the expected address is https://lsyria.github.io/intro-linked/ (not live until GitHub confirms deployment).

**Privacy:** This repository was created public. The code includes a user's real photo and professional history. GitHub Pages will also be publicly accessible once enabled.

## Demo limitations

The demonstration contains an 8-second *synthetic placeholder*; it is **not a recording of Leonard speaking**. A real video recording can replace it inside the UI. Uploaded videos stay in the visitor's browser memory and **are not stored, uploaded to a server, or shared with other visitors**. There is no authentication, database, LinkedIn integration, or public profile publishing yet. Contact/Connect/Share are demonstration actions. Browser autoplay and microphone/camera behavior vary.

## Development

```bash
python3 -m unittest discover -s tests -v
```

See [the roadmap](docs/ROADMAP.md) for the next development stages.

## Independence and usage

Intro Linked is an independent concept and is **not affiliated with, endorsed by, or integrated with LinkedIn**. Do not scrape or mirror LinkedIn accounts. The included headshot is a user-supplied demo asset and is **not stock photography**. No reuse license is granted for the person’s likeness.
