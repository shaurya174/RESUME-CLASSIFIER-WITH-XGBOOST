from pathlib import Path
import csv
import fitz  # PyMuPDF


# Project structure expected:
# RESUME CLASSIFIER/
# └── DATA/
#     ├── extractor.py
#     ├── Resume.csv          <- created by this script
#     └── data/
#         ├── HR/
#         │   ├── 16852973.pdf
#         │   └── ...
#         ├── ACCOUNTANT/
#         └── ...

BASE_DIR = Path(__file__).resolve().parent
PDF_ROOT = BASE_DIR / "data"
OUTPUT_FILE = BASE_DIR / "Resume.csv"


COLUMNS = ["ID", "Resume_str", "Resume_html", "Category"]


def extract_pdf(pdf_path: Path) -> tuple[str, str]:
    """Extract plain text and HTML from a PDF using PyMuPDF."""
    doc = fitz.open(pdf_path)

    text_pages = []
    html_pages = []

    try:
        for page in doc:
            text_pages.append(page.get_text("text"))
            html_pages.append(page.get_text("html"))
    finally:
        doc.close()

    resume_str = "\n".join(text_pages).strip()
    resume_html = "\n".join(html_pages).strip()

    return resume_str, resume_html


def main() -> None:
    if not PDF_ROOT.is_dir():
        raise FileNotFoundError(f"PDF data folder not found: {PDF_ROOT}")

    rows = []

    # Every subfolder under DATA/data is treated as a category.
    for category_dir in sorted(PDF_ROOT.iterdir()):
        if not category_dir.is_dir():
            continue

        category = category_dir.name

        for pdf_path in sorted(category_dir.glob("*.pdf")):
            # PDF filename becomes the resume ID, e.g. 16852973.pdf -> 16852973
            id_value = pdf_path.stem
            try:
                id_value = int(id_value)
            except ValueError:
                pass

            try:
                resume_str, resume_html = extract_pdf(pdf_path)

                rows.append({
                    "ID": id_value,
                    "Resume_str": resume_str,
                    "Resume_html": resume_html,
                    "Category": category,
                })

                print(f"Extracted: {pdf_path.relative_to(BASE_DIR)}")

            except Exception as exc:
                print(f"Skipped: {pdf_path} | Error: {exc}")

    with OUTPUT_FILE.open(
        "w",
        encoding="utf-8-sig",
        newline="",
    ) as file:
        writer = csv.DictWriter(
            file,
            fieldnames=COLUMNS,
            quoting=csv.QUOTE_ALL,
        )
        writer.writeheader()
        writer.writerows(rows)

    print("\nExtraction complete.")
    print(f"Total resumes: {len(rows)}")
    print(f"Output file: {OUTPUT_FILE}")
    print(f"Columns: {COLUMNS}")


if __name__ == "__main__":
    main()