import uvicorn
import argparse
from api.api import app
from videos_maker.main import create_tiktok_video

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="main")

    # API argument
    parser.add_argument("--api", action="store_true", help="To launch the API")
    parser.add_argument("--port", nargs="?", type=int,
                        default=8000, help="API Port")

    # Video maker arguments
    parser.add_argument("--title", nargs="?", default="",
                        help="Give the title of the video")
    parser.add_argument("--description", nargs="?",
                        default="", help="Give the content of the video")

    args = parser.parse_args()

    if args.api:
        uvicorn.run(app, host="0.0.0.0", port=args.port)

    elif (args.title and not args.description) or (not args.title and args.description):
        parser.error(
            "You must give a title AND a description")

    elif args.description and args.title:
        if args.description == "":
            parser.error("Description cannot be empty.")
        elif args.title == "":
            parser.error("Title cannot be empty.")
        else:
            create_tiktok_video(args.title, args.description)

    else:
        parser.error(
            'Please give at least one argument: \n--api\n--title\n--desciption')
