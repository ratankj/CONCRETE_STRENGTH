from concrete_strength.entity.config_entity import DataIngestionConfig
from concrete_strength.entity.artifact_entity import DataIngestionArtifact
from concrete_strength.configuration import *
import os,sys
from concrete_strength.logger import logging
from concrete_strength.pipeline.train import Pipeline
from concrete_strength.exception import ApplicationException

def main():
    try:
        pipeline = Pipeline()
        pipeline.run_pipeline()

    except Exception as e:
        logging.error(f"{e}")
        print(e)

if __name__ == "__main__":
    main()

