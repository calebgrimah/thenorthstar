#!/usr/bin/env python3
"""Check generated pages, assets, links and fragments without extra dependencies."""
import argparse
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


class Page(HTMLParser):
    def __init__(self, source):
        super().__init__()
        self.ids = set()
        self.duplicates = set()
        self.links = []
        self.h1s = 0
        self.redirect = False
        self.feed(source)

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if 'id' in attrs:
            if attrs['id'] in self.ids:
                self.duplicates.add(attrs['id'])
            self.ids.add(attrs['id'])
        if tag == 'h1':
            self.h1s += 1
        if tag == 'meta' and attrs.get('http-equiv', '').lower() == 'refresh':
            self.redirect = True
        if tag in ('a', 'link', 'img', 'script', 'source'):
            for attribute in ('href', 'src'):
                if attribute in attrs:
                    self.links.append(attrs[attribute])
            if 'srcset' in attrs:
                self.links.extend(item.strip().split()[0] for item in attrs['srcset'].split(','))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('directory', nargs='?', default='_site')
    parser.add_argument('--baseurl', default='')
    args = parser.parse_args()
    root = Path(args.directory).resolve()
    pages = {path: Page(path.read_text()) for path in root.rglob('*.html')}
    errors = []
    if not pages:
        errors.append('No built pages found; run bundle exec jekyll build first.')
    for path, page in pages.items():
        name = path.relative_to(root)
        if not page.redirect and page.h1s != 1:
            errors.append(f'{name}: expected one h1, found {page.h1s}')
        if page.duplicates:
            errors.append(f'{name}: duplicate IDs: {page.duplicates}')
        for link in page.links:
            url = urlsplit(link)
            if url.scheme or url.netloc:
                continue
            if not link:
                errors.append(f'{name}: empty resource URL')
                continue
            target_path = unquote(url.path)
            if args.baseurl and target_path.startswith('/'):
                if not target_path.startswith(args.baseurl + '/'):
                    errors.append(f'{name}: URL misses baseurl: {link}')
                    continue
                target_path = target_path[len(args.baseurl):]
            target = (root / target_path.lstrip('/')) if target_path.startswith('/') else (path.parent / target_path if target_path else path)
            target = target.resolve()
            if target.is_dir():
                target /= 'index.html'
            if not target.exists():
                errors.append(f'{name}: missing target: {link}')
            elif url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
                errors.append(f'{name}: missing anchor: {link}')
    if errors:
        print('\n'.join(errors))
        raise SystemExit(1)
    print(f'Passed: {len(pages)} pages; assets, links, fragments, headings and IDs.')


if __name__ == '__main__':
    main()
