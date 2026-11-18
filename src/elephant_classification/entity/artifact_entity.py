from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    """
    Store the path of the ingested Elephant image dataset.
    """
    dataset_dir: str