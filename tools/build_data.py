"""Regenerate the inlined data in baltic-language-atlas.html from data/*.json.

JSON is the golden source. The HTML holds one line `const D = {...};` with
the map geometry (kept as is) plus langs, nodes, contacts and pl, built here.

  uv run tools/build_data.py          # rewrite the HTML
  uv run tools/build_data.py --check  # exit 1 if the HTML is out of sync
"""
import json, math, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / 'baltic-language-atlas'
HTML = ROOT / 'baltic-language-atlas.html'
FILES = ['uralic', 'baltoslavic', 'others']
NODE_ORDER = ['uralic', 'others', 'baltoslavic']  # tree roots are laid out in this order
PREFIX = 'const D = '
# Lambert conformal conic of the inlined map (same constants as LCC in the 3D module)
LCC = dict(n=.842481, k=2128.293, ax=499.643, ay=-429.697, lon0=math.radians(24))
# colour group = first of these tree nodes found in a language's lineage
GROUP_NODES = [('finnic', 'finnic'), ('sami', 'sami'), ('baltic', 'baltic'), ('slavic', 'slavic'),
               ('germanic', 'germanic'), ('italic', 'romance'), ('turkic', 'turkic'), ('uralic', 'uralic')]


def project(lat, lon):
    r = LCC['k'] * math.tan(math.pi / 4 - math.radians(lat) / 2) ** LCC['n']
    t = LCC['n'] * (math.radians(lon) - LCC['lon0'])
    return round(LCC['ax'] + r * math.sin(t), 1), round(LCC['ay'] + r * math.cos(t), 1)


def build(old_geo):
    data = {f: json.loads((ROOT / 'data' / f'{f}.json').read_text(encoding='utf-8')) for f in FILES}
    nodes = [n for f in NODE_ORDER for n in data[f]['nodes']]
    parent = {n['id']: n['parent'] for n in nodes}
    langs = []
    for f in FILES:
        for l in data[f]['languages']:
            chain, p = [], l['parent']
            while p:
                chain.append(p); p = parent[p]
            out = {k: v for k, v in l.items() if k not in ('lat', 'lon')}
            out['g'] = next(g for node, g in GROUP_NODES if node in chain)
            out['x'], out['y'] = project(l['lat'], l['lon'])
            langs.append(out)
    return {'geo': old_geo, 'langs': langs, 'nodes': nodes,
            'contacts': data['others']['contacts'], 'pl': data['baltoslavic']['polish_lithuanian']}


def main():
    html = HTML.read_text(encoding='utf-8')
    lines = html.split('\n')
    i = next(i for i, s in enumerate(lines) if s.startswith(PREFIX))
    old = json.loads(lines[i][len(PREFIX):].rstrip().rstrip(';'))
    new = build(old['geo'])
    if '--check' in sys.argv:
        bad = [k for k in new if new[k] != old.get(k)]
        print('in sync' if not bad else f'OUT OF SYNC: {bad} (run uv run tools/build_data.py)')
        sys.exit(1 if bad else 0)
    lines[i] = PREFIX + json.dumps(new, ensure_ascii=False, separators=(',', ':')) + ';'
    HTML.write_text('\n'.join(lines), encoding='utf-8')
    print(f'wrote {HTML.name}: {len(new["langs"])} languages, {len(new["nodes"])} nodes, '
          f'{len(new["contacts"])} contacts, {len(new["pl"])} notes')


if __name__ == '__main__':
    main()
