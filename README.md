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
