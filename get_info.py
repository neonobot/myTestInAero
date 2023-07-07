import fitz

from helper import parser


def get_all_info_about_file(pdf_path):
    doc = fitz.open(pdf_path)
    extracted_info = {}
    for page in doc:
        text = page.get_text('dict')
        for block in text['blocks']:
            for line in block['lines']:
                for span in line['spans']:
                    key = span['text']
                    parser(span, extracted_info, key=key)

    return extracted_info


# Пример использования
pdf_path = 'pdfData/test_task.pdf'
extracted_text = get_all_info_about_file(pdf_path)
print(extracted_text)
