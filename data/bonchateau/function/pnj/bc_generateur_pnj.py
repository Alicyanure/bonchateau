#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BONCHATEAU - Générateur de PNJ v2.2
Version : 1.21 avec cycle jour/nuit
"""

import csv
import re
import math
from pathlib import Path

# ============================================
# CONFIGURATION
# ============================================

ITEM_NAMESPACE = {
    "medium_amethyst_bud": "minecraft:medium_amethyst_bud",
    "small_amethyst_bud": "minecraft:small_amethyst_bud",
    "large_amethyst_bud": "minecraft:large_amethyst_bud",
    "amethyst_cluster": "minecraft:amethyst_cluster",
    "nether_star": "minecraft:nether_star",
    "golden_helmet": "minecraft:golden_helmet",
    "golden_chestplate": "minecraft:golden_chestplate",
    "golden_leggings": "minecraft:golden_leggings",
    "golden_boots": "minecraft:golden_boots",
    "diamond_helmet": "minecraft:diamond_helmet",
    "diamond_chestplate": "minecraft:diamond_chestplate",
    "diamond_leggings": "minecraft:diamond_leggings",
    "diamond_boots": "minecraft:diamond_boots",
    "cod": "minecraft:cod",
    "morue": "minecraft:cod",
    "string": "minecraft:string",
    "fil": "minecraft:string",
    "bread": "minecraft:bread",
    "pain": "minecraft:bread",
}

MONNAIES_BONCHATEAU = {
    "minecraft:small_amethyst_bud":  {"nom": "Pert",          "valeur": 0.11},
    "minecraft:medium_amethyst_bud": {"nom": "Peore",         "valeur": 1},
    "minecraft:large_amethyst_bud":  {"nom": "Pedisme",       "valeur": 9},
    "minecraft:amethyst_cluster":    {"nom": "Penausme",      "valeur": 81},
    "minecraft:nether_star":         {"nom": "Penerethisme",  "valeur": 729},
}

# ============================================
# HELPERS : construction de composants NBT
# ============================================

def _monnaie_components(item_id):
    """Retourne la chaîne components pour une monnaie."""
    info = MONNAIES_BONCHATEAU[item_id]
    nom = info["nom"]
    valeur = info["valeur"]
    return (
        f'components:{{"minecraft:custom_name":\'{{\"text\":\"{nom}\",\"color\":\"light_purple\",\"italic\":false}}\','
        f'"minecraft:lore":[\'{{\"text\":\"Monnaie\",\"color\":\"gray\",\"italic\":false}}\'],'
        f'"minecraft:custom_data":{{bonchateau_monnaie:"{nom.lower()}",bonchateau_valeur:{valeur}}}}}'
    )

def _custom_name(nom):
    nom = nom.replace("'", "\\'")
    return '"minecraft:custom_name":' + "'{\"text\":\"" + nom + "\"}'"

def _lore(texte):
    texte = texte.replace("'", "\\'")
    return '"minecraft:lore":' + "['{\"text\":\"" + texte + '","color":"gray","italic":false}\']'

def _enchantments(enchants_dict):
    """enchants_dict = {"sharpness": "4", "unbreaking": "2", ...}"""
    inner = ",".join(f"{k}:{v}" for k, v in enchants_dict.items())
    return f'"minecraft:enchantments":{{{inner}}}'

# ============================================
# CONVERSION NBT 1.20.4 → 1.21
# ============================================

def convertir_enchantments(enchantments_str):
    """
    Convertit [{id:sharpness,lvl:4},{id:unbreaking,lvl:2}]
    vers {"sharpness": "4", "unbreaking": "2"}
    """
    pattern = r'\{id:"?(?:minecraft:)?([a-z_]+)"?,lvl:(\d+)\}'
    matches = re.findall(pattern, enchantments_str)
    if not matches:
        print("⚠️  Aucun enchantement trouvé dans :", enchantments_str)
    return {eid: lvl for eid, lvl in matches}


def convertir_tag_vers_components(nbt):
    """
    Convertit toutes les occurrences de l'ancienne syntaxe tag:{...} vers
    la nouvelle syntaxe components:{...} pour Minecraft 1.21.

    Cas gérés :
      A) tag:{display:{Name:"X",Lore:["L"]},Enchantments:[...]}
      B) tag:{display:{Name:"X"},Enchantments:[...]}
      C) tag:{display:{Name:"X",Lore:["L"]}}
      D) tag:{display:{Name:"X"}}
    """

    # ------------------------------------------------------------------ #
    # Regex qui capture les 3 groupes optionnels dans n'importe quel ordre:
    #   group(1) : contenu brut de Name:"..."
    #   group(2) : contenu brut de Lore:[...] (optionnel)
    #   group(3) : contenu brut de Enchantments:[...] (optionnel)
    #
    # On accepte Name ET Lore dans n'importe quel ordre à l'intérieur de
    # display:{...}, puis Enchantments optionnel après display.
    # ------------------------------------------------------------------ #

    def parse_one_tag(match_str):
        """
        Reçoit le contenu ENTRE les accolades de tag:{...}
        et retourne la chaîne components:{...} équivalente.
        """
        # --- Extraire Name ---
        # Après nettoyage CSV, les guillemets sont doublés : Name:""Epée...""
        # On accepte 1 ou 2 guillemets ouvrants/fermants autour du nom réel.
        m_name = re.search(r'Name:"+"([^"]+)"+"', match_str)
        nom = m_name.group(1).strip() if m_name else ""

        # --- Extraire Lore (premier élément) ---
        m_lore = re.search(r'Lore:\[""([^"]+)""', match_str)
        if not m_lore:
            m_lore = re.search(r'Lore:\["([^"]+)"', match_str)
        lore = m_lore.group(1).strip() if m_lore else None

        # --- Extraire Enchantments ---
        m_ench = re.search(r'Enchantments:(\[[^\]]+\])', match_str)
        enchants = convertir_enchantments(m_ench.group(1)) if m_ench else {}

        # --- Construire components ---
        parts = [_custom_name(nom)]
        if lore:
            parts.append(_lore(lore))
        if enchants:
            parts.append(_enchantments(enchants))

        return "components:{" + ",".join(parts) + "}"

    # On cherche tag:{ ... } en comptant les accolades pour délimiter
    # correctement (évite les problèmes de regex gourmandes).
    result = []
    i = 0
    while i < len(nbt):
        # Chercher la prochaine occurrence de "tag:{"
        m = re.search(r'tag:\{', nbt[i:])
        if not m:
            result.append(nbt[i:])
            break

        start = i + m.start()
        result.append(nbt[i:start])       # tout ce qui précède

        # Trouver la fermeture de l'accolade en comptant la profondeur
        depth = 0
        j = start + len("tag:")           # pointe sur '{'
        end = j
        while end < len(nbt):
            if nbt[end] == '{':
                depth += 1
            elif nbt[end] == '}':
                depth -= 1
                if depth == 0:
                    end += 1
                    break
            end += 1

        tag_content = nbt[j:end]          # "{display:{...},...}"
        inner = tag_content[1:-1]         # sans les accolades externes

        result.append(parse_one_tag(inner))
        i = end

    return "".join(result)


def ajouter_namespace_item(match):
    """Ajoute le namespace minecraft: aux IDs d'items."""
    item_id = match.group(1)
    if item_id in ITEM_NAMESPACE:
        return f'id:"{ITEM_NAMESPACE[item_id]}"'
    return f'id:"minecraft:{item_id}"'


