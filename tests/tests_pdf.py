from deepdiff import DeepDiff

from helper import extract_words


def test_pdf():
    assert extract_words('test_task.pdf') == extract_words('test_task.pdf')


def test_pdf2():
    right_pdf = extract_words('test_task.pdf')
    wrong_pdf = extract_words('wrong_file.pdf')
    assert right_pdf == wrong_pdf, f"Values are not equal. Diff: {DeepDiff(right_pdf, wrong_pdf)}"


