import sys
import uvicorn


def main(argv=sys.argv[1:]):
    try:
        uvicorn.run("src.server:app", host="0.0.0.0", port=3001, reload=True)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
