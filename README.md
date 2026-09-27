# Python MCQ Quiz

A responsive, browser-based quiz about Python control flow and functions. The quiz was created from the supplied Python quiz and keeps its original 10 questions, answer key, one-point scoring, and performance thresholds.

## Features

- 10 multiple-choice questions, shown one at a time
- Clickable A/B/C/D answer options with immediate feedback
- Progress bar and live score
- Final score, percentage, correct and incorrect answer counts
- Performance messages based on the score:
  - 80% or higher: **Excellent!**
  - 60% or higher: **Good!**
  - 40% or higher: **Keep Practicing!**
  - Below 40%: **Need More Practice!**
- Restart button to take the quiz again
- Responsive layout for phones, tablets, and desktop screens
- No installation or build step required

## Run locally

1. Download or clone this repository.
2. Open `index.html` in a web browser.
3. Select **Start quiz** to begin.

The quiz works without a server. An internet connection is only needed to load the optional Google Fonts; system fonts are used as a fallback.

## Project files

| File | Purpose |
| --- | --- |
| `index.html` | Page content and quiz screens |
| `style.css` | Responsive layout, colors, and visual styling |
| `script.js` | Questions, answer handling, scoring, and results |

## Built with

- HTML
- CSS
- Vanilla JavaScript

## Quiz details

Each correct answer earns 1 point. Incorrect answers do not subtract points. The quiz displays the correct answer after each response and calculates the final percentage out of 10.

## License

No license has been specified. Add a `LICENSE` file if you want others to have explicit permission to reuse or modify this project.
