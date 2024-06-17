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
      if "UZBEK" in y["lang"]:
        tm  = typer.prompt(f"{typer.style('Manzilingizni qanchalik tez-tez almashishini xohlaysiz?(soniya)',fg=typer.colors.YELLOW)}")
        main_changer(x=int(tm))
      if "RUSSIAN" in y["lang"]:
        tm  = typer.prompt(f"{typer.style('Как часто вы хотите, чтобы ваш адрес менялся? (секунды)',fg=typer.colors.YELLOW)}")
        main_changer(x=int(tm))
      if "ENGLISH" in y["lang"]:
        tm  = typer.prompt(f"{typer.style('How often do you want your address changed? (seconds)',fg=typer.colors.YELLOW)}")
        main_changer(x=int(tm))

if __name__ == "__main__":
  typer.run(main)