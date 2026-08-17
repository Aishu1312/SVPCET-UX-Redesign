# SVPCET UX Redesign

> **Premium UX/UI redesign prototype of the SVPCET website using HCI principles, Nielsen's heuristics, responsive design, accessibility, and Python Streamlit.**

## Project Overview

This repository contains an academically defensible UX/UI redesign of the official St. Vincent Pallotti College of Engineering and Technology (SVPCET) website. It transforms the digital experience into an exceptionally polished, modern, responsive, and accessible prototype built entirely with Python and Streamlit.

**Academic Context:** UDSA — User Design and System Analysis (Teacher Assessment-01)
**Topic:** Usability Evaluation and Prototype Redesign of an Engineering College Website

---

## Problem Statement

The existing SVPCET website suffered from several usability issues, including overlapping modals, hidden navigation, poor scannability of academic programs, and accessibility concerns. This project identifies these issues through rigorous UX research and resolves them systematically in a functional prototype.

---

## Objectives

- Perform a Heuristic Evaluation on the existing portal.
- Redesign the UI to reflect a premium institutional digital experience.
- Implement responsive, mobile-first design methodologies.
- Enhance accessibility (contrast, typography hierarchy, clear CTAs).
- Provide a clear traceability matrix mapping design decisions to identified UX issues.

---

## Usability Evaluation & The 10 Usability Issues

An interactive evaluation dashboard is built directly into the application (`9_UX_Evaluation.py`). The identified issues are:

| ID | Existing Problem | Prototype Solution |
|----|------------------|--------------------|
| UX-01 | Overlapping modals/popups | Clean, non-blocking interface |
| UX-02 | Competing admission buttons | One strong primary Admissions CTA |
| UX-03 | Navigation hidden behind Menu | Persistent primary navigation |
| UX-04 | Cluttered hero section | Strong visual hierarchy |
| UX-05 | Poor programme scannability | Consistent programme cards |
| UX-06 | Weak notices | Filterable notices |
| UX-07 | No prominent search | Highly visible search |
| UX-08 | Contrast problems | Accessible high-contrast design |
| UX-09 | Poor mobile experience | Responsive mobile-first layout |
| UX-10 | Ungrouped footer | Structured footer |

---

## Proposed Solutions & UX Traceability

Every major component maps to a specific usability issue, establishing clear UX traceability:
- **Navbar / Footer**: Addresses UX-03 (Navigation visibility) and UX-10 (Footer grouping).
- **Hero & CTAs**: Addresses UX-01 (Modals) and UX-04 (Clutter). Consolidates CTA (UX-02).
- **Program & Notice Search**: Addresses UX-05, UX-06, and UX-07 (Scannability and Search capability).
- **Color & Layout**: Addresses UX-08 (Contrast) and UX-09 (Responsiveness).

---

## Key Features

- **Multi-page Architecture**: Separate, clean views for Academics, Admissions, Placements, and more.
- **Dynamic Search**: Instant filtering for academic programs and notices.
- **Interactive Dashboards**: Embedded UX evaluation and "Before & After" case studies.
- **Custom Design System**: Injected via `styles/main.css`.

---

## Design System

- **Typography**: `Outfit` (Headings) and `Inter` (Body).
- **Primary Brand**: Deep Institutional Blue (`#0a3d62`) and Accent Orange (`#e58e26`).
- **Layout Framework**: Responsive CSS Grid and Flexbox injected into Streamlit.

---

## Accessibility & Responsive Design

- High-contrast colors adhere to modern WCAG recommendations.
- UI elements gracefully degrade and stack on mobile viewports.
- Clear button affordances and hover states.

---

## Before & After & Screenshots

Check the `10_Before_After.py` page in the deployed app for detailed case studies comparing the existing design against this prototype. 

*(Note: Screenshots are stored in the `screenshots/` directory).*

---

## Tech Stack

- **Framework**: Streamlit (Python)
- **Styling**: Vanilla CSS (CSS Variables)
- **Data Handling**: Native Python JSON processing

---

## Installation

### Local Setup

Clone the repository and set up a virtual environment:

```bash
git clone <repository-url>
cd SVPCET-UX-Redesign
python -m venv venv
```

Activate the virtual environment:
- Windows: `venv\Scripts\activate`
- macOS/Linux: `source venv/bin/activate`

Install dependencies:
```bash
pip install -r requirements.txt
```

Run the application locally:
```bash
streamlit run app.py
```
Open `http://localhost:8501` in your browser.

---

## Deployment

### Streamlit Community Cloud

This project is fully deployment-ready for Streamlit Community Cloud.
1. Log in to Streamlit Community Cloud.
2. Connect your GitHub account.
3. Select this repository and the `main` branch.
4. Set the main file path to `app.py`.
5. Click **Deploy**.

*(No environment variables are strictly required for this prototype unless you add custom external APIs).*

---

## Academic Disclaimer

> **Academic Prototype:** This project is a UX/UI redesign created for UDSA Teacher Assessment-01. It is an academic prototype and is not an official replacement for the St. Vincent Pallotti College of Engineering and Technology website. All data is for mock/prototyping purposes.

---

## Author
Prepared for **UDSA Teacher Assessment-01**.