def ajouter_components_monnaies_dans_nbt(nbt):
    """
    Détecte les items monnaie sans components dans buy/buyB/sell
    et ajoute automatiquement custom_name + lore + custom_data.
    """
    pattern = (
        r'(buy(?:B)?|sell):'
        r'(\{id:"(minecraft:(?:small|medium|large)_amethyst_bud'
        r'|minecraft:amethyst_cluster|minecraft:nether_star)",count:(\d+)\})'
    )

    def remplacer_monnaie(match):
        champ   = match.group(1)
        item_id = match.group(3)
        count   = match.group(4)
        if item_id in MONNAIES_BONCHATEAU:
            return f'{champ}:{{id:"{item_id}",count:{count},{_monnaie_components(item_id)}}}'
        return match.group(0)

    return re.sub(pattern, remplacer_monnaie, nbt)


def equilibrer_accolades(nbt):
    """Retire les '}' terminaux en trop si le NBT est déséquilibré.
    Certaines lignes CSV ont un '}' superflu à la fin (ex: }]}} au lieu de }]}).
    """
    depth = 0
    last_balanced = len(nbt)
    for i, c in enumerate(nbt):
        if c == '{':
            depth += 1
        elif c == '}':
            depth -= 1
            if depth == 0:
                last_balanced = i + 1
    return nbt[:last_balanced]


