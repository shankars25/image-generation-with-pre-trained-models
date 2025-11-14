# stable_diffusion_generation.py
# Image generation using pretrained Stable Diffusion model

from diffusers import StableDiffusionPipeline
import torch

def generate_image(prompt, output_name="sd_output.png"):
    print("Loading Stable Diffusion model...")
    model_id = "runwayml/stable-diffusion-v1-5"

    pipe = StableDiffusionPipeline.from_pretrained(
        model_id,
        torch_dtype=torch.float16
    ).to("cuda")

    print("Generating image...")
    img = pipe(prompt).images[0]
    img.save(output_name)

    print(f"Image saved as {output_name}")


if __name__ == "__main__":
    prompt = input("Enter prompt for Stable Diffusion: ")
    generate_image(prompt)
