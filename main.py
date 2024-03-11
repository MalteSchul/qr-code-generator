import json
import segno
import os

with open("./env.json") as f:
    env = json.load(f)

qrcode = segno.make_qr(env["text"], micro=64)

for file_name in os.listdir(env["generated_folder_name"]):
    os.remove(os.path.join(env["generated_folder_name"], file_name))

for border_size in env["sizes"]["border"]:
    for scale_size in env["sizes"]["scale"]:
        qrcode.save(
            f"{env['generated_folder_name']}/{env['save_name']}_border-size{border_size}_scale-size{scale_size}.png",
            scale=scale_size,
            border=border_size
        )
    qrcode.save(
        f"{env['generated_folder_name']}/{env['save_name']}_border-size{border_size}.pdf",
        scale=1,
        border=border_size
    )
    qrcode.save(
        f"{env['generated_folder_name']}/{env['save_name']}_border-size{border_size}.svg",
        scale=1,
        border=border_size
    )