def convertir_nbt_1_20_vers_1_21(nbt):
    """Convertit un NBT format 1.20.4 vers format 1.21."""
    # Nettoyer les échappements CSV
    nbt = nbt.replace('\\"', '"')
    # Count → count
    nbt = re.sub(r'\bCount:', 'count:', nbt)
    # Ajouter namespace minecraft:
    nbt = re.sub(r'id:([a-z_]+)', ajouter_namespace_item, nbt)
    # Convertir tag → components
    nbt = convertir_tag_vers_components(nbt)
    # Retirer les } terminaux en trop (déséquilibre fréquent dans le CSV)
    nbt = equilibrer_accolades(nbt)
    return nbt

# ============================================
# PARSING FORMAT SIMPLIFIÉ
# ============================================

MONNAIE_MAPPING = {
    "pert":          "minecraft:small_amethyst_bud",
    "peore":         "minecraft:medium_amethyst_bud",
    "pedisme":       "minecraft:large_amethyst_bud",
    "penausme":      "minecraft:amethyst_cluster",
    "penerethisme":  "minecraft:nether_star",
}

def _build_monnaie_nbt(champ, item_id, count):
    return f'{champ}:{{id:"{item_id}",count:{count},{_monnaie_components(item_id)}}}'


def parser_ventes_simplifiees(ventes_str):
    """
    Parse le format simplifié : morue:2,peore:1+pert:3|fil:1,pert:5
    Retourne le NBT Offers complet.
    """
    if not ventes_str or ventes_str.strip() == "":
        return "Offers:{Recipes:[]}"

    ventes = []
    for vente_bloc in ventes_str.split("|"):
        vente_bloc = vente_bloc.strip()
        if not vente_bloc:
            continue

        parties = vente_bloc.split(",")
        objet_parts = parties[0].split(":")
        objet_nom = objet_parts[0].strip()
        objet_quantite = int(objet_parts[1].strip())
        objet_id = ITEM_NAMESPACE.get(objet_nom, f"minecraft:{objet_nom}")

        monnaies_raw = ",".join(parties[1:])
        monnaies = []
        for bloc in monnaies_raw.split("+"):
            bloc = bloc.strip()
            parts = bloc.split(":")
            nom_monnaie = parts[0].strip().lower()
            qte = int(parts[1].strip())
            item_id = MONNAIE_MAPPING.get(nom_monnaie, f"minecraft:{nom_monnaie}")
            monnaies.append((item_id, qte))

        if len(monnaies) == 1:
            buy  = _build_monnaie_nbt("buy", monnaies[0][0], monnaies[0][1])
            buyB = ""
        elif len(monnaies) == 2:
            buy  = _build_monnaie_nbt("buy",  monnaies[0][0], monnaies[0][1])
            buyB = "," + _build_monnaie_nbt("buyB", monnaies[1][0], monnaies[1][1])
        else:
            continue  # plus de 2 monnaies non supporté

        sell = f'sell:{{id:"{objet_id}",count:{objet_quantite}}}'
        ventes.append(f'{{{buy}{buyB},{sell},maxUses:999999,uses:0,rewardExp:0b}}')

    return f"Offers:{{Recipes:[{','.join(ventes)}]}}"

# ============================================
# GÉNÉRATION DES SUMMONS
# ============================================

NIVEAU_MAPPING = {
    "novice": 1, "apprenti": 2, "compagnon": 3,
    "expert": 4, "maitre": 5, "master": 5,
}


