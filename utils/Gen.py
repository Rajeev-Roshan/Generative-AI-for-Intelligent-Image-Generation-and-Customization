import uuid
import random
import json 
import websocket
import uuid
import utils.websockets_api as websockets_api

class ImageGen:
    def __init__(self) -> None:
        self.client_id = str(uuid.uuid4())
        self.server_address = "127.0.0.1:8188"
        with open("Workflows/text_to_image.json", "r", encoding="utf-8") as f:
                self.prompt_text = f.read()

    def Generate(self, Prompt: str):
        prompt = json.loads(self.prompt_text)
        print(prompt)
        seed = random.randint(99, 999999999999)
        prompt["3"]["inputs"]["seed"] = seed
        prompt["18"]["inputs"]["prompt"] = Prompt
        ws = websocket.WebSocket()
        ws.connect("ws://{}/ws?clientId={}".format(self.server_address, self.client_id))
        images = websockets_api.get_images(ws,self.client_id, prompt)
        return images
    





