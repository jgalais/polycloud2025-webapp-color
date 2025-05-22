from flask import Flask, render_template
import socket
import random
import os
import argparse

app = Flask(__name__)

# Color palette
color_codes = {
    "red": "#e74c3c",
    "green": "#16a085",
    "blue": "#2980b9",
    "blue2": "#30336b",
    "pink": "#be2edd",
    "darkblue": "#130f40"
}

SUPPORTED_COLORS = ",".join(color_codes.keys())

# Get color from environment
COLOR_FROM_ENV = os.environ.get('APP_COLOR')

# Default random fallback
COLOR = random.choice(list(color_codes.keys()))


@app.route("/")
def main():
    # Filter ENV_ and APP_COLOR environment variables
    env_vars = {
        k: v for k, v in os.environ.items()
        if k.startswith("ENV_") or k == "APP_COLOR"
    }

    return render_template(
        'hello.html',
        name=socket.gethostname(),
        color=color_codes[COLOR],
        env_vars=env_vars
    )


if __name__ == "__main__":
    print(
        " This is a sample web application that displays a colored background. \n"
        " A color can be specified in two ways. \n"
        "\n"
        " 1. As a command line argument with --color. Accepts one of: " + SUPPORTED_COLORS + "\n"
        " 2. As an environment variable APP_COLOR. Accepts one of: " + SUPPORTED_COLORS + "\n"
        " 3. If neither is provided, a random color is used.\n"
        " Note: Command line overrides environment variable.\n"
    )

    # Command line argument handling
    parser = argparse.ArgumentParser()
    parser.add_argument('--color', required=False)
    args = parser.parse_args()

    if args.color:
        print(f"Color from command line argument = {args.color}")
        COLOR = args.color
        if COLOR_FROM_ENV:
            print(f"Environment variable APP_COLOR was set to {COLOR_FROM_ENV}, "
                  "but command line argument takes precedence.")
    elif COLOR_FROM_ENV:
        print(f"No command line argument. Using color from environment: {COLOR_FROM_ENV}")
        COLOR = COLOR_FROM_ENV
    else:
        print(f"No command line or environment color. Using random color: {COLOR}")

    # Validate color
    if COLOR not in color_codes:
        print(f"Color not supported: '{COLOR}'. Expected one of {SUPPORTED_COLORS}")
        exit(1)

    # Launch Flask app
    app.run(host="0.0.0.0", port=8080)
