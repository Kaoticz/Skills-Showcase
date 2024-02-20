# Skills Showcase

This repository centralizes all personal projects, both big and small, that I have worked on, organized by programming language. Feel free to browse through them.

A brief summary for each of these projects can be found below.

## Table of Contents

- **AoC**
    - **[Advent-Of-Code](#Advent-Of-Code)**
- **C#**
    - **[AkkoBot](#AkkoBot)**
    - **[NadekoHub](#NadekoHub)**
    - **[Json2Sharp](#Json2Sharp)**
    - **[Kotz.Utilities](#kotzutilities)**
    - **[Miaumarro-API](#Miaumarro-API)**
- **C**
    - **[TodoC](#TodoC)**
    - **[DynC](#DynC)**
- **Javascript**
    - **[Embed-Visualizer](#Embed-Visualizer)**
    - **[Miaumarro-Client](#Miaumarro-Client)**
- **Nix**
    - **[NixConf](#NixConf)**
- **Python**
    - **[LLM DocReader](#llm-docreader)**

## Summaries

### AoC

#### [Advent-Of-Code]

Advent of Code is a very popular annual programming competition that runs every December leading up to Christmas Day. It features a series of programming puzzles designed to challenge programmers of all skill levels. This repository contains all my attempts at the annual challenges and should grow over time, as I use the puzzles to hone my skills in different programming languages.

### C#

#### [AkkoBot]

Discord bot designed for **community moderation** that prioritizes **customizability** and features a **plug-in system** for those who wish to extend the functionality of the bot. Its development was motivated over frustrations with existing moderation bots that lacked in functionality or flexibility.
- **DSharpPlus** is used as a Discord wrapper.
- **EF Core** and **LinqToDb** are used to store and retrieve user data from a **PostgreSQL** database.
- **YamlDotNet** is used for configuration files.
- The plug-in system uses **assembly scanning** to load extra functionality into the bot.
- The bot makes heavy use of **events** and **asynchronous programming** for most of its functionality.
- **xUnit** is used for unit testing.
- Custom **logging** and **scheduling** solutions are used for core functionalities. These should be replaced with industry-standard solutions in a future update.
- Has around **42.000 lines of code** and is currently hosted on **Google Cloud Platform** serving over **480 users**.

#### [NadekoHub]

A cross-platform desktop application designed to **manage instances** of the [NadekoBot](https://nadeko.bot/) Discord bot. Users can add, update, remove, execute, and stop as many instances of NadekoBot as they want. The application also **saves logs** and **performs backups** of the bots, minimizes to the system tray when it's not needed, and **automatically updates itself** to the latest version whenever a new version is available.
- Implemented in a **MVVM** pattern with **Avalonia** and **ReactiveUI**.
- The application makes heavy use of **events** to signal and send data to different views and view-models.
- The application **starts external processes** and **redirects their output** for **logging** purposes.
- Features light and dark themes for accessibility.
- **GitHub Actions** CI/CD pipeline to build and publish stable releases.

#### [Json2Sharp] [![Json2Sharp-NuGet Downloads][Json2Sharp-Nuget-Downloads]][Json2Sharp-Nuget-Url]

A command-line interface (CLI) tool and library designed to facilitate the conversion of **JSON** data into programming language **classes**. It originated from a personal necessity for a CLI tool capable of mapping JSON properties to classes across **various programming languages**. I also needed **finer control over the generated class**, a feature that most tools currently available in this category lack. It currently supports C# and Python, with support for additional languages planned for the future.
- **System.CommandLine** is used in the CLI tool.
- **System.Text.Json** is used by the library to process JSON data.
- **xUnit** is used for unit testing.
- **GitHub Actions** CI/CD pipeline to build and publish the stable releases and NuGet packages.
- The CLI tool is published in the **[Arch User Repository (AUR)](https://aur.archlinux.org/packages/json2sharp-bin)**.

#### [Kotz.Utilities]

A set of helper libraries for problems commonly encountered in my projects.
- **[Kotz.Collections]** [![Kotz.Collections-NuGet Downloads][Kotz.Collections-Nuget-Downloads]][Kotz.Collections-Nuget-Url]: Defines implementations of collection types that don't exist in .NET's Base Class Library (BCL).
- **[Kotz.Extensions]** [![Kotz.Extensions-NuGet Downloads][Kotz.Extensions-Nuget-Downloads]][Kotz.Extensions-Nuget-Url]: Defines extension methods for several data types in the BCL.
- **[Kotz.ObjectPool]** [![Kotz.ObjectPool-NuGet Downloads][Kotz.ObjectPool-Nuget-Downloads]][Kotz.ObjectPool-Nuget-Url]: Defines a wrapper for `ObjectPool` that is much easier to use.
- **[Kotz.Events]** [![Kotz.Events-NuGet Downloads][Kotz.Events-Nuget-Downloads]][Kotz.Events-Nuget-Url]: Defines generic and asynchronous event handlers.
- **[Kotz.DependencyInjection]** [![Kotz.DependencyInjection-NuGet Downloads][Kotz.DependencyInjection-Nuget-Downloads]][Kotz.DependencyInjection-Nuget-Url]: Defines attributes and methods for easier registration and resolution of services with `Microsoft.Extensions.DependencyInjection`.
- **xUnit** is used for unit testing.
- **GitHub Actions** CI/CD pipeline to build and publish the NuGet packages.

#### [Miaumarro-API]

Back-end component of the Miaumarro petshop e-commerce, written with **ASP NET Core Web API**. The API allows for user registration and authentication, product search and purchase, and scheduling appointments for services. It was developed in a team of **four people**, where I assumed the **leadership role** for the project from start to finish while also mentoring the other team members so they could keep up with the project's pace and objectives.
- **EF Core** and **LinqToDb** are used to store and retrieve user data from a **SQLite** database.
-  Implementation of **authentication** and **authorization** flows in the API with **JWT Tokens**.
- **OneOf** is used to return strongly-typed responses from the endpoints, mitigating potential bugs during development.
- **xUnit** is used for unit testing.

### C

#### [TodoC]

A simple console application that saves anotations, created for an university assignment where I had to create a C program that performed basic CRUD operations. This program saves **text of arbitrary length** to a **SQLite** database and makes use of most, if not all, features in the C programming language.
- Uses the native **sqlite3** library to create and interact with a **SQLite** database.
- A **Dockerfile** is provided for easy execution of the application.

#### [DynC]

A library offering implementations of various **data structures**. Being my first project, it was conceived to refine my proficiency in the C programming language. It includes generic implementations of an **object** type, a **list**, and a **linked list**.

### Javascript

#### [Embed-Visualizer]

A **single-page web application** designed to generate **Discord embeds in Yaml format** for utilization with AkkoBot. Users are provided with a Discord message template, allowing them to populate fields with their desired content. The template is transformed into Yaml text in real-time, which can be copied and utilized with AkkoBot to produce well formatted messages on Discord.
- **ReactJS** is used as the UI framework.
- **YamlJS** is used to generate the Yaml text.
- **CodeMirror** is used to render Yaml with text highlighting.
- Hosted at: https://akko-bot.github.io/Embed-Visualizer/

#### [Miaumarro-Client]

Front-end component of the Miaumarro petshop e-commerce, written with **VueJs**. The client allows for user registration and authentication, product browsing and purchase, scheduling appointments for services, and bridges any other feature offered by the `Miaumarro-API` in an easy and convenient way.

### Nix

#### [NixConf]

Nix configuration files for a NixOS system. This was my first exploration of the Nix language where I configure a system for **desktop** use with the applications and settings I commonly use.
- Uses **modules** to separate code into domains.
    - Demonstrates how to create **customizable modules** within the constraints of the Nix language.
- Uses **Home Manager** to manage user-related programs and settings.
- Uses the **Nix User Repository (NUR)** to install browser extensions.
- Contains **Bash** scripts to **automate the build and deployment** of new **derivations**.

### Python

#### [LLM DocReader]

Small console application that feeds **PDF** documents into a **Large Language Model (LLM)** AI, then lets the user ask the AI **questions about said documents**.
- **LangChain** is used to interact with the LLM.
- **Ollama** is used to host a locally deployed LLM on the user's machine.

[Advent-Of-Code]: https://github.com/Kaoticz/Advent-Of-Code
[AkkoBot]: https://github.com/Akko-Bot/AkkoBot
[Json2Sharp]: https://github.com/Kaoticz/Json2Sharp
[Kotz.Utilities]: https://github.com/Kaoticz/Kotz.Utilities
[Kotz.Collections]: https://github.com/Kaoticz/Kotz.Utilities/tree/main/Kotz.Collections
[Kotz.Extensions]: https://github.com/Kaoticz/Kotz.Utilities/tree/main/Kotz.Extensions
[Kotz.ObjectPool]: https://github.com/Kaoticz/Kotz.Utilities/tree/main/Kotz.ObjectPool
[Kotz.Events]: https://github.com/Kaoticz/Kotz.Utilities/tree/main/Kotz.Events
[Kotz.DependencyInjection]: https://github.com/Kaoticz/Kotz.Utilities/tree/main/Kotz.DependencyInjection
[Miaumarro-API]: https://github.com/Miaumarro/Miaumarro-API
[NadekoHub]: https://github.com/Kaoticz/NadekoHub
[TodoC]: https://github.com/Kaoticz/TodoC
[DynC]: https://github.com/Kaoticz/DynC
[Embed-Visualizer]: https://github.com/Akko-Bot/Embed-Visualizer
[Miaumarro-Client]: https://github.com/Miaumarro/Miaumarro-Client
[NixConf]: https://github.com/Kaoticz/NixConf
[LLM DocReader]: ./Python/LLM%20DocReader

[Json2Sharp-Nuget-Downloads]: https://img.shields.io/nuget/dt/Json2Sharp?color=00aa00
[Json2Sharp-Nuget-Url]: https://www.nuget.org/packages/Json2Sharp
[Kotz.Collections-Nuget-Downloads]: https://img.shields.io/nuget/dt/Kotz.Collections?color=00aa00
[Kotz.Collections-Nuget-Url]: https://www.nuget.org/packages/Kotz.Collections
[Kotz.Extensions-Nuget-Downloads]: https://img.shields.io/nuget/dt/Kotz.Extensions?color=00aa00
[Kotz.Extensions-Nuget-Url]: https://www.nuget.org/packages/Kotz.Extensions
[Kotz.ObjectPool-Nuget-Downloads]: https://img.shields.io/nuget/dt/Kotz.ObjectPool?color=00aa00
[Kotz.ObjectPool-Nuget-Url]: https://www.nuget.org/packages/Kotz.ObjectPool
[Kotz.Events-Nuget-Downloads]: https://img.shields.io/nuget/dt/Kotz.Events?color=00aa00
[Kotz.Events-Nuget-Url]: https://www.nuget.org/packages/Kotz.Events
[Kotz.DependencyInjection-Nuget-Downloads]: https://img.shields.io/nuget/dt/Kotz.DependencyInjection?color=00aa00
[Kotz.DependencyInjection-Nuget-Url]: https://www.nuget.org/packages/Kotz.DependencyInjection