import os
import re
import sys
import json
import glob


def main():
    argv = sys.argv
    if len(argv) == 1:
        for filepath in glob.glob("md_enorg/*.md"):
            base = os.path.basename(filepath).split(".")[0]
            sub(base)
    elif len(argv) == 2:
        base = argv[1]
        sub(base)
    else:
        message = f"usage: python {argv[0]} basename"
        print(message)


def sub(base):
    input_path = f"md_enorg/{base}.md"
    json_path = f"tex_jpx/{base}.json"
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
    doc = replace_imath(doc, dic, log["imath"])
    doc = replace_emath(doc, dic, log["emath"])

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
        pattern = key + r"(,|\sand\s)" + key
        count = len(re.findall(pattern, doc))
        if count >= 2:
            log[key] = {"count": count, "text": text}  # 複数個マッチした
        if count >= 1:
            doc = re.sub(pattern, escape(text), doc)
            continue

        # "TERM00000" を置換
        pattern = key
        count = len(re.findall(pattern, doc))
        if count >= 2:
            log[key] = {"count": count, "text": text}  # 複数個マッチした
        if count >= 1:
            doc = re.sub(pattern, escape(text), doc)
        else:
            log[key] = {"count": count, "text": text}  # マッチしなかった
    return doc


def replace_emath(doc, dic, log):
    for key, value in dic["emath"].items():
        text = f"$${math2str(value)}$$\n"
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

    return "".join([math2str(value) for value in v])


def escape(text):
    a = repr(text)[1:-1]
    # print(a)
    return a


if __name__ == "__main__":
    main()
