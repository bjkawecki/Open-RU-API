import logging
import sys

import uvicorn


def main(argv=sys.argv[1:]):
    try:
        uvicorn.run(
            "src.server:app",
            host="0.0.0.0",
            port=4000,
            reload=True,
            log_level=logging.WARNING,
        )
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
