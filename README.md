# 🔳 QR Code Toolkit

A small Python toolkit for **generating** and **decoding** QR codes.
Built with [`qrcode`](https://github.com/lincolnloop/python-qrcode) and [`pyzbar`](https://github.com/NaturalHistoryMuseum/pyzbar).

---

## ✨ Features

- **Simple QR generation** — one-liner to create a QR code from any text/URL
- **Advanced QR generation** — control version, error correction, colors, and output folder
- **QR decoding** — read and print the content of any QR image
- **SVG support** — scalable vector output (commented example included)

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/EhsanLarian/qr-code-toolkit.git
cd qr-code-toolkit
```

### 2. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 3. Install the `zbar` system library (required by `pyzbar`)

| OS | Command |
|----|---------|
| Ubuntu / Debian | `sudo apt install libzbar0` |
| macOS | `brew install zbar` |
| Windows | Already bundled with `pyzbar` — no action needed |

---

## 🚀 Usage

### Generate a simple QR code

```bash
python src/simple_qr.py
```

**Output:** `simple_qr.png` in the current directory — encodes `https://www.google.com`.

### Generate a customized QR code

```bash
python src/generate_qr.py
```

**Output:** `generated_qrcodes/custom_qr.png` — black-on-lightyellow, high error correction, auto-sized.

To change the content, edit this line in `src/generate_qr.py`:

```python
qr.add_data('https://www.python.org')
```

To change colors:

```python
img = qr.make_image(fill_color="black", back_color="lightyellow")
```

### Decode an existing QR code

```bash
python src/decode_qr.py
```

**Prerequisite:** The image path inside `decode_qr.py` must exist. By default it looks for:

```
generated_qrcodes/python_01.png
```

Either:
- Rename/copy your QR image to that path, **or**
- Change this line in `src/decode_qr.py`:

```python
img = Image.open('generated_qrcodes/python_01.png')
```

**Output example:**

```
Type: QRCODE
Data: https://www.python.org
```

---

## 🗂️ Project Structure

```
qr-code-toolkit/
├── src/
│   ├── generate_qr.py     # Customizable QR generator
│   ├── simple_qr.py       # Minimal QR generator
│   └── decode_qr.py       # QR decoder
├── examples/
│   └── sample_outputs/    # Sample generated images
├── generated_qrcodes/     # Default output folder
├── requirements.txt
└── README.md
```

---

## ⚙️ Configuration Reference

### `generate_qr.py` parameters

| Parameter | Meaning | Default |
|-----------|---------|---------|
| `version` | QR size (1–40). `None` = auto | `None` |
| `error_correction` | Recovery level (L, M, Q, H) | `H` (~30%) |
| `box_size` | Pixels per module | `10` |
| `border` | Quiet zone (in boxes) | `4` |
| `fill_color` / `back_color` | Foreground / background colors | `black` / `lightyellow` |

### Error correction levels

| Level | Recovery capacity |
|-------|-------------------|
| `L` | ~7% |
| `M` | ~15% |
| `Q` | ~25% |
| `H` | ~30% ✅ (used here) |

---

## 🧪 Testing

Decode the generated QR code to verify correctness:

```bash
python src/generate_qr.py
# then point decode_qr.py to the output file and run:
python src/decode_qr.py
```

---

## ⚠️ Known Limitations

- Input paths are **hardcoded** — edit the scripts or extend them to accept CLI arguments (see *Roadmap*).
- `simple_qr.py` uses the default error correction level (`M`), which is fine for clean images but less robust than `H`.
- Only **UTF-8** text payloads are decoded.

---

## 🛣️ Roadmap (Optional Improvements)

- [ ] Add `argparse` so scripts accept `--data`, `--output`, `--color` flags
- [ ] Support **batch generation** from a CSV file
- [ ] Add **SVG export** as a runtime option (already drafted as comments)
- [ ] Add unit tests with `pytest`
- [ ] Support **Wi-Fi / vCard / email** payload formats
- [ ] Add `--decode-all` to scan a folder of images

---

## 📜 License

MIT License — feel free to use, modify, and share.