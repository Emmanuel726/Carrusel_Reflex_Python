import reflex as rx
import asyncio
from rxconfig import config

class State(rx.State):
    
    lista: list[list[str]] = [
        ["img1","Slider", "Nombre", "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Officiis culpa similique consequuntur, reprehenderit dicta repudiandae.","content"],
        ["img2","Slider", "Nombre", "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Officiis culpa similique consequuntur, reprehenderit dicta repudiandae.","cont"],
        ["img3","Slider", "Nombre", "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Officiis culpa similique consequuntur, reprehenderit dicta repudiandae.","cont"],
        ["img4","Slider", "Nombre", "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Officiis culpa similique consequuntur, reprehenderit dicta repudiandae.","cont"],
        ["img5","Slider", "Nombre", "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Officiis culpa similique consequuntur, reprehenderit dicta repudiandae.","cont"],
        ["img6","Slider", "Nombre", "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Officiis culpa similique consequuntur, reprehenderit dicta repudiandae.","cont"],
        ["img7","Slider", "Nombre", "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Officiis culpa similique consequuntur, reprehenderit dicta repudiandae.","cont"],
        ["img8","Slider", "Nombre", "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Officiis culpa similique consequuntur, reprehenderit dicta repudiandae.","cont"],
        ["img9","Slider", "Nombre", "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Officiis culpa similique consequuntur, reprehenderit dicta repudiandae.","cont"],
        ["img10","Slider", "Nombre", "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Officiis culpa similique consequuntur, reprehenderit dicta repudiandae.","cont"],
        ["img11","Slider", "Nombre", "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Officiis culpa similique consequuntur, reprehenderit dicta repudiandae.","cont"]
    ]
    
    
    # async def fondo(self):
    #     while True:
    #         await asyncio.sleep(4.00),
    #         self.fondos = [self.fondos[-1], *self.fondos[:-1]]
    #         yield
            
    async def id(self):
        while True:
            await asyncio.sleep(7.00),
            self.lista = [self.lista[-1], *self.lista[:-1]]
            yield

style = {
    "#img1": {
        "top": "0",
        "left": "0",
        "width": "100%",
        "height": "100vh",
        "transform": "translate(0,0)",
        "z-index": "1",
    },
    "#img2": {
        "top": "60%",
        "left": "70%", 
        "width": "180px",
        "height": "250px",
        "z-index": "3",
    },
    "#img3": {
        "top": "60%",
        "left": "calc(70% + 200px)",  
        "width": "180px",
        "height": "250px",
        "z-index": "4",
    },
    "#img4": {
        "top": "60%",
        "left": "calc(70% + 400px)",   
        "width": "180px",
        "height": "250px",
        "z-index": "5",
    },
    "#img5": {
        "top": "60%",
        "left": "calc(70% + 600px)",   
        "width": "180px",
        "height": "250px",
        "z-index": "6",
    },
    "#img6": {
        "top": "60%",
        "left": "calc(70% + 800px)",   
        "width": "180px",
        "height": "250px",
        "z-index": "7",
    },
    "#img7": {
        "top": "60%",
        "left": "calc(70% + 1000px)",   
        "width": "180px",
        "height": "250px",
        "z-index": "8",
    },
    "#img8": {
        "top": "60%",
        "left": "calc(70% + 1200px)",   
        "width": "180px",
        "height": "250px",
        "z-index": "9",
    },
    "#img9": {
        "top": "60%",
        "left": "calc(70% + 1400px)",   
        "width": "180px",
        "height": "250px",
        "z-index": "10",
    },
    "#img10": {
        "top": "60%",
        "left": "calc(70% + 1600px)",   
        "width": "180px",
        "height": "250px",
        "z-index": "11",
    },
    "#img11": {
        "top": "60%",
        "left": "calc(70% + 1800px)",   
        "width": "180px",
        "height": "250px",
        "z-index": "2",
    },
    ".content": {
        "position": "absolute",
        "top": "50%",
        "left": "100px",
        "transform": "translateY(-50%)",
        "width": "400px",
        "text-align": "left",
        "color": "#fff",
        "display": "flex",
    },
    ".cont": {
        "display": "none",
    },
    ".title": {
        "font-size": "100px",
        "text-transform": "uppercase",
        "color": "#14ff72cb",
        "font-weight": "bold",
        "line-height": "1",
        "opacity": "0",
        "animation": "animate 1s ease-in-out 0.3s 1 forwards",
    },
    ".name": {
        "font-size": "80px",
        "text-transform": "uppercase",
        "font-weight": "bold",
        "line-height": "1",
        "text-shadow": "3px 4px 4px rgba(255, 255, 255, 0.8)",
        "opacity": "0",
        "animation": "animate 1s ease-in-out 0.6s 1 forwards",
    },
    ".des": {
        "margin-top": "10px",
        "margin-bottom": "20px",
        "font-size": "18px",
        "margin-left": "5px",
        "opacity": "0",
        "animation": "animate 1s ease-in-out 0.9s 1 forwards",
    },
    "@keyframes animate": {
        "from":{
            "opacity": "0",
            "transform": "translate(0, 100px)",
            "filter": "blur(33px)",
        },
        "to":{
            "opacity": "1",
            "transform": "translate(0)",
            "filter": "blur(0)",
        }
    }
}

def boxes(ids: list[str], index: int) -> rx.Component:
    return rx.box(
        rx.flex(
            rx.text(f"{ids[1]}", class_name="title"),
            rx.text(f"{ids[2]}", class_name="name"),
            rx.text(f"{ids[3]}", class_name="des"),
            class_name=f"{ids[4]}",
            direction="column",
            transition="all 1s ease",
            transition_delay=".7s",
        ),
        id=f"{ids[0]}",
        background_image=f"url(/{index + 1}.jpg)",
        position="absolute",
        border_radius="15px",
        box_shadow="0 25px 50px rgba(0, 0, 0, 0.3)",
        background_size="cover",
        background_position="center",
        transition="all 1s ease",
        transition_delay=".1s",
    )

def carrusel() -> rx.Component:
    return rx.flex(
        rx.foreach(
            State.lista,
            lambda ids, index: boxes(ids, index),
        ),
        style={"overflow": "hidden", "position": "relative", "width": "100%", "height": "100vh"},
    )

@rx.page(route="/", title="Carrusel", on_load=State.id)
def index() -> rx.Component:
    return rx.flex(
        carrusel(),
    )


app = rx.App(style=style)
