import os
from biology.helper import *

# target folder : "root/dataset/biology/image"
DESTINATION_FOLDER = os.path.join(
    os.path.dirname(os.getcwd()), "dataset", "biology", "image"
)
os.makedirs(DESTINATION_FOLDER, exist_ok=True)

