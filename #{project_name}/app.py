import logging
import #{project_name}

log = logging.getLogger(__name__)


def main():
    log.info(f"application version {#{project_name}.__version__} start")


if __name__ == "__main__":
    main()