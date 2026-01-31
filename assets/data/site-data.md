---
# LIFTS Site Data - Single Source of Truth
# Edit values here, then run: python build.py
# Last Updated: 2026-01-31

# =============================================================================
# ORGANIZATION
# =============================================================================
organization:
  name: "LIFTS"
  full_name: "Launch Initiatives for Technologies in Space"
  type: "Student Aerospace Research Organization"
  institution: "University of Puerto Rico at Mayagüez"
  institution_short: "UPRM"
  website: "lifts-uprm.github.io"
  email: "lifts@uprm.edu"
  founded: "January 2024"

# =============================================================================
# TEAM
# =============================================================================
team:
  member_count: 17
  member_count_display: "17+"

# =============================================================================
# AGGREGATE STATISTICS
# =============================================================================
stats:
  missions_completed: 1
  missions_planned: 2
  max_altitude_ft: 95000
  max_altitude_display: "95K+"
  recovery_rate: "100%"

# =============================================================================
# MISSIONS
# =============================================================================
missions:
  # ---------------------------------------------------------------------------
  # NEXO Mission (Completed)
  # ---------------------------------------------------------------------------
  nexo:
    name: "NEXO"
    full_name: "Space Navigator for Exploration and Observation"
    status: "completed"
    status_display: "Completed"
    date: "2024-04-08"
    date_display: "April 8, 2024"
    date_month: "APR"
    date_day: "08"
    date_year: "2024"
    location: "Austin, TX"
    location_full: "Austin, TX (Smilin V Scout Ranch)"
    launch_time: "12:30 p.m."
    max_altitude_ft: 95000
    max_altitude_display: "95,000 ft"
    flight_duration: "3.5 hours"
    flight_duration_tracked: "~4.5 hours (tracked)"
    recovery_location: "Tyler, TX"
    recovery_distance: "~200 miles"
    recovery_status: "Recovered intact"

  # ---------------------------------------------------------------------------
  # ASCENT Mission (Upcoming)
  # ---------------------------------------------------------------------------
  ascent:
    name: "ASCENT"
    full_name: "Advanced Science Carrier for Environmental and Near-space Technology"
    status: "upcoming"
    status_display: "Upcoming"
    date: "2026-03-14"
    date_display: "March 14, 2026"
    date_iso: "2026-03-14T00:00:00"
    date_month: "MAR"
    date_day: "14"
    date_year: "2026"
    location: "Mayagüez, PR"
    location_full: "TBD, Puerto Rico"
    target_altitude_ft: 100000
    target_altitude_display: "100,000+ ft"
    target_altitude_short: "100,000 ft"
    est_flight_time: "~3 hours"
    payload_mass_kg: 2.5
    payload_mass_display: "2.5 kg"
    payload_count: 5
    payload_count_display: "5 modules"

  # ---------------------------------------------------------------------------
  # CubeSat Program (In Progress)
  # ---------------------------------------------------------------------------
  cubesat:
    name: "CubeSat Program"
    status: "in-progress"
    status_display: "In Progress"
    form_factor: "1U CubeSat"
    dimensions: "10×10×10 cm"
    mass: "<1.33 kg"
    target_orbit: "LEO (400km)"
    target_orbit_altitude: "~400 km LEO"
    mission_life: "~1 year"
    est_launch_year: 2028
    est_launch_year_display: "2028"

# =============================================================================
# PROGRAMS (General Capabilities)
# =============================================================================
programs:
  hab:
    name: "High-Altitude Balloon (HAB) Program"
    max_altitude_ft: 100000
    max_altitude_display: "100,000+ feet (30+ km)"
    payload_capacity_lbs: 6
    payload_capacity_display: "Up to 6 lbs"
    flight_duration: "2-3 hours typical"

  sounding_rocket:
    name: "Sounding Rocket Program"
    propulsion: "Solid fuel motors"
    target_altitude_ft: 10000
    target_altitude_display: "10,000+ feet"

# =============================================================================
# SOCIAL MEDIA
# =============================================================================
social:
  twitter: "@LIFTS_UPRM"
  instagram: "@lifts_uprm"
  instagram_url: "https://www.instagram.com/liftspr.uprm/"
  linkedin: "LIFTS UPRM"
  linkedin_url: "https://www.linkedin.com/company/liftsuprm"
  youtube: "LIFTS Space"
  youtube_url: "https://www.youtube.com/@LIFTS_UPRM"

# =============================================================================
# CONTACT
# =============================================================================
contact:
  general_email: "lifts@upr.edu"
  media_email: "media@lifts.uprm.edu"
  info_email: "info@lifts.uprm.edu"

# =============================================================================
# DOCUMENT METADATA
# =============================================================================
docs:
  version: "1.0"
  last_updated: "January 2026"
---

# LIFTS Site Data

This file contains all centralized numeric and date values for the LIFTS website.

## Usage

1. Edit the YAML front matter above to update any values
2. Run `python build.py` from the repository root
3. The script will update all HTML files with the new values
4. Commit and push changes to deploy

## Placeholder Syntax

In HTML files, use `{{ key.path }}` syntax:
- `{{ stats.missions_completed }}` → 1
- `{{ missions.ascent.date_display }}` → March 14, 2026
- `{{ team.member_count_display }}` → 17+

## Notes

- All dates use ISO 8601 format for the `date` field
- `_display` suffix variants are pre-formatted for display
- The `date_iso` field is used for JavaScript countdown timers