def generer_summon_pnj(pnj, moment="jour"):
    """Génère la commande summon pour un PNJ."""
    id_pnj        = pnj["id_pnj"]
    nom           = pnj["nom"]
    metier        = pnj["metier"]
    age           = pnj["age"]
    biome         = pnj["biome"]
    ventes_raw    = pnj["ventes"]
    rotation_jour = pnj.get("rotation_jour", "").strip()
    niveau_texte  = pnj["niveau"]

    lieu   = pnj["lieu_jour"] if moment == "jour" else pnj["lieu_nuit"]
    x, y, z = lieu.split()
    rotation = f"[{rotation_jour}]" if rotation_jour and moment == "jour" else "[0f,0f]"
    niveau   = NIVEAU_MAPPING.get(niveau_texte.lower(), 5)

    est_enfant          = age.lower() == "enfant"
    est_adulte          = age.lower() == "adulte"
    est_nitwit          = metier.lower() == "nitwit"
    est_banquier_depot  = metier.lower() == "banquier_depot"
    est_banquier_retrait = metier.lower() == "banquier_retrait"

    tags = ['"pnj_bonchateau"', f'"pnj_{id_pnj}"']
    if est_enfant:
        tags.append('"pnj_enfant"')
        print(id_pnj + " est ENFANT !")
    if est_adulte:
        tags.append('"pnj_adulte"')
        print(id_pnj + " est ADULTE !")
    if est_nitwit:
        tags.append('"pnj_nitwit"')
        print(id_pnj + " est NITWIT !")
    if est_banquier_depot:
        tags.append('"banquier_depot"')
        print(id_pnj + " est banquier_depot !")
        metier = "cartographer"
    if est_banquier_retrait:
        tags.append('"banquier_retrait"')
        print(id_pnj + " est banquier_retrait !")
        return None  # géré par generer_banquier_retrait_double

    no_ai = "0b" if (est_enfant or est_nitwit or moment == "nuit") else "1b"

    # --- Ventes ---
    if moment == "nuit":
        offers_nbt = "Offers:{Recipes:[]}"
    elif est_banquier_depot:
        offers_nbt = "Offers:{Recipes:[]}"
    elif ventes_raw.startswith("Offers:"):
        offers_nbt = convertir_nbt_1_20_vers_1_21(ventes_raw)
        offers_nbt = ajouter_components_monnaies_dans_nbt(offers_nbt)
    else:
        offers_nbt = parser_ventes_simplifiees(ventes_raw)

    tags_str = f"Tags:[{','.join(tags)}]"

    if est_enfant:
        return (
            f'summon minecraft:villager {x} {y} {z} '
            f'{{{tags_str},Age:-1000000,'
            f'CustomName:\'{{\"text\":\"{nom}\",\"color\":\"white\"}}\','
            f'CustomNameVisible:0b,Invulnerable:1b,PersistenceRequired:1b,'
            f'VillagerData:{{type:{biome}}}}}'
        )
    else:
        return (
            f'summon minecraft:villager {x} {y} {z} '
            f'{{{tags_str},'
            f'CustomName:\'{{\"text\":\"{nom}\",\"color\":\"white\"}}\','
            f'CustomNameVisible:0b,NoAI:{no_ai},Invulnerable:1b,'
            f'PersistenceRequired:1b,Silent:1b,Rotation:{rotation},'
            f'VillagerData:{{profession:"minecraft:{metier}",level:{niveau},type:"minecraft:{biome}"}},'
            f'{offers_nbt}{"}"}'
        )


