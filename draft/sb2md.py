# Scrapbox to Markdown
import re


def main():
    with open("p-cum.sb") as fi, open("p-cum.md", "w") as fo:
        title = fi.readline()
        fo.write(f"## {title}")
        for line in fi:
            match_object = re.match(r"\[\*\*.+\]\s+$", line)
            if match_object:
                fo.write(f"\n### {match_object.group().strip()[3:-1]}\n\n")
                continue

            match_object = re.match(r"\[\$.+\]\s+$", line)
            if match_object:
                fo.write(f"\n$$\n{match_object.group().strip()[2:-1]}\n$$\n\n")
                continue

            fo.write(re.sub(r"\[\$\s(.+?)\s\]", r"$\1$", line))


if __name__ == "__main__":
    main()
