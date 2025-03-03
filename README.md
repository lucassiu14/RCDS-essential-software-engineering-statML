# Essential Software Engineering

This repository contains the course materials for the course Essential Software Engineering provided for the StatML CDT by the RCDS team in ECRI.

## Pre-Course Instructions

In order to complete this course, you will need to have a [GitHub](https://github.com/home) account. If you don't have one, you can sign up for free. You will also need to enable [Github Copilot](https://github.com/features/copilot) in your Github account. There are free and paid for tiers of GitHub Copilot. Students and educators can get access to the Pro version through Github Education. You can register for this [here](https://github.com/edu). It may take up to 10 days to receive access. For this course you can probably make do with the free version, but you should register for GitHub Education to get the Pro version to use going forward.

There are several Jupyter notebooks (the files with the extension ```.ipynb```) present in this  repository. You may review them in advance if you want to, but you aren't required to.

This course will take place in an ICT computer room and so laptops are not required but you may bring one if you wish.

## Opening a Codespace

This course is designed to run inside of a [Codespace](https://docs.github.com/en/codespaces/overview). A Codespace is a development environment hosted by GitHub directly from a repository. To use this, you will need to be signed into a GitHub account. To open the Codespace, click the green ```Code``` button at the top right of the repository. Make sure you're in the ```Codespaces``` tab and click the ```Create New Codespace on main``` button. This will create a Codespace of your own. This will take a minute or so to initialise. You may be asked to reload the page. If so, do reload the page. If the Codespace seems to get stuck loading, reloading the page can often fix the problem.

Once your Codespace has initialised, it will remain associated with your GitHub account for around a month, when it will expire. Your Codespace will be given a name like "fuzzy-barnacle" so you can identify it. To reopen it on a future occasion, click the ```Code``` button again, then select the Codespace, click ```Open```, then ```Open in Browser```.

To download the content of the files within the Codespace, open the Files tab on the left, select the files, right click and click ```Download``` button. Alternatively, if you're familiar with GitHub, you can open the source control tab on the left, you can commit and push changes. This will fork the repository with your changes. Either of these options will allow you to keep a copy of the course notes with your solutions to the exercises, etc.

## Accessing Course Materials

The easiest way to run the course materials in a GitHub Codespace (instructions above), which can be done on a computer room computer for a face to face session, or your own laptop. This requires no setup in advance past the pre-course instructions above. 

### Working Locally

If you wish to look *locally* on your own laptop, please install:
- [Visual Studio Code](https://code.visualstudio.com/) and the following extensions within VS Code:
    * [GitHub Copilot](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot) 
    * [GitHub Copilot Chat](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-chat)
    * [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
    * [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)
- [Git](https://git-scm.com/downloads) and this additional extension within VS Code:
    * [Git Graph](https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph)

Then, open VS Code on your laptop, and do the following:
1. Click the **Source Control Panel** icon in the left side bar

    <img src="resources/git/source-control-panel.png" width="25%"/>
2. Click on **Clone Repository**
3. Click **Clone from GitHub** when it appears at the top of the screen
4. Enter `ImperialCollegeLondon/RCDS-essential-software-engineering-statML`
5. Choose a location to store the course materials
6. **Open** the new repository.