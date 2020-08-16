with open('test_session5.py', 'r') as f:
    lines = f.readlines()

    doc_string = []
    is_docstring = False
    for line in lines:
        if 'def ' in line:
            doc_string.append('\n')
            doc_string.append('**{}**\n'.format(line.strip()[4:-1].replace('*', '\*')))
            doc_string.append('\n')

        if '\"\"\"' == line.strip():
            is_docstring = False if is_docstring else True

        if is_docstring and not '\"\"\"' == line.strip():
            doc_string.append(line)

    formatted_doc_string = []
    for line in doc_string:
        formatted_line = line.replace(':', ' : ')
        formatted_doc_string.append(formatted_line)

    with open('temp_readme.md', 'w+') as f1:
        f1.writelines(formatted_doc_string)
