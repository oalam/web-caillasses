#!/usr/bin/env python3
"""
Générateur de site statique pour 'Les Caillasses'
Convertit les fichiers Markdown de content/ en pages HTML statiques.
Sans dépendance externe (uniquement la bibliothèque standard Python 3).
"""

import os
import re
import sys

def parse_frontmatter(text):
    """Extrait le frontmatter YAML et le corps markdown."""
    frontmatter = {}
    content = text
    
    if text.startswith('---'):
        parts = text.split('---', 2)
        if len(parts) >= 3:
            raw_meta = parts[1].strip()
            content = parts[2].strip()
            for line in raw_meta.splitlines():
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                if ':' in line:
                    k, v = line.split(':', 1)
                    frontmatter[k.strip()] = v.strip().strip('"\'')
                    
    return frontmatter, content

def markdown_to_html(md_text):
    """
    Convertit du markdown simple en HTML sans dépendance externe.
    Gère les titres, paragraphes, listes, liens, gras, italique et HTML brut.
    """
    lines = md_text.split('\n')
    output = []
    in_list = False
    
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        
        # Lignes vides
        if not stripped:
            if in_list:
                output.append('</ul>')
                in_list = False
            i += 1
            continue
            
        # Si c'est du HTML brut (balise ouvrante ou fermante)
        if stripped.startswith('<') and not stripped.startswith('<http'):
            if in_list:
                output.append('</ul>')
                in_list = False
            output.append(line)
            i += 1
            continue
            
        # Titres Markdown (#, ##, ###)
        if stripped.startswith('### '):
            if in_list: output.append('</ul>'); in_list = False
            content = stripped[4:]
            output.append(f'<h3>{inline_format(content)}</h3>')
            i += 1
            continue
        elif stripped.startswith('## '):
            if in_list: output.append('</ul>'); in_list = False
            content = stripped[3:]
            output.append(f'<h2>{inline_format(content)}</h2>')
            i += 1
            continue
        elif stripped.startswith('# '):
            if in_list: output.append('</ul>'); in_list = False
            content = stripped[2:]
            output.append(f'<h1>{inline_format(content)}</h1>')
            i += 1
            continue
            
        # Éléments de liste (- ou *)
        if stripped.startswith('- ') or stripped.startswith('* '):
            if not in_list:
                output.append('<ul>')
                in_list = True
            item_text = stripped[2:]
            output.append(f'  <li>{inline_format(item_text)}</li>')
            i += 1
            continue
        else:
            if in_list:
                output.append('</ul>')
                in_list = False
                
        # Paragraphes normaux
        output.append(f'<p>{inline_format(stripped)}</p>')
        i += 1
        
    if in_list:
        output.append('</ul>')
        
    return '\n'.join(output)

def inline_format(text):
    """Formate les balises inline : gras, italique, liens."""
    # Gras : **texte**
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    # Italique : *texte*
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    
    # Liens : [texte](url)
    def link_repl(match):
        label = match.group(1)
        url = match.group(2)
        if url.startswith('http'):
            return f'<a href="{url}" target="_blank" rel="noopener">{label}</a>'
        return f'<a href="{url}">{label}</a>'
        
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', link_repl, text)
    return text

def render_template(template_str, context):
    """Rend un template HTML simple avec remplacement de variables et blocs if."""
    # Gestion des blocs {% if var %}...{% endif %}
    def if_repl(match):
        var_name = match.group(1).strip()
        inner_content = match.group(2)
        val = context.get(var_name)
        if val:
            return inner_content
        return ''
        
    pattern = re.compile(r'\{%\s*if\s+([a-zA-Z0-9_]+)\s*%\}(.*?)\{%\s*endif\s*%\}', re.DOTALL)
    rendered = pattern.sub(if_repl, template_str)
    
    # Remplacement des variables {{ var }}
    for k, v in context.items():
        rendered = rendered.replace(f'{{{{ {k} }}}}', str(v))
        rendered = rendered.replace(f'{{{{{k}}}}}', str(v))
        
    # Nettoyage des variables non définies
    rendered = re.sub(r'\{\{\s*[a-zA-Z0-9_]+\s*\}\}', '', rendered)
    return rendered

def build_site():
    """Génère tous les fichiers HTML du site à partir de content/."""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    content_dir = os.path.join(base_dir, 'content')
    templates_dir = os.path.join(base_dir, 'templates')
    
    base_template_path = os.path.join(templates_dir, 'base.html')
    if not os.path.exists(base_template_path):
        print(f"Erreur : gabarit introuvable à {base_template_path}")
        sys.exit(1)
        
    with open(base_template_path, 'r', encoding='utf-8') as f:
        base_template = f.read()
        
    # Association fichier source markdown -> fichier de sortie HTML
    pages_map = {
        'accueil.md': 'index.html',
        'les-cours.md': 'les-cours.html',
        'la-salle.md': 'la-salle.html',
        'info-falaises.md': 'info-falaises.html',
        'autres-activites.md': 'autres-activites.html',
        'historique.md': 'historique.html',
    }
    
    print("=== Construction du site 'Les Caillasses' ===")
    
    for src_name, out_name in pages_map.items():
        src_path = os.path.join(content_dir, src_name)
        if not os.path.exists(src_path):
            print(f"Avertissement : fichier manquant {src_name}")
            continue
            
        with open(src_path, 'r', encoding='utf-8') as f:
            raw_text = f.read()
            
        meta, md_body = parse_frontmatter(raw_text)
        
        # Contexte pour le gabarit
        context = {
            'title': meta.get('title', 'Les Caillasses'),
            'subtitle': meta.get('subtitle', ''),
            'meta_title': meta.get('meta_title', 'Les caillasses'),
            'meta_description': meta.get('meta_description', "Club d'escalade Les caillasses à Die"),
            'hero_image': meta.get('hero_image', 'assets/images/hero-diois.jpg'),
            'lead': meta.get('lead', ''),
            'content': markdown_to_html(md_body),
            'active_accueil': 'active' if out_name in ['index.html', 'les-cours.html', 'la-salle.html', 'info-falaises.html', 'autres-activites.html'] else '',
            'active_index': 'active' if out_name == 'index.html' else '',
            'active_cours': 'active' if out_name == 'les-cours.html' else '',
            'active_salle': 'active' if out_name == 'la-salle.html' else '',
            'active_falaises': 'active' if out_name == 'info-falaises.html' else '',
            'active_autres': 'active' if out_name == 'autres-activites.html' else '',
            'active_historique': 'active' if out_name == 'historique.html' else '',
        }
        
        html_out = render_template(base_template, context)
        out_path = os.path.join(base_dir, out_name)
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(html_out)
            
        print(f"✓ Généré : {out_name} depuis content/{src_name}")
        
    print("\n✓ Site généré avec succès !")

if __name__ == '__main__':
    build_site()
