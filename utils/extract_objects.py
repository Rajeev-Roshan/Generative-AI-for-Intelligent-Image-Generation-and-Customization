# import json
# import websocket
# import websocket_api
# def extract(Image_base64: str):
#     with open("Workflows/extract_objects.json", "r", encoding="utf-8") as f:
#         prompt_text = f.read()

#     prompt = json.loads(prompt_text)
#     prompt["19"]["inputs"]["image"] = Image_base64
#     ws = websocket.WebSocket()
#     ws.connect("ws://{}/ws?clientId={}".format(server_address, client_id))
#     images = websockets_api.get_images(ws,client_id, prompt)
    