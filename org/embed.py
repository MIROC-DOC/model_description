import re
import sys
import json


def main():
    argv = sys.argv
    if len(argv) != 2:
        message = f"usage: python {argv[0]} basename"
        print(message)
        sys.exit()

    basename = argv[1]
    input_path = f"md_enorg/{basename}.md"
    json_path = f"tex_jpx/{basename}.json"
    output_path = f"md_en/{basename}.md"
    log_path = f"embed_log/{basename}.json"
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
        text = imath2str(value[0])

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


def imath2str(v):
    if isinstance(v, str):
        return v
    return "".join([imath2str(value) for value in v])


def replace_emath(doc, dic, log):
    for key, value in dic["emath"].items():
        text = f"$${emath2str(value)}$$\n"
        pattern = r".*?" + key + r".*?"
        count = len(re.findall(pattern, doc))
        if count == 0:
            log[key] = {"count": count, "text": text}  # マッチしなかった
            continue
        doc = re.sub(pattern, escape(text), doc, 1)
        if count > 1:
            doc = re.sub(pattern, "", doc)  # 2行目以降は空行にする
    return doc


def emath2str(v):
    if isinstance(v, str):
        if v == "&":  # 単体の&があるとエラーになるので空白に置き換える
            return ""
        return v
    return "".join([emath2str(value) for value in v])


def escape(text):
    return repr(text)[1:-1]


if __name__ == "__main__":
    main()
