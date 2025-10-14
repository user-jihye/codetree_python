#!/usr/bin/env python3
import sys
import os
import re
import pyperclip


def convert_to_snake_case(text):
    """하이픈(-)을 언더스코어(_)로 바꾸고 소문자로 변환"""
    return text.replace('-', '_').lower()


def extract_file_name_from_url(url):
    """URL에서 문제 이름 부분만 추출"""
    match = re.search(r'/([^/]+)/[^/]+$', url)
    if match:
        return convert_to_snake_case(match.group(1))
    return None


def is_valid_codetree_url(url):
    """CodeTree URL인지 확인"""
    return url.startswith('https://www.codetree.ai/')


def format_number(num):
    """번호를 항상 두 자리로 포맷"""
    return f"{int(num):02d}"


def create_python_file(trail_num, chapter_num, lesson_num, url):
    if not is_valid_codetree_url(url):
        print("❌ Error: Clipboard does not contain a valid CodeTree URL")
        sys.exit(1)

    file_name = extract_file_name_from_url(url)
    if not file_name:
        print(f"❌ Could not extract file name from URL: {url}")
        return

    # 경로 생성
    dir_path = os.path.join(f"trail{format_number(trail_num)}",
                            f"chapter{format_number(chapter_num)}",
                            f"lesson{format_number(lesson_num)}")
    os.makedirs(dir_path, exist_ok=True)

    # 파일 경로
    py_file = os.path.join(dir_path, f"{file_name}.py")

    # 파일 생성
    with open(py_file, 'w', encoding='utf-8') as f:
        f.write(f'"""\n@see <{url}>\n"""\n\n')

    print(f"✅ Created Python file at: {py_file}")


def main():
    if len(sys.argv) != 4:
        print("Usage: python create_file.py <trail_number> <chapter_number> <lesson_number>")
        sys.exit(1)

    trail_num = sys.argv[1]
    chapter_num = sys.argv[2]
    lesson_num = sys.argv[3]
    url = pyperclip.paste().strip()

    create_python_file(trail_num, chapter_num, lesson_num, url)


if __name__ == "__main__":
    main()
