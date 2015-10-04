META = {
    "name": "gabbi-html",
    "install_requires": ["gabbi", "lxml", "cssselect"],
    "extras_require": {
        "linting": ["pep8"]
    }
}


if __name__ == "__main__":
    setup(**META)