def generer_banquier_retrait_double(pnj, moment="jour"):
    """Génère 2 summons (visible + interaction) pour le banquier retrait."""
    coords = pnj["lieu_jour" if moment == "jour" else "lieu_nuit"].split()
    x, y, z = float(coords[0]), coords[1], float(coords[2])
    rotation_raw = pnj.get("rotation_jour", "0f,0f").strip().strip('"') or "0f,0f"
    nom    = pnj["nom"]
    id_pnj = pnj["id_pnj"]
    biome  = pnj["biome"]

    yaw      = float(rotation_raw.split(',')[0].replace('f', ''))
    offset_x = -0.2 * math.sin(math.radians(yaw))
    offset_z =  0.2 * math.cos(math.radians(yaw))

    if moment == "jour":
        summon1 = (
            f'summon minecraft:villager {x} {y} {z} '
            f'{{Tags:["pnj_bonchateau","pnj_{id_pnj}_visuel","banquier_retrait_visuel"],'
            f'CustomName:\'{{\"text\":\"{nom}\",\"color\":\"white\",\"bold\":true}}\','
            f'CustomNameVisible:0b,NoAI:1b,Invulnerable:1b,PersistenceRequired:1b,Silent:1b,'
            f'Rotation:[{rotation_raw}],'
            f'VillagerData:{{profession:"minecraft:cartographer",level:5,type:"minecraft:{biome}"}},'
            f'Offers:{{Recipes:[]}}}}'
        )
        print(id_pnj + " est banquier_retrait_visuel !")
        x2, z2 = x + offset_x, z + offset_z
        summon2 = (
            f'summon minecraft:villager {x2} {y} {z2} '
            f'{{Tags:["pnj_bonchateau","pnj_{id_pnj}_interaction","banquier_retrait","pnj_adulte"],'
            f'CustomName:\'{{\"text\":\"{nom}banquier\",\"color\":\"white\",\"bold\":true}}\','
            f'CustomNameVisible:0b,NoAI:1b,PersistenceRequired:1b,Silent:1b,'
            f'VillagerData:{{profession:"minecraft:none",type:"minecraft:{biome}"}},'
            f'Offers:{{Recipes:[]}},'
            f'active_effects:['
            f'{{id:"minecraft:invisibility",amplifier:0,duration:-1,show_particles:0b}},'
            f'{{id:"minecraft:regeneration",amplifier:255,duration:-1,show_particles:0b}},'
            f'{{id:"minecraft:resistance",amplifier:255,duration:-1,show_particles:0b}}'
            f']}}'
        )
        print(id_pnj + " est banquier_retrait !")
        return [summon1, summon2]
    else:
        summon = (
            f'summon minecraft:villager {x} {y} {z} '
            f'{{Tags:["pnj_bonchateau","pnj_{id_pnj}","pnj_adulte"],'
            f'CustomName:\'{{\"text\":\"{nom}\",\"color\":\"white\",\"bold\":true}}\','
            f'CustomNameVisible:0b,NoAI:0b,Invulnerable:1b,PersistenceRequired:1b,Silent:1b,'
            f'VillagerData:{{profession:"minecraft:cartographer",level:5,type:"minecraft:{biome}"}},'
            f'Offers:{{Recipes:[]}}}}'
        )
        print(id_pnj + " est banquier_retrait !")
        return [summon]

# ============================================
# GÉNÉRATION DES FICHIERS
# ============================================

