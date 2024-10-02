import asyncio
import random

from flet import Page, app, MainAxisAlignment, CrossAxisAlignment, Image, ImageFit, Theme


def generate_image_url(height: int = 800, width: int = 600):
    return f"https://picsum.photos/seed/{random.randint(1, 1000)}/{width}/{height}"

def update_image(page: Page, image: Image):
    image.src = generate_image_url()
    page.update()

async def main(page: Page):
    page.theme = Theme()
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER

    src = generate_image_url()

    image = Image(src=src, fit=ImageFit.FIT_HEIGHT)
    page.add(image)

    for i in range(100):
        update_image(page, image)
        await asyncio.sleep(5)


app(main)
