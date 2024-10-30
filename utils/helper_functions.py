import fitz
from tqdm.auto import tqdm

def open_and_read_pdf(pdf_path: str) -> list[dict]:
    """
    Opens the pdf, creates a list of dictionaries for each page, and returns the list
    """
    document = fitz.open(pdf_path)
    pages_and_texts = []
    for page_number, page in tqdm(enumerate(document)):
        text = page.get_text()
        text = format_text(input=text)
        pages_and_texts.append({
                "page_number": page_number,
                "page_char_count": len(text),
                "page_word_count": len(text.split(" ")),
                "page_sentence_count_raw": len(text.split(". ")),
                "page_token_count": len(text) / 4,
                "text": text  
        })
        
    return pages_and_texts

def format_text(input: str) -> str:
    """
    Performs text formatting and returns formatted text
    """
    cleaned_text = input.replace("hello world", "Hello World").strip()

    return cleaned_text