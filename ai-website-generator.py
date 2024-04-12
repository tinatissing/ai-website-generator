# pip install dspy-ai
# pip install ipython
# make a requirements.txt file
import dspy

gemini = dspy.Google("models/gemini-1.0-pro",
                        api_key='',
                        temperature=0)
dspy.settings.configure(lm=gemini, max_tokens=1024)

from dspy import Signature, InputField, OutputField

from pydantic import BaseModel, Field
from typing import List

class AIImage(BaseModel):
    """A single generated image."""

    prompt: str = Field(desc="The prompt used to generate the image.")
    url: str = Field(
        desc="The URL of the generated image.", default="./img/placeholder.webp"
    )

class Webpage(BaseModel):
    """A single page in a website."""

    title: str = Field(desc="The page's title.")
    id: str = Field(desc=f"Lowercase of {title}")
    blurb: str = Field(desc="Catchhy blurb or quote about the page.")
    image: AIImage = Field(desc="A nice AI generated image to accompany the page.")
    content: str = Field(desc="Paragraph about the site")
    bullets: List[str] = Field(
        desc="Up to 5 bullet points of concise, relevant content."
    )

    def to_html(self):
        html_output = f'<h2 id="{self.id}">{self.title}</h2><p>{self.blurb}</p><img src="{self.image.url}" width="400" alt="{self.image.prompt}"><p>{self.content}</p><ul>'
        for bullet in self.bullets:
            html_output += f"<li>{bullet}</li>"
        html_output += f"</ul>"
        return html_output

class Website(BaseModel):
    """A complete website with a title, description, and content."""

    title: str = Field(desc="The blog webpage's title in HTML.")
    webpages: List[Webpage] = Field(desc="The pages that make up the website.")
    navbar: str = Field(desc="HTML and CSS to create a dynamic nav bar for each section of the site using their ids.")
    footer: str = Field(desc="Footer for the website.")

    def to_html(self):
        html_output = f"<head><link rel='stylesheet' href='main.css'></head><h1>{self.title}</h1><div>{self.navbar}</div>"
        for webpages in self.webpages:
            html_output += webpages.to_html()
        html_output += f"<footer>{self.footer}</footer>"
        return html_output
    
class Style(BaseModel):
    """A complete website style."""

    css: str = Field(desc="Create custom css for the website to make it feel like a professional blog. Change the font to something modern and trendy. Use colors to make the page unique. There should be appropriate padding around the elements on the page.")

    def to_html(self):
        html_output = f'{self.css}'
        return html_output

class WebsiteCreator(Signature):
    """Create content for a great blog website."""

    website_subject: str = InputField(desc="The subject of the website.")
    website_content: Website = OutputField(desc="The complete website content.")
    website_styling: Style = OutputField(desc="The complete website styling")

from dspy.functional import TypedPredictor

website_creator = TypedPredictor(WebsiteCreator)
blog_website = website_creator(website_subject="Blog About Engineering at the University of Guelph")

from pprint import pprint

pprint(blog_website.website_content.to_html())

with open("home.html", "w") as file:
    file.write(blog_website.website_content.to_html())

with open("css/main.css", "w") as file:
    file.write(blog_website.website_styling.to_html())

from IPython.display import display, HTML
display(HTML(blog_website.website_content.to_html()))