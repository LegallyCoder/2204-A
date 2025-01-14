import json
from PIL import Image
from diffusers import StableDiffusionPipeline
from tqdm import tqdm

pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4-original")

def gen_imgs(json_path):
    with open(json_path, "r") as f:
        prompts = json.load(f)
    for page, prompt in tqdm(prompts.items(), desc="Generating", total=len(prompts)):
        img = pipe(prompt).images[0]
        img.save(f"page_{page}_image.png")
        img.show()

gen_imgs("prompts.json")
