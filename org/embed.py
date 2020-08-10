#!/usr/bin/env python3

import os
import re
import sys
import json
import glob
import pprint


def main():
    argv = sys.argv
    json = None
    exe = argv[0]
    argv.pop(0)
    if argv:
        if os.path.splitext(argv[0])[1] == '.json':
            json = argv[0]
            argv.pop(0)
    files = argv
    if not files:
        files = [os.path.splitext(os.path.basename(f))[0]
                 for f in sorted(glob.glob("md_enorg/*.md"))]
    for base in files:
        sub(base, json)


def sub(base, json_path=None):
    input_path = f"md_enorg/{base}.md"
    json_path = json_path or f"tex_jpx/{base}.json"
    output_path = f"md_en/{base}.md"
    log_path = f"embed_log/{base}.json"
    print(f"{base}")
    embed(input_path, json_path, output_path, log_path)


def embed(input_path, json_path, output_path, log_path):
    with open(input_path) as f:
        doc = f.read()

    with open(json_path) as f:
        dic = json.load(f)

    log = {"imath": {}, "emath": {}, "tabular": {}}
    doc = replace_emath(doc, dic, log["emath"])
    doc = replace_imath(doc, dic, log["imath"])
    doc = process_table(doc, log["tabular"])

    with open(output_path, "w") as fo:
        fo.write(doc)

    with open(log_path, "w") as fo:
        json.dump(log, fo, indent=4)


def replace_imath(doc, dic, log):
    # TERMと数字の間のスペースを削除
    doc = re.sub(r"(TERM) (\d{5})", r"\1\2", doc)

    for key, value in dic["imath"].items():
        text = math2str(value[0])

        # "TERM00000 and TERM00000" と "TERM00000,TERM00000" を置換
        pattern = key + r"(?:(,|,?\s+and\s)\s*" + key + ")+"
        count = len(re.findall(pattern, doc))
        if count >= 2:
            log[key] = {"count": count, "text": text}  # 複数個マッチした
        if count >= 1:
            doc = re.sub(pattern, escape(text), doc)
            # # uncomment below to leave orphaned terms
            # continue

        # "TERM00000" を置換
        mcount = count
        pattern = key
        count = len(re.findall(pattern, doc))
        if count >= 1 and mcount >= 1:
            print(f"Warning: possibly inconsistent translation around {key}={text}.")
        if count >= 2:
            log[key] = {"count": count, "text": text}  # 複数個マッチした
        if count >= 1:
            doc = re.sub(pattern, escape(text), doc)
        elif mcount == 0:
            log[key] = {"count": count, "text": text}  # マッチしなかった
    return doc


def replace_emath(doc, dic, log):
    for key, value in dic["emath"].items():
        text = f"$$\n{math2str(value)}\n$$\n"
        pattern = r".*?" + key + r".*?"
        count = len(re.findall(pattern, doc))
        if count == 0:
            log[key] = {"count": count, "text": text}  # マッチしなかった
            continue
        # print(key)
        doc = re.sub(pattern, escape(text), doc, 1)
        if count > 1:
            doc = re.sub(pattern, "", doc)  # 2行目以降は空行にする
    return doc


def math2str(v):
    text = math2str_sub(v)
    # 空行削除
    return "\n".join([line for line in text.split('\n') if line.strip() != ''])


def math2str_sub(v):
    if isinstance(v, str):
        if v == "&":  # 単体の&があるとエラーになるので空白に置き換える
            return ""
        if v == r"\nonumber":
            return ""
        if v == r"\Dvect":
            return r"\mathbf"
        if v == r"\boldmath":
            return r"\mathbf"
        if v == r"\cal":
            return r"\mathcal"
        if v == r"\mbox":
            return ""
        if v == r"\sl":
            return r"\mathit"
        if v == r"\lefteqn":
            return ""
        if v == "\u3000":  # 全角スペース
            return " "
        return v

    for index, value in enumerate(v):
        if value == r"\DP":
            v[index] = r"\frac"
            v[index + 1].insert(1, r"\partial ")
            v[index + 2].insert(1, r"\partial ")
        if value == r"\DD":
            v[index] = r"\frac"
            v[index + 1].insert(1, r"d")
            v[index + 2].insert(1, r"d")
        if value == r"\label":
            v[index] = ""
            v[index + 1] = ""

    return "".join([math2str_sub(value) for value in v])


def escape(text):
    a = repr(text)[1:-1]
    # print(a)
    return a


def process_table(doc, log):
    output_flag = []
    insert_flag = []
    table_cache = {}
    in_table = False
    lines = doc.split("\n")
    for line in lines:
        m = re.search(r"TAB\d{5}:\d+.\d+", line)
        if m is not None:
            mstr = m.group()
            table_id = int(mstr[3:8])
            row, column = [int(s) for s in mstr[9:].split(".")]
            output_flag.append(False)
            in_table = True
            if row == 0 and column == 0:
                insert_flag.append(table_id)
            else:
                insert_flag.append(None)
                for i in range(len(output_flag) - 2, -1, -1):
                    if not output_flag[i]:
                        break
                    output_flag[i] = False
        else:
            output_flag.append(not in_table)
            insert_flag.append(None)
            if in_table and line.strip() != "":
                if not table_id in table_cache:
                    table_cache[table_id] = {}
                    table_cache[table_id]["max_row"] = 0
                    table_cache[table_id]["max_column"] = 0
                if not row in table_cache[table_id]:
                    table_cache[table_id][row] = {}
                table_cache[table_id][row][column] = line.strip()
                table_cache[table_id]["max_row"] = max(
                    table_cache[table_id]["max_row"], row)
                table_cache[table_id]["max_column"] = max(
                    table_cache[table_id]["max_column"], column)
                in_table = False
                for i in range(len(output_flag) - 2, -1, -1):
                    if not output_flag[i]:
                        break
                    output_flag[i] = False
    output = ""
    for lineno, line in enumerate(lines):
        if output_flag[lineno]:
            output += f"{line}\n"
        if insert_flag[lineno] is not None:
            table_id = insert_flag[lineno]
            table_dic = table_cache[table_id]
            output += format_table(table_id, table_dic, log)
    return output


def format_table(table_id, table_dic, log):
    output = ""
    max_row = table_dic["max_row"]
    max_column = table_dic["max_column"]
    header1 = [f"Header{column}" for column in range(0, max_column+1)]
    header2 = ["-------" for column in range(0, max_column+1)]
    output += f"| {' | '.join(header1)} |\n"
    output += f"| {' | '.join(header2)} |\n"
    log[table_id] = []
    for row in range(0, max_row+1):
        columns = []
        for column in range(0, max_column+1):
            if row in table_dic and column in table_dic[row]:
                columns.append(table_dic[row][column])
            else:
                columns.append("")
                log[table_id].append(f"{row}.{column}")
        output += f"| {' | '.join(columns)} |\n"
    return output


if __name__ == "__main__":
    main()
