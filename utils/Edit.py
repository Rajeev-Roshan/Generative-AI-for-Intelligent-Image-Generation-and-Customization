import uuid
import random
import json 
import websocket
import uuid
import utils.websockets_api as websockets_api

class ImageEdit:
    def __init__(self) -> None:
        self.client_id = str(uuid.uuid4())
        self.server_address = "127.0.0.1:8188"
        with open("Workflows/image_custamization_workflow.json", "r", encoding="utf-8") as f:
                self.prompt_text = f.read()

    def Generate(self, base64_image:str, remove:str, replace=""):
        prompt = json.loads(self.prompt_text)
        seed = random.randint(99, 999999999999)
        prompt["205"]["inputs"]["image"] = base64_image
        prompt["155"]["inputs"]["categories"] = remove
        prompt["207"]["inputs"]["text_b"] = replace
        prompt["189"]["inputs"]["seed"] = seed

        ws = websocket.WebSocket()
        ws.connect("ws://{}/ws?clientId={}".format(self.server_address, self.client_id))
        images = websockets_api.get_images(ws,self.client_id, prompt)
        return images
    
