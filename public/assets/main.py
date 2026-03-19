# main.py
import argparse
import os
import json
import logging
import sys
from analytics_worker.worker import Worker

def get_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler = logging.FileHandler('worker.log')
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger

def main():
    parser = argparse.ArgumentParser(description='Analytics worker')
    parser.add_argument('--config', default='config.json')
    args = parser.parse_args()
    with open(args.config, 'r') as config_file:
        config = json.load(config_file)
    os.environ['ANALYTICS_API_KEY'] = config['api_key']
    os.environ['ANALYTICS_API_SECRET'] = config['api_secret']
    worker = Worker()
    worker.run()

if __name__ == '__main__':
    logger = get_logger()
    try:
        main()
    except Exception as e:
        logger.error(f'Failed to run analytics worker: {str(e)}')
        sys.exit(1)