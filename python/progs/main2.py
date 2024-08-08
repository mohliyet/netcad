import sys
import os

# Use os.path.join for cross-platform compatibility
sys.path.append(os.path.join('..', 'packages'))

import extra.iota
print(extra.iota.funI())


