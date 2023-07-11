import os

import fitz


def parser(span, extracted_info, key):
    font_size = span['size']
    font_name = span['font']
    font_color = span['color']
    flags = span['flags']
    ascender = span['ascender']
    descender = span['descender']
    origin = span['origin']

    extracted_info.update({key: {
        'Размер шрифта': round(font_size, 1),
        'Шрифт': font_name,
        'Цвет шрифта': font_color,
        'Флаги (формат шрифта)': flags,
        'Верхняя граница шрифта': round(ascender, 1),
        'Нижняя граница шрифта': round(descender, 1),
        'Точка отсчета': tuple(round(num, 1) for num in origin)
    }})


def extract_words(file_name):
    script_path = os.path.abspath(__file__)
    project_path = os.path.dirname(script_path)
    pdfs_path = os.path.join(project_path, 'pdfData')
    document_path = os.path.join(pdfs_path, file_name)
    with fitz.open(document_path) as doc:  # добавлен менеджер контекста
        extracted_info = {}
        for page in doc:
            text = page.get_text('dict')
            for block in text['blocks']:
                for line in block['lines']:
                    for span in line['spans']:
                        if block == text['blocks'][0]:
                            parser(span, extracted_info, key=span['text'])
                        elif ':' in span['text']:
                            key, value = span['text'].split(':')
                            parser(span, extracted_info, key=key)
    return extracted_info



