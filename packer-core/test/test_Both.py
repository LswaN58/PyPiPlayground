
from pprint import pprint
# Set up path
import os, sys
from pathlib import Path

# sys.path.insert(0, str(Path(os.getcwd())))
# print(f"Updated path:")
# pprint(sys.path[:5])

sys.path.insert(0, str(Path(os.getcwd()) / "src"))
print(f"Updated path again:")
pprint(sys.path[:5])

import unittest
loader = unittest.TestLoader()
print("Preparing discovery")
tests = loader.discover('./test/cases', pattern="test_*.py", top_level_dir="./")
print("Finished discovery, path is:")
pprint(sys.path[:5])

testRunner = unittest.runner.TextTestRunner()
testRunner.run(tests)
