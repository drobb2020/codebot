<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/drobb2020/codebot">
    <img src="static/assets/logo.png" alt="Logo" width="100">
  </a>

  <h3 align="center">codeBot</h3>

  <p align="center">
    A cool demonstration of Django and openAI
    <br />
    <a href="https://github.com/drobb2020/codebot"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/drobb2020/codebot">View Demo</a>
    ·
    <a href="https://github.com/drobb2020/codebot/issues">Report Bug</a>
    ·
    <a href="https://github.com/drobb2020/codebot/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

<p align="right">(<a href="#top">back to top</a>)</p>

### Built With

List of frameworks/libraries used to bootstrap this project.

- [Python](https://python.org)
- [Django](https://www.djangoproject.com/)
- [openAI](https://openai.com/)
- [Bootstrap](https://getbootstrap.com)
- [Prism](https://prismjs.com/)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

To Start a new Django app perform the following steps

1. Install the latest version of Python, as of this writing version 3.11.1 was installed and used to code this project.
2. Create a top-level folder to hold your project.
3. Change into that directory. Once in the directory create a new python virtual environment with the following command:

   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

4. At a minimum you will need Django and openai

   ```sh
   pip install Django openai
   ```

5. Use the command to start the django project

   ```sh
   django-admin startproject codebot .
   ```

6. Use the command to start a new django app

   ```sh
   python manage.py startapp website
   ```

7. Register the app in settings.py
8. Run the django project using the command

   ```sh
   python manage.py runserver
   ```

### Installation

If you want to skip the steps above you can go ahead and clone this repo, and use my code as a starter.

1. Get a free openai API Key at [https://openai.com/](https://openai.com/)
2. Clone the repo

   ```sh
   git clone https://github.com/drobb2020/codebot.git
   ```

3. Install the required packages

   ```sh
   pip install -r requirements.txt
   ```

4. Enter your API in `.env`

   ```sh
   OPENAI_API_KEY='ENTER YOUR API'
   ```

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->

## Usage

This is a great demo of what openai is capable of doing for coders, from writing simple HTML, to writing code in multiple languages.

<p align="right">(<a href="#top">back to top</a>)</p>

See the [open issues](https://github.com/drobb2020/codebot/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->

## Contact

Your Name - [@davidrobb2](https://twitter.com/davidrobb2) - drobb2011@gmail.com

Project Link: [https://github.com/drobb2020/codebot](https://github.com/drobb2020/codebot)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->

## Acknowledgments

I want to thank John Elder of Codemy.com for creating this course. Check out all of his courses at [codemy.com](https://codemy.com/).

- [Choose an Open Source License](https://choosealicense.com)
- [Img Shields](https://shields.io)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/drobb2020/codebot.svg?style=for-the-badge
[contributors-url]: https://github.com/drobb2020/codebot/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/drobb2020/codebot.svg?style=for-the-badge
[forks-url]: https://github.com/drobb2020/codebot/network/members
[stars-shield]: https://img.shields.io/github/stars/drobb2020/codebot.svg?style=for-the-badge
[stars-url]: https://github.com/drobb2020/codebot/stargazers
[issues-shield]: https://img.shields.io/github/issues/drobb2020/codebot.svg?style=for-the-badge
[issues-url]: https://github.com/drobb2020/codebot/issues
[license-shield]: https://img.shields.io/github/license/drobb2020/codebot.svg?style=for-the-badge
[license-url]: https://github.com/drobb2020/codebot/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: static/assets/screenshot.png