def generer_fichiers_mcfunction():
    csv_path = Path(__file__).parent / "bc_pnj_import.csv"

    print("=" * 60)
    print("BONCHATEAU - Générateur de PNJ v2.2")
    print("=" * 60)
    print(f"📖 Lecture du fichier CSV : {csv_path}")

    pnjs = []
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=";")
        for row in reader:
            pnjs.append(row)

    print(f"✅ {len(pnjs)} PNJ(s) trouvé(s)")

    # ---- Helpers fichier ----

    def header(titre, extra=""):
        lines = [
            "# ============================================",
            f"# BONCHATEAU - {titre}",
            "# Généré automatiquement depuis bc_pnj_import.csv",
            "# NE PAS MODIFIER MANUELLEMENT",
            "# ============================================",
        ]
        if extra:
            lines.append(f"# {extra}")
        lines += ["", "# Supprimer tous les PNJ existants"]
        return lines

    def footer(msg):
        return [
            "",
            "# ============================================",
            "# FIN DU FICHIER",
            "# ============================================",
            f'tellraw @a {{"text":"§a✔ {msg}"}}',
        ]

    def ecrire(path, lines):
        with open(path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        print(f"✅ Fichier généré : {path}")

    def ajouter_pnj(lines, pnj, moment):
        if pnj["metier"].lower() == "banquier_retrait":
            lines.append(f"# BANQUIER RETRAIT : {pnj['nom']} (double)")
            for s in generer_banquier_retrait_double(pnj, moment):
                lines.append(s)
        else:
            summon = generer_summon_pnj(pnj, moment)
            if summon:
                lines.append(f"# PNJ : {pnj['nom']} ({pnj['id_pnj']})")
                lines.append(summon)
        lines.append("")

    # ---- spawn_jour ----
    print("\n🌅 Génération spawn_jour.mcfunction...")
    lines = header("Spawn PNJ (JOUR)")
    lines.append("kill @e[type=minecraft:villager,tag=pnj_bonchateau]")
    lines.append("")
    for pnj in pnjs:
        ajouter_pnj(lines, pnj, "jour")
    lines += footer(f"{len(pnjs)} PNJ(s) spawné(s) (mode JOUR)")
    ecrire(Path(__file__).parent / "spawn_jour.mcfunction", lines)

    # ---- spawn_nuit ----
    print("\n🌙 Génération spawn_nuit.mcfunction...")
    lines = header("Spawn PNJ (NUIT)", "⚠️ La nuit, les PNJ n'ont AUCUN trade (Offers vides)")
    lines.append("kill @e[type=minecraft:villager,tag=pnj_bonchateau]")
    lines.append("")
    for pnj in pnjs:
        ajouter_pnj(lines, pnj, "nuit")
    lines += footer(f"{len(pnjs)} PNJ(s) spawné(s) (mode NUIT - sans trades)")
    ecrire(Path(__file__).parent / "spawn_nuit.mcfunction", lines)

    # ---- spawn_samedi_matin ----
    print("\n📅 Génération spawn_samedi_matin.mcfunction...")
    lines = header("Spawn PNJ SAMEDI MATIN", "Samedi : Seuls les adultes travaillent")
    lines.append("kill @e[type=minecraft:villager,tag=pnj_bonchateau,tag=pnj_adulte]")
    lines.append("")
    adultes = 0
    for pnj in pnjs:
        if pnj["age"].lower() != "enfant":
            ajouter_pnj(lines, pnj, "jour")
            adultes += 1
    lines += footer(f"{adultes} adulte(s) au travail (enfants libres)")
    ecrire(Path(__file__).parent / "spawn_samedi_matin.mcfunction", lines)

    # ---- cycle_jour_nuit ----
    print("\n🔄 Génération cycle_jour_nuit.mcfunction...")
    cycle_lines = [
        "# ============================================",
        "# BONCHATEAU - Cycle jour/nuit des PNJ",
        "# ============================================",
        "# Appelé depuis tick.mcfunction",
        "",
        "# MATIN (2000 ticks)",
        "execute if score temps_minecraft bonchateau_time matches 2000 if score @a[limit=1] jour matches 1..5 run function bonchateau:pnj/spawn_jour",
        "execute if score temps_minecraft bonchateau_time matches 2000 if score @a[limit=1] jour matches 6 run function bonchateau:pnj/spawn_samedi_matin",
        "execute if score temps_minecraft bonchateau_time matches 2000 if score @a[limit=1] jour matches 7 run function bonchateau:pnj/spawn_dimanche_matin",
        "",
        "# Incrémenter le jour à minuit",
        "execute if score temps_minecraft bonchateau_time matches 0 run function bonchateau:system/incrementer_jour",
        "",
        "# SOIR (12000 ticks)",
        "execute if score temps_minecraft bonchateau_time matches 12000 run function bonchateau:pnj/spawn_nuit",
    ]
    ecrire(Path(__file__).parent / "cycle_jour_nuit.mcfunction", cycle_lines)

    print("\n" + "=" * 60)
    print("✅ GÉNÉRATION TERMINÉE")
    print("=" * 60)
    print(f"📊 {len(pnjs)} PNJ(s) traités — 4 fichiers générés")
    print("=" * 60)


if __name__ == "__main__":
    generer_fichiers_mcfunction()
