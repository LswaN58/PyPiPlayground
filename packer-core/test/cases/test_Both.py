# Set up path
import os
import sys
from pathlib import Path
sys.path.insert(0, str(Path(os.getcwd()) / "src"))
print(f"Updated path: {sys.path[:5]}...")
import unittest

loader = unittest.TestLoader()
tests = loader.discover('./test', pattern="test_*.py", top_level_dir="./")
testRunner = unittest.runner.TextTestRunner()
testRunner.run(tests)
