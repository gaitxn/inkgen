# Handwritten Text Engine

A lightweight Python engine that procedurally generates realistic handwriting from plain text. By utilizing mathematical representations (such as Bézier curves) for characters and ligatures, it creates custom, high-fidelity handwriting for any document, design, or digital application.

---

## Features

- **Procedural Generation:** Converts plain-text strings and generator instructions into fluid, handwritten graphical output.
- **Bézier Curve Interpolation:** Uses precise mathematical curves and vectorization (via NumPy) to simulate natural pen strokes.
- **Custom Ligatures & Glyphs:** Supports custom structural definitions for characters and continuous connections between them.
- **Stochastic Variations:** Incorporates natural hand tremors and variations to prevent robotic, repetitive patterns.
- **Lightweight Dependencies:** Built cleanly using Python, NumPy, and Pillow.

---

## Requirements

Ensure you have Python 3 installed on your system. You will also need the following libraries:

- `numpy`
- `pillow`

---

## Installation

1. Clone the repository:
```bash
git clone [https://github.com/gaitxn/inkgen.git](https://github.com/gaitxn/inkgen.git)
```

2. Install the required dependencies:

```bash
pip install numpy pillow
```

3. Usage
Run the main script or interpreter to process your instruction files and generate the handwritten output image:

```bash
python main.py
```
4. Provide the path to your generator instruction file when prompted, and customize your stroke properties as needed.

## Project Structure
```plaintext
inkgen/
│
├── data/               # Glyph and font configuration data
│   ├── glyphs/         # Character and ligature instruction files
│   └── fonts/          # Style configurations (stroke width, jitter, etc.)
│
├── src/                # Core engine source code
│   ├── parser.py       # Instruction file interpreter
│   ├── renderer.py     # Image plotting and curve rendering
│   └── variations.py   # Stochastic pulse and tremor adjustments
│
├── outputs/            # Generated output images
├── main.py             # Entry point script
├── LICENSE.txt         # Project license terms
└── README.md           # Project documentation
```

## Contributing
Contributions, feature suggestions, and pull requests are welcome! Feel free to open an issue or submit a PR if you would like to improve the stroke rendering algorithm or add new glyph sets.

## License

This project is licensed under the **MIT License** — see the [LICENSE.txt](LICENSE.txt) file for details.

Copyright (c) 2026 Daniel Gaitán Alzate
