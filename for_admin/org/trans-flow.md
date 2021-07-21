$ sh ./parse_jp.sh
(tex_jp -> tex_jpx)
$ sh ./tex2md.sh
(tex_jpx -> md_jpx)
translate into English by deepL via word-file
(md_jpx -> md_enorg)
$ python embed.py
(md_enorg -> ../md_en)

