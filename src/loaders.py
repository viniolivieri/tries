from src.trie import Trie
from pathlib import Path
  
def load_file_trie(trie: Trie, dataset: Path):
    """Insert words from a file in a Trie Structure
    
    Args:
        trie: A Trie structure
        dataset: Path to txt file
    """

    with open(dataset) as f:
        while True:
            
            line = f.readline().rstrip('\n')
            if not line:
                break
            else:
                trie.insert(line)
                
def load_data_trie(trie: Trie, dataset: Path):
    """Insert words from files in a Trie Structure
    
    Args:
        trie: A Trie structure
        dataset: Path to folder which contains txt files
    """

    if dataset.is_dir():
        files = Path(dataset).glob('*')
        for file in files:
            load_file_trie(trie, file)
