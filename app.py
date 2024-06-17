import typer
from typing import Optional
import os
import sys
import inquirer

###################
from part.home import home_page
from helper.changer import main_changer
#############################


def main(status: Optional[str] = typer.Argument("home")):
    if status == "home":
      home_page()
      lang = [
        inquirer.List(
          "lang",
          message="Choose your language:",
          choices=[
            typer.style("UZBEK",fg=typer.colors.YELLOW),
            typer.style("ENGLISH",fg=typer.colors.YELLOW),
            typer.style("RUSSIAN",fg=typer.colors.YELLOW),
          ]
        ),
      ]
      y = inquirer.prompt(lang)
      if "Uzbek" in y["lang"]:
        tm  = typer.prompt(f"{typer.style("Har necha sekundda sizning manzilingizni almashtiraylik")}")
        main_changer(x=int(tm))
      if "RUSSIAN" in y["lang"]:
        tm  = typer.prompt(f"{typer.style("Давайте менять ваш адрес каждые несколько секунд")}")
        main_changer(x=int(tm))
      if "ENGLISH" in y["lang"]:
        tm  = typer.prompt(f"{typer.style("Let's change your address every few seconds")}")
        main_changer(x=int(tm))

if __name__ == "__main__":
  typer.run(main)