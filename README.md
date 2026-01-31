# LIFTS Website

A SpaceX-inspired website for Launch Initiatives for Technologies in Space (LIFTS) at UPRM.

## Project Structure

```
Website/
├── index.html              # Home page
├── missions.html           # Missions hub
├── launches.html           # Launch schedule
├── updates.html            # News/blog
├── careers.html            # Join the team
├── about.html              # About LIFTS
├── contact.html            # Contact form
├── privacy.html            # Privacy policy
├── contributors.html       # Contributors
│
├── # Mission Detail Pages
├── nexo.html               # NEXO mission
├── ascent.html             # ASCENT mission
├── cubesat.html            # CubeSat program
│
├── # Stylesheets
├── main.css                # Primary stylesheet (new design)
├── styles.css              # Legacy styles
├── about.css               # Legacy about styles
├── missions.css            # Legacy mission styles
├── legal.css               # Legal page styles
│
├── scripts/
│   ├── main.js             # Primary JavaScript
│   ├── nav.js              # Legacy navigation
│   ├── popup.js            # Popup functionality
│   └── scroll.js           # Scroll effects
│
├── fonts/
│   └── d-din/              # D-DIN font files
│
├── images/
│   ├── logo/               # Logo variations
│   ├── missions/           # Mission photos
│   ├── team/               # Team photos
│   ├── gallery/            # Gallery images
│   └── backgrounds/        # Hero backgrounds
│
└── assets/
    └── documents/          # PDFs, press kit, etc.
```

## Pages Overview

| Page | File | Description |
|------|------|-------------|
| Home | `index.html` | Hero, countdown, mission highlights |
| Missions | `missions.html` | Filterable mission grid |
| Launches | `launches.html` | Schedule and timeline |
| Updates | `updates.html` | News and announcements |
| Careers | `careers.html` | Open positions |
| About | `about.html` | History, team, partners |
| Contact | `contact.html` | Form, FAQ, support |
| NEXO | `nexo.html` | First mission (completed) |
| ASCENT | `ascent.html` | Upcoming mission |
| CubeSat | `cubesat.html` | Satellite program |

## Design System

- **Primary Font:** D-DIN
- **Background:** #000000
- **Text:** #ffffff / #a0a0a0
- **Accent:** #ffffff

## Build System

The website uses a Python-based static site generator to centralize numeric data (dates, statistics, mission parameters) in a single YAML file.

### Setup

```bash
# Install dependencies (one time)
pip install -r requirements.txt
```

### Editing Site Data

All numeric values (dates, heights, team counts, etc.) are defined in:

```
assets/data/site-data.md
```

Edit the YAML front matter in that file to update any values.

### Building the Site

After editing `site-data.md`, run the build script:

```bash
# Build site (replaces placeholders in HTML with values from site-data.md)
python build.py

# Preview changes without writing (dry run)
python build.py --dry-run

# Show detailed replacement info
python build.py --verbose

# Only validate placeholders (no changes)
python build.py --validate
```

The script will:
1. Parse YAML data from `assets/data/site-data.md`
2. Replace all `{{ key.path }}` placeholders in HTML files
3. Generate `scripts/site-data.js` for JavaScript access (countdown timer)
4. Validate that all placeholders have matching data keys

### Placeholder Syntax

In HTML files, use `{{ key.path }}` syntax:
```html
<span>{{ missions.ascent.date_display }}</span>  <!-- March 14, 2026 -->
<span>{{ stats.missions_completed }}</span>       <!-- 1 -->
<span>{{ team.member_count_display }}</span>      <!-- 17+ -->
```

### Workflow

1. Edit `assets/data/site-data.md`
2. Run `python build.py`
3. Test locally (open HTML files in browser)
4. Commit and push to deploy to GitHub Pages

## Development

Open `index.html` in a browser or use Live Server extension.

## Image Placeholders

Currently using Unsplash images. Replace with actual LIFTS photos:
- Hero backgrounds
- Mission photos
- Team portraits
- Gallery images

## TODO

- [ ] Replace placeholder images with actual photos
- [ ] Add team member bios and photos
- [ ] Create press kit PDF
- [ ] Add mission videos
- [ ] Set up form backend
- [ ] Add analytics
