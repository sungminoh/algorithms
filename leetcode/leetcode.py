#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""
from collections import ChainMap
from pathlib import Path
import html
import json
import os
import re
import sys
import functools
import itertools
from concurrent.futures import ThreadPoolExecutor

import requests
import html2markdown


DATUM = [
    {"query":"\n    query questionContent($titleSlug: String!) {\n  question(titleSlug: $titleSlug) {\n    content\n    mysqlSchemas\n    dataSchemas\n  }\n}\n    ","operationName":"questionContent"},
    {"query":"\n    query questionTitle($titleSlug: String!) {\n  question(titleSlug: $titleSlug) {\n    questionId\n    questionFrontendId\n    title\n    titleSlug\n    isPaidOnly\n    difficulty\n    likes\n    dislikes\n    categoryTitle\n  }\n}\n    ","operationName":"questionTitle"},
    {"query":"\n    query questionStats($titleSlug: String!) {\n  question(titleSlug: $titleSlug) {\n    stats\n  }\n}\n    ","operationName":"questionStats"},
    {"query":"\n    query questionEditorData($titleSlug: String!) {\n  question(titleSlug: $titleSlug) {\n    questionId\n    questionFrontendId\n    codeSnippets {\n      lang\n      langSlug\n      code\n    }\n    envInfo\n    enableRunCode\n    hasFrontendPreview\n    frontendPreviews\n  }\n}\n    ","operationName":"questionEditorData"}
]


TEMPLATE = '''
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
{content}
"""
import pytest
import sys


{code}
        pass


@pytest.mark.parametrize('args', [
])
def test(args):
    assert args[-1] == Solution()(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
'''


def construct_header(url):
    header = {
        'authority': 'leetcode.com',
        'accept': '*/*',
        'sec-fetch-dest': 'empty',
        # 'x-csrftoken': resp.cookies['csrftoken'],
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/80.0.3987.122 Safari/537.36',
        'content-type': 'application/json',
        'origin': 'https://leetcode.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'accept-language': 'en-US,en;q=0.9,ko;q=0.8',
        'referer': url,
    }
    return header


def fetch(url):
    parts = url.split('/')
    title = parts[parts.index('problems') + 1]
    headers = construct_header(url)
    futs = []
    pool = ThreadPoolExecutor()
    for d in DATUM:
        data = {**d, 'variables': {'titleSlug': title}}
        futs.append(pool.submit(requests.post, url='https://leetcode.com/graphql', headers=headers, data=json.dumps(data)))
    return ChainMap(*[fut.result().json()['data']['question'] for fut in futs])


def convert_stat_table(stat):
    accepted = stat['totalAcceptedRaw']
    submission = stat['totalSubmissionRaw']
    rate = stat['acRate']
    ret = ( '| Submissions    | Accepted     | Rate   |\n'
            '| -------------- | ------------ | ------ |\n'
           f'| {submission:,} | {accepted:,} | {rate} |')
    return ret


def convert_html_tags(text):
    text = html.unescape(text)
    code_block = re.compile('<pre>(.*?)</pre>', re.DOTALL)
    for code in code_block.findall(text):
        text = text.replace(code, re.compile('<strong>|</strong>').sub('', code))

    replacements = [
        (re.compile(r'<pre>|</pre>'), '```'),
    ]
    for pattern, replacement in replacements:
        text = pattern.sub(replacement, text)

    invalid_code_tag = re.compile(r'(([^\n])```)')
    for p, w in re.findall(invalid_code_tag, text):
        text = re.sub(p, f'{w}\n```', text)
    return text


def remove_html_tags(text):
    text = html.unescape(text)
    replacements = [
        (re.compile(r'\r'), ''),
        (re.compile(r'<[^<]*?>'), ''),
        (re.compile(r'\n\s*\n'), '\n\n'),
    ]
    for pattern, replacement in replacements:
        text = pattern.sub(replacement, text)
    return text


def pack_problem(url):
    data = fetch(url)
    qid = data['questionId']
    title = data['title']
    difficulty = data['difficulty']
    stat = json.loads(data['stats'])
    content = data['content']
    md = html2markdown.convert(content)
    md = convert_html_tags(md)

    d = Path(f'{qid}_{title.replace(" ", "_")}')
    d.mkdir()
    with open(d/'README.md', 'w') as f:
        f.write(f'### [{qid}. {title}]({url})\n\n')
        f.write(f'{difficulty}\n\n')
        f.write(f'{md}\n\n')
        f.write(convert_stat_table(stat))

    code = [s for s in data['codeSnippets'] if s['lang'] == 'Python3'][0]['code']
    with open(d/'solution.py', 'w') as f:
        f.write(TEMPLATE.format(content=remove_html_tags(content).strip(),
                                code=code.strip()).strip())


def main(url):
    pack_problem(url)


if __name__ == '__main__':
    main(sys.argv[1])
